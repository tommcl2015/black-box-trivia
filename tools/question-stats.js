#!/usr/bin/env node
/* Turns real-play results into question fixes.
 *
 * 1. In Google Analytics: Explore → Free form. Rows: the custom dimension "qid". Values: Event count,
 *    and the custom metric "correct" (sum). Filter: Event name = question_answered. Export as CSV.
 * 2. Run:  node tools/question-stats.js path/to/export.csv
 *
 * Questions answered by at least MIN players get a difficulty from how many got them right
 * (data/difficulty-overrides.json). Questions almost nobody gets right are listed in data/review.txt
 * for a human to check: they are often wrong or badly worded. Then run: npm run build:questions */
const fs = require('fs');
const path = require('path');
const MIN = 25;
const file = process.argv[2];
if (!file) { console.error('usage: node tools/question-stats.js export.csv'); process.exit(1); }
const bank = require('../server/questions.json');
const byId = new Map(bank.map(q => [String(q.id), q]));
const lines = fs.readFileSync(file, 'utf8').split(/\r?\n/).filter(l => l && !l.startsWith('#'));
const head = lines.shift().split(',').map(h => h.trim().toLowerCase());
const iq = head.findIndex(h => h.includes('qid')), ic = head.findIndex(h => h.includes('correct')), in_ = head.findIndex(h => h.includes('event count') || h === 'count');
const over = JSON.parse(fs.readFileSync(path.join(__dirname, '../data/difficulty-overrides.json'), 'utf8'));
const review = [];
let n = 0;
for (const l of lines) {
  const c = l.split(','); const id = (c[iq] || '').trim(); const total = +c[in_]; const right = +c[ic];
  const q = byId.get(id); if (!q || !(total >= MIN)) continue;
  const rate = right / total;
  const d = rate > 0.85 ? 1 : rate > 0.65 ? 2 : rate > 0.45 ? 3 : rate > 0.25 ? 4 : 5;
  if (d !== q.d) { over[id] = d; n++; }
  if (rate < 0.1) review.push(`${id}\t${Math.round(rate * 100)}% of ${total}\t${q.q}\t→ ${q.a}`);
}
fs.writeFileSync(path.join(__dirname, '../data/difficulty-overrides.json'), JSON.stringify(over, null, 1));
fs.writeFileSync(path.join(__dirname, '../data/review.txt'), review.join('\n') + '\n');
console.log(`${n} difficulty changes; ${review.length} questions to review in data/review.txt`);
