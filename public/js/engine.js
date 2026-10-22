/* Game rules for one room. Runs on the server (multiplayer) and in the browser (solo/offline).
 * Transport-agnostic: everything goes out through `emit(targetPlayerId | null, event, payload)`
 * where null = everyone in the room. */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory(require('./match.js'));
  else root.TriviaEngine = factory(root.TriviaMatch);
})(typeof self !== 'undefined' ? self : this, function (Match) {
  const MAX_PLAYERS = 8;
  const CATS = ['geo', 'ent', 'his', 'art', 'sci', 'spo'];
  const CAT_NAMES = {
    geo: 'Geography', ent: 'Entertainment', his: 'History',
    art: 'Arts & Literature', sci: 'Science & Nature', spo: 'Sports & Leisure'
  };
  // Picture rounds: questions that carry a 96x64 bitmap (q.img). pr = round key.
  const PIC_ROUNDS = ['flags', 'shapes', 'maps', 'landmarks', 'skylines', 'states', 'aircraft', 'stars', 'animals', 'paintings'];
  const PIC_NAMES = {
    flags: 'Flags', shapes: 'Country shapes', maps: 'Find the country', landmarks: 'Landmarks & wonders', skylines: 'City skylines',
    states: 'US states', aircraft: 'Famous aircraft', stars: 'Constellations', animals: 'Animals', paintings: 'Famous paintings'
  };
  const PIC_SHARE = 0.25;   // share of a mixed game that is picture questions
  const REVEAL_MS = 7000;
  const ICONS = ['disk', 'bomb', 'watch', 'cup', 'bug', 'rocket', 'dog', 'globe'];

  const DEFAULT_SETTINGS = {
    numQuestions: 10, categories: CATS.slice(), difficulty: 'any', mode: 'mixed', timeLimit: 20,
    pictures: 'mix', picRounds: PIC_ROUNDS.slice()
  };

  function shuffle(a, rnd) { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }
  const clamp = (v, lo, hi) => Math.max(lo, Math.min(hi, v));

  function cleanSettings(s, prev) {
    const o = Object.assign({}, prev || DEFAULT_SETTINGS);
    if (!s) return o;
    if (s.numQuestions != null) o.numQuestions = clamp(parseInt(s.numQuestions, 10) || 10, 1, 100);
    if (Array.isArray(s.categories)) {
      const c = s.categories.filter(x => CATS.includes(x));
      o.categories = c.length ? c : CATS.slice();
    }
    if (['any', 'easy', 'medium', 'hard'].includes(s.difficulty)) o.difficulty = s.difficulty;
    if (['mc', 'fib', 'mixed'].includes(s.mode)) o.mode = s.mode;
    if (s.timeLimit != null) o.timeLimit = clamp(parseInt(s.timeLimit, 10) || 20, 5, 120);
    if (['off', 'mix', 'only'].includes(s.pictures)) o.pictures = s.pictures;
    if (Array.isArray(s.picRounds)) {
      const r = s.picRounds.filter(x => PIC_ROUNDS.includes(x));
      o.picRounds = r.length ? r : PIC_ROUNDS.slice();
    }
    return o;
  }

  /* bank: array of {id,c,d,q,a,w?,alt?,fib} */
  function QuestionPicker(bank) {
    const byCat = {}; CATS.forEach(c => byCat[c] = []);
    const byRound = {}; PIC_ROUNDS.forEach(r => byRound[r] = []);
    const known = new Set('Afghanistan,Albania,Algeria,Andorra,Angola,Argentina,Armenia,Australia,Austria,Azerbaijan,Bahamas,Bahrain,Bangladesh,Barbados,Belarus,Belgium,Belize,Benin,Bhutan,Bolivia,Bosnia,Botswana,Brazil,Brunei,Bulgaria,Burkina Faso,Burundi,Cambodia,Cameroon,Canada,Chad,Chile,China,Colombia,Comoros,Congo,Costa Rica,Croatia,Cuba,Cyprus,Czechia,Denmark,Djibouti,Dominica,Ecuador,Egypt,El Salvador,Eritrea,Estonia,Eswatini,Ethiopia,Fiji,Finland,France,Gabon,Gambia,Georgia,Germany,Ghana,Greece,Grenada,Guatemala,Guinea,Guyana,Haiti,Honduras,Hungary,Iceland,India,Indonesia,Iran,Iraq,Ireland,Israel,Italy,Jamaica,Japan,Jordan,Kazakhstan,Kenya,Kiribati,Kosovo,Kuwait,Kyrgyzstan,Laos,Latvia,Lebanon,Lesotho,Liberia,Libya,Liechtenstein,Lithuania,Luxembourg,Madagascar,Malawi,Malaysia,Maldives,Mali,Malta,Mauritania,Mauritius,Mexico,Micronesia,Moldova,Monaco,Mongolia,Montenegro,Morocco,Mozambique,Myanmar,Namibia,Nauru,Nepal,Netherlands,New Zealand,Nicaragua,Niger,Nigeria,North Korea,Norway,Oman,Pakistan,Palau,Panama,Paraguay,Peru,Philippines,Poland,Portugal,Qatar,Romania,Russia,Rwanda,Samoa,San Marino,Saudi Arabia,Senegal,Serbia,Seychelles,Sierra Leone,Singapore,Slovakia,Slovenia,Somalia,South Africa,South Korea,South Sudan,Spain,Sri Lanka,Sudan,Suriname,Sweden,Switzerland,Syria,Taiwan,Tajikistan,Tanzania,Thailand,Togo,Tonga,Tunisia,Turkey,Turkmenistan,Tuvalu,Uganda,Ukraine,Uruguay,Uzbekistan,Vanuatu,Venezuela,Vietnam,Yemen,Zambia,Zimbabwe,Austrian,Australian,Swiss,Swedish,Swede,Danish,Dutch,Spanish,Spaniard,Mali,Malawi,Gambia,Zambia,Guinea,Slovenia,Slovakia,Iran,Iraq,Java,Jakarta,Mercury,Venus,Mars,Saturn,Uranus,Neptune,Pluto'.split(',').map(x => Match.compact(Match.normalize(x))));
    for (const q of bank) {
      if (q.img) { if (byRound[q.pr]) byRound[q.pr].push(q); }
      else if (byCat[q.c]) byCat[q.c].push(q);
      known.add(Match.compact(Match.normalize(q.a)));
      if (q.w) q.w.forEach(w => known.add(Match.compact(Match.normalize(w))));
    }
    return {
      byCat, known,
      count(cat) { return byCat[cat] ? byCat[cat].length : 0; },
      /* Picks a varied set of questions.
       * used: question ids already asked in this room (never repeat within a session)
       * seen: ids this group has seen in earlier games on their devices (avoided while fresh ones remain)
       * Variety rules: rotate categories, choose a question *pattern* before a question so that big
       * template families (e.g. "What is the capital of…") can't crowd a game, cap each pattern per game,
       * never use the same answer twice, and keep video-game questions to about a third of their category. */
      pictureCount(r) { return byRound[r] ? byRound[r].length : 0; },
      pick(settings, used, rnd, seen) {
        seen = seen || new Set();
        const N = settings.numQuestions;
        const diffOk = q => settings.difficulty === 'any' ||
          (settings.difficulty === 'easy' && q.d <= 2) ||
          (settings.difficulty === 'medium' && q.d === 3) ||
          (settings.difficulty === 'hard' && q.d >= 4);
        const modeOk = q => settings.mode === 'mixed' ? (q.w || q.fib) : settings.mode === 'mc' ? !!q.w : !!q.fib;
        const famUsed = new Map(), answers = new Set();
        const ansKey = q => Match.compact(Match.normalize(q.a));
        /* Draws n questions from pools (key -> questions), rotating through keys. */
        const run = (pools, keys, n) => {
          if (n <= 0 || !keys.length) return [];
          const need = Math.ceil(n / keys.length) + 2;
          const famCap = Math.max(1, Math.ceil(n / 15));
          const perCat = {}, nicheCat = {}, groups = {};
          for (const c of keys) {
            const base = pools[c].filter(modeOk);
            let p = base.filter(q => diffOk(q) && !used.has(q.id));
            if (p.length < need) p = base.filter(q => !used.has(q.id));                    // relax difficulty
            if (p.length < need) { base.forEach(q => used.delete(q.id)); p = base.filter(diffOk); if (p.length < need) p = base.slice(); } // recycle
            const unseen = p.filter(q => !seen.has(q.id));
            if (unseen.length >= need) p = unseen;                                           // prefer questions nobody here has seen
            const g = new Map();
            for (const q of shuffle(p, rnd)) { const k = q.f || q.id; if (!g.has(k)) g.set(k, []); g.get(k).push(q); }
            groups[c] = g; perCat[c] = 0; nicheCat[c] = 0;
          }
          const draw = c => {
            const g = groups[c];
            for (let pass = 0; pass < 2; pass++) {
              const fams = [];
              let total = 0;
              for (const [k, list] of g) {
                if (!list.length) continue;
                if (pass === 0 && (famUsed.get(k) || 0) >= famCap) continue;
                const w = Math.sqrt(list.length); fams.push([k, list, w]); total += w;
              }
              for (let tries = 0; tries < 30 && fams.length && total > 0; tries++) {
                let r = rnd() * total, pickF = fams[fams.length - 1];
                for (const f of fams) { r -= f[2]; if (r <= 0) { pickF = f; break; } }
                const [k, list] = pickF;
                const q = list[list.length - 1];
                const niche = q.sub === 'Video Games';
                if (answers.has(ansKey(q)) || (pass === 0 && niche && (nicheCat[c] + 1) * 3 > perCat[c] + 3)) {
                  list.pop(); if (!list.length) { total -= pickF[2]; fams.splice(fams.indexOf(pickF), 1); }
                  continue;
                }
                list.pop();
                famUsed.set(k, (famUsed.get(k) || 0) + 1);
                answers.add(ansKey(q)); perCat[c]++; if (niche) nicheCat[c]++;
                return q;
              }
            }
            return null;
          };
          const out = [];
          let order = shuffle(keys.slice(), rnd), last = null, guard = 0;
          const dry = new Set();
          while (out.length < n && guard++ < 2000 && dry.size < keys.length) {
            if (order.length > 1 && order[0] === last) order.push(order.shift());            // no category twice in a row
            for (const c of order) {
              if (out.length >= n) break;
              if (dry.has(c)) continue;
              const q = draw(c);
              if (q) { out.push(q); used.add(q.id); last = c; } else dry.add(c);
            }
            order = shuffle(order, rnd);
          }
          return out;
        };
        const cats = settings.categories;
        const picMode = settings.pictures || 'off';
        const rounds = (settings.picRounds || PIC_ROUNDS).filter(r => byRound[r]);
        const picPools = {};
        for (const r of rounds) picPools[r] = byRound[r].filter(q => picMode === 'only' || cats.includes(q.c));
        const picKeys = rounds.filter(r => picPools[r].length);
        if (picMode === 'only') return run(picPools, picKeys, N);
        if (picMode === 'off' || !picKeys.length || N < 3) return run(byCat, cats, N);
        const pics = run(picPools, picKeys, Math.max(1, Math.round(N * PIC_SHARE)));
        const texts = run(byCat, cats, N - pics.length);
        // spread the pictures evenly through the game
        const out = texts.slice();
        pics.forEach((q, i) => {
          const target = Math.min(out.length, Math.floor((i + 0.6) * N / pics.length));
          let pos = target;
          for (let k = 0; k <= out.length; k++) {                                            // nearest slot with different neighbours
            const cand = [target + k, target - k].find(x => x >= 0 && x <= out.length && (!out[x - 1] || out[x - 1].c !== q.c) && (!out[x] || out[x].c !== q.c));
            if (cand !== undefined) { pos = cand; break; }
          }
          out.splice(pos, 0, q);
        });
        return out;
      }
    };
  }

  class Room {
    constructor(code, opts) {
      this.code = code;
      this.picker = opts.picker;
      this.emit = opts.emit;
      this.setTimeout = opts.setTimeout || ((fn, ms) => setTimeout(fn, ms));
      this.clearTimeout = opts.clearTimeout || (t => clearTimeout(t));
      this.now = opts.now || (() => Date.now());
      this.rnd = opts.random || Math.random;
      this.players = new Map();       // id -> player
      this.order = [];                // join order of ids
      this.hostId = null;
      this.settings = cleanSettings(opts.settings);
      this.state = 'lobby';
      this.used = new Set();
      this.seen = new Set();          // question ids players saw in earlier games (from their devices)
      this.questions = [];
      this.qIndex = -1;
      this.current = null;
      this.timer = null;
      this.lastActive = this.now();
      this.solo = !!opts.solo;
      this.turns = !!opts.turns;   // pass-and-play: players answer one at a time on one device
    }

    /* ---------- players ---------- */
    addPlayer(id, name) {
      this.lastActive = this.now();
      if (this.players.has(id)) { const p = this.players.get(id); p.connected = true; this.broadcastRoom(); this.syncPlayer(id); return { ok: true }; }
      if (this.players.size >= MAX_PLAYERS) return { ok: false, error: 'This game is full (8 players max).' };
      name = String(name || '').replace(/[\u0000-\u001f<>]/g, '').trim().slice(0, 16) || 'Player';
      // avoid duplicate names
      let base = name, n = 2;
      while ([...this.players.values()].some(p => p.name.toLowerCase() === name.toLowerCase())) name = `${base.slice(0, 13)} ${n++}`;
      const used = new Set([...this.players.values()].map(p => p.icon));
      const icon = ICONS.find(i => !used.has(i)) || ICONS[this.players.size % ICONS.length];
      this.players.set(id, { id, name, icon, score: 0, wedges: [], correct: 0, streak: 0, connected: true, answer: null });
      this.order.push(id);
      if (!this.hostId) this.hostId = id;
      this.broadcastRoom();
      this.syncPlayer(id);
      return { ok: true };
    }

    setConnected(id, connected) {
      const p = this.players.get(id); if (!p) return;
      p.connected = connected;
      if (!connected && this.hostId === id) this.reassignHost();
      if (connected && !this.connectedIds().some(x => x === this.hostId)) this.hostId = id;
      this.broadcastRoom();
      if (this.state === 'question') this.checkAllAnswered();
    }

    removePlayer(id) {
      if (!this.players.has(id)) return;
      this.players.delete(id);
      this.order = this.order.filter(x => x !== id);
      if (this.hostId === id) this.reassignHost();
      this.broadcastRoom();
      if (this.state === 'question') this.checkAllAnswered();
    }

    kick(byId, targetId) {
      if (byId !== this.hostId || targetId === byId) return;
      this.emit(targetId, 'kicked', { message: 'The host removed you from the game.' });
      this.removePlayer(targetId);
    }

    reassignHost() {
      const next = this.order.find(id => this.players.get(id) && this.players.get(id).connected);
      this.hostId = next || this.order[0] || null;
    }

    connectedIds() { return this.order.filter(id => this.players.get(id) && this.players.get(id).connected); }
    isEmpty() { return this.connectedIds().length === 0; }

    publicPlayers() {
      return this.order.map(id => {
        const p = this.players.get(id);
        return { id, name: p.name, icon: p.icon, score: p.score, wedges: p.wedges, correct: p.correct, connected: p.connected, isHost: id === this.hostId, answered: !!p.answer };
      });
    }

    roomState() {
      return { code: this.code, state: this.state, hostId: this.hostId, players: this.publicPlayers(), settings: this.settings, maxPlayers: MAX_PLAYERS, qIndex: this.qIndex, total: this.questions.length, solo: this.solo, passPlay: this.turns };
    }

    broadcastRoom() { this.emit(null, 'room', this.roomState()); }

    syncPlayer(id) {
      // late joiner / reconnect: replay current phase
      if (this.state === 'question' && this.current) this.emit(id, 'question', this.questionPayload(id));
      else if (this.state === 'reveal' && this.lastReveal) this.emit(id, 'reveal', this.lastReveal);
      else if (this.state === 'final' && this.lastFinal) this.emit(id, 'final', this.lastFinal);
    }

    /* ---------- settings / start ---------- */
    addSeen(ids) {
      if (!Array.isArray(ids)) return;
      for (const id of ids.slice(-1500)) if ((typeof id === 'string' && id.length < 12) || Number.isInteger(id)) this.seen.add(id);
      if (this.seen.size > 6000) this.seen = new Set([...this.seen].slice(-4000));
    }

    updateSettings(byId, s) {
      if (byId !== this.hostId || this.state === 'question' || this.state === 'reveal') return;
      this.settings = cleanSettings(s, this.settings);
      this.broadcastRoom();
    }

    start(byId) {
      if (byId !== this.hostId) return { ok: false, error: 'Only the host can start the game.' };
      if (this.state === 'question' || this.state === 'reveal') return { ok: false };
      this.questions = this.picker.pick(this.settings, this.used, this.rnd, this.seen);
      if (!this.questions.length) return { ok: false, error: 'No questions match those settings.' };
      for (const p of this.players.values()) Object.assign(p, { score: 0, wedges: [], correct: 0, streak: 0, answer: null });
      this.qIndex = -1;
      this.lastFinal = null;
      this.emit(null, 'starting', { total: this.questions.length });
      this.next(true);
      return { ok: true };
    }

    backToLobby(byId) {
      if (byId !== this.hostId) return;
      this.clearTimer();
      this.state = 'lobby'; this.current = null; this.qIndex = -1;
      for (const p of this.players.values()) Object.assign(p, { score: 0, wedges: [], correct: 0, streak: 0, answer: null });
      this.broadcastRoom();
    }

    clearTimer() { if (this.timer) { this.clearTimeout(this.timer); this.timer = null; } }

    /* ---------- question loop ---------- */
    next(force) {
      if (!force && this.state !== 'reveal') return;
      this.clearTimer();
      this.qIndex++;
      if (this.qIndex >= this.questions.length) return this.finish();
      const q = this.questions[this.qIndex];
      let type;
      if (this.settings.mode === 'mc') type = 'mc';
      else if (this.settings.mode === 'fib') type = 'fib';
      else type = q.w && q.fib ? (this.rnd() < 0.6 ? 'mc' : 'fib') : (q.w ? 'mc' : 'fib');
      let choices = null, correctIndex = -1;
      if (type === 'mc') {
        choices = shuffle([q.a, ...(q.img ? shuffle(q.w.slice(), this.rnd) : q.w).slice(0, 3)], this.rnd);
        correctIndex = choices.indexOf(q.a);
      }
      const timeLimit = this.settings.timeLimit + (type === 'fib' ? 10 : 0);
      this.current = { q, type, choices, correctIndex, startedAt: this.now(), timeLimit };
      for (const p of this.players.values()) p.answer = null;
      this.state = 'question';
      if (this.turns) {
        this.turnOrder = this.order.slice();
        this.turnIdx = -1;
        this.broadcastRoom();
        return this.nextTurn();
      }
      this.emit(null, 'question', this.questionPayload());
      this.broadcastRoom();
      this.timer = this.setTimeout(() => this.reveal(), timeLimit * 1000 + 600);
    }

    /* ---------- pass-and-play turns ---------- */
    nextTurn() {
      this.clearTimer();
      this.turnIdx++;
      this.turnStarted = null;
      if (this.turnIdx >= this.turnOrder.length) return this.reveal();
      const id = this.turnOrder[this.turnIdx];
      const p = this.players.get(id);
      this.emit(null, 'turn', { id, name: p.name, icon: p.icon, turn: this.turnIdx, turns: this.turnOrder.length, index: this.qIndex, total: this.questions.length, category: this.current.q.c, categoryName: this.current.q.prn || CAT_NAMES[this.current.q.c] });
      this.broadcastRoom();
    }

    beginTurn() {
      if (!this.turns || this.state !== 'question' || this.turnStarted) return;
      this.turnStarted = this.now();
      this.current.startedAt = this.turnStarted;
      this.emit(null, 'question', this.questionPayload());
      this.timer = this.setTimeout(() => this.nextTurn(), this.current.timeLimit * 1000 + 600);
    }

    questionPayload() {
      const c = this.current;
      const elapsed = this.now() - c.startedAt;
      return {
        index: this.qIndex, total: this.questions.length, type: c.type, qid: c.q.id,
        category: c.q.c, categoryName: c.q.prn || CAT_NAMES[c.q.c], difficulty: c.q.d, img: c.q.img || null,
        text: c.q.q, choices: c.choices, timeLimit: c.timeLimit,
        remainingMs: Math.max(0, c.timeLimit * 1000 - elapsed)
      };
    }

    answer(id, data) {
      if (this.state !== 'question' || !this.current) return;
      const p = this.players.get(id); if (!p || p.answer) return;
      if (this.turns && (id !== this.turnOrder[this.turnIdx] || !this.turnStarted)) return;
      const c = this.current;
      const ms = this.now() - c.startedAt;
      if (ms > c.timeLimit * 1000 + 1500) return;
      let correct = false, text = '';
      if (c.type === 'mc') {
        const idx = parseInt(data && data.choice, 10);
        if (!(idx >= 0 && idx < c.choices.length)) return;
        correct = idx === c.correctIndex; text = c.choices[idx];
        p.answer = { choice: idx, text, correct, ms };
      } else {
        text = String((data && data.text) || '').slice(0, 80);
        correct = Match.isCorrect(text, c.q.a, c.q.alt, this.picker.known);
        p.answer = { text, correct, ms };
      }
      this.emit(id, 'answerAck', { received: true });
      this.broadcastRoom();
      if (this.turns) { this.clearTimer(); this.timer = this.setTimeout(() => this.nextTurn(), 900); return; }
      this.checkAllAnswered();
    }

    checkAllAnswered() {
      if (this.turns) return;
      const ids = this.connectedIds();
      if (ids.length && ids.every(id => this.players.get(id).answer)) {
        this.clearTimer();
        this.timer = this.setTimeout(() => this.reveal(), 400);
      }
    }

    reveal() {
      if (this.state !== 'question') return;
      this.clearTimer();
      const c = this.current;
      const results = [];
      const limit = c.timeLimit * 1000;
      for (const id of this.order) {
        const p = this.players.get(id);
        const a = p.answer;
        let points = 0;
        if (a && a.correct) {
          const speed = Math.max(0, 1 - a.ms / limit);
          points = Math.round((c.type === 'fib' ? 150 : 100) + 50 * speed + 10 * (c.q.d - 1));
          p.streak++;
          if (p.streak >= 3) points += 25;
          p.correct++;
          if (!p.wedges.includes(c.q.c)) p.wedges.push(c.q.c);
        } else p.streak = 0;
        p.score += points;
        results.push({ id, name: p.name, icon: p.icon, answered: !!a, text: a ? a.text : '', choice: a ? a.choice : null, correct: !!(a && a.correct), points, ms: a ? a.ms : null, streak: p.streak });
      }
      this.state = 'reveal';
      this.lastReveal = {
        index: this.qIndex, total: this.questions.length, type: c.type, qid: c.q.id,
        category: c.q.c, categoryName: c.q.prn || CAT_NAMES[c.q.c], difficulty: c.q.d, img: c.q.img || null,
        text: c.q.q, choices: c.choices, correctIndex: c.correctIndex, answer: c.q.a,
        results, players: this.publicPlayers(), last: this.qIndex >= this.questions.length - 1,
        nextInMs: REVEAL_MS
      };
      this.emit(null, 'reveal', this.lastReveal);
      this.broadcastRoom();
      this.timer = this.setTimeout(() => this.next(), REVEAL_MS);
    }

    hostNext(byId) { if (byId === this.hostId && this.state === 'reveal') this.next(); }

    finish() {
      this.clearTimer();
      this.state = 'final';
      this.current = null;
      const standings = this.publicPlayers().sort((a, b) => b.score - a.score || b.correct - a.correct);
      let rank = 0, prev = null;
      standings.forEach((p, i) => { if (prev === null || p.score !== prev) rank = i + 1; p.rank = rank; prev = p.score; });
      this.lastFinal = { standings, total: this.questions.length };
      this.emit(null, 'final', this.lastFinal);
      this.broadcastRoom();
    }

    destroy() { this.clearTimer(); }
  }

  return { Room, QuestionPicker, CATS, CAT_NAMES, PIC_ROUNDS, PIC_NAMES, MAX_PLAYERS, DEFAULT_SETTINGS, cleanSettings };
});
