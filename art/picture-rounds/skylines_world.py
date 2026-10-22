#!/usr/bin/env python3
"""World city skylines — 1-bit pixel art."""
import math, random
from PIL import Image, ImageDraw
from common import *

CAT = 'skylines'
REG = {}
def reg(name):
    def deco(fn): REG[name] = fn; return fn
    return deco

def back(im, d, y=56, seed=1, hmin=4, hmax=14, level=2):
    """Distant buildings in grey."""
    m = Image.new('1', im.size, 0); md = ImageDraw.Draw(m)
    r = random.Random(seed); x = 1
    while x < im.width - 2:
        w = r.randint(3, 8); h = r.randint(hmin, hmax)
        md.rectangle((x, y - h, x + w, y), fill=1); x += w + r.randint(0, 2)
    shade(im, lambda dd: dd.bitmap((0, 0), m, fill=1), level)

def front(im, d, y=56, seed=2, hmin=4, hmax=10, x0=1, x1=None):
    city_fill(im, d, y, seed=seed, hmin=hmin, hmax=hmax, x0=x0, x1=x1)

def needle(d, cx, top, base, pods, shaft=1):
    d.polygon([(cx - shaft - 1, base), (cx - shaft, top), (cx + shaft, top), (cx + shaft + 1, base)], fill=BLK)
    for (y, r, h) in pods: d.ellipse((cx - r, y - h, cx + r, y + h), fill=BLK)

def setback(d, cx, base, tiers, fill=BLK):
    """tiers: list of (half_width, height) from the ground up."""
    y = base
    for hw, h in tiers:
        d.rectangle((cx - hw, y - h, cx + hw, y), fill=fill); y -= h
    return y

def lit(im, box, seed=3, density=0.4):
    windows(im, box, random.Random(seed), density)

# ------------------------------------------------------------------ North America
@reg('new-york')
def new_york():
    im, d = canvas(); water(im, 58)
    back(im, d, 56, seed=5, hmax=18)
    # One World Trade Center
    d.polygon([(14, 56), (16, 12), (24, 12), (26, 56)], fill=BLK); d.line((20, 2, 20, 12), fill=BLK)
    d.line((16, 14, 25, 54), fill=WHT); d.line((24, 14, 15, 54), fill=WHT)
    # Empire State Building
    top = setback(d, 50, 56, [(9, 24), (7, 6), (5, 6), (3, 4), (2, 3)])
    d.line((50, top - 8, 50, top), fill=BLK)
    lit(im, (43, 28, 58, 55), 4)
    # Chrysler Building
    setback(d, 72, 56, [(6, 26), (4, 4)])
    for i, r in enumerate((4, 3, 2)):
        d.chord((72 - r, 22 - i * 4 - r, 72 + r, 22 - i * 4 + r), 180, 360, fill=BLK)
        d.point((72, 22 - i * 4 - 1), fill=WHT)
    d.line((72, 8, 72, 13), fill=BLK)
    lit(im, (67, 30, 77, 55), 6)
    front(im, d, 56, 7, 3, 9)
    frame(d); return im

@reg('chicago')
def chicago():
    im, d = canvas(); water(im, 58)
    back(im, d, 56, seed=9, hmax=16)
    # Willis Tower: bundled tubes of different heights, two antennas
    for (x0, x1, top) in ((22, 26, 20), (26, 30, 10), (30, 34, 10), (34, 38, 28)):
        d.rectangle((x0, top, x1, 56), fill=BLK)
    d.line((27, 0, 27, 10), fill=BLK); d.line((31, 2, 31, 10), fill=BLK)
    for y in range(14, 56, 3):
        for x in range(23, 38, 2):
            if random.Random(x * y).random() < 0.3: d.point((x, y), fill=WHT)
    # John Hancock Center: tapering with X-bracing
    d.polygon([(62, 56), (64, 14), (72, 14), (74, 56)], fill=BLK)
    for y0 in (14, 28, 42):
        d.line((64, y0, 73, y0 + 14), fill=WHT); d.line((72, y0, 63, y0 + 14), fill=WHT)
    d.line((66, 4, 66, 14), fill=BLK); d.line((70, 4, 70, 14), fill=BLK)
    # Trump tower-ish stepped glass
    setback(d, 86, 56, [(5, 18), (3, 8), (2, 6)]); d.line((86, 12, 86, 24), fill=BLK)
    front(im, d, 56, 3, 3, 8)
    frame(d); return im

@reg('toronto')
def toronto():
    im, d = canvas(); water(im, 58)
    back(im, d, 56, seed=12, hmax=16)
    cx = 40
    d.polygon([(cx - 3, 56), (cx - 1, 6), (cx + 1, 6), (cx + 3, 56)], fill=BLK)
    d.ellipse((cx - 7, 18, cx + 7, 25), fill=BLK); d.rectangle((cx - 6, 21, cx + 6, 22), fill=WHT)
    d.ellipse((cx - 3, 13, cx + 3, 17), fill=BLK); d.line((cx, 0, cx, 6), fill=BLK)
    d.chord((54, 42, 74, 58), 180, 360, fill=BLK)
    front(im, d, 56, 4, 6, 16, x0=60)
    front(im, d, 56, 8, 4, 12, x0=1, x1=30)
    frame(d); return im

