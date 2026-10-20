/* Spelling-tolerant answer matching. Shared by server (Node) and browser (solo mode). */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.TriviaMatch = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  const NUM_WORDS = {
    zero: 0, one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9, ten: 10,
    eleven: 11, twelve: 12, thirteen: 13, fourteen: 14, fifteen: 15, sixteen: 16, seventeen: 17,
    eighteen: 18, nineteen: 19, twenty: 20, thirty: 30, forty: 40, fifty: 50, sixty: 60, seventy: 70,
    eighty: 80, ninety: 90, hundred: 100, thousand: 1000, first: 1, second: 2, third: 3, fourth: 4,
    fifth: 5, sixth: 6, seventh: 7, eighth: 8, ninth: 9, tenth: 10
  };

  function normalize(s) {
    if (s == null) return '';
    s = String(s).normalize('NFD').replace(/[̀-ͯ]/g, '');
    s = s.toLowerCase()
      .replace(/ø/g, 'o').replace(/æ/g, 'ae').replace(/ß/g, 'ss').replace(/ł/g, 'l')
      .replace(/&/g, ' and ')
      .replace(/(\d),(\d)/g, '$1$2')          // 1,000 -> 1000
      .replace(/['’‘`".]/g, '')               // drop apostrophes, quotes, periods
      .replace(/[^a-z0-9]+/g, ' ')            // everything else -> space
      .trim();
    s = s.replace(/^(the|a|an) /, '');
    s = s.split(' ').map(w => (w in NUM_WORDS ? String(NUM_WORDS[w]) : w))
      .map(w => w.replace(/(\d+)(st|nd|rd|th)$/, '$1')).join(' ');
    return s;
  }

  function compact(s) { return s.replace(/ /g, ''); }

  function phonetic(s) {
    return s.replace(/ph/g, 'f').replace(/ck/g, 'k').replace(/tch/g, 'ch').replace(/sch/g, 'sh')
      .replace(/c(?=[eiy])/g, 's').replace(/c/g, 'k').replace(/q/g, 'k').replace(/x/g, 'ks')
      .replace(/z/g, 's').replace(/w/g, 'v').replace(/y/g, 'i').replace(/gh/g, 'g')
      .replace(/([a-z])\1+/g, '$1')                 // collapse doubles
      .replace(/(?!^)[aeiou]+/g, m => m[0]);        // squash vowel runs
  }

  // Optimal string alignment distance (Levenshtein + adjacent transpositions)
  function dist(a, b, max) {
    const n = a.length, m = b.length;
    if (Math.abs(n - m) > max) return max + 1;
    let prev2 = null, prev = new Array(m + 1), cur = new Array(m + 1);
    for (let j = 0; j <= m; j++) prev[j] = j;
    for (let i = 1; i <= n; i++) {
      cur[0] = i; let rowMin = i;
      for (let j = 1; j <= m; j++) {
        const cost = a[i - 1] === b[j - 1] ? 0 : 1;
        let v = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost);
        if (prev2 && i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) v = Math.min(v, prev2[j - 2] + 1);
        cur[j] = v; if (v < rowMin) rowMin = v;
      }
      if (rowMin > max) return max + 1;
      prev2 = prev.slice(); [prev, cur] = [cur, prev];
    }
    return prev[m];
  }

  function allowance(len) {
    if (len <= 3) return 0;
    if (len <= 5) return 1;
    if (len <= 8) return 2;
    if (len <= 12) return 3;
    return Math.min(5, Math.floor(len * 0.25));
  }

  const isNum = s => /^\d+$/.test(s);

  function matchOne(guess, answer) {
    const g = normalize(guess), a = normalize(answer);
    if (!g || !a) return false;
    if (g === a) return true;
    const gc = compact(g), ac = compact(a);
    if (gc === ac) return true;
    // numbers must be exact (allow "1977" vs "in 1977")
    if (isNum(ac)) return g.split(' ').includes(ac) && g.split(' ').filter(isNum).length === 1;
    if (/\d/.test(ac) && ac.length <= 6) return false; // short alphanumerics like "PS4", "B12" must be exact
    const allow = allowance(ac.length);
    if (allow === 0) return false;
    if (dist(gc, ac, allow) <= allow) return true;
    const gp = phonetic(gc), ap = phonetic(ac);
    if (gp === ap && ac.length >= 4) return true;
    if (dist(gp, ap, allowance(ap.length)) <= allowance(ap.length) && ac.length >= 6) return true;
    return false;
  }

  // known: optional Set of normalized real answers (other questions' answers, distractors).
  // A guess that is exactly a *different* real answer is treated as that answer, not a typo.
  function isCorrect(guess, answer, alts, known) {
    const g = normalize(guess);
    const exact = [answer].concat(alts || []).some(x => normalize(x) === g || compact(normalize(x)) === compact(g));
    if (exact) return true;
    if (known && known.has(compact(g))) return false;
    if (matchOne(guess, answer)) return true;
    if (alts) for (const alt of alts) if (matchOne(guess, alt)) return true;
    return false;
  }

  return { normalize, compact, isCorrect, matchOne, dist };
});
