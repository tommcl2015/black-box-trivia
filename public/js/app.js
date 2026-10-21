/* Black Box Trivia – client */
(function () {
  'use strict';
  const CFG = Object.assign({ siteName: 'Black Box Trivia', adsenseClient: '', adSlots: {}, maxPlayers: 8, questionCount: 0, adPreview: false, offline: false }, window.APP_CONFIG || {});
  const { CAT_NAMES, CATS } = window.TriviaEngine;
  const $ = s => document.querySelector(s);
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const store = {
    get(k, d) { try { const v = localStorage.getItem('td_' + k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem('td_' + k, JSON.stringify(v)); } catch (e) {} },
    del(k) { try { localStorage.removeItem('td_' + k); } catch (e) {} }
  };
  const fmtCode = c => c ? String(c).replace(/^(\d{3})(\d{3})$/, '$1 $2') : '';
  const isLocalhost = /^(localhost|127\.|0\.0\.0\.0)/.test(location.hostname);
  const adPreview = CFG.adPreview || /[?&]ads=preview/.test(location.search) || (isLocalhost && !CFG.adsenseClient);

  /* ================= state ================= */
  const S = {
    screen: 'home', name: store.get('name', ''), me: null, room: null, q: null, reveal: null, final: null,
    myAnswer: null, deadline: 0, net: null, mode: null, prevPlayers: 0, joinCode: ''
  };

  /* ================= networking ================= */
  function OnlineNet() {
    const handlers = {};
    let token = store.get('token', null);
    const socket = window.io({ auth: { token }, transports: ['websocket', 'polling'] });
    socket.on('hello', d => { token = d.token; store.set('token', token); });
    socket.on('connect_error', () => setStatus('Connecting…'));
    socket.on('disconnect', () => { setStatus('Reconnecting…'); });
    socket.on('connect', () => setStatus(''));
    ['room', 'question', 'reveal', 'final', 'starting', 'answerAck', 'kicked', 'rejoined', 'react'].forEach(ev => socket.on(ev, d => (handlers[ev] || []).forEach(fn => fn(d))));
    return {
      kind: 'online',
      on(ev, fn) { (handlers[ev] = handlers[ev] || []).push(fn); },
      emit(ev, data, ack) { socket.emit(ev, data, ack); },
      close() { socket.close(); }
    };
  }

  let bankPromise = null;
  function loadBank() {
    if (window.EMBEDDED_BANK) return Promise.resolve(window.EMBEDDED_BANK);
    if (!bankPromise) bankPromise = fetch('/api/questions').then(r => { if (!r.ok) throw new Error('load'); return r.json(); });
    return bankPromise;
  }

  function LocalNet(bank, pass) {
    const handlers = {};
    const fire = (ev, d) => (handlers[ev] || []).forEach(fn => fn(d));
    const room = new TriviaEngine.Room(pass ? 'PASS' : 'SOLO', {
      picker: TriviaEngine.QuestionPicker(bank), solo: !pass, turns: !!pass,
      emit: (target, ev, payload) => setTimeout(() => fire(ev, JSON.parse(JSON.stringify(payload))), 0)
    });
    let me = 'me';
    const turnPlayer = () => (room.turnOrder && room.turnOrder[room.turnIdx]) || me;
    return {
      kind: 'local', room,
      on(ev, fn) { (handlers[ev] = handlers[ev] || []).push(fn); },
      emit(ev, data, ack) {
        ack = typeof ack === 'function' ? ack : () => {};
        switch (ev) {
          case 'create':
            if (data && data.settings) room.settings = TriviaEngine.cleanSettings(data.settings);
            if (pass) {
              (data.names || []).forEach((n, i) => room.addPlayer('p' + (i + 1), n));
              me = 'p1'; ack({ ok: true, code: 'PASS', you: me });
            } else ack(Object.assign(room.addPlayer(me, data && data.name), { code: 'SOLO', you: me }));
            break;
          case 'settings': room.updateSettings(me, data); break;
          case 'start': ack(room.start(me)); break;
          case 'beginTurn': room.beginTurn(); break;
          case 'answer': room.answer(pass ? turnPlayer() : me, data); break;
          case 'next': room.hostNext(me); break;
          case 'lobby': room.backToLobby(me); break;
          case 'leave': room.destroy(); break;
          case 'react': setTimeout(() => fire('react', { id: me, e: data.e }), 0); break;
        }
      },
      close() { room.destroy(); }
    };
  }

  function bindNet(net) {
    S.net = net;
    net.on('room', onRoom);
    net.on('question', onQuestion);
    net.on('reveal', onReveal);
    net.on('final', onFinal);
    net.on('starting', () => Sounds.start());
    net.on('turn', d => { S.turn = d; S.q = null; S.myAnswer = null; stopTimer(); go('handoff'); Sounds.join(); });
    net.on('kicked', d => { teardown(); go('home'); alertBox('stop', d.message || 'You were removed from the game.'); });
    net.on('rejoined', d => { S.me = d.you; store.set('session', { code: d.code }); if (S.room) render(); toast('Reconnected to game ' + fmtCode(d.code)); });
    net.on('react', d => floatReaction(d.e));
  }

  function online() {
    if (S.net && S.net.kind === 'online') return S.net;
    if (S.net) S.net.close();
    let net;
    if (CFG.transport === 'room' && window.RoomNet) net = window.RoomNet(loadBank);
    else if (window.io) net = OnlineNet();
    else { alertBox('stop', 'Online play is not available here. Try Solo Practice.'); return null; }
    bindNet(net); S.mode = 'online'; return net;
  }

  function teardown() {
    if (S.net) { try { S.net.emit('leave'); } catch (e) {} S.net.close(); }
    S.net = null; S.room = null; S.q = null; S.reveal = null; S.final = null; S.me = null; S.mode = null;
    store.del('session');
    stopTimer();
    renderMenubar();
  }

  /* ================= event handlers ================= */
  function onRoom(r) {
    const prev = S.room;
    S.room = r;
    if (prev && r.state === 'lobby') {
      if (r.players.length > S.prevPlayers) Sounds.join();
      else if (r.players.length < S.prevPlayers) Sounds.leave();
    }
    S.prevPlayers = r.players.length;
    if (r.state === 'lobby' && S.screen !== 'lobby') go('lobby');
    else if (S.screen === 'lobby') renderLobby();
    else if (S.screen === 'question') updateAnswerStrip();
    renderMenubar();
  }

  function onQuestion(q) {
    if (S.room && S.room.passPlay && S.turn) S.me = S.turn.id;
    S.q = q; S.myAnswer = null; S.reveal = null;
    S.deadline = performance.now() + q.remainingMs;
    S.lastTick = null;
    go('question');
    Sounds.whoosh();
  }

  function onReveal(rv) {
    S.reveal = rv; stopTimer();
    go('reveal');
    const mine = (S.room && S.room.passPlay) ? (rv.results.find(x => x.correct) || rv.results[0]) : rv.results.find(x => x.id === S.me);
    if (mine && mine.correct) Sounds.correct();
    else if (mine && !mine.answered) Sounds.timeout();
    else Sounds.wrong();
  }

  function onFinal(f) {
    S.final = f; stopTimer(); go('final');
    const mine = (S.room && S.room.passPlay) ? f.standings[0] : f.standings.find(x => x.id === S.me);
    if (mine && mine.rank === 1) Sounds.win(); else Sounds.lose();
  }

  /* ================= navigation ================= */
  function go(screen) {
    S.screen = screen;
    render();
    window.scrollTo(0, 0);
  }

  function render() {
    const fns = { home: renderHome, join: renderJoin, ppsetup: renderPassSetup, handoff: renderHandoff, lobby: renderLobby, question: renderQuestion, reveal: renderReveal, final: renderFinal, help: renderHelp, about: renderAbout };
    (fns[S.screen] || renderHome)();
    renderMenubar();
    renderFoot();
  }

  /* ================= building blocks ================= */
  function win({ title, body, cls = '', close = null, status = '' }) {
    return `<section class="window ${cls}" role="dialog" aria-label="${esc(title)}">
      <div class="titlebar">${close ? `<button class="closebox" data-act="${close}" aria-label="Close"></button>` : ''}<span class="ttl">${esc(title)}</span></div>
      <div class="win-body">${body}</div>${status ? `<div class="statusbar">${status}</div>` : ''}
    </section>`;
  }

  function ad(slotKey) {
    const slot = CFG.adSlots && CFG.adSlots[slotKey];
    if (CFG.adsenseClient && slot) {
      return `<div class="ad-wrap"><section class="window"><div class="titlebar"><span class="ttl">Advertisement</span></div>
        <div class="win-body tight ad-slot"><ins class="adsbygoogle" style="display:block" data-ad-client="${esc(CFG.adsenseClient)}" data-ad-slot="${esc(slot)}" data-ad-format="auto" data-full-width-responsive="true"></ins></div></section></div>`;
    }
    if (!CFG.adsenseClient && adPreview) {
      return `<div class="ad-wrap"><section class="window"><div class="titlebar"><span class="ttl">Advertisement</span></div>
        <div class="win-body tight ad-slot"><div class="ad-placeholder"><span>Ad space · "${esc(slotKey)}" slot</span><span class="small">Shows a Google AdSense unit once configured</span></div></div></section></div>`;
    }
    return '';
  }

  function pushAds() {
    if (!CFG.adsenseClient) return;
    document.querySelectorAll('ins.adsbygoogle:not([data-adsbygoogle-status])').forEach(() => {
      try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
    });
  }

  function mount(html) {
    $('#app').innerHTML = html;
    pushAds();
  }

  const isHost = () => S.room && (S.room.passPlay || S.room.hostId === S.me);
  const meP = () => S.room && S.room.players.find(p => p.id === S.me);

  /* ================= HOME ================= */
  function renderHome() {
    const count = CFG.questionCount ? CFG.questionCount.toLocaleString() + ' questions · ' : '';
    mount(win({
      title: CFG.siteName, cls: 'narrow',
      body: `
        <div class="bb-logo">
          <div class="bb-box">${Art.pie(CATS, 'lg', 2.5)}</div>
          <div class="bb-word"><span class="bb-inv">BLACK BOX</span><span class="bb-sub">TRIVIA</span>
            <div class="tagline">${count}up to ${CFG.maxPlayers} players<br>Six categories. One box.</div></div>
        </div>
        <hr class="divider">
        <form id="homeForm" autocomplete="off">
          <div class="field"><label for="name">Your name</label>
            <input class="text" id="name" maxlength="16" value="${esc(S.name)}" placeholder="e.g. Tom" autocapitalize="words" enterkeyhint="go"></div>
          <div class="btn-stack">
            <button class="btn default big block" type="submit" data-act="new" ${CFG.offline ? 'disabled' : ''}><span>New Game</span></button>
            <button class="btn big block" type="button" data-act="goJoin" ${CFG.offline ? 'disabled' : ''}><span>Join Game</span></button>
            <button class="btn block" type="button" data-act="goPass"><span>Pass &amp; Play (one phone)</span></button>
            <button class="btn block" type="button" data-act="solo"><span>Solo Practice</span></button>
          </div>
          ${CFG.offline ? '<p class="small center">Preview build: online play needs the server. Solo works here.</p>' : ''}
          ${CFG.transport === 'room' ? '<p class="small center">Preview: friends join with the code while signed in to Claude, with this page shared to them.</p>' : ''}
        </form>`,
      status: `<span>Host a game and share the code</span><span>v1.0</span>`
    }));
    const f = $('#homeForm');
    f.addEventListener('submit', e => { e.preventDefault(); act('new'); });
  }

  function readName() {
    const el = $('#name');
    const n = (el ? el.value : S.name).trim().slice(0, 16);
    if (!n) { if (el) { el.focus(); el.classList.add('shake'); setTimeout(() => el.classList.remove('shake'), 400); } Sounds.beep(); return null; }
    S.name = n; store.set('name', n); return n;
  }

  /* ================= JOIN ================= */
  function renderJoin() {
    mount(win({
      title: 'Join Game', cls: 'narrow', close: 'home',
      body: `
        <form id="joinForm" autocomplete="off">
          <div class="field"><label for="code">Enter the 6-digit game code</label>
            <input class="text code" id="code" inputmode="numeric" pattern="[0-9]*" maxlength="7" value="${esc(S.joinCode)}" placeholder="000000" autocomplete="one-time-code" enterkeyhint="go"></div>
          <div class="field"><label for="name">Your name</label>
            <input class="text" id="name" maxlength="16" value="${esc(S.name)}" placeholder="e.g. Sam" autocapitalize="words"></div>
          <div class="btn-row"><button class="btn" type="button" data-act="home">Cancel</button><button class="btn default" type="submit">Join</button></div>
        </form>`
    }));
    const code = $('#code');
    code.addEventListener('input', () => { code.value = code.value.replace(/\D/g, '').slice(0, 6); S.joinCode = code.value; });
    $('#joinForm').addEventListener('submit', e => { e.preventDefault(); doJoin(); });
    (S.joinCode.length === 6 ? $('#name') : code).focus();
  }

  function doJoin() {
    const code = ($('#code').value || '').replace(/\D/g, '');
    if (code.length !== 6) { Sounds.beep(); return alertBox('caution', 'Game codes are 6 digits.'); }
    const name = readName(); if (!name) return;
    const net = online(); if (!net) return;
    busy(true);
    net.emit('join', { code, name }, res => {
      busy(false);
      if (!res || !res.ok) { Sounds.beep(); return alertBox('stop', (res && res.error) || 'Could not join that game.'); }
      S.me = res.you; store.set('session', { code: res.code });
      history.replaceState(null, '', location.pathname);
    });
  }

  /* ================= PASS & PLAY ================= */
  function renderPassSetup() {
    if (!S.ppNames) S.ppNames = store.get('ppnames', null) || [S.name || '', ''];
    while (S.ppNames.length < 2) S.ppNames.push('');
    const rows = S.ppNames.map((n, i) => `<div class="pp-row">${Art.icon(['disk', 'bomb', 'watch', 'cup', 'bug', 'rocket', 'dog', 'globe'][i])}
        <input class="text" id="pp${i}" data-i="${i}" maxlength="16" value="${esc(n)}" placeholder="Player ${i + 1}" autocapitalize="words">
        ${S.ppNames.length > 2 ? `<button class="btn small" type="button" data-act="ppDel" data-i="${i}" aria-label="Remove player ${i + 1}">−</button>` : ''}</div>`).join('');
    mount(win({
      title: 'Pass & Play', cls: 'narrow', close: 'home',
      body: `<p class="muted" style="margin-top:0">Everyone shares this phone. Before each question it tells you who to pass it to, so nobody sees the others' answers.</p>
        <form id="ppForm" autocomplete="off"><div class="pp-list">${rows}</div>
        ${S.ppNames.length < 8 ? '<button class="btn small" type="button" data-act="ppAdd">+ Add player</button>' : ''}
        <div class="btn-row"><button class="btn" type="button" data-act="home">Cancel</button><button class="btn default" type="submit">Next ▸</button></div></form>`,
      status: `<span>2 to 8 players</span><span>${S.ppNames.length} of 8</span>`
    }));
    $('#app').querySelectorAll('.pp-row input').forEach(el => el.addEventListener('input', () => { S.ppNames[+el.dataset.i] = el.value; }));
    $('#ppForm').addEventListener('submit', e => { e.preventDefault(); startPass(); });
    const empty = $('#app').querySelector('.pp-row input[value=""]'); if (empty) empty.focus();
  }

  async function startPass() {
    const names = S.ppNames.map(n => n.trim()).filter(Boolean);
    if (names.length < 2) { Sounds.beep(); return alertBox('caution', 'Add at least two players.'); }
    store.set('ppnames', names);
    busy(true);
    try {
      const bank = await loadBank();
      if (S.net) S.net.close();
      const net = LocalNet(bank, true); bindNet(net); S.mode = 'local';
      net.emit('create', { names, settings: store.get('settings', null) }, res => { S.me = res.you; });
    } catch (e) { alertBox('stop', 'Could not load questions. Check your connection.'); }
    busy(false);
  }

  function renderHandoff() {
    const t = S.turn; if (!t) return;
    mount(win({
      title: `Question ${t.index + 1} of ${t.total}`, cls: 'narrow',
      body: `<div class="handoff">
          <div class="muted">Pass the phone to</div>
          ${Art.icon(t.icon, 'xl')}
          <div class="handoff-name">${esc(t.name)}</div>
          <div class="q-cat" style="justify-content:center">${Art.swatch(t.category)}<span>${esc(t.categoryName)}</span></div>
          <button class="btn default big block" data-act="beginTurn">I'm ${esc(t.name)} — show question</button>
          <div class="muted">Turn ${t.turn + 1} of ${t.turns} · no peeking!</div>
        </div>`
    }));
  }

  /* ================= LOBBY ================= */
  function renderLobby() {
    const r = S.room; if (!r) return renderHome();
    const host = isHost();
    const st = r.settings;
    const slots = [];
    for (let i = 0; i < r.maxPlayers; i++) {
      const p = r.players[i];
      if (!p) { slots.push(`<div class="player-slot empty">${r.solo ? '' : 'waiting…'}</div>`); continue; }
      slots.push(`<div class="player-slot ${p.id === S.me ? 'me' : ''} ${p.connected ? '' : 'offline'}">
        ${host && p.id !== S.me && !r.solo && !r.passPlay ? `<button class="kick" data-act="kick" data-id="${esc(p.id)}" aria-label="Remove ${esc(p.name)}">×</button>` : ''}
        ${Art.icon(p.icon)}<span class="nm">${esc(p.name)}</span>
        <span class="tag">${r.passPlay ? 'player ' + (i + 1) : (p.isHost ? 'host' : p.connected ? '' : 'offline') + (p.id === S.me ? (p.isHost ? ' · you' : 'you') : '')}</span></div>`);
    }
    const dis = host ? '' : 'disabled';
    const radio = (name, val, label) => `<label class="opt"><input type="radio" name="${name}" value="${val}" ${st[name] === val ? 'checked' : ''} ${dis}><span>${label}</span></label>`;
    const cats = CATS.map(c => `<label class="opt cat-opt"><input type="checkbox" name="cat" value="${c}" ${st.categories.includes(c) ? 'checked' : ''} ${dis}>${Art.swatch(c)}<span>${CAT_NAMES[c]}</span></label>`).join('');
    const presets = [5, 10, 20, 30, 50].map(n => `<button class="btn small ${st.numQuestions === n ? 'pressed' : ''}" data-act="nq" data-n="${n}" ${dis}>${n}</button>`).join('');
    const times = [10, 15, 20, 30, 45, 60].map(t => `<option value="${t}" ${st.timeLimit === t ? 'selected' : ''}>${t} seconds</option>`).join('');

    const codeBox = (r.solo || r.passPlay) ? '' : `
      <div class="code-box"><div class="label">Game code — share it with friends</div>
        <div class="code" id="codeText">${fmtCode(r.code)}</div>
        <div class="btn-row center" style="margin-top:0">${CFG.transport === 'room' ? '' : '<button class="btn small" data-act="share">Share invite</button>'}<button class="btn small" data-act="copy">${CFG.transport === 'room' ? 'Copy code' : 'Copy link'}</button></div>
      </div>`;

    mount(win({
      title: r.solo ? 'Solo Practice' : r.passPlay ? `Pass & Play — ${r.players.length} players` : `Lobby — ${r.players.length} of ${r.maxPlayers} players`, cls: 'wide', close: 'leave',
      body: `${codeBox}
        ${r.solo ? '' : `<h3>Players</h3><div class="players">${slots.join('')}</div><hr class="divider">`}
        <h3>Game settings ${host ? '' : '<span class="pill">set by host</span>'}</h3>
        <div class="settings-grid">
          <div class="lbl">Questions</div>
          <div style="display:flex;align-items:center;flex-wrap:wrap;gap:6px">
            <div class="stepper"><button data-act="nqm" ${dis} aria-label="Fewer">−</button><output>${st.numQuestions}</output><button data-act="nqp" ${dis} aria-label="More">+</button></div>
            <div class="presets">${presets}</div></div>
          <div class="lbl">Categories</div><div class="cat-grid">${cats}</div>
          <div class="lbl">Question type</div><div class="radio-group">${radio('mode', 'mixed', 'Mixed')}${radio('mode', 'mc', 'Multiple choice (A–D)')}${radio('mode', 'fib', 'Fill in the blank')}</div>
          <div class="lbl">Difficulty</div><div class="radio-group">${radio('difficulty', 'any', 'Any')}${radio('difficulty', 'easy', 'Easy')}${radio('difficulty', 'medium', 'Medium')}${radio('difficulty', 'hard', 'Hard')}</div>
          <div class="lbl"><label for="timeSel">Time per question</label></div><div><select class="select" id="timeSel" ${dis}>${times}</select> <span class="muted">+10s for fill-in</span></div>
        </div>
        <div class="btn-row">
          <button class="btn" data-act="leave">${r.solo || r.passPlay ? 'Quit' : 'Leave'}</button>
          ${r.passPlay ? '<button class="btn" data-act="editPlayers">Edit players</button>' : ''}
          ${host ? `<button class="btn default big" data-act="start">Start Game</button>` : `<span class="muted"><span class="blink">▪</span> Waiting for ${esc((r.players.find(p => p.isHost) || {}).name || 'host')} to start…</span>`}
        </div>`,
      status: `<span>${r.solo ? 'Practice on your own' : r.passPlay ? 'Everyone takes turns on this device' : 'Up to 8 players · anyone can join with the code'}</span><span>${(CFG.questionCount || '').toLocaleString()} questions</span>`
    }) + ad('lobby'));

    if (host) {
      $('#app').querySelectorAll('input[type=radio]').forEach(el => el.addEventListener('change', () => sendSettings({ [el.name]: el.value })));
      $('#app').querySelectorAll('input[name=cat]').forEach(el => el.addEventListener('change', () => {
        const cats = [...$('#app').querySelectorAll('input[name=cat]:checked')].map(x => x.value);
        if (!cats.length) { el.checked = true; Sounds.beep(); return; }
        sendSettings({ categories: cats });
      }));
      $('#timeSel').addEventListener('change', e => sendSettings({ timeLimit: +e.target.value }));
    }
  }

  function sendSettings(s) { Sounds.click(); S.net && S.net.emit('settings', s); }

  /* ================= QUESTION ================= */
  let rafId = null;
  function renderQuestion() {
    const q = S.q; if (!q) return;
    const keys = ['A', 'B', 'C', 'D'];
    const diff = [1, 2, 3, 4, 5].map(i => `<i class="${i <= q.difficulty ? 'on' : ''}"></i>`).join('');
    let answerUi;
    if (q.type === 'mc') {
      answerUi = `<div class="choices">${q.choices.map((c, i) => `<button class="choice" data-act="pick" data-i="${i}"><span class="key">${keys[i]}</span><span>${esc(c)}</span></button>`).join('')}</div>`;
    } else {
      answerUi = `<form id="fibForm" autocomplete="off"><div class="fib-row">
          <input class="text" id="fib" maxlength="80" placeholder="Type your answer…" autocapitalize="off" autocorrect="off" spellcheck="false" enterkeyhint="send">
          <button class="btn default" type="submit">Submit</button></div>
          <div class="fib-hint">Spelling doesn't need to be perfect.</div></form>`;
    }
    mount(win({
      title: S.room && S.room.passPlay && S.turn ? `${S.turn.name} — Question ${q.index + 1} of ${q.total}` : `Question ${q.index + 1} of ${q.total}`, cls: 'wide',
      body: `
        <div class="q-head"><div class="q-cat">${Art.swatch(q.category)}<span>${esc(q.categoryName)}</span></div>
          <div style="display:flex;align-items:center;gap:8px"><span class="muted">${q.type === 'mc' ? 'Multiple choice' : 'Fill in the blank'}</span><span class="diff" title="Difficulty ${q.difficulty}/5">${diff}</span></div></div>
        <div class="timer" id="timer"><div class="fill" id="timerFill"></div><span class="secs" id="timerSecs"></span></div>
        <div class="q-text">${esc(q.text)}</div>
        <div id="answerArea">${answerUi}</div>
        <div id="waitArea"></div>
        <div class="answer-strip" id="strip"></div>`
    }));
    if (q.type === 'fib') {
      const inp = $('#fib');
      $('#fibForm').addEventListener('submit', e => {
        e.preventDefault();
        const v = inp.value.trim(); if (!v) { Sounds.beep(); return; }
        submitAnswer({ text: v }, v);
      });
      setTimeout(() => inp.focus(), 50);
    }
    updateAnswerStrip();
    startTimer();
  }

  function submitAnswer(data, label) {
    if (S.myAnswer || !S.q) return;
    S.myAnswer = { data, label };
    Sounds.click();
    S.net.emit('answer', data);
    if (S.q.type === 'mc') {
      document.querySelectorAll('.choice').forEach((b, i) => { b.disabled = true; if (i === data.choice) b.classList.add('picked'); else b.classList.add('dim'); });
    } else {
      $('#fib').disabled = true; $('#fibForm button').disabled = true;
    }
    const others = S.room && S.room.players.filter(p => p.connected).length > 1;
    const msg = S.room && S.room.passPlay ? 'Locked in! Pass the phone on…' : `Answer locked in${others ? ' — waiting for the others…' : '…'}`;
    $('#waitArea').innerHTML = `<div class="waiting">${Art.icon('watch')}<span>${msg}</span></div>`;
  }

  function updateAnswerStrip() {
    const el = $('#strip'); if (!el || !S.room) return;
    if (S.room.solo) { el.hidden = true; return; }
    if (S.room.passPlay) { el.innerHTML = `<span class="muted">${esc(S.turn ? S.turn.name : '')}'s turn · ${S.turn ? S.turn.turn + 1 : 1} of ${S.turn ? S.turn.turns : 1}</span>`; return; }
    el.innerHTML = S.room.players.filter(p => p.connected).map(p => `<span class="chip ${p.answered ? 'done' : ''}">${Art.icon(p.icon, 'sm')}${esc(p.name)}${p.answered ? ' ✓' : ''}</span>`).join('');
  }

  function startTimer() {
    stopTimer();
    const total = S.q.timeLimit * 1000;
    const fill = $('#timerFill'), secsEl = $('#timerSecs'), box = $('#timer');
    const loop = () => {
      const left = Math.max(0, S.deadline - performance.now());
      if (fill) fill.style.transform = `scaleX(${left / total})`;
      const secs = Math.ceil(left / 1000);
      if (secsEl) { secsEl.textContent = secs + 's'; secsEl.style.display = 'block'; }
      if (left <= 5000 && box) box.classList.add('urgent');
      if (left > 0 && left <= 5000 && S.lastTick !== secs && !S.myAnswer) { S.lastTick = secs; Sounds.tick(); }
      if (left > 0) rafId = requestAnimationFrame(loop);
      else if (!S.myAnswer) {
        document.querySelectorAll('.choice').forEach(b => { b.disabled = true; b.classList.add('dim'); });
        const f = $('#fib'); if (f) { f.disabled = true; }
        const w = $('#waitArea'); if (w && !w.innerHTML) w.innerHTML = `<div class="waiting">${Art.icon('watch')}<span>Time's up!</span></div>`;
      }
    };
    rafId = requestAnimationFrame(loop);
  }
  function stopTimer() { if (rafId) cancelAnimationFrame(rafId); rafId = null; }

  /* ================= REVEAL ================= */
  let nextTimer = null;
  function renderReveal() {
    const rv = S.reveal; if (!rv) return;
    const mine = rv.results.find(x => x.id === S.me) || {};
    const keys = ['A', 'B', 'C', 'D'];
    let choices = '';
    if (rv.type === 'mc' && rv.choices) {
      choices = `<div class="choices" style="margin-bottom:14px">${rv.choices.map((c, i) => {
        const cls = i === rv.correctIndex ? 'right' : (!(S.room && S.room.passPlay) && mine.choice === i ? 'wrong' : 'dim');
        return `<button class="choice ${cls}" disabled><span class="key">${keys[i]}</span><span>${esc(c)}</span></button>`;
      }).join('')}</div>`;
    }
    const pp = S.room && S.room.passPlay;
    const nRight = rv.results.filter(x => x.correct).length;
    const verdict = pp ? (nRight === 0 ? 'Nobody got it!' : nRight === rv.results.length ? 'Everyone got it!' : `${nRight} of ${rv.results.length} got it right`) : mine.correct ? `Correct! +${mine.points}${mine.streak >= 3 ? ` · ${mine.streak} in a row` : ''}` : mine.answered ? 'Not quite.' : "Time's up!";
    const sorted = rv.players.slice().sort((a, b) => b.score - a.score);
    const resById = Object.fromEntries(rv.results.map(x => [x.id, x]));
    const rows = sorted.map((p, i) => {
      const r = resById[p.id] || {};
      return `<tr class="${p.id === S.me ? 'me' : ''}"><td style="width:22px">${i + 1}.</td><td class="ic">${Art.icon(p.icon, 'sm')}</td>
        <td>${esc(p.name)}<div class="ans muted">${r.answered ? esc(r.text) : '—'}</div></td>
        <td style="width:24px"><span class="mark ${r.correct ? 'ok' : ''}">${r.correct ? '✓' : '×'}</span></td>
        <td class="pts">${r.points ? '+' + r.points : ''}<br><b>${p.score}</b></td><td style="width:40px">${Art.pie(p.wedges)}</td></tr>`;
    }).join('');
    const reactions = S.room && !S.room.solo && !S.room.passPlay ? `<div class="reactions">${['👍', '😂', '😮', '🔥', '👏', '😭'].map(e => `<button data-act="react" data-e="${e}" aria-label="React ${e}">${e}</button>`).join('')}</div>` : '<span></span>';
    mount(win({
      title: `Answer — Question ${rv.index + 1} of ${rv.total}`, cls: 'wide',
      body: `
        <div class="q-head"><div class="q-cat">${Art.swatch(rv.category)}<span>${esc(rv.categoryName)}</span></div></div>
        <div class="verdict">${esc(verdict)}</div>
        <div class="q-text" style="font-size:17px;min-height:0;margin-bottom:10px">${esc(rv.text)}</div>
        ${choices || `<div class="answer-box"><span class="lbl">The answer was</span>${esc(rv.answer)}</div>`}
        ${!pp && rv.type === 'fib' && mine.answered ? `<p class="center muted" style="margin-top:-6px">You said: “${esc(mine.text)}”</p>` : ''}
        <table class="results">${rows}</table>
        <div class="next-row">${reactions}
          <div style="display:flex;align-items:center;gap:10px"><span class="muted" id="nextIn"></span>${isHost() ? `<button class="btn default" data-act="next">${rv.last ? 'Final Scores' : 'Next'} ▸</button>` : ''}</div></div>`
    }) + (CFG.adSlots && CFG.adSlots.reveal ? ad('reveal') : (adPreview && (rv.index + 1) % 3 === 0 ? ad('reveal') : '')));
    clearInterval(nextTimer);
    const end = performance.now() + rv.nextInMs;
    const tick = () => { const el = $('#nextIn'); if (!el) return clearInterval(nextTimer); const s = Math.max(0, Math.ceil((end - performance.now()) / 1000)); el.textContent = (rv.last ? 'Scores in ' : 'Next in ') + s + 's'; };
    tick(); nextTimer = setInterval(tick, 250);
  }

  /* ================= FINAL ================= */
  function renderFinal() {
    const f = S.final; if (!f) return;
    const st = f.standings;
    const podiumOrder = [st[1], st[0], st[2]];
    const pod = st.length > 1 ? `<div class="podium">${podiumOrder.map((p, i) => p ? `<div class="col p${[2, 1, 3][i]}">
        ${[2, 1, 3][i] === 1 ? Art.icon('trophy') : Art.icon(p.icon)}<span class="nm">${esc(p.name)}</span><span class="sc">${p.score} pts</span>
        <div class="blk"><span>${p.rank}</span></div></div>` : '<div class="col"></div>').join('')}</div>` : '';
    const ppMode = S.room && S.room.passPlay;
    const me = (ppMode ? st[0] : st.find(p => p.id === S.me)) || {};
    const winners = st.filter(p => p.rank === 1);
    const headline = ppMode ? (winners.length > 1 ? "It's a tie for first!" : `${me.name} wins!`) : S.room && S.room.solo ? `You scored ${me.score} — ${me.correct} of ${f.total} correct`
      : me.rank === 1 ? (st.filter(p => p.rank === 1).length > 1 ? "It's a tie for first!" : 'You win!') : `You finished #${me.rank}`;
    const rows = st.map(p => `<tr class="${p.id === S.me ? 'me' : ''}"><td style="width:28px">${p.rank}.</td><td class="ic">${Art.icon(p.icon, 'sm')}</td><td>${esc(p.name)}<div class="muted">${p.correct} of ${f.total} correct</div></td>
      <td class="pts"><b>${p.score}</b></td><td style="width:44px">${Art.pie(p.wedges)}</td></tr>`).join('');
    const host = isHost();
    mount(win({
      title: 'Final Scores', cls: 'wide', close: 'leave',
      body: `<h2 class="center">${esc(headline)}</h2>
        <div class="center" style="margin:6px 0 10px">${Art.pie(me.wedges, 'lg', 2.5)}<div class="muted">${(me.wedges || []).length} of 6 pieces</div></div>
        ${pod}
        <table class="results">${rows}</table>
        <div class="btn-row">
          <button class="btn" data-act="leave">Leave</button>
          ${host ? `<button class="btn" data-act="lobby">Change Settings</button><button class="btn default" data-act="again">Play Again</button>` : `<span class="muted">The host can start another round.</span>`}
        </div>`
    }) + ad('final'));
  }

  /* ================= HELP / ABOUT ================= */
  function renderHelp() {
    mount(win({
      title: 'How to Play', close: 'back',
      body: `<div class="prose">
        <p><b>Host:</b> tap <i>New Game</i>. You'll get a 6-digit code. Share it (or the invite link) with up to 7 friends, pick the number of questions and categories, then press <i>Start Game</i>.</p>
        <p><b>Friends:</b> tap <i>Join Game</i> and type the code. Everyone plays on their own phone or computer at the same time.</p>
        <p><b>Questions</b> are either multiple choice (A–D) or fill in the blank. For fill-in answers, spelling doesn't have to be perfect — close is good enough.</p>
        <p><b>Scoring:</b> 100 points for a correct multiple-choice answer, 150 for fill-in, plus up to 50 for speed and a bonus for harder questions. Three in a row earns a streak bonus.</p>
        <p><b>The box:</b> your cube has six pieces, one for each category. Get a question right in a category to fill in its piece. Try to complete your whole box!</p>
        <ul>${CATS.map(c => `<li style="display:flex;gap:8px;align-items:center;list-style:none;margin-left:-20px;padding:2px 0">${Art.swatch(c)} ${CAT_NAMES[c]}</li>`).join('')}</ul>
        <p class="muted">Keyboard: press A–D or 1–4 to answer, Enter to submit.</p></div>
        <div class="btn-row"><button class="btn default" data-act="back">OK</button></div>`
    }));
  }
  function renderAbout() {
    mount(win({
      title: 'About ' + CFG.siteName, cls: 'narrow', close: 'back',
      body: `<div class="logo-row">${Art.pie(CATS, 'lg', 2.5)}<div><h2>${esc(CFG.siteName)}</h2><div class="muted">Version 1.0</div></div></div>
        <div class="prose"><p>A free multiplayer trivia game with a classic black &amp; white desktop look.</p>
        <p class="muted">Questions written for Black Box Trivia. Thanks to the Open Trivia Database community for inspiration. Font: ChicagoFLF (public domain).</p></div>
        <div class="btn-row"><a class="btn" href="privacy.html">Privacy</a><button class="btn default" data-act="back">OK</button></div>`
    }));
  }

  /* ================= menubar ================= */
  function renderMenubar() {
    const inGame = !!S.room;
    const host = isHost();
    const r = S.room;
    const menus = [
      { id: 'apple', label: `<svg width="15" height="15" viewBox="0 0 100 100" aria-label="${esc(CFG.siteName)} menu"><path d="M50 4L90 27L90 73L50 96L10 73L10 27Z" fill="#000"/><path d="M50 50L10 27M50 50L90 27M50 50L50 96" stroke="#fff" stroke-width="9"/></svg>`, items: [
        { label: `About ${CFG.siteName}…`, act: 'about' }, { label: 'How to Play…', act: 'help' }] },
      { id: 'file', label: 'File', items: [
        { label: 'New Game', act: 'new', kbd: '⌘N', disabled: inGame || CFG.offline }, { label: 'Join Game…', act: 'goJoin', kbd: '⌘J', disabled: inGame || CFG.offline },
        { label: 'Pass & Play…', act: 'goPass', disabled: inGame }, { label: 'Solo Practice', act: 'solo', disabled: inGame }, '-', { label: 'Leave Game', act: 'leave', disabled: !inGame }] },
      { id: 'game', label: 'Game', items: [
        { label: 'Start Game', act: 'start', disabled: !(host && r && (r.state === 'lobby' || r.state === 'final')) },
        { label: 'Next Question', act: 'next', disabled: !(host && r && r.state === 'reveal') },
        { label: 'Back to Lobby', act: 'lobby', disabled: !(host && r && r.state !== 'lobby') }, '-',
        { label: 'Copy Invite Link', act: 'copy', disabled: !(r && !r.solo && !r.passPlay) }] },
      { id: 'sound', label: 'Sound', items: [{ label: 'Sound Effects', act: 'toggleSound', check: Sounds.enabled }, { label: 'Test Beep', act: 'beep' }] },
      { id: 'help', label: 'Help', items: [{ label: 'How to Play…', act: 'help' }, { label: 'Privacy Policy', act: 'privacy' }] }
    ];
    const open = document.querySelector('.menu.open');
    const openId = open && open.dataset.id;
    $('#menubar').innerHTML = menus.map(m => `<div class="menu ${openId === m.id ? 'open' : ''}" data-id="${m.id}"><button aria-haspopup="true" data-menu="${m.id}">${m.label}</button>
      <div class="dropdown" role="menu">${m.items.map(it => it === '-' ? '<hr>' :
        `<button role="menuitem" data-act="${it.act}" class="${it.check ? 'check' : ''}" ${it.disabled ? 'disabled' : ''}><span>${esc(it.label)}</span>${it.kbd ? `<kbd>${it.kbd}</kbd>` : ''}</button>`).join('')}</div></div>`).join('')
      + `<div class="spacer"></div><div class="status" id="mbStatus">${r && r.passPlay ? `Pass & Play · ${r.players.length} players` : ''}${r && !r.solo && !r.passPlay ? `Game ${fmtCode(r.code)} · ${r.players.filter(p => p.connected).length}/${r.maxPlayers}` : ''}</div>`;
  }
  function setStatus(txt) { const el = $('#mbStatus'); if (el && txt) el.textContent = txt; else if (el) renderMenubar(); }

  function renderFoot() {
    $('#foot').innerHTML = `<a href="/how-to-play">How to play</a> <span>·</span> <a href="/sample-questions">Sample questions</a> <span>·</span> <a href="/about">About</a> <span>·</span> <a href="/contact">Contact</a> <span>·</span> <a href="/privacy">Privacy</a>`;
    $('#deskIcons').innerHTML = `<button class="desk-icon" data-act="help">${Art.icon('doc')}<span>Read Me</span></button>
      <button class="desk-icon" data-act="trash">${Art.icon('trash')}<span>Trash</span></button>`;
  }

  /* ================= dialogs ================= */
  function alertBox(kind, msg, buttons) {
    if (kind !== 'note') Sounds.beep();
    buttons = buttons || [{ label: 'OK', act: 'closeModal', def: true }];
    $('#modal').innerHTML = `<div class="modal-backdrop"><div class="alert" role="alertdialog" aria-live="assertive">
      <div class="alert-row">${Art.ALERT[kind] || Art.ALERT.note}<p>${esc(msg)}</p></div>
      <div class="btn-row">${buttons.map(b => `<button class="btn ${b.def ? 'default' : ''}" data-act="${b.act}">${esc(b.label)}</button>`).join('')}</div></div></div>`;
    const d = $('#modal .btn.default'); d && d.focus();
  }
  function closeModal() { $('#modal').innerHTML = ''; }
  let toastT;
  function toast(msg) {
    let el = $('.toast'); if (!el) { el = document.createElement('div'); el.className = 'toast'; document.body.appendChild(el); }
    el.textContent = msg; el.hidden = false; clearTimeout(toastT); toastT = setTimeout(() => { el.hidden = true; }, 2200);
  }
  function busy(on) { document.body.style.cursor = on ? 'progress' : ''; }
  function floatReaction(e) {
    const el = document.createElement('div'); el.className = 'float-react'; el.textContent = e;
    el.style.left = (15 + Math.random() * 70) + 'vw'; el.style.bottom = '60px';
    document.body.appendChild(el); setTimeout(() => el.remove(), 2100);
  }

  /* ================= actions ================= */
  function inviteUrl() { return `${location.origin}${location.pathname}?join=${S.room.code}`; }

  async function act(a, el) {
    Sounds.unlock();
    switch (a) {
      case 'home': S.screen = 'home'; render(); break;
      case 'back': go(S.room ? ({ lobby: 'lobby', question: 'question', reveal: 'reveal', final: 'final' }[S.room.state] || 'lobby') : 'home'); break;
      case 'goJoin': if (!S.room) { const n = $('#name'); if (n && n.value.trim()) { S.name = n.value.trim(); store.set('name', S.name); } go('join'); } break;
      case 'new': {
        if (S.room) return;
        const name = S.screen === 'home' ? readName() : (S.name || null);
        if (!name) { if (S.screen !== 'home') go('home'); return; }
        const net = online(); if (!net) return;
        busy(true);
        net.emit('create', { name, settings: store.get('settings', null) }, res => {
          busy(false);
          if (!res || !res.ok) return alertBox('stop', (res && res.error) || 'Could not create a game.');
          S.me = res.you; store.set('session', { code: res.code });
        });
        break;
      }
      case 'goPass': {
        if (S.room) return;
        const n = $('#name'); if (n && n.value.trim()) { S.name = n.value.trim(); store.set('name', S.name); }
        S.ppNames = null; go('ppsetup'); break;
      }
      case 'ppAdd': if (S.ppNames.length < 8) { S.ppNames.push(''); renderPassSetup(); } break;
      case 'ppDel': S.ppNames.splice(+el.dataset.i, 1); renderPassSetup(); break;
      case 'beginTurn': Sounds.click(); S.net && S.net.emit('beginTurn'); break;
      case 'editPlayers': { const names = S.room.players.map(p => p.name); teardown(); S.ppNames = names; go('ppsetup'); break; }
      case 'solo': {
        if (S.room) return;
        const nameEl = $('#name');
        const name = (nameEl && nameEl.value.trim()) || S.name || 'You';
        busy(true);
        try {
          const bank = await loadBank();
          if (S.net) S.net.close();
          const net = LocalNet(bank); bindNet(net); S.mode = 'local';
          net.emit('create', { name, settings: store.get('settings', null) }, res => { S.me = res.you; });
        } catch (e) { alertBox('stop', 'Could not load questions. Check your connection.'); }
        busy(false);
        break;
      }
      case 'leave':
        if (!S.room) return go('home');
        if (S.room.solo || S.room.passPlay || S.room.state === 'final' || S.room.players.length <= 1) { teardown(); go('home'); }
        else alertBox('caution', 'Leave this game? Your score will be lost.', [{ label: 'Cancel', act: 'closeModal' }, { label: 'Leave', act: 'leaveConfirm', def: true }]);
        break;
      case 'leaveConfirm': closeModal(); teardown(); go('home'); break;
      case 'closeModal': closeModal(); break;
      case 'start': case 'again':
        if (!isHost()) return;
        store.set('settings', S.room.settings);
        S.net.emit('start', null, res => { if (res && !res.ok && res.error) alertBox('caution', res.error); });
        break;
      case 'next': if (isHost()) S.net.emit('next'); break;
      case 'lobby': if (isHost()) S.net.emit('lobby'); break;
      case 'kick': if (isHost()) alertBox('caution', 'Remove this player from the game?', [{ label: 'Cancel', act: 'closeModal' }, { label: 'Remove', act: 'kickConfirm:' + el.dataset.id, def: true }]); break;
      case 'nq': sendSettings({ numQuestions: +el.dataset.n }); break;
      case 'nqm': sendSettings({ numQuestions: Math.max(1, S.room.settings.numQuestions - (S.room.settings.numQuestions > 10 ? 5 : 1)) }); break;
      case 'nqp': sendSettings({ numQuestions: Math.min(100, S.room.settings.numQuestions + (S.room.settings.numQuestions >= 10 ? 5 : 1)) }); break;
      case 'pick': submitAnswer({ choice: +el.dataset.i }, el.textContent); break;
      case 'react': S.net && S.net.emit('react', { e: el.dataset.e }); break;
      case 'copy': {
        const txt = CFG.transport === 'room' ? `Join my ${CFG.siteName} game! Code: ${fmtCode(S.room.code)}` : inviteUrl();
        try { await navigator.clipboard.writeText(txt); toast(CFG.transport === 'room' ? 'Invite copied' : 'Invite link copied'); }
        catch (e) { const el = $('#codeText'); if (el) { const r = document.createRange(); r.selectNodeContents(el); const sel = getSelection(); sel.removeAllRanges(); sel.addRange(r); } toast('Select and copy the code'); }
        break;
      }
      case 'share':
        if (navigator.share && CFG.transport !== 'room') { try { await navigator.share({ title: CFG.siteName, text: `Join my trivia game! Code: ${S.room.code}`, url: inviteUrl() }); } catch (e) {} }
        else act('copy');
        break;
      case 'toggleSound': Sounds.enabled = !Sounds.enabled; if (Sounds.enabled) Sounds.beep(); renderMenubar(); break;
      case 'beep': Sounds.beep(); break;
      case 'help': go('help'); break;
      case 'about': go('about'); break;
      case 'privacy': location.href = 'privacy.html'; break;
      case 'trash': alertBox('note', 'The Trash is empty.'); break;
      default:
        if (a && a.startsWith('kickConfirm:')) { closeModal(); S.net.emit('kick', { id: a.split(':')[1] }); }
    }
  }

  /* ================= global input ================= */
  document.addEventListener('click', e => {
    const menuBtn = e.target.closest('[data-menu]');
    const openMenu = document.querySelector('.menu.open');
    if (menuBtn) {
      const m = menuBtn.parentElement; const was = m.classList.contains('open');
      document.querySelectorAll('.menu.open').forEach(x => x.classList.remove('open'));
      if (!was) { m.classList.add('open'); Sounds.click(); }
      e.preventDefault(); return;
    }
    const t = e.target.closest('[data-act]');
    if (openMenu) openMenu.classList.remove('open');
    if (!t || t.disabled) return;
    if (t.tagName === 'A') e.preventDefault();
    if (t.type === 'submit' && t.form) return; // forms handle themselves
    // menu item flash, like the real thing
    if (t.closest('.dropdown')) { act(t.dataset.act, t); return; }
    act(t.dataset.act, t);
  });
  // drag across the menubar opens neighbouring menus
  document.addEventListener('mouseover', e => {
    const b = e.target.closest('[data-menu]'); const open = document.querySelector('.menu.open');
    if (b && open && b.parentElement !== open) { open.classList.remove('open'); b.parentElement.classList.add('open'); }
  });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') { closeModal(); document.querySelectorAll('.menu.open').forEach(x => x.classList.remove('open')); return; }
    if ($('#modal').innerHTML && e.key === 'Enter') { const d = $('#modal .btn.default'); if (d) { e.preventDefault(); d.click(); } return; }
    if (S.screen === 'question' && S.q && S.q.type === 'mc' && !S.myAnswer && !e.metaKey && !e.ctrlKey) {
      const idx = { a: 0, b: 1, c: 2, d: 3, 1: 0, 2: 1, 3: 2, 4: 3 }[e.key.toLowerCase()];
      if (idx != null && S.q.choices[idx] != null) { const b = document.querySelector(`.choice[data-i="${idx}"]`); b && b.click(); }
    }
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'j' && !S.room && !CFG.offline) { e.preventDefault(); act('goJoin'); }
  });

  /* ================= boot ================= */
  function boot() {
    Art.installDefs();
    if (CFG.adsenseClient && !document.querySelector('script[src*="adsbygoogle.js"]')) {
      const s = document.createElement('script'); s.async = true; s.crossOrigin = 'anonymous';
      s.src = `https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${encodeURIComponent(CFG.adsenseClient)}`;
      document.head.appendChild(s);
    }
    const params = new URLSearchParams(location.search);
    const join = (params.get('join') || '').replace(/\D/g, '').slice(0, 6);
    render();
    if (join.length === 6 && !CFG.offline) { S.joinCode = join; go('join'); }
    else if (store.get('session', null) && !CFG.offline && CFG.transport !== 'room') {
      // try to resume a game after a refresh or a dropped connection
      online();
      setTimeout(() => { if (!S.room) store.del('session'); }, 4000);
    }
    document.addEventListener('visibilitychange', () => { if (!document.hidden && S.screen === 'question') startTimer(); });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();
})();
