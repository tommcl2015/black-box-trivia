"""Generic 1-bit silhouette renderer for picture rounds (ships, tanks, rockets, spacecraft, trains).
Takes 2D polygons in real units (y up), fits them in the 96x64 frame and adds a scene, matching aircraft3d.py."""
import math
from PIL import Image, ImageDraw
from common import *

def fit_draw(polys, scene='sky', pad=6, ground_h=12, align='bottom', holes=(), scale_max=None, vpad=None, xmin=None, exag=1.0):
    """polys: list of [(x,y),...] in real units, y up. holes: polys punched white after fill."""
    polys = list(polys)
    allp = [p for q in [(x[1] if isinstance(x, tuple) else x) for x in polys] + list(holes) for p in q]
    xs = [x for x, _ in allp]; ys = [y for _, y in allp]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    if xmin is not None: x0 = xmin                 # anything further left runs off the edge of the picture
    SC = 8; BW, BH = W * SC, H * SC
    GY = H - ground_h if scene in ('sky', 'water', 'rails', 'pad', 'moonground', 'air') else H
    top = 4 if vpad is None else vpad
    avail_h = (GY - top - 1) if scene != 'space' else H - 2 * pad
    s = min((W - 2 * pad) * SC / max(1e-9, x1 - x0), avail_h * SC / max(1e-9, y1 - y0))
    if scale_max: s = min(s, scale_max * SC)
    ox = (BW - (x1 - x0) * s) / 2
    if scene == 'space': oy = (BH - (y1 - y0) * s) / 2
    elif scene == 'air': oy = (GY * SC - (y1 - y0) * s) / 2
    else:
        sink = {'water': 0.8, 'rails': -1.0}.get(scene, 0)          # ships sit a little in the water; trains sit on the rail
        oy = (GY + sink) * SC - (y1 - y0) * s
    T = lambda p: ((p[0] - x0) * s + ox, (y1 - p[1]) * s + oy)
    big = Image.new('L', (BW, BH), 0); bd = ImageDraw.Draw(big)
    for p in polys:                               # ('h', poly) entries cut a hole at that point in the drawing order
        if isinstance(p, tuple): bd.polygon([T(v) for v in p[1]], fill=0)
        elif len(p) >= 3: bd.polygon([T(v) for v in p], fill=255)
    for p in holes:
        if len(p) >= 3: bd.polygon([T(v) for v in p], fill=0)
    small = big.resize((W, H), Image.BOX)
    im, d = canvas(); px = im.load(); sp = small.load()
    if scene in ('sky', 'pad', 'water', 'rails', 'air'): clouds(d, [(6, 5), (72, 9)] if scene != 'air' else [(4, 40), (76, 44)])
    if scene in ('space', 'moonground'):
        import random
        r = random.Random(7)
        for _ in range(40 if scene == 'space' else 18): px[r.randrange(2, W - 2), r.randrange(2, (H - 2) if scene == 'space' else GY - 2)] = BLK
    for y in range(H):
        for x in range(W):
            if sp[x, y] > 70: px[x, y] = BLK
            elif scene == 'space' and sp[x, y] > 20: px[x, y] = WHT
    if scene in ('sky', 'pad', 'air'):
        d.line((1, GY, W - 2, GY), fill=BLK); fill_pattern(im, (1, GY + 1, W - 1, H - 1), 6)
    if scene == 'moonground':
        d.line((1, GY, W - 2, GY), fill=BLK); fill_pattern(im, (1, GY + 1, W - 1, H - 1), 1)
        for cx, cy in [(12, GY + 5), (70, GY + 7), (44, GY + 9)]: d.ellipse((cx - 4, cy - 1, cx + 4, cy + 1), outline=BLK, fill=WHT)
        for y in range(GY + 1, H - 1):
            for x in range(1, W - 1):
                if sp[x, y] > 70: px[x, y] = BLK
    if scene == 'water':
        for y in range(GY, H - 1):
            for x in range(1, W - 1):
                if sp[x, y] <= 70 and (y - GY) % 3 == 0 and (x + y) % 6 < 3: px[x, y] = BLK
    if scene == 'rails':
        d.line((1, GY, W - 2, GY), fill=BLK); d.line((1, GY + 1, W - 2, GY + 1), fill=BLK)
        for x in range(2, W - 2, 4): d.line((x, GY + 2, x + 1, GY + 2), fill=BLK)
        fill_pattern(im, (1, GY + 4, W - 1, H - 1), 6)
    frame(d)
    return im

# ---- shape helpers (real units, y up) ----
def rect(x0, y0, x1, y1): return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
def circle(cx, cy, r, n=28): return [(cx + r * math.cos(2 * math.pi * i / n), cy + r * math.sin(2 * math.pi * i / n)) for i in range(n)]
def ellipse(cx, cy, rx, ry, n=32): return [(cx + rx * math.cos(2 * math.pi * i / n), cy + ry * math.sin(2 * math.pi * i / n)) for i in range(n)]
def line(x0, y0, x1, y1, w):
    dx, dy = x1 - x0, y1 - y0; L = math.hypot(dx, dy) or 1; nx, ny = -dy / L * w / 2, dx / L * w / 2
    return [(x0 + nx, y0 + ny), (x1 + nx, y1 + ny), (x1 - nx, y1 - ny), (x0 - nx, y0 - ny)]
def revolve(profile, axis='y'):
    """profile: [(r, h)] from bottom to top for an axisymmetric rocket -> side-view polygon."""
    right = [(r, h) for r, h in profile]; left = [(-r, h) for r, h in reversed(profile)]
    return right + left
