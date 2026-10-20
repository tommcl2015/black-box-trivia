#!/usr/bin/env node
/* Turns the fact tables in data/facts/*.js into question packs (data/new/3xx-facts-*.txt).
 * Wrong answers are drawn from the same table, so they are always plausible.
 * Re-run after editing any fact table:  node tools/build-facts.js && npm run build:questions */
const fs = require('fs');
const path = require('path');
const F = n => require(path.join(__dirname, '..', 'data', 'facts', n));
const H = F('history-events.js'), C = F('culture.js'), W = F('world.js'), S = F('sports.js');
const OUT = path.join(__dirname, '..', 'data', 'new');

// deterministic RNG so rebuilding gives the same packs
let seed = 20261020;
const rnd = () => { seed = (seed * 1664525 + 1013904223) % 4294967296; return seed / 4294967296; };
const shuffle = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
const rows = txt => txt.trim().split('\n').map(l => l.split('|').map(s => s.trim()));
const clean = s => String(s).replace(/\|/g, '/').replace(/;/g, ',');
const ord = n => n + (['th', 'st', 'nd', 'rd'][(n % 100 - 20) % 10] || ['th', 'st', 'nd', 'rd'][n % 100] || 'th');

function pick(pool, answer, n = 3, prefer) {
  const uniq = [...new Set(pool.filter(x => x && x !== answer))];
  let cands = prefer ? uniq.filter(prefer) : uniq;
  if (cands.length < n) cands = uniq;
  return shuffle(cands).slice(0, n);
}
function nearYears(y, step) {
  const s = new Set();
  for (const d of shuffle([-3, -2, -1, 1, 2, 3])) { if (s.size < 3) s.add(String(+y + d * step)); }
  return [...s];
}
const packs = {};
function add(pack, c, d, q, a, wrong, alt) {
  if (!wrong || wrong.length < 3) return;
  (packs[pack] = packs[pack] || []).push([c, d, clean(q), clean(a), wrong.map(clean).join(';'), (alt || []).map(clean).join(';')].join('|'));
}

/* ---------- Oscars ---------- */
{
  const r = rows(H.bestPicture);
  const films = r.map(x => x[1]);
  for (const [y, film, d] of r) {
    add('ent-oscars', 'ent', +d, `Which film won the Academy Award for Best Picture for ${y}?`, film, pick(films, film, 3, f => Math.abs(r.find(x => x[1] === f)[0] - y) <= 12));
    if (+d <= 3) add('ent-oscars', 'ent', Math.min(5, +d + 1), `"${film}" won Best Picture for films of which year?`, y, nearYears(y, 1));
  }
}

