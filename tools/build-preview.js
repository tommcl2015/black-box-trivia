#!/usr/bin/env node
/* Builds a single self-contained HTML file (solo play only, no server) for previews. */
const fs = require('fs');
const path = require('path');
const R = p => fs.readFileSync(path.join(__dirname, '..', p), 'utf8');
const out = process.argv[2] || path.join(__dirname, '..', 'preview.html');
const mock = process.argv[3] ? fs.readFileSync(process.argv[3], 'utf8') : '';

const woff2 = fs.readFileSync(path.join(__dirname, '..', 'public/fonts/ChicagoFLF.woff2')).toString('base64');
let css = R('public/css/retro.css')
  .replace(/src: url\('..\/fonts\/ChicagoFLF.woff2'\)[^;]+;/, `src: url(data:font/woff2;base64,${woff2}) format('woff2');`);
css += `\n.desktop{padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}\n`;
const bank = R('server/questions.json');
const cfg = { siteName: 'Black Box Trivia', adsenseClient: '', adSlots: {}, maxPlayers: 8, questionCount: JSON.parse(bank).length, adPreview: true, offline: false, transport: 'room' };
const body = R('public/index.html').split('<body>')[1].split('<script')[0];
const js = ['match.js', 'engine.js', 'sounds.js', 'art.js', 'roomnet.js', 'app.js'].map(f => R('public/js/' + f)).join('\n;\n');

const html = `<title>Black Box Trivia</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>${css}</style>
${body}
${mock ? '<script>' + mock + '</script>' : ''}
<script>window.APP_CONFIG=${JSON.stringify(cfg)};window.EMBEDDED_BANK=${bank};</script>
<script>${js.replace(/<\/script>/g, '<\\/script>')}</script>
`;
fs.writeFileSync(out, html);
console.log('wrote', out, (html.length / 1024).toFixed(0) + ' KB');
