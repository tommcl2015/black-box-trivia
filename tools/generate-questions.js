#!/usr/bin/env node
/*
 * Draft new questions with the Claude API, for human review.
 *
 *   ANTHROPIC_API_KEY=sk-... node tools/generate-questions.js --cat geo --count 100 --topic "African rivers and lakes"
 *
 * Writes data/drafts/<timestamp>-<cat>.txt in the pack format. Review every line
 * (facts can be wrong!), then move the file into data/new/ and run:
 *   npm run build:questions
 * Duplicates against the existing bank are removed automatically at build time.
 */
const fs = require('fs');
const path = require('path');

const args = Object.fromEntries(process.argv.slice(2).join(' ').split('--').filter(Boolean).map(s => {
  const [k, ...v] = s.trim().split(' '); return [k, v.join(' ')];
}));
const CAT = args.cat || 'geo';
const COUNT = Math.min(200, parseInt(args.count || '100', 10));
const TOPIC = args.topic || '';
const MODEL = args.model || process.env.MODEL || 'claude-sonnet-5-5';
const NAMES = { geo: 'Geography', ent: 'Entertainment (film, TV, music)', his: 'History', art: 'Arts & Literature (books, art, mythology, classical music)', sci: 'Science & Nature (incl. technology, animals, the human body)', spo: 'Sports & Leisure (sports, food & drink, games, hobbies)' };
if (!process.env.ANTHROPIC_API_KEY) { console.error('Set ANTHROPIC_API_KEY'); process.exit(1); }
if (!NAMES[CAT]) { console.error('cat must be one of', Object.keys(NAMES).join(', ')); process.exit(1); }

const bankPath = path.join(__dirname, '..', 'server', 'questions.json');
const existing = fs.existsSync(bankPath) ? require(bankPath).filter(q => q.c === CAT).map(q => q.q) : [];
const sample = existing.sort(() => Math.random() - 0.5).slice(0, 120).join('\n');

const prompt = `Write ${COUNT} new pub-trivia questions for the category "${NAMES[CAT]}"${TOPIC ? `, focused on: ${TOPIC}` : ''}.
Audience: adults in Canada and the US playing a Trivial Pursuit-style party game.

Rules:
- Only well-established facts that will not change. No "current" office-holders, no records likely to be broken, no disputed claims.
- Mix difficulty 1 (everyone knows) to 5 (expert). Roughly 15% 1s, 30% 2s, 30% 3s, 15% 4s, 10% 5s.
- Short answers (1–4 words) so they also work as fill-in-the-blank.
- Three plausible wrong answers of the same type as the right one.
- Do not repeat these existing questions:
${sample}

Output ONLY lines in this exact format, no numbering, no commentary:
${CAT}|difficulty|question|answer|wrong1;wrong2;wrong3|optional alternate accepted answers separated by ;`;

(async () => {
  const res = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: { 'content-type': 'application/json', 'x-api-key': process.env.ANTHROPIC_API_KEY, 'anthropic-version': '2023-06-01' },
    body: JSON.stringify({ model: MODEL, max_tokens: 16000, messages: [{ role: 'user', content: prompt }] })
  });
  if (!res.ok) { console.error(res.status, await res.text()); process.exit(1); }
  const data = await res.json();
  const text = data.content.map(c => c.text || '').join('');
  const lines = text.split('\n').map(l => l.trim()).filter(l => l.startsWith(CAT + '|') && l.split('|').length >= 5);
  const dir = path.join(__dirname, '..', 'data', 'drafts');
  fs.mkdirSync(dir, { recursive: true });
  const file = path.join(dir, `${Date.now()}-${CAT}.txt`);
  fs.writeFileSync(file, `# DRAFT — review every fact before moving to data/new/\n${lines.join('\n')}\n`);
  console.log(`Wrote ${lines.length} draft questions to ${file}`);
})();
