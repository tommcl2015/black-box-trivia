#!/usr/bin/env python3
"""Famous NASCAR ovals drawn from their shapes (no external data), same style as circuits.py."""
import math, sys
from circuits import draw
from common import save

def hull_of_circles(circles, n=90):
    pts = [(cx + r * math.cos(2 * math.pi * k / n), cy + r * math.sin(2 * math.pi * k / n)) for cx, cy, r in circles for k in range(n)]
    pts = sorted(set(pts))
    def half(P):
        h = []
        for p in P:
            while len(h) >= 2 and (h[-1][0] - h[-2][0]) * (p[1] - h[-2][1]) - (h[-1][1] - h[-2][1]) * (p[0] - h[-2][0]) <= 0: h.pop()
            h.append(p)
        return h
    lo, up = half(pts), half(pts[::-1]); H = lo[:-1] + up[:-1]
    i = min(range(len(H)), key=lambda j: (H[j][1] + abs(H[j][0] - sum(c[0] for c in circles) / len(circles)) * .05))
    return H[i:] + H[:i]                                              # start on the front stretch (bottom)

def scale(pts, s=.01): return [(x * s, y * s) for x, y in pts]

TRACKS = {
    'martinsville': hull_of_circles([(-2.6, 0, .75), (2.6, 0, .75)]),                    # the "paperclip"
    'bristol': hull_of_circles([(-.8, 0, 1.25), (.8, 0, 1.25)]),                          # short, round half-mile
    'darlington': hull_of_circles([(-1.4, 0, 1.15), (1.6, 0, .72)]),                      # the egg: turns 3-4 much tighter
    'pocono': hull_of_circles([(-2.4, 0, .5), (2.6, 0, .55), (-1.1, 2.6, .55)]),          # the "Tricky Triangle"
    'daytona': hull_of_circles([(-1.7, 0, 1.0), (1.7, 0, 1.0), (0, -1.0, .6)]),           # tri-oval
}
if __name__ == '__main__':
    for k in sys.argv[1:] or TRACKS: save(draw(scale(TRACKS[k])), 'circuits', 'nascar-' + k)