@reg('seattle')
def seattle():
    im, d = canvas()
    d.polygon([(46, 34), (70, 12), (96, 34)], fill=WHT, outline=BLK)
    d.polygon([(64, 18), (70, 12), (77, 18), (73, 20), (70, 17), (67, 20)], fill=BLK)
    back(im, d, 56, seed=9, hmax=14); water(im, 58)
    cx = 26
    d.line((cx - 4, 56, cx - 1, 20), fill=BLK); d.line((cx + 4, 56, cx + 1, 20), fill=BLK); d.line((cx - 3, 40, cx + 3, 40), fill=BLK)
    d.polygon([(cx - 9, 16), (cx + 9, 16), (cx + 5, 21), (cx - 5, 21)], fill=BLK)
    d.polygon([(cx - 3, 16), (cx, 9), (cx + 3, 16)], fill=BLK); d.line((cx, 4, cx, 9), fill=BLK)
    front(im, d, 56, 9, 6, 18, x0=40)
    frame(d); return im

@reg('san-francisco')
def san_francisco():
    im, d = canvas(); water(im, 56)
    back(im, d, 54, seed=17, hmax=12)
    # Transamerica Pyramid
    d.polygon([(30, 54), (36, 4), (42, 54)], fill=BLK)
    d.polygon([(26, 54), (30, 30), (31, 54)], fill=BLK); d.polygon([(46, 54), (42, 30), (41, 54)], fill=BLK)
    # Salesforce Tower (rounded top)
    d.rectangle((56, 14, 66, 54), fill=BLK); d.chord((56, 8, 66, 20), 180, 360, fill=BLK)
    for y in range(18, 54, 3): d.line((57, y, 65, y), fill=WHT)
    front(im, d, 54, 5, 3, 10)
    # Bay Bridge suspension spans
    for tx in (76, 90): d.line((tx, 30, tx, 56), fill=BLK, width=2)
    d.line((66, 48, 96, 48), fill=BLK)
    pts = [(76 + i, 31 + 8 * math.sin(math.pi * i / 14)) for i in range(15)]; d.line(pts, fill=BLK)
    d.line((66, 44, 76, 31), fill=BLK)
    frame(d); return im

@reg('las-vegas')
def las_vegas():
    im, d = canvas(); fill_pattern(im, (1, 58, W - 1, H - 1), 1)
    for x, y in ((8, 6), (30, 10), (60, 4), (88, 12)): d.point((x, y), fill=BLK)
    # Stratosphere / The STRAT
    needle(d, 12, 6, 58, [(12, 5, 3)], 1); d.line((12, 0, 12, 6), fill=BLK)
    d.line((6, 58, 11, 30), fill=BLK); d.line((18, 58, 13, 30), fill=BLK)
    # Paris Las Vegas Eiffel replica
    d.polygon([(30, 58), (36, 18), (38, 18), (44, 58)], fill=BLK); d.chord((32, 50, 42, 62), 180, 360, fill=WHT)
    d.rectangle((33, 40, 41, 41), fill=BLK)
    # Luxor pyramid with sky beam
    d.polygon([(52, 58), (66, 34), (80, 58)], fill=BLK); shade(im, lambda dd: dd.polygon([(66, 34), (80, 58), (68, 58)], fill=1), 2)
    d.line((66, 0, 66, 34), fill=BLK)
    # palm + sign
    d.line((88, 58, 90, 40), fill=BLK)
    for a in (-150, -120, -60, -30): r = math.radians(a); d.line((90, 40, 90 + 6 * math.cos(r), 40 - 4 * math.sin(r) + 3), fill=BLK)
    d.polygon([(46, 50), (50, 46), (54, 50), (50, 54)], outline=BLK); d.point((50, 50), fill=BLK)
    frame(d); return im

@reg('vancouver')
def vancouver():
    im, d = canvas()
    d.polygon([(0, 36), (14, 18), (24, 26), (40, 12), (56, 24), (70, 14), (96, 30), (96, 50), (0, 50)], fill=WHT, outline=BLK)
    for x, y in ((14, 18), (40, 12), (70, 14)): d.polygon([(x - 4, y + 4), (x, y), (x + 4, y + 4)], fill=BLK)
    back(im, d, 52, seed=31, hmax=18); water(im, 54)
    # Harbour Centre with its "flying saucer"
    d.rectangle((24, 20, 28, 52), fill=BLK); d.ellipse((20, 16, 32, 22), fill=BLK); d.line((26, 10, 26, 16), fill=BLK)
    front(im, d, 52, 31, 6, 16, x0=34, x1=60)
    # Canada Place sails
    d.rectangle((62, 48, 92, 52), fill=BLK)
    for x in range(64, 92, 6): d.polygon([(x, 48), (x + 3, 38), (x + 6, 48)], fill=WHT, outline=BLK)
    frame(d); return im

