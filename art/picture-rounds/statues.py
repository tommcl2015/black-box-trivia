#!/usr/bin/env python3
"""Famous statues in the 1-bit landmark style: crisp silhouettes (drawn as vector outlines, supersampled) on patterned plinths."""
import sys, math
from PIL import Image, ImageDraw
from common import *

def vmask(items, sx, sy, ox, oy):
    """items: polys or ('h', poly) in unit coords (y up). Pixel = (ox + x*sx, oy - y*sy)."""
    SC = 8; big = Image.new('L', (W * SC, H * SC), 0); bd = ImageDraw.Draw(big)
    for it in items:
        hole = isinstance(it, tuple); p = it[1] if hole else it
        bd.polygon([((ox + x * sx) * SC, (oy - y * sy) * SC) for x, y in p], fill=0 if hole else 255)
    return big.resize((W, H), Image.BOX).point(lambda v: 255 if v > 100 else 0).convert('1')

def put(im, m, level=None):
    if level is None: im.paste(Image.new('1', im.size, BLK), (0, 0), m); return
    full = Image.new('1', im.size, WHT); fill_pattern(full, (0, 0, W, H), level); im.paste(full, (0, 0), m)

def ell(cx, cy, rx, ry, n=24, a0=0, a1=360): return [(cx + rx * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + ry * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
def R(x0, y0, x1, y1): return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
def seg(x0, y0, x1, y1, w):
    dx, dy = x1 - x0, y1 - y0; L = math.hypot(dx, dy) or 1; nx, ny = -dy / L * w / 2, dx / L * w / 2
    return [(x0 + nx, y0 + ny), (x1 + nx, y1 + ny), (x1 - nx, y1 - ny), (x0 - nx, y0 - ny)]

def gallery_wall(im, d):
    fill_pattern(im, (1, 1, W - 1, 50), 6); d.line((1, 50, W - 2, 50), fill=BLK); fill_pattern(im, (1, 51, W - 1, H - 1), 4)

def plinth(im, d, x0, x1, y0, y1=None, level=2):
    y1 = y1 or 58
    d.rectangle((x0, y0, x1, y1), fill=WHT, outline=BLK); fill_pattern(im, (x0 + 1, y0 + 1, x1, y1), level)
    d.rectangle((x0 - 2, y0 - 2, x1 + 2, y0), fill=WHT, outline=BLK)

REG = {}
def reg(n):
    def f(fn): REG[n] = fn; return fn
    return f

@reg('the-thinker')
def thinker():
    im, d = canvas(); gallery_wall(im, d)
    rock = [(-36, -4), (40, -4), (38, 14), (24, 26), (-14, 32), (-34, 26)]
    body = [(-26, 30), (-28, 40), (-27, 52), (-23, 62), (-16, 70), (-8, 74), (-2, 76), (0, 82), (4, 87), (10, 89), (15, 87), (18, 82), (20, 77),
            (21, 73), (24, 73), (25, 70), (22, 67), (21, 58), (22, 50), (27, 49), (31, 46), (30, 40), (28, 10), (36, 4), (37, 0), (20, 0), (20, 4),
            (20, 16), (18, 30), (4, 33), (-10, 32)]
    gaps = [('h', [(2, 66), (15, 66), (18, 56), (9, 46), (0, 50)]), ('h', [(22, 44), (26, 44), (25, 34), (23, 34)])]
    sx = 0.52; put(im, vmask([rock], sx, sx, 46, 52), 3); put(im, vmask([body] + gaps, sx, sx, 46, 52))
    plinth(im, d, 26, 68, 53, 61, 2)
    frame(d); return im

@reg('michelangelos-david')
def david():
    im, d = canvas(); gallery_wall(im, d)
    head = ell(1, 93, 6.0, 6.8)
    body = [(-3, 87), (-13, 83), (-15, 70), (-15, 55), (-16, 46), (-13, 44), (-11, 48), (-11, 58), (-9, 66), (-8, 57), (-10, 51), (-9, 30), (-8, 4), (-11, 0), (-2, 0),
            (-3, 26), (-2, 44), (0, 45), (3, 40), (6, 22), (9, 4), (8, 0), (17, 0), (15, 5), (13, 24), (11, 40), (10, 51), (8, 57), (10, 68), (12, 79), (17, 71), (19, 74), (14, 84), (10, 87), (3, 87)]
    gap = ('h', [(10, 76), (15, 72), (11, 70)])
    s = 0.48; put(im, vmask([head, body, gap], s, s, 48, 50))
    plinth(im, d, 36, 60, 51, 61, 2)
    frame(d); return im

@reg('venus-de-milo')
def venus():
    im, d = canvas(); gallery_wall(im, d)
    head = ell(2, 93, 5.5, 6.5); bun = ell(-4, 95, 3, 3)
    torso = [(-2, 87), (-11, 83), (-14, 77), (-12, 75), (-9, 78), (-8, 66), (-7, 58), (-11, 52), (11, 50), (8, 58), (9, 68), (11, 79), (14, 80), (13, 84), (6, 87), (4, 87)]
    drape = [(-11, 52), (11, 50), (14, 40), (14, 30), (16, 16), (17, 0), (-15, 0), (-13, 18), (-14, 34), (-12, 46)]
    folds = [('h', seg(-9, 46, 9, 38, 1.2)), ('h', seg(-10, 34, 3, 12, 1.2)), ('h', seg(4, 30, 10, 4, 1.2)), ('h', seg(-6, 24, -8, 4, 1.2))]
    s = 0.48; put(im, vmask([head, bun, torso, drape] + folds, s, s, 48, 50))
    plinth(im, d, 38, 58, 51, 61, 2)
    frame(d); return im

@reg('winged-victory-of-samothrace')
def nike():
    im, d = canvas(); gallery_wall(im, d)
    body = [(-6, 0), (14, 0), (12, 20), (14, 36), (16, 50), (14, 62), (9, 70), (3, 72), (-1, 68), (-4, 58), (-8, 44), (-9, 28), (-12, 14)]
    wing = [(2, 66), (-6, 72), (-18, 82), (-30, 94), (-36, 96), (-32, 86), (-38, 84), (-30, 74), (-36, 70), (-26, 62), (-30, 56), (-18, 52), (-6, 54)]
    folds = [('h', seg(-4, 40, 10, 6, 1.4)), ('h', seg(4, 48, 12, 18, 1.2)), ('h', seg(-26, 80, -12, 66, 1.2)), ('h', seg(-30, 70, -14, 60, 1.2))]
    prow = [(-26, -2), (30, -2), (38, -14), (-26, -14)]
    s = 0.47; put(im, vmask([body, wing] + folds, s, s, 50, 44)); put(im, vmask([prow], s, s, 50, 44), 3)
    plinth(im, d, 30, 70, 51, 61, 2)
    frame(d); return im

@reg('discobolus')
def discobolus():
    im, d = canvas(); gallery_wall(im, d)
    disc = ell(-30, 74, 6.5, 6.5)
    body = [(-25, 70), (-12, 62), (-2, 58), (6, 62), (12, 64), (16, 62), (14, 58), (10, 56), (8, 50), (12, 44), (14, 40), (12, 36), (6, 38), (2, 42),
            (-4, 38), (-2, 30), (6, 22), (10, 12), (12, 2), (4, 0), (-2, 0), (4, 6), (0, 18), (-10, 28), (-16, 22), (-24, 12), (-30, 2), (-36, 0), (-38, 4), (-30, 12),
            (-22, 26), (-12, 40), (-10, 52), (-16, 62), (-26, 66)]
    head = ell(16, 58, 4.6, 5)
    s = 0.62; put(im, vmask([disc, body, head], s, s, 52, 50))
    plinth(im, d, 24, 66, 51, 61, 2)
    frame(d); return im

@reg('terracotta-army')
def terracotta():
    im, d = canvas()
    fill_pattern(im, (1, 1, W - 1, H - 1), 1)
    def warrior(cx, base, sc):
        p = [ell(0, 92, 5, 6), R(-2, 96, 2, 101),
             [(-4, 86), (-12, 82), (-13, 62), (-10, 56), (-11, 44), (-9, 40), (-8, 4), (-11, 0), (-1, 0), (0, 30), (1, 0), (11, 0), (8, 4), (9, 40), (11, 44), (10, 56), (13, 62), (12, 82), (4, 86)],
             ('h', R(-8, 60, 8, 61.5)), ('h', R(-8, 52, 8, 53.5)), ('h', R(-9, 44, 9, 45.5))]
        put(im, vmask(p, sc, sc, cx, base))
    for row, (base, sc, n) in enumerate([(30, 0.22, 7), (42, 0.3, 5), (61, 0.42, 4)]):
        for i in range(n):
            warrior((i + 0.5) * W / n + (row % 2) * 3, base, sc)
        d.line((1, base, W - 2, base), fill=BLK)
    frame(d); return im

@reg('great-buddha-of-kamakura')
def kamakura():
    im, d = canvas(); clouds(d, [(4, 6), (74, 10)])
    for x in (6, 84):
        d.ellipse((x - 7, 26, x + 7, 44), fill=BLK); d.line((x, 44, x, 55), fill=BLK, width=2)
    body = [(-40, 0), (40, 0), (38, 10), (30, 22), (28, 44), (22, 56), (12, 60), (8, 62), (-8, 62), (-12, 60), (-22, 56), (-28, 44), (-30, 22), (-38, 10)]
    head = ell(0, 74, 11, 13); top = ell(0, 87, 7, 4); ears = [R(-13, 64, -9, 76), R(9, 64, 13, 76)]
    lap = ('h', ell(0, 22, 14, 4)); hands = ('h', ell(0, 26, 6, 3))
    robe = [('h', seg(-26, 40, -10, 8, 1.6)), ('h', seg(26, 40, 10, 8, 1.6)), ('h', seg(-4, 60, -14, 30, 1.2)), ('h', seg(4, 60, 14, 30, 1.2))]
    s = 0.5; put(im, vmask([body, head, top] + ears + [lap, hands] + robe, s, s, 48, 54))
    face = [('h', R(-6, 74, -2, 75.5)), ('h', R(2, 74, 6, 75.5)), ('h', R(-1, 68, 1, 70))]
    put(im, vmask([R(-1, 1, 1, 2)], s, s, 48, 54))
    m = vmask([R(-7, 73.5, -1.5, 75.5), R(1.5, 73.5, 7, 75.5)], s, s, 48, 54); im.paste(Image.new('1', im.size, WHT), (0, 0), m)
    plinth(im, d, 20, 76, 55, 61, 3)
    frame(d); return im

@reg('lincoln-memorial-statue')
def lincoln():
    im, d = canvas()
    fill_pattern(im, (1, 1, W - 1, H - 1), 6)
    for x in (6, 18, 76, 88):
        d.rectangle((x - 3, 4, x + 3, 56), fill=WHT, outline=BLK); d.line((x - 1, 6, x - 1, 54), fill=BLK); d.line((x + 1, 6, x + 1, 54), fill=BLK)
    d.rectangle((1, 1, W - 2, 4), fill=BLK)
    chair = [(-26, 0), (26, 0), (26, 56), (20, 60), (20, 36), (-20, 36), (-20, 60), (-26, 56)]
    man = [ell(0, 80, 6.5, 8), [(-4, 72), (-16, 68), (-18, 52), (-20, 40), (-14, 38), (-12, 50), (-12, 36), (-14, 34), (-12, 4), (-15, 0), (-4, 0), (-3, 30), (3, 30),
           (4, 0), (15, 0), (12, 4), (14, 34), (12, 36), (12, 50), (14, 38), (20, 40), (18, 52), (16, 68), (4, 72)], ell(0, 74, 5, 4)]
    s = 0.55; put(im, vmask([chair], s, s, 47, 52), 3); put(im, vmask(man, s, s, 47, 52))
    plinth(im, d, 28, 66, 53, 61, 2)
    frame(d); return im

@reg('bust-of-nefertiti')
def nefertiti():
    im, d = canvas(); gallery_wall(im, d)
    p = [[(-20, 0), (20, 0), (17, 10), (12, 20), (10, 30), (8, 40), (12, 47), (13, 51), (15, 54), (19, 58), (16, 61), (15, 64), (13, 66),
          (8, 96), (-26, 92), (-24, 84), (-17, 64), (-10, 54), (-7, 40), (-10, 26), (-16, 14)],
         ('h', seg(13, 70, -21, 70, 1.6)), ('h', ell(11, 61, 2.0, 1.0))]
    s = 0.5; put(im, vmask(p, s, s, 50, 50))
    plinth(im, d, 36, 64, 51, 61, 2)
    frame(d); return im

@reg('tutankhamun-mask')
def tut():
    im, d = canvas(); fill_pattern(im, (1, 1, W - 1, H - 1), 6)
    nemes = [(-34, 0), (34, 0), (30, 20), (22, 36), (24, 64), (18, 82), (8, 90), (-8, 90), (-18, 82), (-24, 64), (-22, 36), (-30, 20)]
    face = [(-12, 40), (12, 40), (14, 58), (12, 74), (6, 80), (-6, 80), (-12, 74), (-14, 58)]
    beard = R(-3, 24, 3, 40)
    collar = [(-34, 0), (34, 0), (30, 20), (14, 30), (-14, 30), (-30, 20)]
    s = 0.62; ox, oy = 48, 60
    put(im, vmask([nemes], s, s, ox, oy), 4)                      # striped headcloth
    put(im, vmask([collar], s, s, ox, oy), 7)
    for poly in (face, beard): im.paste(Image.new('1', im.size, WHT), (0, 0), vmask([poly], s, s, ox, oy))
    put(im, vmask([beard], s, s, ox, oy), 4)
    put(im, vmask([ell(-6, 64, 3, 1.4), ell(6, 64, 3, 1.4), R(-1, 52, 1, 60), R(-4, 48, 4, 49.5), R(-8, 67, -3, 68.2), R(3, 67, 8, 68.2)], s, s, ox, oy))
    put(im, vmask([ell(0, 87, 3, 3), R(-1.5, 84, 1.5, 90)], s, s, ox, oy))     # cobra and vulture on the brow
    m = vmask([nemes], s, s, ox, oy); edge = Image.new('1', im.size, 0)
    from PIL import ImageChops, ImageFilter
    ol = ImageChops.subtract(m.convert('L'), m.convert('L').filter(ImageFilter.MinFilter(3))).point(lambda v: 255 if v else 0).convert('1')
    put(im, ol)
    frame(d); return im

@reg('abu-simbel')
def abu_simbel():
    im, d = canvas()
    shade(im, lambda dd: dd.polygon([(0, 60), (0, 10), (12, 4), (48, 2), (84, 4), (96, 10), (96, 60)], fill=1), 2)
    d.rectangle((4, 6, 92, 56), fill=WHT, outline=BLK); fill_pattern(im, (5, 7, 92, 56), 6)
    d.rectangle((44, 38, 52, 56), fill=BLK); d.rectangle((41, 8, 55, 10), fill=BLK)
    def colossus(cx, broken=False):
        crown = [(-5, 86), (5, 86), (4, 96), (2, 100), (-2, 100), (-4, 96)]
        head = [(-9, 86), (9, 86), (10, 72), (12, 60), (6, 62), (-6, 62), (-12, 60), (-10, 72)]
        torso = [(-13, 62), (13, 62), (12, 44), (16, 40), (16, 34), (-16, 34), (-16, 40), (-12, 44)]
        legs = [(-14, 34), (-3, 34), (-3, 0), (-14, 0)], [(3, 34), (14, 34), (14, 0), (3, 0)]
        throne = R(-19, 0, 19, 50)
        fig = ([] if broken else [crown, head]) + [torso if not broken else [(-13, 50), (6, 58), (13, 46), (16, 40), (16, 34), (-16, 34), (-16, 40)]] + list(legs)
        put(im, vmask([throne], 0.48, 0.48, cx, 56), 3)
        put(im, vmask(fig + [('h', ell(-5, 76, 2, 1)), ('h', ell(5, 76, 2, 1))], 0.48, 0.48, cx, 56))
        if broken: put(im, vmask([ell(0, 6, 9, 6), [(-4, 10), (4, 10), (2, 16), (-2, 16)]], 0.48, 0.48, cx + 4, 56))
    for cx, b in ((14, False), (31, True), (65, False), (82, False)): colossus(cx, b)
    d.line((1, 56, W - 2, 56), fill=BLK); fill_pattern(im, (1, 57, W - 1, H - 1), 1)
    frame(d); return im

@reg('manneken-pis')
def manneken():
    im, d = canvas()
    fill_pattern(im, (1, 1, W - 1, H - 1), 6)
    d.rectangle((26, 4, 70, 60), fill=WHT, outline=BLK); fill_pattern(im, (27, 5, 70, 60), 2)
    d.rectangle((34, 10, 62, 44), fill=WHT, outline=BLK)
    d.pieslice((34, 4, 62, 18), 180, 360, fill=WHT, outline=BLK)
    boy = [ell(0, 70, 6, 6.5), [(-3, 64), (-8, 60), (-9, 48), (-12, 42), (-9, 40), (-7, 44), (-6, 36), (-6, 20), (-7, 0), (-1, 0), (0, 18), (1, 0), (7, 0), (6, 20),
           (7, 34), (9, 38), (12, 46), (9, 48), (7, 44), (8, 58), (3, 64)]]
    put(im, vmask(boy, 0.42, 0.42, 48, 40))
    for i in range(7):
        t = i / 6; x = 51 + t * 7; y = 32 + 7 * t * t
        d.point((int(x), int(y)), fill=BLK)
    d.rectangle((38, 40, 58, 44), fill=BLK)
    d.ellipse((36, 46, 60, 54), fill=WHT, outline=BLK); fill_pattern(im, (38, 48, 58, 53), 4)
    d.line((26, 60, 70, 60), fill=BLK)
    frame(d); return im

@reg('nelsons-column')
def nelson():
    im, d = canvas(); clouds(d, [(6, 8), (66, 14)])
    d.rectangle((44, 14, 52, 46), fill=WHT, outline=BLK)
    for x in (46, 48, 50): d.line((x, 16, x, 45), fill=BLK)
    d.rectangle((42, 11, 54, 14), fill=BLK); d.rectangle((43, 9, 53, 11), fill=WHT, outline=BLK)
    put(im, vmask([ell(0, 20, 2.6, 3), [(-3, 17), (3, 17), (4, 0), (-4, 0)], [(-2, 22), (3, 23), (2, 21)]], 0.42, 0.42, 48, 9))
    d.rectangle((40, 46, 56, 56), fill=WHT, outline=BLK); fill_pattern(im, (41, 47, 56, 56), 2)
    for x in (22, 74):
        lion = [[(-10, 0), (10, 0), (12, 4), (8, 8), (4, 8), (-6, 7), (-10, 4)], ell(8, 9, 4, 4)]
        put(im, vmask(lion, 0.5, 0.5, x, 56))
        d.rectangle((x - 7, 56, x + 7, 58), fill=BLK)
    d.line((1, 58, W - 2, 58), fill=BLK); fill_pattern(im, (1, 59, W - 1, H - 1), 1)
    frame(d); return im

if __name__ == '__main__':
    for n in sys.argv[1:] or REG: save(REG[n](), 'statues', n); print(n)
