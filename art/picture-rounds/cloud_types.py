#!/usr/bin/env python3
"""Cloud types as NES-style 8-bit scenes at full 96x64, NES palette only, with a strip of landscape for scale."""
import sys, math, random
from PIL import Image, ImageDraw
from common import W, H, save
from paintings_nes import K

SKY = [(60, 188, 252), (104, 136, 252), (0, 120, 248)]       # bottom -> top bands
WH, L1, L2, G1, G2, G3 = (252, 252, 252), (216, 216, 216), (188, 188, 188), (124, 124, 124), (120, 120, 120), (80, 80, 80)
GRASS, GRASS_D, HILL = (0, 168, 0), (0, 104, 0), (0, 120, 0)

def sky(d, top=None, mid=None, bot=None, y_end=54):
    cols = [top or SKY[2], mid or SKY[1], bot or SKY[0]]
    for y in range(y_end):
        t = y / y_end; i = 0 if t < .33 else 1 if t < .66 else 2
        for x in range(W):
            # ordered dither at band edges
            edge = (t * 3) % 1
            c = cols[i]
            if i < 2 and edge > .8 and (x + y) % 2 == 0: c = cols[i + 1]
            d.point((x, y), fill=c)

def land(d, y=54, hills=True, col=GRASS):
    if hills:
        for cx, r in ((14, 14), (52, 18), (88, 12)): d.ellipse((cx - r, y - r // 3, cx + r, y + r), fill=HILL)
    d.rectangle((0, y + 2, W, H), fill=col)
    rnd = random.Random(3)
    for _ in range(40): d.point((rnd.randrange(W), rnd.randrange(y + 3, H)), fill=GRASS_D)

def puff(d, cx, cy, r, lit=WH, shade=L2, base=None):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=shade)
    d.ellipse((cx - r + 1, cy - r, cx + r - 2, cy + r - 2), fill=lit)

def cumulus_blob(d, x, y, w, h, rnd, lit=WH, shade=L2, base_col=G1):
    """Cauliflower heap: round cells filling a dome of width w and height h, flat grey base on y."""
    pts = []
    for _ in range(int(w * h / 6)):
        u = rnd.uniform(-1, 1); top = y - h * (1 - u * u) ** .5
        r = rnd.uniform(2.5, 6); px = x + w / 2 + u * (w / 2 - r)
        py = rnd.uniform(min(top + r, y - r), y - r); pts.append((px, py, r))
    pts.sort(key=lambda p: p[1])
    for px, py, r in pts: d.ellipse((px - r + 1, py - r + 1, px + r + 1, py + r + 1), fill=shade)
    for px, py, r in pts: d.ellipse((px - r, py - r, px + r - 1, py + r - 1.5), fill=lit)
    d.rectangle((x + 2, y - 2, x + w - 2, y - 1), fill=L1); d.rectangle((x + 3, y - 1, x + w - 3, y), fill=base_col)

def finish(im):
    ImageDraw.Draw(im).rectangle((0, 0, W - 1, H - 1), outline=K); return im

def new(): im = Image.new('RGB', (W, H)); return im, ImageDraw.Draw(im)

def cumulus():
    im, d = new(); sky(d); rnd = random.Random(1)
    for x, y, w, h in ((4, 34, 30, 18), (42, 24, 24, 13), (70, 40, 22, 11)): cumulus_blob(d, x, y, w, h, rnd)
    land(d); return im

def cumulonimbus():
    im, d = new(); sky(d); rnd = random.Random(2)
    d.polygon([(22, 15), (34, 8), (60, 5), (92, 8), (92, 11), (66, 14), (46, 18)], fill=L2)   # anvil, sheared right
    d.polygon([(26, 13), (36, 8), (60, 6), (90, 8), (64, 10), (46, 13)], fill=WH)
    for k in range(9):                                            # the tower: stacked puffs
        yy = 44 - k * 3.6; ww = 15 - k * .6
        for j in range(4):
            px = 46 + rnd.uniform(-ww, ww); r = rnd.uniform(4, 6.5)
            d.ellipse((px - r + 1, yy - r + 1, px + r + 1, yy + r + 1), fill=L2); d.ellipse((px - r, yy - r, px + r - 1, yy + r - 1.5), fill=WH)
    d.rectangle((28, 44, 66, 47), fill=G1); d.rectangle((30, 47, 64, 48), fill=G3)
    for x in range(31, 63, 3):
        for y in range(49, 56, 2): d.point((x + (y // 2) % 2, y), fill=L2)    # rain shafts
    d.line([(58, 48), (55, 52), (58, 52), (54, 57)], fill=(248, 216, 120))     # lightning
    land(d); return im

def cirrus():
    im, d = new(); sky(d); rnd = random.Random(3)
    for sx, sy, ln in ((6, 12, 30), (34, 6, 34), (52, 20, 30), (10, 30, 24), (66, 34, 22)):
        for k in range(3):
            pts = [(sx + t + k, sy + k * 2 + 3 * math.sin(t / ln * 2.4) + (t / ln) ** 3 * 10) for t in range(0, ln - k * 4)]
            d.line(pts, fill=WH if k != 1 else L1)
    land(d); return im

def stratus():
    im, d = new(); sky(d, top=L2, mid=L2, bot=L1)
    for y in range(4, 46):
        for x in range(W):
            if (x * 7 + y * 13) % 11 == 0: d.point((x, y), fill=L1)
    d.rectangle((0, 40, W, 47), fill=L1)
    land(d, col=(0, 136, 0)); d.rectangle((0, 44, W, 52), fill=L1)
    for x in range(0, W, 2): d.point((x, 52), fill=L2)
    return im

def nimbostratus():
    im, d = new(); sky(d, top=G3, mid=G1, bot=G1)
    for y in range(2, 30):
        for x in range(W):
            if (x + y * 3) % 7 == 0: d.point((x, y), fill=G2)
    rnd = random.Random(5)
    for _ in range(170):
        x, y = rnd.randrange(W), rnd.randrange(26, 54); d.line((x, y, x - 1, y + 2), fill=L2)
    land(d, col=(0, 104, 0)); return im

def altocumulus():
    im, d = new(); sky(d); rnd = random.Random(6)
    for row in range(5):
        for col in range(9):
            cx = 6 + col * 11 + row * 3 + rnd.uniform(-1, 1); cy = 8 + row * 7 + rnd.uniform(-1, 1)
            r = 3.4 - row * .2
            d.ellipse((cx - r * 1.4, cy - r, cx + r * 1.4, cy + r), fill=L1)
            d.ellipse((cx - r * 1.2, cy - r, cx + r * 1.1, cy + r - 1.2), fill=WH)
    land(d); return im

def cirrocumulus():
    im, d = new(); sky(d); rnd = random.Random(7)
    for y in range(4, 36, 3):
        for x in range(4, 92, 3):
            if math.sin(x / 9 + y / 6) + rnd.uniform(-.4, .4) > -.3 and (y - 4) / 34 < 1 - abs(x - 48) / 60:
                d.rectangle((x + (y // 3) % 2, y, x + 1 + (y // 3) % 2, y + 1), fill=WH)
    land(d); return im

def mammatus():
    im, d = new(); sky(d, top=(248, 120, 88), mid=(252, 160, 68), bot=(252, 224, 168))
    d.rectangle((0, 0, W, 7), fill=G3)
    rows = [(12, range(0, W + 14, 14), 7), (22, range(7, W + 14, 28), 6), (31, (35, 63), 4)]
    for y, xs, r in rows:                                  # pouches hanging DOWN, lower rows drawn over upper
        for x in xs:
            d.ellipse((x - r, y - r, x + r, y + r), fill=G3)
            d.arc((x - r, y - r, x + r, y + r), 20, 160, fill=(248, 164, 192))          # sunset glow underneath
            d.arc((x - r + 1, y - r, x + r - 1, y + r - 1), 40, 140, fill=G1)
    d.rectangle((0, 0, W, 9), fill=G3)
    land(d, col=(0, 104, 0)); return im

def lenticular():
    im, d = new(); sky(d, top=(0, 88, 248), mid=(104, 136, 252), bot=(252, 160, 68))
    d.polygon([(10, 56), (48, 24), (86, 56)], fill=(80, 48, 0)); d.polygon([(48, 24), (40, 31), (44, 30), (48, 33), (52, 30), (56, 31)], fill=WH)
    for i, (y, w) in enumerate(((10, 30), (14, 34), (18, 28))):
        d.ellipse((48 - w, y - 2, 48 + w, y + 3), fill=L1 if i % 2 else WH)
        d.line((48 - w + 4, y + 3, 48 + w - 4, y + 3), fill=L2)
    land(d, hills=False); return im

ITEMS = dict(cumulus=cumulus, cumulonimbus=cumulonimbus, cirrus=cirrus, stratus=stratus, nimbostratus=nimbostratus,
             altocumulus=altocumulus, cirrocumulus=cirrocumulus, mammatus=mammatus, lenticular=lenticular)
if __name__ == '__main__':
    for k in sys.argv[1:] or ITEMS: save(finish(ITEMS[k]()), 'clouds', k)
