/* Retro Trivia – multiplayer server
 * Serves the web client and runs game rooms over Socket.IO. */
const path = require('path');
const http = require('http');
const crypto = require('crypto');
const express = require('express');
const compression = require('compression');
const helmet = require('helmet');
const { Server } = require('socket.io');
const { Room, QuestionPicker, MAX_PLAYERS } = require('../public/js/engine.js');

const PORT = process.env.PORT || 3000;
const SITE_NAME = process.env.SITE_NAME || 'Black Box Trivia';
const ADSENSE_CLIENT = process.env.ADSENSE_CLIENT ?? 'ca-pub-8705243334753575';   // set ADSENSE_CLIENT= (empty) to turn ads off
const SITE_URL = (process.env.SITE_URL || 'https://blackboxtrivia.com').replace(/\/$/, '');
const GA_ID = process.env.GA_ID ?? 'G-010HNT0LFF';   // Google Analytics 4 measurement ID, e.g. G-XXXXXXXXXX
const CONTACT_EMAIL = process.env.CONTACT_EMAIL || 'blackboxtrivia@gmail.com';
const AD_SLOTS = {
  lobby: process.env.AD_SLOT_LOBBY || '',
  reveal: process.env.AD_SLOT_REVEAL || '',
  final: process.env.AD_SLOT_FINAL || ''
};
const MAX_ROOMS = parseInt(process.env.MAX_ROOMS || '5000', 10);
const ROOM_IDLE_MS = 15 * 60 * 1000;

const bank = require('./questions.json');
const LB = require('./leaderboard.js');
// Build version: added to script/style URLs so browsers fetch fresh files after every deploy.
const VERSION = (process.env.RENDER_GIT_COMMIT || '').slice(0, 8) || Date.now().toString(36);
const picker = QuestionPicker(bank);
const textCount = bank.filter(q => !q.img).length, pictureCount = bank.length - textCount;
console.log(`Loaded ${textCount} questions and ${pictureCount} picture questions`);

const app = express();
app.set('trust proxy', 1);
app.use(compression());
// CSP is disabled so ad networks can load their scripts/iframes; other helmet protections stay on.
app.use(helmet({ contentSecurityPolicy: false, crossOriginEmbedderPolicy: false }));

app.get('/config.js', (req, res) => {
  res.type('application/javascript').set('Cache-Control', 'no-cache').send(
    `window.APP_CONFIG=${JSON.stringify({ siteName: SITE_NAME, adsenseClient: ADSENSE_CLIENT, adSlots: AD_SLOTS, contactEmail: CONTACT_EMAIL, maxPlayers: MAX_PLAYERS, questionCount: textCount, pictureCount, version: VERSION })};`
  );
});
app.get('/ads.txt', (req, res) => {
  if (!ADSENSE_CLIENT) return res.status(404).type('text/plain').send('');
  res.type('text/plain').send(`google.com, ${ADSENSE_CLIENT.replace(/^ca-/, '')}, DIRECT, f08c47fec0942fa0\n`);
});
app.get('/healthz', (req, res) => res.json({ ok: true, rooms: rooms.size, questions: textCount, pictures: pictureCount }));
app.get('/api/stats', (req, res) => {
  const byCat = {}; for (const c of Object.keys(picker.byCat)) byCat[c] = picker.count(c);
  res.json({ total: textCount, pictures: pictureCount, byCat, rooms: rooms.size });
});
// leaderboard: top 10 per game length
const clientIp = req => String(req.headers['x-forwarded-for'] || '').split(',')[0].trim() || req.ip || req.socket.remoteAddress || '';
app.get('/api/leaderboard', (req, res) => res.set('Cache-Control', 'no-cache').json({ boards: LB.BOARDS, leaders: LB.list() }));
const lbHits = new Map();   // ip -> recent submission times (flood control)
app.post('/api/leaderboard', express.json({ limit: '4kb' }), (req, res) => {
  const ip = clientIp(req), now = Date.now();
  const hits = (lbHits.get(ip) || []).filter(t => now - t < 3600e3);
  if (hits.length >= 20) return res.status(429).json({ placed: [] });
  hits.push(now); lbHits.set(ip, hits);
  const b = req.body || {};
  res.json({ placed: LB.submit(b.players, b.questions, ip, b.kind === 'pass' ? 'pass' : 'solo') });
});
setInterval(() => { const now = Date.now(); for (const [ip, h] of lbHits) if (!h.some(t => now - t < 3600e3)) lbHits.delete(ip); }, 600e3).unref();
// solo play: client fetches the bank once and runs the engine locally (no server load)
app.get('/api/questions', (req, res) => {
  res.set('Cache-Control', 'public, max-age=3600').json(bank);
});
require('./pages.js')(app, { siteName: SITE_NAME, siteUrl: SITE_URL, contactEmail: CONTACT_EMAIL, adsenseClient: ADSENSE_CLIENT, gaId: GA_ID, bank: bank.filter(q => !q.img), pictureCount, leaderboard: LB, version: VERSION });
app.use(express.static(path.join(__dirname, '..', 'public'), { maxAge: '1h', extensions: ['html'] }));

