/* Retro 1-bit-era sound effects, synthesized live with the Web Audio API (no audio files). */
(function () {
  let ctx = null, master = null;
  let enabled = true;
  try { enabled = localStorage.getItem('td_sound') !== 'off'; } catch (e) {}

  function ac() {
    if (!ctx) {
      const AC = window.AudioContext || window.webkitAudioContext;
      if (!AC) return null;
      ctx = new AC();
      master = ctx.createGain(); master.gain.value = 0.22; master.connect(ctx.destination);
    }
    if (ctx.state === 'suspended') ctx.resume();
    return ctx;
  }

  // one tone with a fast attack / exponential decay envelope
  function tone({ type = 'square', f = 880, f2 = null, t = 0, dur = 0.15, vol = 1, filter = null }) {
    const c = ac(); if (!c || !enabled) return;
    const start = c.currentTime + t;
    const o = c.createOscillator(); o.type = type;
    o.frequency.setValueAtTime(f, start);
    if (f2) o.frequency.exponentialRampToValueAtTime(f2, start + dur);
    const g = c.createGain();
    g.gain.setValueAtTime(0.0001, start);
    g.gain.exponentialRampToValueAtTime(vol, start + 0.005);
    g.gain.exponentialRampToValueAtTime(0.0001, start + dur);
    let node = o;
    if (filter) { const bq = c.createBiquadFilter(); Object.assign(bq, { type: filter.type || 'bandpass' }); bq.frequency.value = filter.f; bq.Q.value = filter.q || 4; o.connect(bq); node = bq; }
    node.connect(g); g.connect(master);
    o.start(start); o.stop(start + dur + 0.02);
  }

  function noise(t = 0, dur = 0.01, vol = 0.6, hp = 3000) {
    const c = ac(); if (!c || !enabled) return;
    const len = Math.max(1, Math.floor(c.sampleRate * dur));
    const buf = c.createBuffer(1, len, c.sampleRate), d = buf.getChannelData(0);
    for (let i = 0; i < len; i++) d[i] = (Math.random() * 2 - 1) * (1 - i / len);
    const s = c.createBufferSource(); s.buffer = buf;
    const f = c.createBiquadFilter(); f.type = 'highpass'; f.frequency.value = hp;
    const g = c.createGain(); g.gain.value = vol;
    s.connect(f); f.connect(g); g.connect(master); s.start(c.currentTime + t);
  }

  const S = {
    // the classic short system alert beep
    beep() { tone({ type: 'square', f: 1046, dur: 0.18, vol: 0.7 }); tone({ type: 'square', f: 1050, t: 0.0, dur: 0.18, vol: 0.2 }); },
    click() { noise(0, 0.012, 0.5, 2500); },
    // rising chirp, played twice ("eep-eep")
    correct() { tone({ type: 'sine', f: 700, f2: 2000, dur: 0.09, vol: 0.9 }); tone({ type: 'sine', f: 900, f2: 2600, t: 0.1, dur: 0.11, vol: 0.9 }); },
    // nasal honk – a duck-ish "wrong" sound
    wrong() {
      tone({ type: 'sawtooth', f: 330, f2: 210, dur: 0.22, vol: 0.9, filter: { f: 1100, q: 3 } });
      tone({ type: 'sawtooth', f: 300, f2: 190, t: 0.24, dur: 0.26, vol: 0.9, filter: { f: 900, q: 3 } });
    },
    tick() { noise(0, 0.008, 0.7, 4000); tone({ type: 'square', f: 2200, dur: 0.02, vol: 0.15 }); },
    join() { tone({ type: 'square', f: 660, dur: 0.06, vol: 0.5 }); tone({ type: 'square', f: 990, t: 0.07, dur: 0.08, vol: 0.5 }); },
    leave() { tone({ type: 'square', f: 990, dur: 0.06, vol: 0.4 }); tone({ type: 'square', f: 660, t: 0.07, dur: 0.08, vol: 0.4 }); },
    start() { [523, 659, 784, 1046].forEach((f, i) => tone({ type: 'triangle', f, t: i * 0.07, dur: 0.5 - i * 0.05, vol: 0.8 })); },
    timeout() { [784, 622, 494].forEach((f, i) => tone({ type: 'square', f, t: i * 0.12, dur: 0.11, vol: 0.5 })); },
    whoosh() { tone({ type: 'triangle', f: 200, f2: 1200, dur: 0.18, vol: 0.4 }); },
    win() {
      const notes = [523, 659, 784, 1046, 784, 1046, 1318];
      const times = [0, .1, .2, .3, .45, .55, .7];
      notes.forEach((f, i) => tone({ type: 'square', f, t: times[i], dur: i === notes.length - 1 ? .5 : .12, vol: .45 }));
    },
    lose() { [392, 370, 349, 330].forEach((f, i) => tone({ type: 'triangle', f, t: i * 0.22, dur: i === 3 ? .6 : .2, vol: .7 })); },
    unlock() { ac(); },
    get enabled() { return enabled; },
    set enabled(v) { enabled = !!v; try { localStorage.setItem('td_sound', enabled ? 'on' : 'off'); } catch (e) {} }
  };
  window.Sounds = S;
})();
