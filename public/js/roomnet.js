/* RoomNet — multiplayer over the Claude artifact "room" capability (preview build only).
 * The host's page runs the game engine and publishes the whole game state in its
 * presence; players publish their name and current answer in theirs. Presence is
 * handed to late joiners automatically, so nobody misses a phase. */
(function () {
  const clone = o => JSON.parse(JSON.stringify(o));
  const rand6 = () => String(100000 + Math.floor(Math.random() * 900000));
  const rid = () => Math.random().toString(36).slice(2, 10);
  const roomName = code => 'bbt-' + code;
  let roomApiPromise = null;
  function roomApi() {
    if (!roomApiPromise) roomApiPromise = (window.claude && window.claude.use) ? window.claude.use('room').catch(() => null) : Promise.resolve(null);
    return roomApiPromise;
  }
  // start connecting as soon as the page loads, so Join is quick
  setTimeout(roomApi, 0);

  const NO_ROOM = 'Online play in this preview needs you to be signed in to Claude, viewing this page inside Claude. You can still play Solo Practice.';

  window.RoomNet = function (loadBank) {
    const handlers = {};
    const fire = (ev, d) => (handlers[ev] || []).forEach(fn => { try { fn(d); } catch (e) { console.error(e); } });
    let named = null, role = null, code = null, me = null, name = '';
    let unsub = [];
    let closed = false;

    /* ---------------- host ---------------- */
    let engine = null, game = 0, kicked = new Set(), rejected = new Set(), pubTimer = null;
    const peerPid = new Map();       // peer label -> player id
    const lastAns = new Map();       // pid -> answer key processed

    function hostEmit(target, ev, payload) {
      if (ev === 'kicked' && target !== me) { kicked.add(target); schedulePublish(); return; }
      if (target === null || target === me) setTimeout(() => fire(ev, clone(payload)), 0);
      if (target === null) schedulePublish();
    }
    function snapshot() {
      const st = engine.roomState();
      let ph = null;
      if (engine.state === 'question' && engine.current) ph = { t: 'q', d: engine.questionPayload() };
      else if (engine.state === 'reveal' && engine.lastReveal) { const r = Object.assign({}, engine.lastReveal); delete r.players; ph = { t: 'r', d: r }; }
      else if (engine.state === 'final' && engine.lastFinal) ph = { t: 'f', d: engine.lastFinal };
      let s = { h: 1, c: code, g: game, k: [...kicked], x: [...rejected], room: st, ph };
      if (JSON.stringify(s).length > 3900 && ph && ph.t === 'r') { ph.d = Object.assign({}, ph.d); ph.d.results = ph.d.results.map(r => Object.assign({}, r, { text: String(r.text || '').slice(0, 24) })); }
      if (JSON.stringify(s).length > 3900 && ph && ph.t === 'r') { delete ph.d.text; }
      return s;
    }
    function schedulePublish() {
      if (pubTimer || !named) return;
      pubTimer = setTimeout(() => { pubTimer = null; if (named && !closed) named.presence({ bbt: snapshot() }).catch(e => console.warn('presence', e)); }, 40);
    }
    function hostPeers(ch) {
      for (const p of ch.peers) {
        if (p.sameTab) continue;
        const pl = p.presence && p.presence.pl;
        if (!pl || typeof pl.id !== 'string' || pl.c !== code) continue;
        const pid = pl.id.slice(0, 24);
        peerPid.set(p.peer, pid);
        if (kicked.has(pid) || rejected.has(pid)) continue;
        if (!engine.players.has(pid) || !engine.players.get(pid).connected) {
          const res = engine.addPlayer(pid, String(pl.n || 'Player'));
          if (!res.ok) { rejected.add(pid); schedulePublish(); continue; }
        }
        const a = pl.a;
        if (a && a.g === game && a.i === engine.qIndex && engine.state === 'question') {
          const key = game + ':' + a.i;
          if (lastAns.get(pid) !== key) { lastAns.set(pid, key); engine.answer(pid, a.d || {}); }
        }
      }
      for (const p of ch.left) {
        const pid = peerPid.get(p.peer);
        if (pid && engine.players.has(pid)) engine.setConnected(pid, false);
        peerPid.delete(p.peer);
      }
    }

    /* ---------------- player ---------------- */
    let seenRoom = '', seenPh = '', seenGame = -1, hostSeen = false, hostGoneTimer = null, curQ = null, lastRoom = null;
    let joinResolve = null;
    function findHost(peers) { return peers.find(p => p.presence && p.presence.bbt && p.presence.bbt.h === 1 && p.presence.bbt.c === code); }
    function playerPeers(ch) {
      const host = findHost(ch.peers);
      if (!host) {
        if (hostSeen && !hostGoneTimer) hostGoneTimer = setTimeout(() => { if (!findHost(named ? named.peers() : [])) { fire('kicked', { message: 'The host closed the game.' }); close(); } }, 6000);
        return;
      }
      clearTimeout(hostGoneTimer); hostGoneTimer = null; hostSeen = true;
      const s = host.presence.bbt;
      if (Array.isArray(s.k) && s.k.includes(me)) { fire('kicked', { message: 'The host removed you from the game.' }); close(); return; }
      if (joinResolve) {
        if (Array.isArray(s.x) && s.x.includes(me)) { joinResolve({ ok: false, error: 'This game is full (8 players max).' }); joinResolve = null; close(); return; }
        if (s.room && s.room.players.some(p => p.id === me)) { joinResolve({ ok: true, code, you: me }); joinResolve = null; }
        else return;
      }
      if (s.g !== seenGame) { if (seenGame !== -1) fire('starting', {}); seenGame = s.g; }
      const rj = JSON.stringify(s.room);
      if (rj !== seenRoom) { seenRoom = rj; lastRoom = s.room; fire('room', clone(s.room)); }
      const ph = s.ph;
      const key = ph ? `${s.g}:${ph.t}:${ph.d && ph.d.index != null ? ph.d.index : ''}` : '';
      if (ph && key !== seenPh) {
        seenPh = key;
        if (ph.t === 'q') { curQ = { g: s.g, i: ph.d.index }; fire('question', clone(ph.d)); }
        else if (ph.t === 'r') { const r = clone(ph.d); r.players = clone(lastRoom ? lastRoom.players : []); fire('reveal', r); }
        else if (ph.t === 'f') fire('final', clone(ph.d));
      }
    }

    /* ---------------- shared ---------------- */
    const rxSeen = new Map();
    function reactions(ch) {
      for (const p of ch.updated.concat(ch.joined)) {
        if (p.sameTab) continue;
        const rx = p.presence && p.presence.rx;
        if (!rx || typeof rx.t !== 'number') continue;
        const prev = rxSeen.get(p.peer);
        rxSeen.set(p.peer, rx.t);
        if (prev !== undefined && prev !== rx.t && ['👍', '😂', '😮', '🔥', '👏', '😭'].includes(rx.e)) fire('react', { e: rx.e });
      }
    }

    async function enterRoom(c) {
      const api = await roomApi();
      if (!api) throw new Error(NO_ROOM);
      named = await api.join(roomName(c));
      unsub.push(named.onPeers(ch => { if (closed) return; reactions(ch); if (role === 'host') hostPeers(ch); else playerPeers(ch); }));
      unsub.push(named.onConnection(ok => { if (!closed) fire('conn', ok); }));
    }

    function close() {
      closed = true;
      unsub.forEach(u => { try { u(); } catch (e) {} }); unsub = [];
      if (engine) engine.destroy();
      if (named) named.leave().catch(() => {});
      named = null;
    }

    async function create(data, ack) {
      try {
        const bank = await loadBank();
        role = 'host'; code = rand6(); me = 'h' + rid(); name = (data && data.name) || 'Host';
        engine = new TriviaEngine.Room(code, { picker: TriviaEngine.QuestionPicker(bank), emit: hostEmit });
        if (data && data.settings) engine.settings = TriviaEngine.cleanSettings(data.settings);
        if (data && data.seen) engine.addSeen(data.seen);
        const origStart = engine.start.bind(engine);
        engine.start = (by) => { const r = origStart(by); if (r.ok) { game++; lastAns.clear(); schedulePublish(); } return r; };
        await enterRoom(code);
        engine.addPlayer(me, name);
        ack({ ok: true, code, you: me });
        schedulePublish();
      } catch (e) { ack({ ok: false, error: e.message || NO_ROOM }); close(); }
    }

    async function join(data, ack) {
      try {
        role = 'player'; code = String(data.code); name = (data && data.name) || 'Player';
        let pid = null; try { pid = sessionStorage.getItem('bbt_pid_' + code); } catch (e) {}
        me = pid || ('p' + rid()); try { sessionStorage.setItem('bbt_pid_' + code, me); } catch (e) {}
        await enterRoom(code);
        await named.presence({ pl: { id: me, n: name.slice(0, 16), c: code } });
        const result = await new Promise(resolve => {
          joinResolve = resolve;
          setTimeout(() => { if (joinResolve) { joinResolve = null; resolve({ ok: false, error: hostSeen ? 'The host did not let you in. Try again.' : `No game found with code ${code}. Check the code with the host.` }); } }, 8000);
          playerPeers({ peers: named.peers(), joined: [], left: [], updated: [] });
        });
        if (!result.ok) close();
        ack(result);
      } catch (e) { ack({ ok: false, error: e.message || NO_ROOM }); close(); }
    }

    function hostAct(fn) { if (role === 'host' && engine) fn(); }

    return {
      kind: 'online',
      on(ev, fn) { (handlers[ev] = handlers[ev] || []).push(fn); },
      emit(ev, data, ack) {
        ack = typeof ack === 'function' ? ack : () => {};
        switch (ev) {
          case 'create': create(data, ack); break;
          case 'join': join(data, ack); break;
          case 'settings': hostAct(() => engine.updateSettings(me, data)); break;
          case 'start': if (role === 'host') ack(engine.start(me)); break;
          case 'next': hostAct(() => engine.hostNext(me)); break;
          case 'lobby': hostAct(() => engine.backToLobby(me)); break;
          case 'kick': hostAct(() => engine.kick(me, data && data.id)); break;
          case 'answer':
            if (role === 'host') engine.answer(me, data);
            else if (named && curQ) named.presence({ pl: { id: me, n: name.slice(0, 16), c: code, a: { g: curQ.g, i: curQ.i, d: data } } }).catch(() => {});
            break;
          case 'react':
            if (named) named.presence({ rx: { e: data.e, t: Date.now() } }).catch(() => {});
            setTimeout(() => fire('react', { e: data.e }), 0);
            break;
          case 'leave': close(); break;
        }
      },
      close
    };
  };
})();