const server = http.createServer(app);
const io = new Server(server, { cors: { origin: false }, pingInterval: 10000, pingTimeout: 20000 });

/* ---------- rooms ---------- */
const rooms = new Map();          // code -> Room
const tokens = new Map();         // secret token -> { pid, code }
const playerIps = new Map();      // pid -> ip, used to show a top-10 player's country

function newCode() {
  for (let i = 0; i < 50; i++) {
    const code = String(crypto.randomInt(100000, 1000000));
    if (!rooms.has(code)) return code;
  }
  return null;
}

function makeRoom() {
  const code = newCode();
  if (!code) return null;
  const room = new Room(code, {
    picker,
    emit: (target, event, payload) => {
      if (target === null) io.to('room:' + code).emit(event, payload);
      else io.to('p:' + target).emit(event, payload);
      if (event === 'final' && target === null) {
        // multiplayer games run on the server, so their scores go straight to the leaderboard
        const placed = [];
        for (const p of payload.standings) placed.push(...LB.submit([p], payload.total, playerIps.get(p.id), 'online').map(x => Object.assign(x, { id: p.id })));
        if (placed.length) io.to('room:' + code).emit('leaderboard', { placed });
      }
    }
  });
  rooms.set(code, room);
  return room;
}

function destroyRoom(code) {
  const r = rooms.get(code); if (!r) return;
  for (const pid of r.players.keys()) playerIps.delete(pid);
  r.destroy(); rooms.delete(code);
  for (const [t, v] of tokens) if (v.code === code) tokens.delete(t);
}

setInterval(() => {
  const now = Date.now();
  for (const [code, r] of rooms) {
    if (r.isEmpty() && now - r.lastActive > ROOM_IDLE_MS) destroyRoom(code);
    else if (now - r.lastActive > 3 * 60 * 60 * 1000) destroyRoom(code); // hard cap 3h idle
  }
}, 60 * 1000).unref();

