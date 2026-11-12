/* Crawlable trivia library: topic pages (/trivia), picture quizzes (/picture-quiz), the daily quiz (/daily-quiz) and guides (/guides).
 * Gives visitors (and search engines) real content to read outside the one-page game. Returns the URLs for the sitemap. */
const fs = require('fs');
const path = require('path');
const TOPICS = require('./content-topics.js');
const GUIDES = require('./content-guides.js');

const CATS = { geo: 'Geography', ent: 'Entertainment', his: 'History', art: 'Arts & Literature', sci: 'Science & Nature', spo: 'Sports & Leisure' };
const DIFF = ['', 'Easy', 'Easy', 'Medium', 'Hard', 'Very hard'];
const LAUNCH = '2026-11-12';             // first daily quiz
const TZ = 'America/Toronto';

const norm = s => String(s).toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
function hash(str) { let h = 2166136261; for (let i = 0; i < str.length; i++) { h ^= str.charCodeAt(i); h = Math.imul(h, 16777619); } return h >>> 0; }
function rng(seed) { let a = hash(seed); return () => { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
const shuffled = (arr, r) => { const a = arr.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(r() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };

// Picture quiz pages: key, title, filter on the picture questions, intro.
const PICS = [
  ['flags', 'Flags quiz', q => q.pr === 'flags' && !/\/(roundel|signal)-/.test(q.img), 'Name the country from its flag, drawn in classic one-bit pixel art. Without colour, you have to recognise each flag from its shapes alone: stripes, stars, crosses and emblems.'],
  ['air-force-roundels', 'Air force roundels quiz', q => /\/roundel-/.test(q.img), 'Military aircraft carry a national marking called a roundel. Most are rings of colour, but some countries use a leaf, a kangaroo or a star. Which air force uses each one?'],
  ['signal-flags', 'Maritime signal flags quiz', q => /\/signal-/.test(q.img), 'Ships signal each other with a set of international flags, one for each letter of the alphabet. Each flag also has its own meaning: Alfa means "diver down; keep well clear". Which letter is each flag?'],
  ['country-shapes', 'Country shapes quiz', q => q.pr === 'shapes', 'Every country has a shape, but how many do you really know? Name the country from its outline alone.'],
  ['find-the-country', 'Find the country on the map', q => q.pr === 'maps', 'One country is highlighted on a small map of its region. Can you name it?'],
  ['us-states', 'US states quiz', q => q.pr === 'states', 'Name the US state from its outline. The squares of the west are harder than they look.'],
  ['islands-and-lakes', 'Islands and lakes quiz', q => q.pr === 'islands', 'Famous islands and lakes from around the world, drawn from public-domain map data. Name each one from its shape.'],
  ['landmarks', 'Landmarks and wonders quiz', q => q.pr === 'landmarks', 'From the Eiffel Tower to the Seven Wonders of the Ancient World, name the landmark from its silhouette.'],
  ['mountains-and-volcanoes', 'Mountains and volcanoes quiz', q => q.pr === 'mountains', 'Famous mountains, volcanoes and rock formations, drawn as skyline silhouettes. Can you tell Fuji from Kilimanjaro?'],
  ['city-skylines', 'City skylines quiz', q => q.pr === 'skylines', 'Name the city from its skyline. Look for the one or two buildings that give each city away.'],
  ['famous-statues', 'Famous statues quiz', q => q.pr === 'statues', 'Famous statues and sculptures, from ancient Greece to Copenhagen\'s harbour. Name each one.'],
  ['famous-aircraft', 'Famous aircraft quiz', q => q.pr === 'aircraft', 'Aircraft silhouettes traced from flight-simulator models. Name the plane from its outline.'],
  ['famous-ships', 'Famous ships quiz', q => q.pr === 'ships', 'Famous ships and types of ship, from Viking longships to the Titanic.'],
  ['famous-trains', 'Famous trains quiz', q => q.pr === 'trains', 'Famous locomotives and trains, digitised in 8-bit colour from photographs.'],
  ['tanks-and-war-machines', 'Tanks and war machines quiz', q => q.pr === 'tanks', 'Tanks and war machines from the First World War to today. Name each one from its silhouette.'],
  ['rockets-and-spacecraft', 'Rockets and spacecraft quiz', q => q.pr === 'spacecraft', 'Rockets, space stations, probes and landers, traced from NASA 3D models.'],
  ['sports-stadiums', 'Sports stadiums quiz', q => q.pr === 'stadiums', 'Famous sports stadiums, drawn as silhouettes with the sport\'s ball in the corner as a clue.'],
  ['racing-circuits', 'Racing circuits quiz', q => q.pr === 'circuits', 'Formula 1 circuits and NASCAR tracks, drawn from their layouts. Name the track from its shape.'],
  ['cloud-types', 'Cloud types quiz', q => q.pr === 'clouds', 'Cumulus, cirrus, stratus and the rest, in 8-bit colour. What type of cloud is each one?'],
  ['writing-systems', 'Writing systems quiz', q => q.pr === 'scripts', 'Each picture shows the word "hello" written in a different script. Which writing system is it?'],
  ['constellations', 'Constellations quiz', q => q.pr === 'stars', 'Name the constellation from its pattern of stars.'],
  ['famous-paintings', 'Famous paintings quiz', q => q.pr === 'paintings', 'Famous public-domain paintings redrawn in 8-bit pixel art. Name the painting, or the artist.'],
  ['famous-inventions', 'Famous inventions quiz', q => q.pr === 'inventions', 'Inventions that changed the world, drawn in 8-bit colour. Name each one.'],
  ['road-signs-and-symbols', 'Road signs and symbols quiz', q => q.pr === 'signs', 'What does each sign or symbol mean?']
];

module.exports = function content(app, { page, esc, bank, siteName }) {
  const text = bank.filter(q => !q.img), pics = bank.filter(q => q.img);
  const byText = new Map(); for (const q of text) if (!byText.has(norm(q.q))) byText.set(norm(q.q), q);
  const cache = (fn) => { let v; return () => v || (v = fn()); };
  const send = body => (req, res) => res.type('html').set('Cache-Control', 'public, max-age=600').send(body());

  // ---------- question rendering ----------
  const qItem = (q, seed) => {
    const opts = q.w && q.w.length ? shuffled([q.a, ...q.w.slice(0, 3)], rng(seed + q.id)) : null;
    return `<li class="tq-item"><p class="tq">${esc(q.q)} <span class="muted">(${CATS[q.c] ? CATS[q.c] + ', ' : ''}${DIFF[q.d] || ''})</span></p>${opts ? `<p class="tq-opts">${opts.map((o, i) => `<span>${'ABCD'[i]}. ${esc(o)}</span>`).join(' ')}</p>` : ''}<details><summary>Show answer</summary><p>Answer: <b>${esc(q.a)}</b></p></details></li>`;
  };
  const picItem = (q, seed) => {
    const opts = q.w && q.w.length ? shuffled([q.a, ...q.w.slice(0, 3)], rng(seed + q.img)) : null;
    return `<li class="pq-item"><img src="${esc(q.img)}" alt="Picture question: ${esc(q.q)}" width="192" height="128" loading="lazy"><p class="tq">${esc(q.q)}</p>${opts ? `<p class="tq-opts">${opts.map((o, i) => `<span>${'ABCD'[i]}. ${esc(o)}</span>`).join(' ')}</p>` : ''}<details><summary>Show answer</summary><p>Answer: <b>${esc(q.a)}</b></p></details></li>`;
  };
  const crumbs = parts => `<p class="crumbs">${parts.map(([h, t]) => h ? `<a href="${h}">${esc(t)}</a>` : esc(t)).join(' › ')}</p>`;

  // ---------- topic pages ----------
  function topicQuestions(t) {
    const out = [], seen = new Set();
    for (const [file, sections] of t.src) {
      let cur = null;
      for (const line of fs.readFileSync(path.join(__dirname, '..', 'data', 'new', file), 'utf8').split('\n')) {
        const m = line.match(/^# --- (.*) ---/); if (m) { cur = m[1]; continue; }
        if (!line.trim() || line.startsWith('#')) continue;
        if (sections && !sections.includes(cur)) continue;
        const q = byText.get(norm(line.split('|')[2] || ''));
        if (q && !seen.has(q.id)) { seen.add(q.id); out.push(q); }
      }
    }
    if (t.match) for (const q of text) if (!seen.has(q.id) && t.match.test(q.q) && !(t.exclude && t.exclude.test(q.q))) { seen.add(q.id); out.push(q); }
    const r = rng(t.slug);
    return shuffled(out, r).slice(0, 30).sort((a, b) => a.d - b.d);
  }
  const topicPage = t => {
    const qs = topicQuestions(t);
    const related = TOPICS.filter(x => x.cat === t.cat && x.slug !== t.slug).slice(0, 6);
    return page(`trivia/${t.slug}`, t.title, t.desc, `
        ${crumbs([['/trivia', 'Trivia library'], [`/trivia#${t.cat}`, CATS[t.cat]], [null, t.title]])}
        <h2>${esc(t.title)}</h2>
        ${t.intro.map(p => `<p>${esc(p)}</p>`).join('\n        ')}
        <div class="dyk"><h3>Did you know?</h3><ul>${t.facts.map(f => `<li>${esc(f)}</li>`).join('')}</ul></div>
        <h3>${qs.length} questions</h3>
        <p class="muted">Tap "Show answer" to check yourself. Questions go from easiest to hardest.</p>
        <ol class="tq-list">${qs.map(q => qItem(q, t.slug)).join('\n')}</ol>
        <p>These questions are part of the ${text.length.toLocaleString('en-CA')} in ${esc(siteName)}. Start a game to play them against your friends, with a timer, points and up to eight players.</p>
        ${related.length ? `<h3>More ${esc(CATS[t.cat])} trivia</h3><ul>${related.map(x => `<li><a href="/trivia/${x.slug}">${esc(x.title)}</a></li>`).join('')}</ul>` : ''}`);
  };
  for (const t of TOPICS) app.get(`/trivia/${t.slug}`, send(cache(() => topicPage(t))));

  app.get('/trivia', send(cache(() => page('trivia', 'Trivia library', `Free trivia questions with answers on ${TOPICS.length} topics: history, film and TV, music, science, geography, sport and more.`, `
        <h2>Trivia library</h2>
        <p>Free trivia questions with answers, sorted by topic. Use them for a quiz night, a classroom, a road trip, or just to test yourself. Every question here is also in the game, where you can play against up to eight friends.</p>
        <p>Looking for something visual? Try the <a href="/picture-quiz">picture quizzes</a>. Want something new every day? Try the <a href="/daily-quiz">daily quiz</a>.</p>
        ${Object.entries(CATS).map(([c, n]) => `<h3 id="${c}">${esc(n)}</h3><ul>${TOPICS.filter(t => t.cat === c).map(t => `<li><a href="/trivia/${t.slug}">${esc(t.title)}</a> – <span class="muted">${esc(t.desc.split(':')[0].replace(/ with answers$/, ''))}</span></li>`).join('')}</ul>`).join('\n        ')}`))));

  // ---------- picture quizzes ----------
  const picPage = ([key, title, filter, intro]) => {
    const all = pics.filter(filter);
    const qs = shuffled(all, rng(key)).slice(0, 24).sort((a, b) => a.d - b.d);
    const others = PICS.filter(p => p[0] !== key);
    const more = shuffled(others, rng(key + 'more')).slice(0, 6);
    return page(`picture-quiz/${key}`, title, `${title} with answers: ${intro.split('. ')[0]}.`, `
        ${crumbs([['/picture-quiz', 'Picture quizzes'], [null, title]])}
        <h2>${esc(title)}</h2>
        <p>${esc(intro)}</p>
        <p class="muted">Showing ${qs.length} of the ${all.length} pictures in this round. Tap "Show answer" to check yourself; in the game, the pictures come up at random with a timer.</p>
        <ol class="pq-list">${qs.map(q => picItem(q, key)).join('\n')}</ol>
        <p>Learn how these pictures are made in <a href="/guides/how-the-pixel-art-is-made">How the pixel art is made</a>.</p>
        <h3>More picture quizzes</h3><ul>${more.map(p => `<li><a href="/picture-quiz/${p[0]}">${esc(p[1])}</a></li>`).join('')}</ul>`);
  };
  for (const p of PICS) app.get(`/picture-quiz/${p[0]}`, send(cache(() => picPage(p))));
  app.get('/picture-quiz', send(cache(() => page('picture-quiz', 'Picture quizzes', `${PICS.length} free picture quizzes in pixel art: flags, country shapes, landmarks, skylines, aircraft, racing circuits, clouds and more.`, `
        <h2>Picture quizzes</h2>
        <p>Every picture in ${esc(siteName)} is a tiny 96 by 64 pixel drawing, most of them in classic black and white. Each quiz below shows a selection with the answers hidden. In the game you can mix pictures in with the regular questions or play pictures only.</p>
        <ul class="pq-hub">${PICS.map(([k, t, f]) => { const ex = pics.filter(f)[0]; return `<li><a href="/picture-quiz/${k}">${ex ? `<img src="${esc(ex.img)}" alt="" width="96" height="64" loading="lazy">` : ''}<span>${esc(t)}</span></a></li>`; }).join('')}</ul>
        <p>Curious how they are drawn? Read <a href="/guides/how-the-pixel-art-is-made">How the pixel art is made</a>.</p>`))));

  // ---------- daily quiz ----------
  const today = () => new Intl.DateTimeFormat('en-CA', { timeZone: TZ, year: 'numeric', month: '2-digit', day: '2-digit' }).format(new Date());
  const fmt = d => new Date(d + 'T12:00:00Z').toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' });
  const days = () => { const out = [], t = today(); for (let d = new Date(t + 'T12:00:00Z'); d.toISOString().slice(0, 10) >= LAUNCH; d.setUTCDate(d.getUTCDate() - 1)) out.push(d.toISOString().slice(0, 10)); return out; };
  const dailyQs = date => {
    const r = rng('daily' + date), qs = [];
    for (const c of Object.keys(CATS)) qs.push(...shuffled(text.filter(q => q.c === c && q.w && q.d <= 3 && q.q.length < 160), r).slice(0, 2));
    const rounds = shuffled([...new Set(pics.map(q => q.pr))], r).slice(0, 3);
    const pq = rounds.map(pr => shuffled(pics.filter(q => q.pr === pr && q.d <= 3), r)[0]).filter(Boolean);
    return { qs: shuffled(qs, r), pq };
  };
  const dailyPage = date => {
    const { qs, pq } = dailyQs(date), isToday = date === today(), list = days();
    return page(isToday ? 'daily-quiz' : `daily-quiz/${date}`, isToday ? 'Daily quiz' : `Daily quiz: ${fmt(date)}`, `${siteName} daily quiz for ${fmt(date)}: twelve trivia questions and three picture questions, with answers.`, `
        ${crumbs([['/daily-quiz', 'Daily quiz'], [null, fmt(date)]])}
        <h2>Daily quiz: ${esc(fmt(date))}</h2>
        <p>Twelve questions, two from each category, plus three picture questions. A new quiz appears every day at midnight (Eastern time). Keep score: 15 out of 15 is a perfect day.</p>
        <ol class="tq-list">${qs.map(q => qItem(q, 'daily' + date)).join('\n')}</ol>
        <h3>Picture round</h3>
        <ol class="pq-list">${pq.map(q => picItem(q, 'daily' + date)).join('\n')}</ol>
        <p>Want more? <a href="/">Start a game</a> and challenge your friends, or browse the <a href="/trivia">trivia library</a>.</p>
        ${list.length > 1 ? `<h3>Previous quizzes</h3><ul>${list.filter(d => d !== date).slice(0, 30).map(d => `<li><a href="/daily-quiz/${d}">${esc(fmt(d))}</a></li>`).join('')}</ul>` : ''}`);
  };
  app.get('/daily-quiz', (req, res) => res.type('html').set('Cache-Control', 'public, max-age=300').send(dailyPage(today())));
  app.get('/daily-quiz/:date', (req, res, next) => {
    const d = req.params.date;
    if (!/^\d{4}-\d{2}-\d{2}$/.test(d) || d < LAUNCH || d > today()) return next();
    if (d === today()) return res.redirect(301, '/daily-quiz');
    res.type('html').set('Cache-Control', 'public, max-age=86400').send(dailyPage(d));
  });

  // ---------- guides ----------
  for (const g of GUIDES) app.get(`/guides/${g.slug}`, send(cache(() => page(`guides/${g.slug}`, g.title, g.desc, `
        ${crumbs([['/guides', 'Guides'], [null, g.title]])}
        <h2>${esc(g.title)}</h2>${g.body}`))));
  app.get('/guides', send(cache(() => page('guides', 'Guides', 'Guides to hosting trivia nights, office team building, family trivia, and how Black Box Trivia\'s pixel art is made.', `
        <h2>Guides</h2>
        <ul>${GUIDES.map(g => `<li><a href="/guides/${g.slug}">${esc(g.title)}</a> – <span class="muted">${esc(g.desc)}</span></li>`).join('')}</ul>`))));

  // Links for the home page and footer
  const homeLinks = `<section class="library-links" aria-label="More trivia">
      <h2>More from ${esc(siteName)}</h2>
      <p><a href="/daily-quiz">Daily quiz</a> · <a href="/trivia">Trivia library</a> (${TOPICS.length} topics) · <a href="/picture-quiz">Picture quizzes</a> (${PICS.length} rounds) · <a href="/guides">Guides</a></p>
      <p class="muted">Popular: ${['world-war-2', 'the-simpsons', 'harry-potter', 'movie-titles-in-other-words', 'english-expressions', 'kids-trivia'].map(s => TOPICS.find(t => t.slug === s)).filter(Boolean).map(t => `<a href="/trivia/${t.slug}">${esc(t.title)}</a>`).join(' · ')} · <a href="/picture-quiz/flags">Flags quiz</a> · <a href="/picture-quiz/racing-circuits">Racing circuits</a></p>
    </section>`;

  const urls = ['/daily-quiz', '/trivia', ...TOPICS.map(t => `/trivia/${t.slug}`), '/picture-quiz', ...PICS.map(p => `/picture-quiz/${p[0]}`), '/guides', ...GUIDES.map(g => `/guides/${g.slug}`)];
  return { urls, dailyUrls: () => days().slice(1).map(d => `/daily-quiz/${d}`), homeLinks };
};
