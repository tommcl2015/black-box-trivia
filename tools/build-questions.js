#!/usr/bin/env node
/*
 * Builds server/questions.json from:
 *   data/raw/opentdb.js      – the original JS array (deduped here)
 *   data/raw/tm.tsv          – Tom's spreadsheet export (+ data/tm_fixes.json corrections)
 *   data/new/*.txt           – additional question packs, one per line:
 *        cat|difficulty|question|answer|wrong1;wrong2;wrong3|alt1;alt2
 *      cat = geo | ent | his | art | sci | spo   difficulty = 1 (easy) .. 5 (hard)
 * Usage: node tools/build-questions.js
 */
const fs = require('fs');
const path = require('path');
const he = require('he');
const { normalize } = require('../public/js/match.js');

const ROOT = path.join(__dirname, '..');
const D = p => path.join(ROOT, 'data', p);

const CATS = {
  geo: 'Geography', ent: 'Entertainment', his: 'History',
  art: 'Arts & Literature', sci: 'Science & Nature', spo: 'Sports & Leisure'
};

const out = [];
const seen = new Map(); // normalized question -> item
let stats = { opentdb: 0, tm: 0, packs: 0, dupes: 0, dropped: 0 };

const byAnswer = new Map();
const STOP = new Set('what which who whom whose this that these those the and for with from was were has have had are its his her their name called known famous most first only into over also during novel book wrote write written film movie song play country city state world does did how many much year'.split(' '));
function dedupeKey(q) { return normalize(q).replace(/ /g, ''); }