/* ---------- sockets ---------- */
io.on('connection', socket => {
  let token = String((socket.handshake.auth && socket.handshake.auth.token) || '').slice(0, 64);
  if (!/^[a-zA-Z0-9_-]{16,64}$/.test(token)) token = crypto.randomBytes(18).toString('base64url');
  socket.emit('hello', { token });

  let session = tokens.get(token) || null;   // { pid, code }
  const room = () => session && rooms.get(session.code);

  // reconnect to an existing room automatically
  if (session && room()) {
    socket.join('room:' + session.code); socket.join('p:' + session.pid);
    socket.emit('rejoined', { code: session.code, you: session.pid });
    room().setConnected(session.pid, true);
    room().syncPlayer(session.pid);
  } else session = null;

  // simple flood control
  let bucket = 30, last = Date.now();
  const allow = () => {
    const now = Date.now(); bucket = Math.min(30, bucket + (now - last) / 100); last = now;
    if (bucket < 1) return false; bucket -= 1; return true;
  };

  function enter(r, name, ack) {
    if (session) leave();
    const pid = crypto.randomBytes(6).toString('hex');
    const res = r.addPlayer(pid, LB.cleanName(name));
    if (!res.ok) return ack && ack(res);
    session = { pid, code: r.code };
    tokens.set(token, session);
    playerIps.set(pid, String(socket.handshake.headers['x-forwarded-for'] || '').split(',')[0].trim() || socket.handshake.address);
    socket.join('room:' + r.code); socket.join('p:' + pid);
    r.lastActive = Date.now();
    ack && ack({ ok: true, code: r.code, you: pid });
    r.broadcastRoom(); r.syncPlayer(pid);
  }

  function leave() {
    const r = room();
    if (r) {
      r.removePlayer(session.pid);
      socket.leave('room:' + r.code); socket.leave('p:' + session.pid);
      if (r.players.size === 0) destroyRoom(r.code);
    }
    tokens.delete(token); session = null;
  }

  const on = (ev, fn) => socket.on(ev, (...args) => {
    if (!allow()) return;
    try { fn(...args); } catch (e) { console.error(ev, e); }
  });

  on('create', (data, ack) => {
    if (typeof ack !== 'function') ack = () => {};
    if (rooms.size >= MAX_ROOMS) return ack({ ok: false, error: 'Servers are busy. Try again in a minute.' });
    const r = makeRoom();
    if (!r) return ack({ ok: false, error: 'Could not create a game code. Try again.' });
    if (data && data.settings) r.settings = require('../public/js/engine.js').cleanSettings(data.settings);
    if (data && data.seen) r.addSeen(data.seen);
    enter(r, data && data.name, ack);
  });

  on('join', (data, ack) => {
    if (typeof ack !== 'function') ack = () => {};
    const code = String((data && data.code) || '').replace(/\D/g, '');
    const r = rooms.get(code);
    if (!r) return ack({ ok: false, error: 'No game found with code ' + (code || '??????') + '.' });
    if (session && session.code === code && r.players.has(session.pid)) { r.setConnected(session.pid, true); return ack({ ok: true, code, you: session.pid }); }
    if (data && data.seen) r.addSeen(data.seen);
    enter(r, data && data.name, ack);
  });

  on('leave', () => leave());
  on('settings', s => { const r = room(); if (r) { r.lastActive = Date.now(); r.updateSettings(session.pid, s); } });
  on('start', (_, ack) => { const r = room(); if (!r) return; r.lastActive = Date.now(); const res = r.start(session.pid); if (typeof ack === 'function') ack(res); });
  on('answer', d => { const r = room(); if (r) { r.lastActive = Date.now(); r.answer(session.pid, d); } });
  on('next', () => { const r = room(); if (r) r.hostNext(session.pid); });
  on('lobby', () => { const r = room(); if (r) r.backToLobby(session.pid); });
  on('kick', d => { const r = room(); if (r && d) { const target = d.id; r.kick(session.pid, target); io.in('p:' + target).socketsLeave(['room:' + r.code]); for (const [t, v] of tokens) if (v.pid === target) tokens.delete(t); } });
  on('react', d => {
    const r = room(); if (!r || !d) return;
    const e = String(d.e || '').slice(0, 8);
    if (['👍', '😂', '😮', '🔥', '👏', '😭'].includes(e)) io.to('room:' + r.code).emit('react', { id: session.pid, e });
  });

  socket.on('disconnect', () => {
    const r = room();
    if (r) {
      // only mark offline if no other socket of this player is still connected
      const still = io.sockets.adapter.rooms.get('p:' + session.pid);
      if (!still || still.size === 0) r.setConnected(session.pid, false);
    }
  });
});

server.listen(PORT, () => console.log(`${SITE_NAME} listening on http://localhost:${PORT}`));