/* ---------- Olympics / World Cup ---------- */
{
  const s = rows(H.summerOlympics), w = rows(H.winterOlympics);
  const sc = s.map(x => x[1]), wc = w.map(x => x[1]);
  for (const [y, city, d] of s) {
    add('spo-olympics', 'spo', +d, `Which city hosted the ${y} Summer Olympics?`, city, pick(sc, city));
    if (sc.filter(x => x === city).length === 1) add('spo-olympics', 'spo', Math.min(5, +d + 1), `In which year did ${city} host the Summer Olympics?`, y, nearYears(y, 4));
  }
  add('spo-olympics', 'spo', 3, 'Tokyo hosted the 2020 Summer Olympics in which year, after a delay?', '2021', ['2020', '2022', '2019']);
  add('spo-olympics', 'spo', 2, 'Which city will host the 2028 Summer Olympics?', 'Los Angeles', ['Brisbane', 'Paris', 'Madrid']);
  add('spo-olympics', 'spo', 3, 'Which city will host the 2032 Summer Olympics?', 'Brisbane', ['Los Angeles', 'Doha', 'Budapest']);
  for (const [y, city, d] of w) {
    add('spo-olympics', 'spo', +d, `Which city hosted the ${y} Winter Olympics?`, city, pick(wc, city));
    if (wc.filter(x => x === city).length === 1) add('spo-olympics', 'spo', Math.min(5, +d + 1), `In which year did ${city} host the Winter Olympics?`, y, nearYears(y, 4));
  }
  add('spo-olympics', 'spo', 3, 'Which two Italian locations shared the 2026 Winter Olympics?', 'Milan and Cortina d\'Ampezzo', ['Turin and Sestriere', 'Rome and Bormio', 'Venice and Livigno'], ['Milan Cortina;Milan-Cortina']);

  const wcRows = rows(H.worldCup);
  const winners = [...new Set(wcRows.map(x => x[2]))], hosts = wcRows.map(x => x[1]);
  for (const [y, host, win] of wcRows) {
    const d = +y >= 1990 ? 3 : +y >= 1966 ? 4 : 5;
    add('spo-worldcup', 'spo', d, `Which country won the ${y} FIFA World Cup?`, win, pick(winners.concat(['Netherlands', 'Croatia', 'Hungary', 'Sweden', 'Portugal']), win));
    if (!host.includes(' and ')) add('spo-worldcup', 'spo', d, `Which country hosted the ${y} FIFA World Cup?`, host, pick(hosts.filter(h => !h.includes(' and ')), host));
  }
  add('spo-worldcup', 'spo', 3, 'Which two countries co-hosted the 2002 FIFA World Cup?', 'South Korea and Japan', ['China and Japan', 'South Korea and China', 'Japan and Australia'], ['Japan and South Korea;Korea and Japan']);
  add('spo-worldcup', 'spo', 2, 'Which three countries co-hosted the 2026 FIFA World Cup?', 'Canada, Mexico and the United States', ['Canada, the United States and Cuba', 'Mexico, the United States and Costa Rica', 'Canada, Mexico and Brazil']);
  const ww = rows(H.womensWorldCup), wwin = [...new Set(ww.map(x => x[1]))].concat(['Sweden', 'Brazil', 'England', 'Canada']);
  for (const [y, win] of ww) add('spo-worldcup', 'spo', 4, `Which country won the ${y} FIFA Women's World Cup?`, win, pick(wwin, win));
}

/* ---------- Leaders ---------- */
{
  const p = rows(H.usPresidents), names = p.map(x => x[1]);
  for (const [n, name, d] of p) {
    const i = names.indexOf(name);
    const near = names.filter((x, j) => j !== i && Math.abs(j - i) <= 4);
    add('his-leaders', 'his', +d, `Who was the ${ord(+n)} President of the United States?`, name, pick(near.length >= 3 ? near : names, name));
  }
  const c = rows(H.canadianPMs), pm = c.map(x => x[1]);
  for (const [n, name, d] of c) {
    const i = pm.indexOf(name);
    const near = pm.filter((x, j) => j !== i && Math.abs(j - i) <= 4);
    add('his-leaders', 'his', Math.max(+d, 3), `Who was Canada's ${ord(+n)} Prime Minister?`, name, pick(near.length >= 3 ? near : pm, name));
  }
}

/* ---------- Dates, wonders, ancient sites ---------- */
{
  const H2 = F('history2.js');
  for (const [y, q, d] of rows(H2.events)) add('his-dates', 'his', +d, q, y, nearYears(y, +y > 1900 ? 1 : 2));
  const w = rows(H2.wonders), places = w.map(x => x[1]), names = w.map(x => x[0]);
  for (const [name, place, d] of w) {
    add('his-ancient', 'his', +d, `Which Wonder of the Ancient World stood at ${place}?`, `The ${name}`, pick(names, name).map(x => 'The ' + x), [name]);
    add('his-ancient', 'his', +d, `Where did the ancient ${name.replace(/ \(.*\)/, '')} wonder stand?`, place, pick(places, place));
  }
  const a = rows(H2.ancient), countries = [...new Set(a.map(x => x[1]))];
  for (const [site, country, d] of a) add('his-ancient', 'his', +d, `The ruins of ${site} are in which modern country?`, country, pick(countries, country));
}