# ------------------------------------------------------------------ Europe
@reg('london')
def london():
    im, d = canvas(); water(im, 58)
    back(im, d, 56, seed=12, hmax=14)
    d.ellipse((58, 14, 88, 44), outline=BLK, fill=WHT)
    for a in range(0, 360, 30):
        r = math.radians(a); x, y = 73 + 15 * math.cos(r), 29 + 15 * math.sin(r)
        d.line((73, 29, x, y), fill=BLK); d.rectangle((x - 1, y - 1, x + 1, y + 1), fill=BLK)
    d.line((73, 29, 66, 56), fill=BLK); d.line((73, 29, 80, 56), fill=BLK)
    d.polygon([(30, 56), (36, 4), (44, 56)], fill=BLK); d.line((37, 10, 40, 50), fill=WHT)        # Shard
    d.ellipse((46, 26, 54, 56), fill=BLK)                                                           # Gherkin
    for y in range(30, 56, 4): d.line((47, y, 53, y - 2), fill=WHT)
    d.rectangle((12, 20, 18, 56), fill=BLK); d.polygon([(12, 20), (15, 12), (18, 20)], fill=BLK); d.ellipse((13, 22, 17, 26), fill=WHT)
    frame(d); return im

@reg('paris')
def paris():
    im, d = canvas(); ground(im, d, 58)
    # Haussmann blocks with mansard roofs
    for x in range(1, 95, 12):
        d.rectangle((x, 46, x + 11, 58), fill=WHT, outline=BLK)
        d.polygon([(x, 46), (x + 2, 42), (x + 9, 42), (x + 11, 46)], fill=BLK)
        for wx in range(x + 2, x + 10, 3): d.rectangle((wx, 49, wx + 1, 51), fill=BLK); d.rectangle((wx, 54, wx + 1, 56), fill=BLK)
    # Eiffel Tower
    cx = 26; L, R = [], []
    for i in range(31):
        t = i / 30; y = 42 - t * 40; half = 1 + 14 * (1 - t) ** 2.4
        L.append((cx - half, y)); R.append((cx + half, y))
    d.polygon(L + R[::-1], fill=BLK); d.chord((cx - 7, 36, cx + 7, 48), 180, 360, fill=WHT)
    # Sacré-Cœur on its hill
    d.polygon([(54, 42), (60, 30), (90, 30), (94, 42)], fill=WHT, outline=BLK)
    for x, r in ((66, 4), (84, 4)): d.chord((x - r, 24, x + r, 32), 180, 360, fill=WHT, outline=BLK); d.line((x, 20, x, 24), fill=BLK)
    d.rectangle((70, 22, 80, 30), fill=WHT, outline=BLK); d.chord((68, 10, 82, 30), 180, 360, fill=WHT, outline=BLK); d.line((75, 5, 75, 10), fill=BLK)
    frame(d); return im

@reg('rome')
def rome():
    im, d = canvas(); ground(im, d, 58)
    clouds(d, [(70, 4)])
    # St Peter's dome
    d.rectangle((20, 34, 52, 50), fill=WHT, outline=BLK)
    for x in range(22, 50, 4): d.line((x, 37, x, 50), fill=BLK)
    d.rectangle((28, 24, 44, 34), fill=WHT, outline=BLK); d.chord((26, 6, 46, 42), 180, 360, fill=WHT, outline=BLK); d.rectangle((34, 2, 38, 6), fill=BLK)
    # Colosseum fragment
    d.rectangle((60, 36, 92, 50), fill=WHT, outline=BLK)
    for y in (39, 45):
        for x in range(62, 90, 4): d.rectangle((x, y, x + 1, y + 4), fill=BLK)
    # umbrella pines
    for x in (8, 56):
        d.line((x, 58, x, 44), fill=BLK); d.ellipse((x - 8, 38, x + 8, 46), fill=BLK)
    d.rectangle((1, 50, W - 2, 58), fill=WHT); d.line((1, 50, W - 2, 50), fill=BLK)
    for x in range(1, 95, 8): d.rectangle((x, 51, x + 6, 57), outline=BLK)
    frame(d); return im

@reg('venice')
def venice():
    im, d = canvas(); water(im, 46)
    d.rectangle((1, 30, W - 2, 46), fill=WHT); d.line((1, 46, W - 2, 46), fill=BLK)
    for x in range(1, 95, 4): d.chord((x, 38, x + 3, 44), 180, 360, fill=BLK); d.rectangle((x, 41, x + 3, 46), fill=BLK)
    # St Mark's Campanile
    d.rectangle((20, 8, 26, 46), fill=BLK); d.rectangle((19, 12, 27, 16), fill=WHT, outline=BLK)
    d.polygon([(19, 8), (23, 0), (27, 8)], fill=BLK)
    # St Mark's Basilica domes
    for x in (40, 52, 64): d.chord((x - 5, 22, x + 5, 34), 180, 360, fill=WHT, outline=BLK); d.line((x, 18, x, 22), fill=BLK)
    d.rectangle((34, 28, 70, 36), fill=WHT, outline=BLK)
    # gondola with gondolier
    d.polygon([(30, 56), (62, 56), (66, 52), (60, 58), (32, 58), (26, 52)], fill=BLK)
    d.line((58, 56, 58, 48), fill=BLK); d.point((58, 47), fill=BLK); d.line((56, 50, 66, 60), fill=BLK)
    frame(d); return im

