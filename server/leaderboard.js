/* High-score leaderboard: top 10 per game length, saved to a JSON file.
 * On Render the app's own folder is wiped on every deploy, so point LEADERBOARD_FILE at a persistent disk
 * (e.g. /var/data/leaderboard.json) to keep scores between deploys. */
const fs = require('fs');
const path = require('path');
const { RegExpMatcher, TextCensor, englishDataset, englishRecommendedTransformers } = require('obscenity');
let geoip = null; try { geoip = require('geoip-country'); } catch (e) { /* optional */ }

const BOARDS = [10, 20, 30, 50];          // a game's length decides which board it competes on
const KEEP = 10;
const MAX_PER_Q = 150 + 50 + 40 + 25;    // best case per question: typed answer + full speed + hardest + streak
const FILE = process.env.LEADERBOARD_FILE || path.join(__dirname, '..', 'data', 'runtime', 'leaderboard.json');
const COUNTRIES = (() => { try { return require('../data/countries.json'); } catch (e) { return {}; } })();

const matcher = new RegExpMatcher({ ...englishDataset.build(), ...englishRecommendedTransformers });
const censor = new TextCensor();          // replaces rude words with symbols, e.g. "#@$%"

function cleanName(name) {
  let n = String(name || '').replace(/[\u0000-\u001f<>]/g, '').replace(/\s+/g, ' ').trim().slice(0, 16) || 'Player';
  const hits = matcher.getAllMatches(n);
  if (hits.length) n = censor.applyTo(n, hits);
  return n;
}

let data = load();
function load() {
  try {
    const d = JSON.parse(fs.readFileSync(FILE, 'utf8'));
    for (const b of BOARDS) if (!Array.isArray(d[b])) d[b] = [];
    return d;
  } catch (e) { const d = {}; BOARDS.forEach(b => d[b] = []); return d; }
}
let saveTimer = null;
function save() {
  clearTimeout(saveTimer);
  saveTimer = setTimeout(() => {
    try {
      fs.mkdirSync(path.dirname(FILE), { recursive: true });
      const tmp = FILE + '.tmp';
      fs.writeFileSync(tmp, JSON.stringify(data));
      fs.renameSync(tmp, FILE);
    } catch (e) { console.error('leaderboard save failed', e.message); }
  }, 200);
}

function country(ip) {
  if (!geoip || !ip) return null;
  try {
    const g = geoip.lookup(String(ip).replace(/^::ffff:/, ''));
    if (!g || !g.country) return null;
    const c = COUNTRIES[g.country];
    return { code: g.country, name: (c && c.name) || g.name || g.country, flag: (c && c.flag) || null };
  } catch (e) { return null; }
}

const qualifies = (board, score) => score > 0 && (data[board].length < KEEP || score > data[board][data[board].length - 1].score);

/* entries: [{ name, score, correct }], questions: game length, ip: player's address.
 * Returns the placements: [{ name, rank, board }]. */
function submit(entries, questions, ip, source) {
  const board = Number(questions);
  if (!BOARDS.includes(board) || !Array.isArray(entries)) return [];
  const placed = [];
  for (const e of entries.slice(0, 8)) {
    const score = Math.round(Number(e && e.score));
    const correct = Math.round(Number(e && e.correct));
    if (!(score > 0) || !(correct >= 1) || correct > board) continue;
    if (score > correct * MAX_PER_Q || score < correct * 100) continue;       // impossible scores are ignored
    if (!qualifies(board, score)) continue;
    const row = { name: cleanName(e.name), score, correct, at: new Date().toISOString().slice(0, 10), src: source || 'game' };
    const c = country(ip);                                                     // looked up only for top-10 scores
    if (c) row.country = c;
    data[board].push(row);
    data[board].sort((a, b) => b.score - a.score || b.correct - a.correct || (a.at < b.at ? -1 : 1));
    data[board] = data[board].slice(0, KEEP);
    const rank = data[board].indexOf(row) + 1;
    if (rank > 0) placed.push({ name: row.name, rank, board });
  }
  if (placed.length) save();
  return placed;
}

function storage() {
  let writable = false;
  try { fs.mkdirSync(path.dirname(FILE), { recursive: true }); fs.accessSync(path.dirname(FILE), fs.constants.W_OK); writable = true; } catch (e) {}
  let disk = false; try { fs.accessSync('/var/data', fs.constants.W_OK); disk = true; } catch (e) {}
  return { file: FILE, configured: !!process.env.LEADERBOARD_FILE, writable, saved: fs.existsSync(FILE), diskAtVarData: disk };
}

function list() { const o = {}; for (const b of BOARDS) o[b] = data[b]; return o; }

module.exports = { BOARDS, KEEP, cleanName, submit, list, qualifies, storage, _reset() { data = load(); BOARDS.forEach(b => data[b] = []); } };