function fibEligible(q, a, hasChoices) {
  if (!hasChoices) return true;
  if (/which of (the|these)|which one of|of the following|following|\bnot\b|n't\b|except|\bnone\b|\ball of\b/i.test(q)) return false;
  if (/^(true|false|yes|no)$/i.test(a)) return false;
  const words = a.trim().split(/\s+/).length;
  if (a.length > 32 || words > 5) return false;
  if (/[,;:]/.test(a) && !/^\d[\d,]*$/.test(a)) return false;
  return true;
}

const GENERIC = /\b(lake|river|mount|mountains|mountain|desert|ocean|sea|city|island|islands|empire|civilization|civilisation|dynasty|battle of|operation|the|national park|cathedral|railway|canal|gulf|bay|kingdom|republic of|ancient|amendment|line)\b/gi;

function autoAlts(q, a) {
  const alts = new Set();
  let base = a.replace(/^["“]|["”]$/g, '').trim();
  if (base !== a) alts.add(base);
  // "A / B", "A or B"
  if (/\s\/\s/.test(base)) base.split(/\s\/\s/).forEach(x => alts.add(x.trim()));
  // "Kiev (Kyiv)"
  const paren = base.match(/^(.*?)\s*\((.*?)\)\s*$/);
  if (paren) { alts.add(paren[1]); alts.add(paren[2]); }
  // strip generic geographic / historical words
  const stripped = base.replace(GENERIC, ' ').replace(/\s+/g, ' ').trim();
  if (stripped && stripped !== base && stripped.length >= 3) alts.add(stripped);
  // surname for "Who ..." questions about people
  const words = base.replace(/[()]/g, '').split(/\s+/);
  if (/^\s*(who|(this|what is the name of the) .*?(composer|author|painter|artist|president|scientist|leader|writer|singer|actor|actress|inventor|explorer|philosopher|emperor|player|athlete|director|mathematician|astronomer|poet|novelist|sculptor|architect|physicist|chemist|economist|queen|king))/i.test(q) &&
      words.length >= 2 && words.length <= 4 && words.every(w => /^[A-ZÀ-Ý]/.test(w) || /^(van|von|de|da|der|la|le|di)$/.test(w))) {
    let last = words[words.length - 1];
    if (/^(Jr\.?|Sr\.?|II|III|IV)$/.test(last) && words.length > 2) last = words[words.length - 2];
    const prev = words[words.length - 2];
    if (/^(van|von|de|da|der|la|le|di|du)$/i.test(prev)) last = prev + ' ' + last;
    if (last.length >= 4) alts.add(last);
    if (words.length === 3 && /^(van|von|de|da)$/i.test(words[1])) alts.add(words[0]); // Rembrandt van Rijn -> Rembrandt
  }
  // "Title by Author"
  const by = base.match(/^(.*?) by [A-Z]/);
  if (by) alts.add(by[1]);
  return [...alts].filter(x => x && normalize(x) !== normalize(a));
}

function add(item) {
  item.q = item.q.replace(/\s+/g, ' ').trim();
  item.a = item.a.replace(/\s+/g, ' ').trim().replace(/^["“](.*)["”]$/, '$1');
  if (!/[?.!_)"'”]$/.test(item.q)) item.q += /^(what|who|which|where|when|how|in what|in which|on what|at what|is|are|does|do|can|was|were|name)\b/i.test(item.q) ? '?' : '.';
  const k = dedupeKey(item.q);
  if (seen.has(k)) { stats.dupes++; return false; }
  // near-duplicate: same answer and mostly the same words
  const ak = normalize(item.a).replace(/ /g, '');
  const toks = new Set(normalize(item.q).split(' ').filter(t => t.length > 2 && !STOP.has(t)));
  const prior = byAnswer.get(ak) || [];
  for (const t of prior) {
    let inter = 0; for (const x of toks) if (t.has(x)) inter++;
    const j = inter / Math.min(toks.size || 1, t.size || 1);
    if (j >= 0.6) { stats.nearDupes = (stats.nearDupes || 0) + 1; return false; }
  }
  prior.push(toks); byAnswer.set(ak, prior);
  seen.set(k, item);
  item.alt = [...new Set([...(item.alt || []), ...autoAlts(item.q, item.a)])];
  if (!item.alt.length) delete item.alt;
  item.fib = fibEligible(item.q, item.a, item.w && item.w.length >= 3);
  out.push(item);
  return true;
}

/* ---------- 1. OpenTDB-style array ---------- */
(function loadOpenTdb() {
  const src = fs.readFileSync(D('raw/opentdb.js'), 'utf8')
    .replace(/^\s*const\s+triviaQuestions\s*=\s*/, '').replace(/;\s*$/, '');
  const arr = JSON.parse(src);
  const gk = JSON.parse(fs.readFileSync(D('gk_categories.json'), 'utf8'));
  const catMap = { 10: ['art', 'Books'], 11: ['ent', 'Film'], 12: ['ent', 'Music'], 14: ['ent', 'Television'], 15: ['spo', 'Video Games'] };
  let gkIndex = -1;
  const gkSeen = new Set();
  // questions already rewritten in original wording (data/rewrite/) are skipped here
  const doneFile = D('rewrite/done-sources.txt');
  const done = new Set(fs.existsSync(doneFile) ? fs.readFileSync(doneFile, 'utf8').split('\n').filter(Boolean).map(dedupeKey) : []);
  for (const x of arr) {
    const qText = he.decode(x.question).trim();
    if (done.has(dedupeKey(qText)) || done.has(dedupeKey(qText + '?')) || done.has(dedupeKey(qText + '.'))) {
      if (x.category === 9) { const key = qText.toLowerCase(); if (!gkSeen.has(key)) { gkSeen.add(key); gkIndex++; } }
      stats.rewritten = (stats.rewritten || 0) + 1; continue;
    }
    let c, sub;
    if (x.category === 9) {
      const key = qText.toLowerCase();
      if (!gkSeen.has(key)) { gkSeen.add(key); gkIndex++; }
      const idx = [...gkSeen].indexOf(key);
      if (gk.drop.includes(idx)) { stats.dropped++; continue; }
      c = Object.keys(gk.cats).find(k => gk.cats[k].includes(idx)) || 'spo';
      sub = 'General Knowledge';
    } else [c, sub] = catMap[x.category] || ['spo', 'General'];
    const ok = add({
      c, sub, d: 3, src: 'opentdb',
      q: qText, a: he.decode(x.correctAnswer).trim(),
      w: x.incorrectAnswers.map(w => he.decode(w).trim())
    });
    if (ok) stats.opentdb++;
  }
})();

/* ---------- 2. Tom's sheet ---------- */
(function loadTm() {
  const fixes = JSON.parse(fs.readFileSync(D('tm_fixes.json'), 'utf8'));
  const lines = fs.readFileSync(D('raw/tm.tsv'), 'utf8').split(/\r?\n/);
  const map = {
    geography: 'geo', 'world geography': 'geo', 'u.s. states': 'geo', 'world landmarks': 'geo', 'world capitals': 'geo', 'u.s. geography': 'geo',
    history: 'his', 'world history': 'his', 'ancient civilizations': 'his', 'u.s. presidents': 'his', 'u.s. government': 'his', politics: 'his',
    'american history': 'his', 'european history': 'his', '20th century': 'his', 'world leaders': 'his', 'famous women': 'his',
    science: 'sci', technology: 'sci', animals: 'sci', astronomy: 'sci', biology: 'sci', anatomy: 'sci',
    literature: 'art', art: 'art', 'art history': 'art', mythology: 'art', shakespeare: 'art', 'classical music': 'art',
    culture: 'ent', entertainment: 'ent', film: 'ent', movies: 'ent', television: 'ent', music: 'ent', 'pop culture': 'ent', business: 'ent',
    sports: 'spo', 'food and drink': 'spo', food: 'spo'
  };
  lines.forEach((line, i) => {
    const ln = i + 1;
    if (ln === 1 || !line.trim()) return;
    const [cat, q, a, diff] = line.split('\t');
    const fx = fixes[String(ln)] || {};
    if (fx.drop) { stats.dropped++; return; }
    const sub = (fx.c || cat || '').trim();
    const c = map[sub.toLowerCase()] || 'ent';
    const d = Math.min(5, Math.max(1, parseInt(diff, 10) || 3));
    const ok = add({ c, sub: sub.replace(/^GEography$/, 'Geography'), d, src: 'tm', q: fx.q || q, a: fx.a || a, alt: fx.alt, w: fx.w });
    if (ok) stats.tm++;
  });
})();

/* ---------- 3. New packs ---------- */
(function loadPacks() {
  for (const sub of ['rewrite', 'new']) {
  const dir = D(sub);
  if (!fs.existsSync(dir)) continue;
  for (const f of fs.readdirSync(dir).filter(f => f.endsWith('.txt') && f !== 'done-sources.txt').sort()) {
    const lines = fs.readFileSync(path.join(dir, f), 'utf8').split(/\r?\n/);
    lines.forEach((line, i) => {
      if (!line.trim() || line.startsWith('#')) return;
      const p = line.split('|');
      if (p.length < 5) { console.warn(`${f}:${i + 1} malformed`); return; }
      const [c, d, q, a, w, alt] = p.map(s => s.trim());
      if (!CATS[c]) { console.warn(`${f}:${i + 1} bad category ${c}`); return; }
      const wrong = w ? w.split(';').map(s => s.trim()).filter(Boolean) : [];
      if (wrong.length && wrong.length !== 3) console.warn(`${f}:${i + 1} needs 3 wrong answers`);
      if (wrong.some(x => normalize(x) === normalize(a))) { console.warn(`${f}:${i + 1} distractor equals answer`); return; }
      const ok = add({ c, sub: CATS[c], d: +d || 3, src: sub === 'rewrite' ? 'rewrite' : 'pack', q, a, w: wrong.length === 3 ? wrong : undefined, alt: alt ? alt.split(';').map(s => s.trim()).filter(Boolean) : undefined });
      if (ok) stats.packs++;
    });
  }
  }
})();

/* ---------- write ---------- */
out.forEach((x, i) => { x.id = i + 1; if (!x.w) delete x.w; });
const final = out.map(({ id, c, sub, d, q, a, w, alt, fib, src }) => ({ id, c, sub, d, q, a, w, alt, fib, src }));
fs.writeFileSync(path.join(ROOT, 'server', 'questions.json'), JSON.stringify(final));
const byCat = {}; final.forEach(x => byCat[x.c] = (byCat[x.c] || 0) + 1);
console.log('Built', final.length, 'questions', stats);
console.log('By category', byCat);
console.log('Multiple-choice capable', final.filter(x => x.w).length, '| fill-in capable', final.filter(x => x.fib).length);