@reg('berlin')
def berlin():
    im, d = canvas(); ground(im, d, 58)
    back(im, d, 56, seed=44, hmax=10)
    # Fernsehturm
    cx = 30
    d.polygon([(cx - 3, 56), (cx - 1, 20), (cx + 1, 20), (cx + 3, 56)], fill=BLK)
    d.ellipse((cx - 7, 12, cx + 7, 26), fill=BLK); d.rectangle((cx - 7, 18, cx + 7, 19), fill=WHT)
    d.line((cx, 0, cx, 12), fill=BLK, width=2)
    # Brandenburg Gate
    d.rectangle((48, 40, 78, 43), fill=BLK)
    for x in range(50, 78, 5): d.rectangle((x, 43, x + 1, 56), fill=BLK)
    d.rectangle((58, 34, 68, 40), fill=BLK)
    # Reichstag glass dome
    d.rectangle((82, 44, 95, 56), fill=WHT, outline=BLK); d.chord((84, 36, 94, 50), 180, 360, fill=WHT, outline=BLK)
    for x in (86, 89, 92): d.line((x, 38, x, 44), fill=BLK)
    front(im, d, 56, 22, 3, 8, x0=1, x1=20)
    frame(d); return im

@reg('barcelona')
def barcelona():
    im, d = canvas(); water(im, 58)
    back(im, d, 56, seed=51, hmax=10)
    # Sagrada Família spires
    for x, top in ((18, 18), (24, 12), (30, 10), (36, 14)):
        d.polygon([(x - 3, 56), (x - 1, top), (x + 1, top), (x + 3, 56)], fill=BLK); d.point((x, top - 2), fill=BLK)
    d.polygon([(25, 56), (27, 4), (29, 4), (31, 56)], fill=BLK)
    # Torre Glòries (bullet)
    d.rectangle((60, 20, 70, 56), fill=BLK); d.chord((60, 10, 70, 30), 180, 360, fill=BLK)
    for y in range(18, 56, 3):
        for x in range(61, 70, 2):
            if (x * 7 + y) % 5 == 0: d.point((x, y), fill=WHT)
    # Hotel W sail
    d.polygon([(84, 56), (86, 26), (92, 40), (92, 56)], fill=BLK)
    frame(d); return im

@reg('moscow')
def moscow():
    im, d = canvas(); ground(im, d, 58)
    # Moscow City glass towers
    for x, top in ((60, 6), (68, 12), (76, 4), (84, 16)):
        d.polygon([(x - 3, 56), (x - 3, top + 4), (x, top), (x + 3, top + 4), (x + 3, 56)], fill=BLK)
        for y in range(top + 6, 56, 3): d.point((x, y), fill=WHT)
    # Stalinist "Seven Sisters" tower
    cx = 34
    setback(d, cx, 56, [(10, 14), (6, 8), (4, 8), (2, 6)]); d.polygon([(cx - 2, 20), (cx, 6), (cx + 2, 20)], fill=BLK); d.point((cx, 4), fill=BLK)
    for x in (cx - 8, cx + 8): d.polygon([(x - 2, 42), (x, 34), (x + 2, 42)], fill=BLK)
    lit(im, (25, 42, 44, 55), 2)
    # St Basil's domes
    for x, r in ((8, 4), (16, 5)):
        d.rectangle((x - 3, 48, x + 3, 56), fill=BLK); onion(d, x, 48, r, fill=WHT, outline=BLK)
    frame(d); return im

@reg('istanbul')
def istanbul():
    im, d = canvas(); water(im, 52)
    # Blue Mosque: cascading domes + six minarets
    d.rectangle((14, 38, 62, 52), fill=WHT, outline=BLK)
    for x, r in ((22, 5), (54, 5), (30, 6), (46, 6)): d.chord((x - r, 38 - r, x + r, 38 + r), 180, 360, fill=WHT, outline=BLK)
    d.chord((28, 18, 48, 42), 180, 360, fill=WHT, outline=BLK); d.line((38, 14, 38, 18), fill=BLK)
    for x in (8, 12, 18, 58, 64, 68):
        d.line((x, 52, x, 16), fill=BLK, width=2); d.polygon([(x - 1, 16), (x, 10), (x + 1, 16)], fill=BLK)
        d.line((x - 1, 28, x + 1, 28), fill=BLK)
    # Galata tower across the water
    d.rectangle((80, 30, 88, 50), fill=BLK); d.polygon([(79, 30), (84, 20), (89, 30)], fill=BLK)
    for x in (81, 84, 87): d.point((x, 33), fill=WHT)
    frame(d); return im

@reg('cairo')
def cairo():
    im, d = canvas(); water(im, 56)
    sun(im, d, 82, 10, 4)
    for x, h in ((8, 10), (22, 14), (34, 8)): d.polygon([(x - h, 46), (x, 46 - h), (x + h, 46)], fill=WHT, outline=BLK)   # pyramids on horizon
    back(im, d, 54, seed=63, hmin=3, hmax=8)
    # Cairo Tower (lotus lattice)
    cx = 60
    d.polygon([(cx - 3, 54), (cx - 2, 14), (cx + 2, 14), (cx + 3, 54)], fill=BLK)
    for y in range(18, 54, 3): d.line((cx - 2, y, cx + 2, y - 2), fill=WHT)
    d.polygon([(cx - 6, 14), (cx - 3, 8), (cx + 3, 8), (cx + 6, 14)], fill=BLK); d.line((cx, 2, cx, 8), fill=BLK)
    # felucca
    d.polygon([(70, 58), (86, 58), (84, 61), (72, 61)], fill=BLK); d.line((76, 58, 82, 40), fill=BLK); d.polygon([(82, 40), (76, 57), (86, 57)], fill=WHT, outline=BLK)
    frame(d); return im

