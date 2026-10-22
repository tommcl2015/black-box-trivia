/* Plain, crawlable content pages (About, How to Play, Contact, Sample Questions), robots.txt and sitemap.xml.
 * The game itself is a one-page app; these pages give visitors and ad reviewers real text to read. */
const fs = require('fs');
const path = require('path');

const CATS = { geo: 'Geography', ent: 'Entertainment', his: 'History', art: 'Arts & Literature', sci: 'Science & Nature', spo: 'Sports & Leisure' };
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

module.exports = function pages(app, { siteName, siteUrl, contactEmail, adsenseClient, gaId, bank, pictureCount, leaderboard, version }) {
  const gaHead = gaId
    ? `<script async src="https://www.googletagmanager.com/gtag/js?id=${esc(gaId)}"></script>\n  <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','${esc(gaId)}');</script>\n  `
    : '';
  const adHead = gaHead + (adsenseClient
    ? `<meta name="google-adsense-account" content="${esc(adsenseClient)}">\n  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${esc(adsenseClient)}" crossorigin="anonymous"></script>\n`
    : '');

  // Add the AdSense account tag + script to the <head> of a static HTML file (cached after first read).
  const cache = new Map();
  const withHead = file => {
    if (!cache.has(file)) {
      const html = fs.readFileSync(path.join(__dirname, '..', 'public', file), 'utf8')
        .replace('</head>', `  ${adHead}</head>`)
        .replace(/privacy@example\.com/g, esc(contactEmail))
        .replace(/(src|href)="((?:js|css)\/[\w.-]+\.(?:js|css))"/g, `$1="$2?v=${version || ''}"`);
      cache.set(file, html);
    }
    return cache.get(file);
  };
  const send = file => (req, res) => res.type('html').set('Cache-Control', 'no-cache').send(withHead(file));
  app.get(['/', '/index.html'], send('index.html'));
  app.get(['/privacy', '/privacy.html'], send('privacy.html'));

  const nav = `<nav class="menubar"><div class="menu"><a class="mb-link" href="/">◀ Play ${esc(siteName)}</a></div></nav>`;
  const foot = `<div class="foot"><a href="/">Play</a> <span>·</span> <a href="/how-to-play">How to play</a> <span>·</span> <a href="/sample-questions">Sample questions</a> <span>·</span> <a href="/about">About</a> <span>·</span> <a href="/contact">Contact</a> <span>·</span> <a href="/privacy">Privacy</a></div>`;
  const page = (slug, title, desc, body) => `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${esc(title)} – ${esc(siteName)}</title>
  <meta name="description" content="${esc(desc)}">
  <link rel="canonical" href="${esc(siteUrl)}/${slug}">
  <link rel="stylesheet" href="/css/retro.css">
  ${adHead}</head>
<body>
  ${nav}
  <main class="desktop">
    <section class="window">
      <div class="titlebar"><span class="ttl">${esc(title)}</span></div>
      <div class="win-body prose">
${body}
        <div class="btn-row"><a class="btn default" href="/">Play now</a></div>
      </div>
    </section>
    ${foot}
  </main>
</body>
</html>`;

  const counts = {}; for (const q of bank) counts[q.c] = (counts[q.c] || 0) + 1;
  const total = bank.length.toLocaleString('en-CA');
  const catList = Object.entries(CATS).map(([k, n]) => `<li><b>${n}</b> – ${(counts[k] || 0).toLocaleString('en-CA')} questions</li>`).join('');

  const html = {
    about: page('about', 'About', `${siteName} is a free multiplayer trivia game with a classic black-and-white computer look.`, `
        <h2>About ${esc(siteName)}</h2>
        <p>${esc(siteName)} is a free trivia game for friends and family. One person starts a game, shares a six-digit code, and up to eight people join from their own phones or computers. There is nothing to download and no account to create.</p>
        <p>It was built for the moments when you want a quick game together: a party, a family night, a team break, or a long drive with kids in the back seat. If you only have one phone, Pass &amp; Play mode lets everyone take turns on the same device.</p>
        <p>The look is a tribute to the black-and-white personal computers of the 1980s: one-bit graphics, pull-down menus, little window title bars and simple beeps.</p>
        <p>${esc(siteName)} was created by <b>Tom M</b>.</p>
        <!--LEADERBOARD-->
        <h3>The questions</h3>
        <p>The game has ${total} questions in six categories:</p>
        <ul>${catList}</ul>
        <p>There are also ${(pictureCount || 0).toLocaleString('en-CA')} picture questions drawn in the same one-bit style: flags, country shapes, maps, landmarks and wonders, city skylines, US states, famous aircraft, constellations, animals and famous paintings.</p>
        <p>The collection began with questions written by the game's creator, and it has grown with new questions on film, music, TV, sports, geography, history, science and plenty of odd facts. Questions are checked against reliable sources, and we fix mistakes as soon as we hear about them.</p>
        <p>Found an error, or have a question you'd like to see in the game? <a href="/contact">Let us know</a>.</p>`),

    'how-to-play': page('how-to-play', 'How to Play', `How to play ${siteName}: start a game, share the code, answer multiple-choice and fill-in-the-blank questions, and collect all six category pieces.`, `
        <h2>How to play</h2>
        <h3>Start a game</h3>
        <ol>
          <li>Type your name and choose <b>New Game</b>.</li>
          <li>You'll get a six-digit game code. Share it, or use the <b>Share invite</b> button to send a link.</li>
          <li>Friends choose <b>Join Game</b> and type the code. Up to eight players can join.</li>
          <li>As host, pick the number of questions, the categories, picture rounds, the difficulty, the question type and the time limit, then press <b>Start Game</b>.</li>
        </ol>
        <h3>Answering</h3>
        <p>Every question is either <b>multiple choice</b> (pick A, B, C or D) or <b>fill in the blank</b> (type your answer). For typed answers, spelling doesn't have to be perfect: "Missisipi" counts for Mississippi. A different real answer does not count, so "Austria" is still wrong when the answer is Australia.</p>
        <h3>Scoring</h3>
        <ul>
          <li>A correct answer earns 100 points, or 150 for a typed answer.</li>
          <li>Answer faster for a speed bonus of up to 50 points.</li>
          <li>Harder questions are worth a little more.</li>
          <li>Get three or more in a row for a streak bonus.</li>
        </ul>
        <h3>Picture rounds</h3>
        <p>Some questions show a little black-and-white picture instead: name the flag, the country from its shape or from a map, the landmark, the city skyline, the aircraft and more. In the lobby, the host chooses <b>Mixed in</b> (about one question in four is a picture), <b>Pictures only</b>, or <b>Off</b>, and can pick which picture rounds to use.</p>
        <h3>Fill your box</h3>
        <p>Each category has its own piece of the box. Answer a question correctly in a category to earn that piece. Six categories, one box: try to fill all six before the game ends. The player with the most points wins.</p>
        <h3>Pass &amp; Play</h3>
        <p>Only one phone? Choose <b>Pass &amp; Play</b>, add everyone's names, and pass the phone around. Each player gets their own turn, and the screen hides the next question until the right person is holding the phone.</p>
        <h3>Solo practice</h3>
        <p>Play on your own to warm up. Solo games run entirely on your device.</p>
        <h3>Tips</h3>
        <ul>
          <li>If your connection drops, reopen the page and you'll rejoin your game automatically.</li>
          <li>Turn sound on or off from the <b>Sound</b> menu.</li>
          <li>Choose "Easy" difficulty for younger players.</li>
        </ul>`),

    contact: page('contact', 'Contact', `Contact the ${siteName} team.`, `
        <h2>Contact</h2>
        <p>Questions, suggestions, or found a wrong answer? We'd love to hear from you.</p>
        <p>Email: <a href="mailto:${esc(contactEmail)}">${esc(contactEmail)}</a></p>
        <p>When reporting a question, please include the question text and what you think the right answer is. Thanks for helping make the game better.</p>`)
  };

  // Sample questions: 10 per category, chosen deterministically so the page is stable between visits.
  const sample = Object.keys(CATS).map(c => {
    const qs = bank.filter(q => q.c === c && q.w && q.d <= 3 && q.q.length < 140);
    const step = Math.max(1, Math.floor(qs.length / 10));
    return [c, qs.filter((_, i) => i % step === 0).slice(0, 10)];
  });
  html['sample-questions'] = page('sample-questions', 'Sample Questions', `Sample trivia questions with answers from ${siteName}: geography, entertainment, history, arts, science and sports.`, `
        <h2>Sample trivia questions</h2>
        <p>Here's a taste of the ${total} questions in ${esc(siteName)}. Tap a question to reveal the answer.</p>
        ${sample.map(([c, qs]) => `<h3>${CATS[c]}</h3>
        <ol>${qs.map(q => `<li><details><summary>${esc(q.q)}</summary><p>Answer: <b>${esc(q.a)}</b></p></details></li>`).join('')}</ol>`).join('\n        ')}
        <p>Ready for more? Start a game and invite up to eight friends.</p>`);

  // Leaderboard tables (the About page is rendered on each visit so the scores are current)
  const lbHtml = () => {
    if (!leaderboard) return '';
    const L = leaderboard.list();
    return `<h3 id="leaderboard">Leaderboard</h3>
        <p>The ten highest scores for each game length. Scores from online, solo and Pass &amp; Play games all count.</p>
        ${leaderboard.BOARDS.map(b => `<h4>${b}-question games</h4>` + (L[b].length ? `<table class="lb"><tbody>${L[b].map((r, i) => `<tr><td>${i + 1}.</td><td>${esc(r.name)}</td><td>${r.country ? (r.country.flag ? `<img src="${esc(r.country.flag)}" alt="" width="24" height="16"> ` : '') + esc(r.country.name) : ''}</td><td class="num">${r.score.toLocaleString('en-CA')}</td></tr>`).join('')}</tbody></table>` : '<p class="muted">No scores yet. Be the first!</p>')).join('\n        ')}`;
  };
  for (const [slug, body] of Object.entries(html)) app.get([`/${slug}`, `/${slug}.html`], (req, res) => res.type('html').set('Cache-Control', 'no-cache').send(slug === 'about' ? body.replace('<!--LEADERBOARD-->', lbHtml()) : body));

  app.get('/robots.txt', (req, res) => res.type('text/plain').send(`User-agent: *\nAllow: /\nDisallow: /api/\nSitemap: ${siteUrl}/sitemap.xml\n`));
  app.get('/sitemap.xml', (req, res) => {
    const urls = ['', '/how-to-play', '/sample-questions', '/about', '/contact', '/privacy'];
    res.type('application/xml').send(`<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls.map(u => `  <url><loc>${siteUrl}${u}</loc></url>`).join('\n')}\n</urlset>\n`);
  });
};
