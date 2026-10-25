#!/usr/bin/env python3
"""Famous sports stadiums: 1-bit silhouettes (drawn supersampled, landmark style) with the sport's ball in the top corner."""
import sys, math
from PIL import Image, ImageDraw
from common import *

SS = 8
class Pic:
    """Draw in output-pixel coordinates (floats ok) on an 8x canvas; black ink, with white cut-outs."""
    def __init__(self):
        self.k = Image.new('L', (W * SS, H * SS), 0); self.kd = ImageDraw.Draw(self.k)
    def _p(self, pts): return [(x * SS, y * SS) for x, y in pts]
    def poly(self, pts, ink=255): self.kd.polygon(self._p(pts), fill=ink)
    def rect(self, x0, y0, x1, y1, ink=255): self.kd.rectangle((x0 * SS, y0 * SS, x1 * SS - 1, y1 * SS - 1), fill=ink)
    def ell(self, x0, y0, x1, y1, ink=255): self.kd.ellipse((x0 * SS, y0 * SS, x1 * SS, y1 * SS), fill=ink)
    def line(self, pts, w=1.0, ink=255): self.kd.line(self._p(pts), fill=ink, width=max(1, int(w * SS)), joint='curve')
    def arc_pts(self, cx, cy, rx, ry, a0, a1, n=40): return [(cx + rx * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + ry * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    def mask(self, thr=110): return self.k.resize((W, H), Image.BOX).point(lambda v: 255 if v > thr else 0).convert('1')

GY = 54
def scene(clouds_at=((4, 6), (40, 4))):
    im, d = canvas(); clouds(d, clouds_at)
    d.line((1, GY, W - 2, GY), fill=BLK); fill_pattern(im, (1, GY + 1, W - 1, H - 1), 6)
    return im, d

def finish(im, d, p, ball):
    im.paste(Image.new('1', im.size, BLK), (0, 0), p.mask())
    BALLS[ball](im, d)
    frame(d); return im

# ---------------- ball icons, top-right corner ----------------
BX, BY, BR = 87, 9, 6
def soccer(im, d):
    d.ellipse((BX - BR, BY - BR, BX + BR, BY + BR), fill=WHT, outline=BLK)
    pent = [(BX + 2.6 * math.cos(math.radians(-90 + 72 * i)), BY + 2.6 * math.sin(math.radians(-90 + 72 * i))) for i in range(5)]
    d.polygon(pent, fill=BLK)
    for x, y in pent: d.line((x, y, BX + (x - BX) * 2.2, BY + (y - BY) * 2.2), fill=BLK)
def football(im, d):
    d.ellipse((BX - 7, BY - 4, BX + 7, BY + 4), fill=BLK)
    d.line((BX - 3, BY, BX + 3, BY), fill=WHT)
    for x in (BX - 2, BX, BX + 2): d.line((x, BY - 1, x, BY + 1), fill=WHT)
    d.line((BX - 6, BY - 1, BX - 6, BY + 1), fill=WHT); d.line((BX + 6, BY - 1, BX + 6, BY + 1), fill=WHT)
def baseball(im, d):
    d.ellipse((BX - BR, BY - BR, BX + BR, BY + BR), fill=WHT, outline=BLK)
    d.arc((BX - BR - 5, BY - BR, BX - 1, BY + BR), -50, 50, fill=BLK); d.arc((BX + 1, BY - BR, BX + BR + 5, BY + BR), 130, 230, fill=BLK)
    for t in (-3, 0, 3):
        d.point((BX - 3, BY + t), fill=BLK); d.point((BX + 3, BY + t), fill=BLK)
def cricket(im, d):
    d.line((BX - 7, BY + 6, BX - 4, BY + 3), fill=BLK, width=1)                                       # handle
    d.polygon([(BX - 4, BY + 1), (BX - 2, BY + 3), (BX + 6, BY - 5), (BX + 4, BY - 7)], fill=BLK)      # blade
    d.ellipse((BX + 1, BY + 2, BX + 6, BY + 7), fill=BLK); d.point((BX + 3, BY + 4), fill=WHT); d.point((BX + 4, BY + 5), fill=WHT)
def basketball(im, d):
    d.ellipse((BX - BR, BY - BR, BX + BR, BY + BR), fill=BLK)
    d.line((BX - BR, BY, BX + BR, BY), fill=WHT); d.line((BX, BY - BR, BX, BY + BR), fill=WHT)
    d.arc((BX - BR - 3, BY - BR + 1, BX - 1, BY + BR - 1), -60, 60, fill=WHT); d.arc((BX + 1, BY - BR + 1, BX + BR + 3, BY + BR - 1), 120, 240, fill=WHT)
BALLS = {'soccer': soccer, 'football': football, 'baseball': baseball, 'cricket': cricket, 'basketball': basketball}

REG = {}
def reg(name, ball, sport):
    def f(fn): REG[name] = (fn, ball, sport); return fn
    return f

# ---------------- stadiums ----------------
@reg('wembley-stadium', 'soccer', 'Football (soccer)')
def wembley():
    im, d = scene(((4, 6), (30, 12))); p = Pic()
    p.poly([(6, GY), (6, 44), (14, 40), (82, 40), (90, 44), (90, GY)])                               # bowl
    p.rect(10, 41.5, 86, 42.5, 0)                                                                    # roof edge
    arch = [(8 + 80 * t, GY - 46 * 4 * t * (1 - t)) for t in [i / 60 for i in range(61)]]
    p.line(arch, 1.6)
    for t in (0.22, 0.34, 0.46, 0.58, 0.7, 0.8):                                                     # roof cables
        x = 8 + 80 * t; p.line([(x, GY - 46 * 4 * t * (1 - t)), (x - 3, 40.5)], 0.35)
    for x in range(12, 86, 4): p.rect(x, 46, x + 2, 48, 0)
    return finish(im, d, p, 'soccer')

@reg('allianz-arena', 'soccer', 'Football (soccer)')
def allianz():
    im, d = scene(((4, 6), (34, 4))); p = Pic()
    p.ell(8, 26, 88, GY + 6); p.rect(8, GY, 88, GY + 6, 0)
    for k in range(-12, 14):                                                                         # the inflated diamond panels
        x = 48 + k * 6.2
        p.line([(x - 14, GY + 1), (x + 14, 26)], 1.0, 0); p.line([(x + 14, GY + 1), (x - 14, 26)], 1.0, 0)
    m = Image.new('L', (W * SS, H * SS), 0); ImageDraw.Draw(m).ellipse((8 * SS, 26 * SS, 88 * SS, (GY + 6) * SS), fill=255)
    p.k = Image.composite(p.k, Image.new('L', p.k.size, 0), m)
    p.rect(30, 50, 66, GY, 255)
    return finish(im, d, p, 'soccer')

@reg('birds-nest-beijing', 'soccer', 'Olympic stadium (athletics and football)')
def birdsnest():
    im, d = scene(((4, 6), (36, 4))); p = Pic()
    top = [(6 + 84 * t, 30 + 7 * math.sin(math.pi * t) ** 2 * -1 + 7) for t in [i / 40 for i in range(41)]]   # saddle-shaped rim
    top = [(x, 26 + 9 * (1 - abs(2 * (x - 6) / 84 - 1)) ** 1.5) for x, _ in top]
    p.poly(top + [(90, GY), (6, GY)])
    import random; r = random.Random(4)
    for _ in range(30):                                                                              # the steel "twigs"
        x0 = r.uniform(4, 92); x1 = x0 + r.uniform(-30, 30)
        p.line([(x0, 25), (x1, GY + 1)], 1.0, 0)
    p.line(top, 1.2)
    m = Image.new('L', p.k.size, 0); ImageDraw.Draw(m).polygon([(x * SS, y * SS) for x, y in top + [(90, GY), (6, GY)]], fill=255)
    p.k = Image.composite(p.k, Image.new('L', p.k.size, 0), m)
    return finish(im, d, p, 'soccer')

@reg('san-siro', 'soccer', 'Football (soccer)')
def sansiro():
    im, d = scene(((4, 6), (34, 4))); p = Pic()
    p.rect(4, 32, 92, 36)                                                                            # stands
    p.rect(2, 22, 94, 26)                                                                            # roof girders
    for x in (8, 26, 44, 62, 80): p.rect(x, 26, x + 2, 32)
    for i in range(18): p.line([(4 + i * 5, 22), (7 + i * 5, 26)], 0.5, 0)
    for cx in (12, 36, 60, 84):                                                                      # spiral ramp towers
        p.rect(cx - 5, 26, cx + 5, GY, 0); p.rect(cx - 4.5, 27, cx + 4.5, GY)
        for y in range(28, int(GY), 4): p.line([(cx - 4.5, y + 2.5), (cx + 4.5, y)], 1.1, 0)
    shade(im, lambda dd: dd.rectangle((4, 36, 92, GY), fill=1), 3)
    return finish(im, d, p, 'soccer')

@reg('caesars-superdome', 'football', 'American football')
def superdome():
    im, d = scene(((4, 6), (36, 4))); p = Pic()
    p.rect(8, 40, 88, GY)                                                                            # cylindrical base
    p.poly(p.arc_pts(48, 40, 44, 16, 180, 360) + [(92, 40), (4, 40)])                               # low dome
    for r in (0.8, 0.55, 0.3): p.line(p.arc_pts(48, 40, 44 * r, 16 * r + 1, 195, 345), 1.0, 0)
    for x in range(10, 88, 4): p.line([(x, 43), (x, GY - 1)], 1.0, 0)
    p.rect(4, 39, 92, 41)
    return finish(im, d, p, 'football')

@reg('att-stadium', 'football', 'American football')
def att():
    im, d = scene(((4, 6), (36, 4))); p = Pic()
    p.poly(p.arc_pts(48, 50, 44, 18, 180, 360) + [(92, 50), (92, GY), (4, GY), (4, 50)])
    for dx in (-10, 10):                                                                             # the two huge arches
        p.line(p.arc_pts(48 + dx * 0.2, GY, 46, 30, 180, 360), 2.0)
    p.rect(28, 40, 68, GY, 0); p.rect(29, 41, 67, GY)                                                # glass end wall
    for x in range(32, 67, 4): p.line([(x, 42), (x, GY)], 1.0, 0)
    return finish(im, d, p, 'football')

@reg('rose-bowl', 'football', 'American football')
def rosebowl():
    im, d = scene(((4, 6), (36, 4)))
    shade(im, lambda dd: dd.polygon([(1, 40), (12, 26), (22, 32), (36, 18), (50, 30), (64, 22), (80, 32), (95, 26), (95, 46), (1, 46)], fill=1), 2)   # San Gabriel Mountains
    p = Pic()
    p.poly([(10, GY), (14, 40), (82, 40), (86, GY)])
    p.ell(12, 37, 84, 43)
    for x in range(16, 82, 4): p.rect(x, 46, x + 2, 50, 0)
    for x in (4, 92):                                                                                # palm trees
        p.line([(x, GY), (x + 1, 34)], 0.9)
        for a in (200, 230, 260, 290, 320, 340): p.line([(x + 1, 34), (x + 1 + 6 * math.cos(math.radians(a)), 34 + 4 * math.sin(math.radians(a)) + 3)], 0.8)
    return finish(im, d, p, 'football')

@reg('rogers-centre', 'baseball', 'Baseball')
def rogers():
    im, d = scene(((30, 6), (56, 14))); p = Pic()
    p.rect(30, 42, 92, GY)
    p.poly(p.arc_pts(61, 42, 31, 12, 180, 360) + [(92, 42), (30, 42)])                              # retractable dome
    for x in (45, 61, 77): p.line([(x, 41), (x, 31 + abs(x - 61) * 0.3)], 1.0, 0)
    for x in range(33, 92, 4): p.line([(x, 45), (x, GY - 1)], 1.0, 0)
    p.poly([(14, GY), (18, GY), (16.6, 20), (15.4, 20)])                                             # CN Tower
    p.ell(12.5, 17, 19.5, 22); p.rect(15.3, 4, 16.7, 18); p.rect(15.6, 1, 16.4, 4)
    return finish(im, d, p, 'baseball')

@reg('yankee-stadium', 'baseball', 'Baseball')
def yankee():
    im, d = scene(((4, 6), (40, 4))); p = Pic()
    p.rect(4, 26, 92, GY)
    for i in range(16):                                                                              # the famous frieze
        x = 6 + i * 5.4; p.poly([(x, 26.5), (x + 5.4, 26.5), (x + 5.4, 30)] + p.arc_pts(x + 2.7, 30, 2.7, 2.2, 0, -180, 10)[::-1], 0)
    p.rect(4, 22, 92, 26.5)
    for x in (8, 30, 66, 88): p.rect(x - 0.6, 10, x + 0.6, 22); p.rect(x - 2.5, 7, x + 2.5, 11)      # light towers
    for x in range(8, 90, 6): p.rect(x, 36, x + 3, 44, 0)                                            # facade arches
    return finish(im, d, p, 'baseball')

@reg('wrigley-field', 'baseball', 'Baseball')
def wrigley():
    im, d = scene(((4, 6), (40, 4))); p = Pic()
    p.rect(4, 36, 92, GY)                                                                            # brick grandstand
    for x in range(8, 92, 8): p.rect(x, 40, x + 4, 48, 0)
    p.rect(30, 14, 66, 28)                                                                           # the marquee sign
    p.rect(31.5, 15.5, 64.5, 21, 0)
    for i, x in enumerate(range(33, 64, 3)): p.rect(x, 16.5, x + 1.5, 19.5)                          # letters
    p.rect(33, 22.5, 63, 26, 0)
    for x in range(34, 63, 2): p.rect(x, 23.3, x + 1, 25.2)
    p.rect(46, 28, 50, 36)
    for x in (10, 86): p.rect(x - 0.6, 12, x + 0.6, 36); p.rect(x - 3, 9, x + 3, 13)
    return finish(im, d, p, 'baseball')

@reg('montreal-olympic-stadium', 'baseball', 'Olympic stadium (home of the Expos, baseball)')
def montreal():
    im, d = scene(((44, 6), (64, 18))); p = Pic()
    p.poly(p.arc_pts(58, 46, 34, 10, 180, 360) + [(92, 46), (92, GY), (24, GY), (24, 46)])
    for x in range(28, 90, 5): p.line([(x, 47), (x - 2, GY)], 1.0, 0)
    p.poly([(12, GY), (19, GY), (30, 8), (27, 6)])                                                   # the inclined tower
    p.rect(25, 4, 31, 8)
    for t in (0.3, 0.5, 0.7, 0.9): p.line([(28.5, 8), (34 + 50 * t, 46 - 10 * math.sin(math.pi * t))], 0.35)   # roof cables
    return finish(im, d, p, 'baseball')

@reg('lords-cricket-ground', 'cricket', 'Cricket')
def lords():
    im, d = scene(((4, 6), (40, 4))); p = Pic()
    p.rect(2, 42, 60, GY)                                                                            # Victorian pavilion
    for x in (6, 52): p.rect(x, 32, x + 6, 42); p.poly([(x - 0.5, 32), (x + 6.5, 32), (x + 3, 27)])
    p.rect(14, 38, 50, 42)
    for x in range(16, 50, 4): p.rect(x, 44, x + 2, 50, 0)
    p.ell(56, 22, 92, 38)                                                                            # the Media Centre "pod"
    p.rect(60, 30, 88, 32, 0); p.rect(60, 31, 88, 31.6)
    for x in (64, 84): p.line([(x, 36), (x - 2, GY)], 1.0)
    return finish(im, d, p, 'cricket')

@reg('melbourne-cricket-ground', 'cricket', 'Cricket')
def mcg():
    im, d = scene(((4, 6), (40, 4))); p = Pic()
    p.poly(p.arc_pts(48, 44, 46, 8, 180, 360) + [(94, 44), (94, GY), (2, GY), (2, 44)])
    for x in range(5, 94, 4): p.line([(x, 45), (x, GY)], 1.0, 0)
    for x, h in ((10, 12), (30, 8), (66, 8), (86, 12)):                                              # tall light towers
        p.poly([(x - 1.2, 40), (x + 1.2, 40), (x + 0.5, h), (x - 0.5, h)])
        p.poly([(x - 4, h - 1), (x + 4, h - 2), (x + 4, h + 3), (x - 4, h + 4)])
        for k in range(3): p.rect(x - 3 + k * 2.5, h, x - 2 + k * 2.5, h + 2, 0)
    return finish(im, d, p, 'cricket')

@reg('madison-square-garden', 'basketball', 'Basketball (and ice hockey)')
def msg():
    im, d = scene(((4, 6), (40, 4))); p = Pic()
    p.rect(14, 24, 82, GY)                                                                           # drum
    p.ell(14, 20, 82, 28)
    for x in range(16, 82, 4): p.rect(x, 28, x + 1.6, GY - 6, 0)                                     # vertical ribs
    p.rect(14, 46, 82, 48, 0)
    p.rect(2, 44, 14, GY); p.rect(82, 40, 94, GY)                                                    # Penn Station buildings
    for x in range(4, 13, 3): p.rect(x, 46, x + 1.5, 52, 0)
    for x in range(84, 93, 3): p.rect(x, 42, x + 1.5, 52, 0)
    return finish(im, d, p, 'basketball')

if __name__ == '__main__':
    for n in sys.argv[1:] or REG: save(REG[n][0](), 'stadiums', n); print(n)