@reg('athens')
def athens():
    im, d = canvas()
    d.polygon([(10, 64), (18, 36), (30, 30), (70, 30), (82, 38), (90, 64)], fill=BLK)
    shade(im, lambda dd: dd.polygon([(14, 64), (20, 40), (30, 34), (70, 34), (80, 40), (86, 64)], fill=1), 3)
    d.rectangle((30, 18, 66, 30), fill=WHT)
    d.rectangle((28, 16, 68, 19), fill=BLK); d.polygon([(28, 16), (48, 10), (68, 16)], fill=WHT, outline=BLK)
    for x in range(30, 68, 5): d.rectangle((x, 20, x + 1, 30), fill=BLK)
    d.rectangle((26, 30, 70, 31), fill=BLK)
    front(im, d, 62, 70, 2, 6)
    frame(d); return im

@reg('amsterdam')
def amsterdam():
    im, d = canvas(); water(im, 52)
    x = 1
    for i, gable in enumerate(('step', 'bell', 'neck', 'step', 'bell', 'neck', 'step', 'bell')):
        w = 11; top = 14 + (i * 5) % 9
        d.rectangle((x, top + 6, x + w, 50), fill=WHT, outline=BLK)
        if gable == 'step': d.polygon([(x, top + 6), (x, top + 4), (x + 2, top + 4), (x + 2, top + 2), (x + 4, top + 2), (x + 4, top), (x + 7, top), (x + 7, top + 2), (x + 9, top + 2), (x + 9, top + 4), (x + 11, top + 4), (x + 11, top + 6)], fill=WHT, outline=BLK)
        elif gable == 'bell': d.chord((x + 1, top, x + 10, top + 12), 180, 360, fill=WHT, outline=BLK)
        else: d.rectangle((x + 3, top, x + 8, top + 6), fill=WHT, outline=BLK)
        for wy in range(top + 9, 48, 6):
            d.rectangle((x + 2, wy, x + 4, wy + 3), fill=BLK); d.rectangle((x + 7, wy, x + 9, wy + 3), fill=BLK)
        x += w + 1
    d.rectangle((1, 48, W - 2, 52), fill=WHT, outline=BLK)
    d.chord((30, 46, 66, 62), 180, 360, fill=WHT, outline=BLK)                # canal bridge
    # bicycle on the bridge
    d.ellipse((42, 42, 46, 46), outline=BLK); d.ellipse((50, 42, 54, 46), outline=BLK); d.line((44, 44, 48, 41, 52, 44), fill=BLK)
    frame(d); return im

@reg('prague')
def prague():
    im, d = canvas(); water(im, 52)
    # castle + St Vitus on the hill
    d.polygon([(0, 40), (20, 30), (70, 30), (96, 38), (96, 46), (0, 46)], fill=BLK)
    d.rectangle((14, 22, 70, 30), fill=WHT, outline=BLK)
    for x in range(16, 70, 3): d.point((x, 26), fill=BLK)
    for x, top in ((38, 4), (44, 6), (52, 2)):
        d.polygon([(x - 2, 22), (x, top), (x + 2, 22)], fill=BLK)
    d.rectangle((48, 10, 56, 22), fill=BLK); d.polygon([(48, 10), (52, 2), (56, 10)], fill=BLK)
    # Charles Bridge
    d.rectangle((1, 44, W - 2, 46), fill=BLK)
    for x in range(4, 95, 14): d.chord((x, 46, x + 12, 58), 180, 360, fill=WHT, outline=BLK)
    for x in (2, 94): d.rectangle((x - 2, 34, x + 2, 44), fill=BLK); d.polygon([(x - 3, 34), (x, 28), (x + 3, 34)], fill=BLK)
    for x in range(10, 90, 8): d.line((x, 40, x, 44), fill=BLK); d.point((x, 39), fill=BLK)   # statues
    frame(d); return im

@reg('budapest')
def budapest():
    im, d = canvas(); water(im, 48)
    # Parliament: long neo-gothic front, central dome, many spires
    d.rectangle((6, 34, 90, 48), fill=WHT, outline=BLK)
    for x in range(8, 90, 3): d.line((x, 37, x, 46), fill=BLK)
    d.chord((38, 16, 58, 40), 180, 360, fill=WHT, outline=BLK); d.line((48, 6, 48, 16), fill=BLK)
    for x in range(42, 56, 3): d.line((x, 22, x, 28), fill=BLK)
    for x in (10, 22, 32, 64, 74, 86): d.polygon([(x - 2, 34), (x, 24), (x + 2, 34)], fill=BLK)
    for x in (16, 80): d.rectangle((x - 2, 26, x + 2, 34), fill=BLK); d.polygon([(x - 3, 26), (x, 18), (x + 3, 26)], fill=BLK)
    frame(d); return im

@reg('edinburgh')
def edinburgh():
    im, d = canvas()
    d.polygon([(0, 64), (0, 44), (14, 36), (22, 26), (60, 24), (74, 30), (88, 44), (96, 50), (96, 64)], fill=BLK)
    shade(im, lambda dd: dd.polygon([(60, 26), (74, 32), (88, 46), (96, 52), (96, 64), (66, 64)], fill=1), 2)
    d.rectangle((20, 12, 62, 26), fill=WHT, outline=BLK)
    for x in range(20, 63, 3): d.rectangle((x, 10, x + 1, 12), fill=BLK)
    for x in (24, 40, 56): d.rectangle((x - 3, 6, x + 3, 26), fill=WHT, outline=BLK); [d.rectangle((xx, 4, xx, 6), fill=BLK) for xx in range(x - 3, x + 4, 2)]
    for x in range(22, 62, 4): d.rectangle((x, 16, x + 1, 19), fill=BLK)
    # Scott Monument spire in the city below
    d.polygon([(80, 56), (84, 32), (88, 56)], fill=BLK)
    front(im, d, 62, 77, 2, 8)
    frame(d); return im

