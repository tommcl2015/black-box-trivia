/* 1-bit artwork: pixel icons, category fill patterns, pie wedges. All drawn as inline SVG. */
(function () {
  const PIX = {
    disk: [
      '################',
      '#..#########.#.#',
      '#..#########.#.#',
      '#..#########...#',
      '#..#########...#',
      '#..............#',
      '#..............#',
      '#.############.#',
      '#.#..........#.#',
      '#.#.########.#.#',
      '#.#..........#.#',
      '#.#.######...#.#',
      '#.#..........#.#',
      '#.#..........#.#',
      '##############.#',
      '.###############'],
    bomb: [
      '..........#.#...',
      '...........#....',
      '..........#.#...',
      '.........#......',
      '......###.......',
      '.....#####......',
      '...#########....',
      '..###########...',
      '.#############..',
      '.##.##########..',
      '.#.###########..',
      '.##.##########..',
      '.#############..',
      '..###########...',
      '...#########....',
      '.....#####......'],
    watch: [
      '.....######.....',
      '...##......##...',
      '..#....#.....#..',
      '.#.....#......#.',
      '.#.....#......#.',
      '#......#.......#',
      '#......#.......#',
      '#......#####...#',
      '#..............#',
      '#..............#',
      '.#............#.',
      '.#............#.',
      '..#..........#..',
      '...##......##...',
      '.....######.....',
      '................'],
    cup: [
      '................',
      '....#..#..#.....',
      '.....#..#..#....',
      '....#..#..#.....',
      '................',
      '.###########....',
      '.#.........####.',
      '.#.........#..#.',
      '.#.........#..#.',
      '.#.........####.',
      '.#.........#....',
      '..#.......#.....',
      '...#######......',
      '.#############..',
      '..###########...',
      '................'],
    bug: [
      '....#......#....',
      '.....#....#.....',
      '......####......',
      '.....######.....',
      '.#..########..#.',
      '..#.###..###.#..',
      '...##########...',
      '#...###..###...#',
      '.#############..',
      '...##########...',
      '..#.###..###.#..',
      '.#..########..#.',
      '....########....',
      '...#..####..#...',
      '..#....##....#..',
      '................'],
    rocket: [
      '.......##.......',
      '......####......',
      '.....#....#.....',
      '.....#.##.#.....',
      '.....#.##.#.....',
      '.....#....#.....',
      '.....#....#.....',
      '.....#....#.....',
      '....##....##....',
      '...#.#....#.#...',
      '..#..#....#..#..',
      '..#..######..#..',
      '..####.##.####..',
      '......#..#......',
      '.....#.##.#.....',
      '......#..#......'],
    dog: [
      '................',
      '.##.........##..',
      '####.......####.',
      '##.#########.##.',
      '#.............#.',
      '#..##.....##..#.',
      '#..##.....##..#.',
      '#.............#.',
      '.#....###....#..',
      '.#....###....#..',
      '..#....#....#...',
      '...#..#.#..#....',
      '....#.....#.....',
      '.....#####......',
      '................',
      '................'],
    globe: [
      '.....######.....',
      '...##..#...##...',
      '..#...#.#....#..',
      '.#...#...#....#.',
      '.##############.',
      '#....#...#.....#',
      '#....#...#.....#',
      '################',
      '#....#...#.....#',
      '#....#...#.....#',
      '.##############.',
      '.#...#...#....#.',
      '..#...#.#....#..',
      '...##..#...##...',
      '.....######.....',
      '................'],
    trophy: [
      '..############..',
      '###.########.###',
      '#.#.########.#.#',
      '#.#.########.#.#',
      '.##.########.##.',
      '...#.######.#...',
      '....#.####.#....',
      '.....#.##.#.....',
      '......#..#......',
      '.......##.......',
      '.......##.......',
      '......####......',
      '.....######.....',
      '....########....',
      '....#......#....',
      '....########....'],
    doc: [
      '.#########......',
      '.#.......##.....',
      '.#.......#.#....',
      '.#.......####...',
      '.#..........#...',
      '.#.#######..#...',
      '.#..........#...',
      '.#.######...#...',
      '.#..........#...',
      '.#.#######..#...',
      '.#..........#...',
      '.#.#####....#...',
      '.#..........#...',
      '.#..........#...',
      '.############...',
      '................'],
    trash: [
      '......####......',
      '.....#....#.....',
      '.##############.',
      '.#............#.',
      '.##############.',
      '..#..........#..',
      '..#.#..#..#..#..',
      '..#.#..#..#..#..',
      '..#.#..#..#..#..',
      '..#.#..#..#..#..',
      '..#.#..#..#..#..',
      '..#.#..#..#..#..',
      '..#.#..#..#..#..',
      '..#..........#..',
      '..############..',
      '................']
  };

  function pixPath(rows) {
    let d = '';
    rows.forEach((r, y) => {
      let x = 0;
      while (x < r.length) {
        if (r[x] === '#') { let w = 1; while (r[x + w] === '#') w++; d += `M${x} ${y}h${w}v1h-${w}z`; x += w; } else x++;
      }
    });
    return d;
  }
  const pathCache = {};
  function icon(name, cls) {
    const rows = PIX[name] || PIX.disk;
    const d = pathCache[name] || (pathCache[name] = pixPath(rows));
    // white backing so icons read on the dithered desktop
    return `<svg class="icon ${cls || ''}" viewBox="0 0 16 16" shape-rendering="crispEdges" aria-hidden="true"><path d="${d}" fill="#000"/></svg>`;
  }

  /* 8x8 category patterns */
  const PATTERNS = {
    geo: ['10001000', '00000000', '00100010', '00000000', '10001000', '00000000', '00100010', '00000000'], // dots
    ent: ['10001000', '01000100', '00100010', '00010001', '10001000', '01000100', '00100010', '00010001'], // diagonal
    his: ['11111111', '00000000', '00000000', '00000000', '11111111', '00000000', '00000000', '00000000'], // horizontal
    art: ['10101010', '01010101', '10101010', '01010101', '10101010', '01010101', '10101010', '01010101'], // 50% gray
    sci: ['10001000', '10001000', '10001000', '10001000', '10001000', '10001000', '10001000', '10001000'], // vertical
    spo: ['11111111', '10001000', '10001000', '10001000', '11111111', '10001000', '10001000', '10001000']  // grid
  };
  const CAT_ORDER = ['geo', 'ent', 'his', 'art', 'sci', 'spo'];

  function patRects(rows) {
    let s = '';
    rows.forEach((r, y) => [...r].forEach((c, x) => { if (c === '1') s += `<rect x="${x}" y="${y}" width="1" height="1"/>`; }));
    return s;
  }
  function patternDataUri(cat) {
    const svg = `<svg xmlns='http://www.w3.org/2000/svg' width='8' height='8' shape-rendering='crispEdges'><rect width='8' height='8' fill='#fff'/><g fill='#000'>${patRects(PATTERNS[cat])}</g></svg>`;
    return `url("data:image/svg+xml,${encodeURIComponent(svg)}")`;
  }

  function installDefs() {
    const ns = 'http://www.w3.org/2000/svg';
    const svg = document.createElementNS(ns, 'svg');
    svg.setAttribute('width', '0'); svg.setAttribute('height', '0');
    svg.style.position = 'absolute';
    svg.innerHTML = '<defs>' + CAT_ORDER.map(c =>
      `<pattern id="pat-${c}" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#fff"/><g fill="#000" shape-rendering="crispEdges">${patRects(PATTERNS[c])}</g></pattern>`
    ).join('') + '</defs>';
    document.body.appendChild(svg);
    const style = document.createElement('style');
    style.textContent = CAT_ORDER.map(c => `.sw-${c}{background-image:${patternDataUri(c)};background-size:8px 8px;image-rendering:pixelated}`).join('\n');
    document.head.appendChild(style);
  }

  // six-wedge pie; `have` = array of category ids earned
  // Isometric cube: three visible faces, each split into two triangles = six category pieces.
  // Pieces run clockwise from the top face, matching CAT_ORDER.
  const CUBE = { T: [50, 4], UR: [90, 27], LR: [90, 73], B: [50, 96], LL: [10, 73], UL: [10, 27], C: [50, 50] };
  const PIECES = [['T', 'UR', 'C'], ['UR', 'LR', 'C'], ['LR', 'B', 'C'], ['B', 'LL', 'C'], ['LL', 'UL', 'C'], ['UL', 'T', 'C']];
  function cube(have, cls, scale) {
    have = have || [];
    const w = scale || 3;
    const pt = k => CUBE[k].join(' ');
    let paths = '';
    CAT_ORDER.forEach((c, i) => {
      const fill = have.includes(c) ? `url(#pat-${c})` : '#fff';
      paths += `<path d="M${PIECES[i].map(pt).join('L')}Z" fill="${fill}" stroke="#000" stroke-width="${w * 0.5}" stroke-linejoin="round"/>`;
    });
    // cube edges drawn heavier than the diagonals that split each face
    const edges = `<path d="M${pt('T')}L${pt('UR')}L${pt('LR')}L${pt('B')}L${pt('LL')}L${pt('UL')}Z M${pt('C')}L${pt('UL')} M${pt('C')}L${pt('UR')} M${pt('C')}L${pt('B')}" fill="none" stroke="#000" stroke-width="${w}" stroke-linejoin="round"/>`;
    return `<svg class="pie cube ${cls || ''}" viewBox="0 0 100 100" role="img" aria-label="${have.length} of 6 sides of the box">${paths}${edges}</svg>`;
  }
  const pie = cube;

  function swatch(cat) { return `<span class="swatch sw-${cat}" aria-hidden="true"></span>`; }

  const ALERT = {
    stop: '<svg viewBox="0 0 32 32" shape-rendering="crispEdges"><path d="M10 1h12l9 9v12l-9 9H10l-9-9V10z" fill="#fff" stroke="#000" stroke-width="2"/><path d="M10 10l12 12M22 10L10 22" stroke="#000" stroke-width="3"/></svg>',
    caution: '<svg viewBox="0 0 32 32" shape-rendering="crispEdges"><path d="M16 2L31 29H1z" fill="#fff" stroke="#000" stroke-width="2"/><rect x="14.5" y="11" width="3" height="10" fill="#000"/><rect x="14.5" y="23" width="3" height="3" fill="#000"/></svg>',
    note: '<svg viewBox="0 0 32 32" shape-rendering="crispEdges"><path d="M4 4h24v18H14l-7 7v-7H4z" fill="#fff" stroke="#000" stroke-width="2"/><rect x="14.5" y="7" width="3" height="3" fill="#000"/><rect x="14.5" y="12" width="3" height="7" fill="#000"/></svg>'
  };

  window.Art = { icon, pie, cube, swatch, installDefs, ALERT, CAT_ORDER, PATTERNS };
})();