/* ---------- Culture ---------- */
function simple(pack, cat, table, qfn, opts = {}) {
  const r = rows(table), vals = r.map(x => x[1]);
  for (const [k, v, d] of r) add(pack, cat, +(d || 3), qfn(k, v), v, pick(vals, v, 3, opts.prefer && opts.prefer(k, v, r)), opts.alt && opts.alt(k, v));
}
simple('art-authors', 'art', C.novels, k => `Who wrote "${k}"${/[?!]$/.test(k) ? '' : '?'}`);
simple('ent-songs', 'ent', C.songs, k => `Which artist had a hit with "${k}"?`);
simple('ent-directors', 'ent', C.directors, k => `Who directed "${k}"?`);
simple('art-paintings', 'art', C.paintings, k => `Which artist created "${k}"?`);
simple('art-composers', 'art', C.composers, k => `Who composed "${k}"?`);
simple('art-shakespeare', 'art', C.shakespeare, k => `${k} ${k.endsWith(',') ? 'appears' : 'is a character'} in which Shakespeare play?`.replace(', appears', ' appears'));
simple('sci-inventors', 'sci', C.inventions, k => `Who is credited with the ${k.charAt(0).toLowerCase() + k.slice(1)}?`);

/* ---------- World ---------- */
{
  const r = rows(W.capitals);
  for (const [country, cap, cont, d] of r) {
    const sameCont = r.filter(x => x[2] === cont && x[0] !== country);
    add('geo-capitals', 'geo', +d, `What is the capital of ${country}?`, cap, pick(sameCont.map(x => x[1]), cap));
    add('geo-capitals', 'geo', Math.min(5, +d + 1), `${cap} is the capital of which country?`, country, pick(sameCont.map(x => x[0]), country));
  }
  const s = rows(W.usStates), st = s.map(x => x[0]), caps = s.map(x => x[1]);
  for (const [state, cap, d] of s) {
    add('geo-usstates', 'geo', +d, `What is the capital of ${state}?`, cap, pick(caps, cap));
    add('geo-usstates', 'geo', Math.min(5, +d + 1), `${cap} is the capital of which US state?`, state, pick(st, state));
  }
  simple('geo-landmarks', 'geo', W.landmarks, k => `In which country would you find ${k}?`, { prefer: (k, v) => x => !x.includes(' and ') });
  simple('spo-dishes', 'spo', W.dishes, k => `${k} is a classic dish from which country?`);
  simple('sci-moons', 'sci', W.moons, k => `${k} is a moon of which planet?`);
  const e = rows(W.elements), syms = e.map(x => x[0]), els = e.map(x => x[1]);
  for (const [sym, el, d] of e) {
    add('sci-elements', 'sci', +d, `Which element has the chemical symbol ${sym}?`, el, pick(els, el, 3, x => x[0] === el[0] || x[0] === sym[0]));
    add('sci-elements', 'sci', Math.min(5, +d + 1), `What is the chemical symbol for ${el.toLowerCase()}?`, sym, pick(syms, sym, 3, x => x[0] === sym[0] || x[0] === el[0]));
  }
}

/* ---------- Sports ---------- */
for (const lg of ['NHL', 'NBA', 'NFL', 'MLB', 'CFL']) {
  const r = rows(S[lg]), cities = r.map(x => x[1]);
  const nick = { NHL: 'NHL', NBA: 'NBA', NFL: 'NFL', MLB: 'MLB', CFL: 'CFL' }[lg];
  for (const [team, city, d] of r) add('spo-teams', 'spo', +d, `In which city do the ${nick}'s ${team} play?`, city, pick(cities, city));
}
simple('spo-terms', 'spo', S.terms, k => `The term "${k}" comes from which sport?`);

/* ---------- write ---------- */
let total = 0;
for (const f of fs.readdirSync(OUT)) if (f.startsWith('3') && f.includes('-facts-')) fs.unlinkSync(path.join(OUT, f));
Object.entries(packs).forEach(([name, lines], i) => {
  const file = path.join(OUT, `3${String(i).padStart(2, '0')}-facts-${name}.txt`);
  fs.writeFileSync(file, `# Generated by tools/build-facts.js from data/facts/ — edit the tables, not this file\n${lines.join('\n')}\n`);
  total += lines.length;
  console.log(name.padEnd(18), lines.length);
});
console.log('total', total);