# ------------------------------------------------------------------ Middle East, Asia, Oceania, Latin America, Africa
@reg('dubai')
def dubai():
    im, d = canvas(); water(im, 58)
    back(im, d, 56, seed=81, hmax=18)
    cx = 40
    steps = [(56, 7), (44, 6), (34, 5), (26, 4), (18, 3), (12, 2), (7, 1)]
    for (y, w), (y2, _) in zip(steps, steps[1:] + [(3, 0)]):
        d.rectangle((cx - w, y2, cx + w, y), fill=BLK)
        d.rectangle((cx - w - 2, y - 3, cx - w, y), fill=BLK); d.rectangle((cx + w, y - 6, cx + w + 2, y), fill=BLK)
    d.line((cx, 0, cx, 3), fill=BLK)
    # Burj Al Arab sail on the right
    d.line((80, 56, 80, 22), fill=BLK, width=2)
    d.polygon([(81, 22)] + [(81 + 10 * math.sin(math.pi * t), 22 + 34 * t) for t in [i / 12 for i in range(13)]], fill=WHT, outline=BLK)
    # Cayan twisting tower
    for y in range(20, 56): d.line((60 + math.sin(y / 6) * 2 - 3, y, 60 + math.sin(y / 6) * 2 + 3, y), fill=BLK)
    front(im, d, 56, 82, 3, 8, x0=1, x1=30)
    frame(d); return im

@reg('singapore')
def singapore():
    im, d = canvas(); water(im, 54)
    back(im, d, 52, seed=91, hmax=20)
    for x in (40, 54, 68):
        d.polygon([(x - 5, 52), (x - 4, 20), (x + 4, 20), (x + 5, 52)], fill=BLK)
        for y in range(24, 50, 4): d.line((x - 3, y, x + 3, y), fill=WHT)
    d.polygon([(30, 18), (80, 16), (82, 20), (32, 21)], fill=BLK)
    # Singapore Flyer
    d.ellipse((4, 18, 28, 42), outline=BLK, fill=WHT)
    for a in range(0, 360, 45): r = math.radians(a); d.line((16, 30, 16 + 12 * math.cos(r), 30 + 12 * math.sin(r)), fill=BLK)
    d.line((16, 30, 10, 52), fill=BLK); d.line((16, 30, 22, 52), fill=BLK)
    # Merlion
    d.rectangle((86, 44, 90, 54), fill=BLK); d.ellipse((84, 38, 92, 46), fill=BLK); d.line((84, 42, 76, 48), fill=BLK)
    frame(d); return im

@reg('hong-kong')
def hong_kong():
    im, d = canvas()
    d.polygon([(0, 30), (20, 18), (40, 22), (60, 14), (80, 20), (96, 26), (96, 50), (0, 50)], fill=WHT, outline=BLK)   # Victoria Peak
    fill_pattern(im, (1, 20, W - 1, 50), 6)
    water(im, 54)
    back(im, d, 52, seed=101, hmax=22)
    # Bank of China Tower (stacked triangular prisms)
    d.polygon([(24, 52), (24, 18), (30, 8), (36, 18), (36, 52)], fill=BLK)
    for y0 in (18, 30, 42): d.line((24, y0 + 10, 30, y0), fill=WHT); d.line((30, y0, 36, y0 + 10), fill=WHT); d.line((24, y0 + 10, 36, y0 + 10), fill=WHT)
    d.line((28, 2, 28, 10), fill=BLK); d.line((32, 2, 32, 10), fill=BLK)
    # IFC 2
    d.rectangle((52, 12, 62, 52), fill=BLK); d.polygon([(52, 12), (54, 6), (60, 6), (62, 12)], fill=BLK)
    for y in range(14, 52, 4): d.line((53, y, 61, y), fill=WHT)
    front(im, d, 52, 103, 6, 16, x0=66)
    # junk boat with batten sails
    d.polygon([(6, 58), (22, 58), (20, 61), (8, 61)], fill=BLK)
    d.polygon([(10, 57), (12, 44), (18, 46), (17, 57)], fill=BLK)
    for y in range(46, 57, 3): d.line((12, y, 17, y), fill=WHT)
    frame(d); return im

@reg('tokyo')
def tokyo():
    im, d = canvas()
    d.polygon([(54, 40), (70, 22), (76, 22), (92, 40)], fill=WHT, outline=BLK)      # Fuji in the distance
    d.polygon([(70, 22), (76, 22), (79, 26), (67, 26)], fill=BLK)
    back(im, d, 58, seed=111, hmax=16); ground(im, d, 58)
    # Tokyo Skytree
    cx = 20
    d.polygon([(cx - 5, 58), (cx - 1, 10), (cx + 1, 10), (cx + 5, 58)], fill=BLK)
    for y in range(20, 58, 4): d.line((cx - 2, y, cx + 2, y + 3), fill=WHT)
    d.ellipse((cx - 3, 22, cx + 3, 26), fill=BLK); d.ellipse((cx - 2, 14, cx + 2, 17), fill=BLK); d.line((cx, 0, cx, 10), fill=BLK)
    # Tokyo Tower (lattice, Eiffel-like)
    cx = 46; L, R = [], []
    for i in range(21):
        t = i / 20; y = 58 - t * 46; half = 1 + 10 * (1 - t) ** 2
        L.append((cx - half, y)); R.append((cx + half, y))
    d.polygon(L + R[::-1], fill=BLK)
    for y in range(26, 56, 4):
        half = 1 + 10 * (1 - (58 - y) / 46) ** 2
        d.line((cx - half + 1, y, cx + half - 1, y), fill=WHT)
    d.rectangle((cx - 4, 30, cx + 4, 33), fill=BLK); d.rectangle((cx - 2, 20, cx + 2, 22), fill=BLK); d.line((cx, 4, cx, 12), fill=BLK)
    front(im, d, 58, 113, 4, 10, x0=60)
    frame(d); return im

@reg('sydney')
def sydney():
    im, d = canvas()
    back(im, d, 46, seed=121, hmax=12)
    # Sydney Tower
    needle(d, 30, 4, 46, [(12, 4, 3)], 1); d.line((30, 0, 30, 4), fill=BLK)
    # Harbour Bridge
    d.arc((44, 18, 96, 70), 200, 340, fill=BLK); d.arc((44, 22, 96, 74), 200, 340, fill=BLK)
    d.line((40, 40, 96, 40), fill=BLK)
    for x in range(50, 92, 4):
        yy = 44 - math.sqrt(max(0, 26 ** 2 - (x - 70) ** 2)); d.line((x, yy, x, 40), fill=BLK)
    d.rectangle((42, 32, 46, 46), fill=BLK); d.rectangle((90, 32, 94, 46), fill=BLK)
    water(im, 48)
    d.rectangle((2, 50, 40, 53), fill=BLK)
    for (xr, r) in ((12, 14), (22, 13), (30, 9), (36, 6)):
        d.pieslice((xr - r, 50 - r, xr + r, 50 + r), 180, 270, fill=WHT, outline=BLK)
    frame(d); return im

@reg('rio-de-janeiro')
def rio():
    im, d = canvas()
    d.polygon([(1, 60), (8, 40), (18, 26), (26, 24), (34, 34), (44, 60)], fill=BLK)
    d.rectangle((24, 9, 26, 24), fill=BLK); d.rectangle((17, 11, 33, 12), fill=BLK); d.ellipse((23, 6, 27, 10), fill=BLK)
    d.polygon([(56, 60), (62, 34), (66, 26), (72, 26), (76, 34), (80, 60)], fill=BLK)
    d.polygon([(80, 60), (84, 48), (90, 46), (95, 60)], fill=BLK)
    d.line((70, 26, 87, 46), fill=BLK); d.rectangle((77, 34, 79, 36), fill=BLK)
    for y in range(52, H - 1):
        for x in range(1, W - 1):
            if im.getpixel((x, y)) == WHT and y % 3 == 0 and (x + y) % 6 < 3: im.putpixel((x, y), BLK)
    frame(d); return im

@reg('kuala-lumpur')
def kuala_lumpur():
    im, d = canvas(); ground(im, d, 60)
    back(im, d, 60, seed=131, hmax=14)
    for cx in (22, 42):
        for i, (y0, y1, w) in enumerate(((22, 60, 6), (16, 22, 5), (12, 16, 4), (9, 12, 3))):
            d.rectangle((cx - w, y0, cx + w, y1), fill=BLK)
        for x in range(cx - 4, cx + 5, 2): d.line((x, 24, x, 58), fill=WHT)
        d.line((cx, 2, cx, 9), fill=BLK)
    d.rectangle((28, 32, 36, 34), fill=BLK)
    # KL Tower
    needle(d, 74, 10, 60, [(20, 6, 3)], 1); d.line((74, 0, 74, 10), fill=BLK)
    d.polygon([(70, 14), (74, 12), (78, 14)], fill=BLK)
    frame(d); return im

@reg('seoul')
def seoul():
    im, d = canvas()
    d.polygon([(0, 46), (12, 34), (24, 28), (36, 34), (48, 46)], fill=BLK)       # Namsan
    needle(d, 24, 6, 30, [(14, 4, 2)], 1); d.line((24, 0, 24, 6), fill=BLK)
    back(im, d, 56, seed=141, hmax=12); water(im, 58)
    # Lotte World Tower: tall tapering cone
    d.polygon([(60, 56), (66, 4), (68, 4), (74, 56)], fill=BLK)
    d.line((67, 8, 67, 54), fill=WHT); d.line((64, 6, 64, 8), fill=BLK)
    front(im, d, 56, 143, 4, 12, x0=76)
    frame(d); return im

@reg('taipei')
def taipei():
    im, d = canvas()
    d.polygon([(0, 30), (20, 20), (44, 28), (70, 16), (96, 26), (96, 58), (0, 58)], fill=WHT, outline=BLK)
    fill_pattern(im, (1, 22, W - 1, 58), 6)
    back(im, d, 58, seed=151, hmax=12); ground(im, d, 58)
    cx = 48
    d.rectangle((cx - 6, 46, cx + 6, 58), fill=BLK)
    y = 46
    for i in range(8):
        d.polygon([(cx - 4, y), (cx - 6, y - 4), (cx + 6, y - 4), (cx + 4, y)], fill=BLK); d.line((cx - 5, y - 4, cx + 5, y - 4), fill=WHT); y -= 4
    d.rectangle((cx - 3, y - 4, cx + 3, y), fill=BLK); d.line((cx, y - 12, cx, y - 4), fill=BLK)
    frame(d); return im

@reg('bangkok')
def bangkok():
    im, d = canvas(); water(im, 54)
    # Wat Arun prang
    cx = 30
    pts = []
    for i in range(21):
        t = i / 20; y = 52 - 46 * t; w = 14 * (1 - t) ** 1.3 + 1
        pts.append((cx - w, y))
    d.polygon(pts + [(2 * cx - x, y) for x, y in reversed(pts)], fill=BLK)
    for y in range(14, 52, 5):
        w = 14 * ((y - 6) / 46) ** 1.3; d.line((cx - w + 1, y, cx + w - 1, y), fill=WHT)
    for x in (10, 50): d.polygon([(x - 4, 52), (x, 34), (x + 4, 52)], fill=BLK)
    # MahaNakhon "pixelated" tower
    d.rectangle((70, 6, 80, 52), fill=BLK)
    for y in range(8, 50, 4):
        off = int(3 * math.sin(y / 5)); d.rectangle((70 + 4 + off, y, 72 + 4 + off, y + 2), fill=WHT)
    # long-tail boat
    d.polygon([(52, 58), (66, 58), (68, 56), (64, 60), (54, 60)], fill=BLK)
    frame(d); return im

@reg('mumbai')
def mumbai():
    im, d = canvas(); water(im, 52)
    # Gateway of India
    d.rectangle((8, 26, 40, 52), fill=WHT, outline=BLK)
    d.chord((18, 32, 30, 48), 180, 360, fill=BLK); d.rectangle((18, 40, 30, 52), fill=BLK)
    for x in (8, 36): d.rectangle((x, 20, x + 4, 26), fill=WHT, outline=BLK); onion(d, x + 2, 20, 2.5)
    d.rectangle((6, 24, 42, 26), fill=BLK)
    for x in range(12, 38, 4): d.rectangle((x, 28, x + 1, 30), fill=BLK)
    # Taj Mahal Palace hotel dome
    d.rectangle((50, 30, 92, 52), fill=WHT, outline=BLK)
    for y in range(34, 50, 5):
        for x in range(52, 90, 4): d.rectangle((x, y, x + 1, y + 2), fill=BLK)
    d.chord((64, 14, 78, 36), 180, 360, fill=WHT, outline=BLK); fill_pattern(im, (66, 17, 77, 25), 2); d.line((71, 10, 71, 14), fill=BLK)
    for x in (52, 90): d.chord((x - 3, 24, x + 3, 34), 180, 360, fill=BLK)
    frame(d); return im

@reg('buenos-aires')
def buenos_aires():
    im, d = canvas(); ground(im, d, 58, 5)
    back(im, d, 56, seed=171, hmax=20)
    d.polygon([(44, 56), (46, 8), (48, 4), (50, 8), (52, 56)], fill=BLK)        # Obelisco
    d.rectangle((47, 10, 49, 12), fill=WHT)
    front(im, d, 56, 172, 3, 10, x0=1, x1=38); front(im, d, 56, 173, 3, 10, x0=58)
    frame(d); return im

@reg('mexico-city')
def mexico_city():
    im, d = canvas(); ground(im, d, 58)
    d.polygon([(54, 34), (66, 16), (72, 18), (80, 14), (94, 34)], fill=WHT, outline=BLK)       # Popocatépetl
    d.polygon([(64, 19), (66, 16), (72, 18), (80, 14), (83, 19)], fill=BLK)
    back(im, d, 56, seed=181, hmax=12)
    # Angel of Independence column
    d.rectangle((22, 46, 32, 56), fill=BLK); d.rectangle((25, 14, 29, 46), fill=BLK); d.rectangle((24, 12, 30, 14), fill=BLK)
    d.ellipse((25, 6, 29, 10), fill=BLK); d.line((22, 8, 32, 6), fill=BLK, width=2)
    # Torre Latinoamericana
    setback(d, 48, 56, [(5, 30), (3, 6), (2, 4)]); d.line((48, 8, 48, 16), fill=BLK)
    lit(im, (44, 28, 53, 55), 9)
    frame(d); return im

@reg('cape-town')
def cape_town():
    im, d = canvas(); water(im, 56)
    d.polygon([(0, 46), (8, 30), (14, 18), (20, 16), (24, 22), (30, 20), (34, 14), (74, 14), (78, 20), (86, 30), (96, 40), (96, 54), (0, 54)], fill=BLK)
    d.polygon([(30, 13), (78, 13), (76, 9), (62, 10), (46, 8), (32, 10)], fill=WHT, outline=BLK)
    for x in range(36, 76, 4): d.line((x, 14, x + 1, 18), fill=WHT)
    fill_pattern(im, (1, 42, W - 1, 54), 0)
    city_fill(im, d, 54, seed=11, hmin=3, hmax=12, x0=2, x1=94, wmin=2, wmax=6)
    frame(d); return im

if __name__ == '__main__':
    for n, f in REG.items(): save(f(), CAT, n)
    print(len(REG))
