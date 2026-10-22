#!/usr/bin/env python3
"""Wonders of the world (new 7, ancient 7) — 1-bit pixel art."""
import math
from PIL import Image, ImageDraw
from common import *

CAT = 'landmarks'
REG = {}
def reg(name):
    def deco(fn): REG[name] = fn; return fn
    return deco

# ------------------------------------------------------------------ New Seven Wonders
@reg('great-wall-of-china')
def great_wall():
    im, d = canvas()
    clouds(d, [(6, 6), (66, 4)])
    path = [(0, 52), (14, 40), (26, 46), (42, 26), (56, 34), (72, 18), (86, 26), (96, 22)]
    # far ridge
    shade(im, lambda dd: dd.polygon([(0, 34), (20, 24), (34, 30), (52, 14), (70, 22), (84, 10), (96, 16), (96, 64), (0, 64)], fill=1), 6)
    # near hills under the wall
    hill = path + [(96, 64), (0, 64)]
    d.polygon(hill, fill=WHT); shade(im, lambda dd: dd.polygon(hill, fill=1), 5)
    for a, b in zip(path, path[1:]):
        d.line((a[0], a[1], b[0], b[1]), fill=BLK, width=5)
    for a, b in zip(path, path[1:]):
        d.line((a[0], a[1] + 1, b[0], b[1] + 1), fill=WHT, width=1)
    # crenellations
    for a, b in zip(path, path[1:]):
        n = int(math.hypot(b[0] - a[0], b[1] - a[1]) // 3)
        for i in range(n):
            t = i / max(1, n); x = a[0] + (b[0] - a[0]) * t; y = a[1] + (b[1] - a[1]) * t
            d.rectangle((x, y - 4, x + 1, y - 3), fill=BLK)
    for (x, y) in [path[1], path[3], path[5], path[6]]:
        d.rectangle((x - 4, y - 10, x + 4, y + 1), fill=BLK)
        for cx in range(x - 4, x + 5, 2): d.point((cx, y - 11), fill=BLK)
        d.rectangle((x - 1, y - 7, x + 1, y - 4), fill=WHT)
    frame(d); return im

@reg('petra-treasury')
def petra():
    im, d = canvas()
    fill_pattern(im, (1, 1, W - 1, H - 1), 3)                    # rose rock
    for x in (6, 12, 84, 90):
        d.line((x, 2, x + 3, 62), fill=WHT)
    d.rectangle((22, 6, 74, 60), fill=WHT)
    # lower storey
    d.rectangle((22, 32, 74, 35), fill=BLK); d.line((22, 37, 74, 37), fill=BLK)
    d.polygon([(34, 31), (48, 23), (62, 31)], outline=BLK, fill=WHT)
    for x in (25, 31, 38, 58, 65, 71):
        d.rectangle((x, 38, x + 1, 58), fill=BLK); d.rectangle((x - 1, 38, x + 2, 39), fill=BLK)
    d.rectangle((44, 42, 52, 58), fill=BLK)                       # doorway
    d.line((22, 59, 74, 59), fill=BLK)
    # upper storey: tholos + side pavilions
    d.rectangle((41, 10, 55, 28), outline=BLK, fill=WHT)
    for x in (43, 48, 53): d.line((x, 12, x, 27), fill=BLK)
    d.polygon([(40, 10), (48, 3), (56, 10)], fill=BLK)
    d.rectangle((47, 0, 49, 3), fill=BLK)                          # urn
    for x0 in (23, 59):
        d.rectangle((x0, 12, x0 + 13, 28), outline=BLK, fill=WHT)
        for x in range(x0 + 2, x0 + 13, 4): d.line((x, 14, x, 27), fill=BLK)
        d.polygon([(x0, 12), (x0 + 13, 12), (x0 + (13 if x0 < 48 else 0), 7)], fill=BLK)
    d.line((22, 29, 74, 29), fill=BLK)
    # tiny visitors and a camel for scale
    for x in (14, 80): d.rectangle((x, 56, x + 1, 60), fill=BLK); d.point((x, 55), fill=BLK)
    frame(d); return im

@reg('christ-the-redeemer')
def christ():
    im, d = canvas()
    clouds(d, [(4, 30), (74, 36)])
    mt = [(0, 64), (10, 54), (26, 46), (40, 41), (56, 41), (70, 46), (86, 54), (96, 60), (96, 64)]
    d.polygon(mt, fill=BLK)
    shade(im, lambda dd: dd.polygon([(60, 44), (70, 46), (86, 54), (96, 60), (96, 64), (66, 64)], fill=1), 2)
    d.rectangle((44, 34, 52, 42), fill=BLK)                       # pedestal
    d.polygon([(45, 34), (44, 15), (52, 15), (51, 34)], fill=BLK)   # robe
    d.polygon([(18, 15), (78, 15), (78, 18), (52, 19), (44, 19), (18, 18)], fill=BLK)   # outstretched arms
    d.rectangle((16, 15, 18, 19), fill=BLK); d.rectangle((78, 15, 80, 19), fill=BLK)     # hands
    d.ellipse((45, 7, 51, 14), fill=BLK)
    d.line((48, 20, 48, 33), fill=WHT)                            # robe fold
    frame(d); return im

@reg('machu-picchu')
def machu():
    im, d = canvas()
    # Huayna Picchu
    peak = [(40, 64), (52, 22), (58, 10), (64, 8), (70, 14), (74, 28), (86, 46), (96, 52), (96, 64)]
    d.polygon(peak, fill=BLK)
    shade(im, lambda dd: dd.polygon([(64, 8), (70, 14), (74, 28), (86, 46), (96, 52), (96, 64), (70, 64)], fill=1), 3)
    for y in range(18, 46, 5): d.point((60 + (y % 7), y), fill=WHT)
    # far ridge
    d.line((0, 30, 20, 22), fill=BLK); d.line((20, 22, 40, 34), fill=BLK)
    clouds(d, [(4, 8), (24, 4)])
    # terraces
    for i, y in enumerate(range(44, 64, 4)):
        d.polygon([(0, y), (60 - i * 3, y - 2), (60 - i * 3, y), (0, y + 2)], fill=WHT)
        d.line((0, y + 2, 60 - i * 3, y), fill=BLK)
    # ruins: gabled stone houses
    for x, y in ((8, 40), (18, 38), (28, 37), (38, 38), (14, 46), (26, 45)):
        d.rectangle((x, y - 5, x + 7, y), outline=BLK, fill=WHT)
        d.polygon([(x, y - 5), (x + 3, y - 9), (x + 7, y - 5)], outline=BLK, fill=WHT)
        d.point((x + 3, y - 2), fill=BLK)
    # llama
    d.polygon([(70, 60), (71, 54), (78, 54), (79, 50), (81, 50), (80, 56), (79, 60), (78, 56), (73, 57), (72, 60)], fill=WHT, outline=BLK)
    frame(d); return im

@reg('chichen-itza')
def chichen():
    im, d = canvas(); ground(im, d, 58)
    sun(im, d, 82, 10)
    for i in range(9):
        y1 = 58 - i * 4; half = 40 - i * 3.2
        d.rectangle((48 - half, y1 - 4, 48 + half, y1), fill=WHT, outline=BLK)
        shade(im, lambda dd, y1=y1, half=half: dd.rectangle((48 + 7, y1 - 3, 48 + half - 1, y1 - 1), fill=1), 2)
    # staircase
    d.rectangle((42, 22, 54, 58), fill=WHT, outline=BLK)
    for y in range(24, 58, 2): d.line((43, y, 53, y), fill=BLK)
    d.rectangle((40, 54, 42, 58), fill=BLK); d.rectangle((54, 54, 56, 58), fill=BLK)   # serpent heads
    # temple on top
    d.rectangle((38, 10, 58, 22), fill=WHT, outline=BLK)
    d.rectangle((38, 10, 58, 13), fill=BLK)
    for x in (41, 47, 53): d.rectangle((x, 15, x + 2, 22), fill=BLK)
    frame(d); return im

@reg('colosseum')
def colosseum():
    im, d = canvas(); ground(im, d, 58)
    clouds(d, [(70, 4)])
    # outer wall, full height on the left, stepped down on the right (ruined side)
    top = lambda x: 10 + int(((x - 48) / 46) ** 2 * 6)
    for x in range(4, 92):
        t = top(x)
        if x > 62: t = max(t, 24 if x < 78 else 34)
        d.line((x, t, x, 58), fill=WHT)
        d.point((x, t), fill=BLK)
    d.line((4, top(4), 4, 58), fill=BLK); d.line((91, 34, 91, 58), fill=BLK)
    for (y0, y1) in ((47, 57), (36, 45), (25, 34)):
        d.line((4, y1 + 1, 91, y1 + 1), fill=BLK)
        for x in range(6, 90, 5):
            t = top(x) if x <= 62 else (24 if x < 78 else 34)
            if y0 < t: continue
            d.rectangle((x, y0 + 2, x + 2, y1), fill=BLK); d.point((x, y0 + 2), fill=WHT); d.point((x + 2, y0 + 2), fill=WHT)
    # attic storey: small square windows
    for x in range(8, 62, 6): d.rectangle((x, 16, x + 1, 18), fill=BLK)
    d.line((4, 23, 62, 23), fill=BLK)
    # inner ring visible through the broken side
    for x in range(64, 90, 4): d.rectangle((x, 20, x + 1, 23), fill=BLK)
    frame(d); return im

@reg('taj-mahal')
def taj():
    im, d = canvas(); ground(im, d, 56)
    cx = 48
    d.rectangle((14, 52, 82, 56), outline=BLK, fill=WHT)
    d.rectangle((28, 30, 68, 52), outline=BLK, fill=WHT)
    d.polygon([(cx - 6, 52), (cx - 6, 40), (cx, 34), (cx + 6, 40), (cx + 6, 52)], fill=BLK)
    for x in (32, 60):
        d.polygon([(x, 50), (x, 44), (x + 2, 42), (x + 4, 44), (x + 4, 50)], fill=BLK)
        d.polygon([(x, 40), (x, 35), (x + 2, 33), (x + 4, 35), (x + 4, 40)], fill=BLK)
    d.rectangle((cx - 8, 26, cx + 8, 30), outline=BLK, fill=WHT)
    d.ellipse((cx - 11, 8, cx + 11, 28), outline=BLK, fill=WHT)
    d.polygon([(cx - 4, 10), (cx, 3), (cx + 4, 10)], fill=WHT, outline=BLK)
    d.line((cx, 1, cx, 4), fill=BLK)
    d.rectangle((cx - 11, 22, cx + 11, 26), fill=WHT); d.line((cx - 11, 26, cx + 11, 26), fill=BLK)
    d.line((cx - 11, 22, cx - 11, 26), fill=BLK); d.line((cx + 11, 22, cx + 11, 26), fill=BLK)
    for x in (34, 62):
        d.ellipse((x - 4, 22, x + 4, 30), outline=BLK, fill=WHT); d.line((x, 19, x, 22), fill=BLK)
    for x in (18, 78):
        d.rectangle((x - 2, 20, x + 2, 52), outline=BLK, fill=WHT)
        for y in (28, 38): d.line((x - 3, y, x + 3, y), fill=BLK)
        d.ellipse((x - 3, 15, x + 3, 21), outline=BLK, fill=WHT); d.line((x, 12, x, 15), fill=BLK)
    d.rectangle((44, 57, 52, 62), fill=WHT, outline=BLK)
    frame(d); return im

@reg('pyramids-of-giza')
def pyramids():
    im, d = canvas()
    sun(im, d, 78, 12)
    sand = 54
    fill_pattern(im, (1, sand, W - 1, H - 1), 1)
    for (x, base, h) in ((30, 54, 34), (60, 54, 26), (80, 54, 14)):
        apex = (x, base - h); l = (x - h, base); r = (x + h, base)
        d.polygon([apex, l, r], fill=WHT, outline=BLK)
        shade(im, lambda dd, apex=apex, x=x, base=base, r=r: dd.polygon([apex, (x + 2, base), r], fill=1), 2)
        d.line((apex, (x + 2, base)), fill=BLK)
        for yy in range(base - h + 4, base, 4):
            off = (yy - (base - h)); d.line((x - off + 1, yy, x, yy), fill=BLK)
    cam = [(10, 52), (12, 47), (14, 46), (15, 48), (17, 45), (19, 48), (20, 46), (22, 46), (21, 49), (19, 50), (19, 53), (18, 53), (18, 50), (13, 50), (13, 53), (12, 53)]
    d.polygon(cam, fill=BLK)
    d.line((1, sand, W - 2, sand), fill=BLK)
    frame(d); return im

# ------------------------------------------------------------------ Ancient wonders (reconstructions)
@reg('hanging-gardens-of-babylon')
def hanging():
    im, d = canvas(); ground(im, d, 58)
    for i in range(4):
        y1 = 58 - i * 11; half = 40 - i * 9
        d.rectangle((48 - half, y1 - 10, 48 + half, y1), fill=WHT, outline=BLK)
        for x in range(48 - half + 2, 48 + half - 1, 4):
            d.rectangle((x, y1 - 6, x + 1, y1 - 1), fill=BLK)          # arches
        # hanging greenery
        shade(im, lambda dd, y1=y1, half=half: dd.rectangle((48 - half, y1 - 10, 48 + half, y1 - 8), fill=1), 3)
        for x in range(48 - half + 1, 48 + half, 3):
            ln = 2 + (x * 7 + i) % 5; d.line((x, y1 - 8, x, y1 - 8 + ln), fill=BLK)
    # palms on top
    for x in (42, 54):
        d.line((x, 14, x, 6), fill=BLK)
        for a in (-50, -20, 20, 50, 180 + 30, 180 - 30):
            r = math.radians(a - 90); d.line((x, 6, x + 5 * math.cos(r), 6 + 3 * math.sin(r) + 2), fill=BLK)
    frame(d); return im

@reg('colossus-of-rhodes')
def colossus():
    im, d = canvas()
    water(im, 48)
    sun(im, d, 84, 10, 4)
    # harbour moles
    d.rectangle((1, 44, 30, 50), fill=BLK); d.rectangle((66, 44, 94, 50), fill=BLK)
    d.rectangle((24, 36, 34, 44), fill=BLK); d.rectangle((62, 36, 72, 44), fill=BLK)   # pedestals
    d.polygon([(29, 36), (42, 22), (46, 22), (32, 36)], fill=BLK)      # left leg
    d.polygon([(67, 36), (54, 22), (50, 22), (64, 36)], fill=BLK)      # right leg
    d.polygon([(42, 24), (54, 24), (53, 12), (43, 12)], fill=BLK)      # torso
    d.ellipse((45, 6, 51, 12), fill=BLK)
    d.polygon([(53, 13), (59, 6), (61, 7), (55, 15)], fill=BLK)        # raised arm
    d.polygon([(58, 6), (60, 1), (62, 6)], fill=BLK)                   # torch flame
    d.line((43, 14, 38, 24), fill=BLK, width=2)                        # lowered arm
    for a in range(-60, 61, 30):                                       # sun crown
        r = math.radians(a - 90); d.line((48, 9, 48 + 6 * math.cos(r), 9 + 6 * math.sin(r)), fill=BLK)
    # a ship sailing between the legs
    d.polygon([(40, 52), (58, 52), (55, 56), (43, 56)], fill=BLK)
    d.line((49, 52, 49, 40), fill=BLK); d.polygon([(49, 41), (49, 50), (56, 50)], fill=WHT, outline=BLK)
    frame(d); return im

@reg('lighthouse-of-alexandria')
def pharos():
    im, d = canvas()
    water(im, 54)
    d.rectangle((14, 50, 82, 56), fill=BLK)                             # island
    cx = 48
    d.rectangle((cx - 13, 26, cx + 13, 50), outline=BLK, fill=WHT)      # square base
    for y in (32, 38, 44):
        for x in range(cx - 10, cx + 11, 5): d.rectangle((x, y, x + 1, y + 2), fill=BLK)
    d.rectangle((cx - 15, 24, cx + 15, 26), fill=BLK)
    d.polygon([(cx - 9, 24), (cx - 8, 12), (cx + 8, 12), (cx + 9, 24)], outline=BLK, fill=WHT)  # octagonal tier
    shade(im, lambda dd: dd.polygon([(cx + 3, 23), (cx + 3, 13), (cx + 8, 13), (cx + 8, 23)], fill=1), 2)
    d.rectangle((cx - 10, 10, cx + 10, 12), fill=BLK)
    d.rectangle((cx - 5, 4, cx + 5, 10), outline=BLK, fill=WHT)         # round lantern
    for x in (cx - 3, cx, cx + 3): d.line((x, 4, x, 9), fill=BLK)
    d.polygon([(cx - 5, 4), (cx, 1), (cx + 5, 4)], fill=BLK)
    # fire glow
    for a in range(0, 360, 45):
        r = math.radians(a); d.line((cx + 8 * math.cos(r), 6 + 5 * math.sin(r), cx + 12 * math.cos(r), 6 + 7 * math.sin(r)), fill=BLK)
    # boat
    d.polygon([(70, 58), (84, 58), (81, 61), (73, 61)], fill=BLK); d.line((77, 58, 77, 50), fill=BLK)
    d.polygon([(77, 51), (77, 57), (82, 57)], outline=BLK, fill=WHT)
    frame(d); return im

def greek_temple(d, im, x0, x1, base, top, ncols, pediment=8, steps=3):
    for i in range(steps):
        d.rectangle((x0 - 2 * (steps - i), base + i * 2 - steps * 2 + 2, x1 + 2 * (steps - i), base + i * 2 - steps * 2 + 3), fill=BLK)
    yb = base - steps * 2 + 1
    d.rectangle((x0, top, x1, top + 4), fill=BLK)                       # entablature
    for x in range(top + 1, top + 4): pass
    sp = (x1 - x0) / (ncols - 1)
    for i in range(ncols):
        x = round(x0 + i * sp)
        d.rectangle((x - 1, top + 5, x + 1, yb), fill=BLK)
        d.point((x, top + 7), fill=WHT)
    d.polygon([(x0 - 1, top), ((x0 + x1) / 2, top - pediment), (x1 + 1, top)], fill=WHT, outline=BLK)
    d.line((x0 + 3, top - 1, x1 - 3, top - 1), fill=BLK)

@reg('temple-of-artemis')
def artemis():
    im, d = canvas(); ground(im, d, 58)
    greek_temple(d, im, 10, 86, 58, 24, 12, pediment=12)
    for i in range(6):                                                  # second row of columns behind
        x = 16 + i * 13; d.line((x + 3, 30, x + 3, 50), fill=BLK)
    clouds(d, [(6, 4), (74, 6)])
    frame(d); return im

@reg('statue-of-zeus-at-olympia')
def zeus():
    im, d = canvas()
    fill_pattern(im, (1, 1, W - 1, H - 1), 6)
    d.rectangle((1, 56, W - 2, 62), fill=BLK)
    for x in (6, 16, 80, 90): d.rectangle((x - 2, 4, x + 2, 56), fill=WHT, outline=BLK)
    d.rectangle((1, 2, W - 2, 5), fill=BLK)
    cx = 48
    d.rectangle((28, 44, 68, 56), fill=WHT, outline=BLK)                # plinth
    d.rectangle((32, 14, 64, 44), fill=WHT, outline=BLK)                # throne back
    d.rectangle((30, 30, 34, 46), fill=BLK); d.rectangle((62, 30, 66, 46), fill=BLK)    # armrests
    d.polygon([(40, 44), (40, 32), (56, 32), (56, 44)], fill=BLK)       # lap/robe
    d.rectangle((40, 44, 44, 52), fill=BLK); d.rectangle((52, 44, 56, 52), fill=BLK)     # legs
    d.polygon([(42, 32), (43, 16), (53, 16), (54, 32)], fill=BLK)       # torso
    d.ellipse((44, 7, 52, 16), fill=BLK); d.rectangle((44, 13, 52, 19), fill=BLK)        # head + beard
    d.line((58, 4, 58, 46), fill=BLK, width=2); d.line((53, 20, 58, 22), fill=BLK, width=2)   # sceptre
    d.ellipse((57, 3, 60, 6), fill=BLK)
    d.line((43, 22, 38, 30), fill=BLK, width=2); d.ellipse((35, 27, 39, 31), fill=BLK)    # Nike in hand
    frame(d); return im

@reg('mausoleum-at-halicarnassus')
def mausoleum():
    im, d = canvas(); ground(im, d, 58)
    d.rectangle((20, 36, 76, 58), fill=WHT, outline=BLK)                # podium
    for y in range(40, 58, 4): d.line((20, y, 76, y), fill=BLK)
    for x in range(22, 76, 6):
        for y in range(36, 58, 8): d.line((x + (3 if (y // 4) % 2 else 0), y, x + (3 if (y // 4) % 2 else 0), y + 4), fill=BLK)
    d.rectangle((24, 22, 72, 36), fill=WHT, outline=BLK)
    d.rectangle((24, 22, 72, 24), fill=BLK)
    for x in range(26, 72, 4): d.rectangle((x, 25, x + 1, 35), fill=BLK)
    for i in range(6):                                                  # stepped pyramid roof
        y = 22 - i * 2; half = 26 - i * 3
        d.rectangle((48 - half, y - 2, 48 + half, y), fill=WHT, outline=BLK)
    # quadriga on top
    d.rectangle((40, 4, 56, 8), fill=BLK)
    for x in (41, 45, 49, 53): d.line((x, 8, x, 10), fill=BLK)
    d.rectangle((54, 0, 57, 4), fill=BLK); d.ellipse((50, 3, 54, 7), fill=WHT, outline=BLK)
    frame(d); return im

@reg('great-sphinx-of-giza')
def sphinx():
    im, d = canvas()
    fill_pattern(im, (1, 52, W - 1, H - 1), 1); d.line((1, 52, W - 2, 52), fill=BLK)
    d.polygon([(52, 52), (74, 14), (96, 46), (96, 52)], fill=WHT, outline=BLK)      # pyramid behind
    shade(im, lambda dd: dd.polygon([(74, 14), (78, 52), (96, 52), (96, 46)], fill=1), 2)
    # body
    d.polygon([(8, 52), (10, 40), (22, 34), (54, 34), (66, 40), (68, 52)], fill=BLK)
    d.rectangle((54, 46, 76, 52), fill=BLK)                             # front paws
    shade(im, lambda dd: dd.polygon([(12, 38), (52, 36), (52, 44), (12, 46)], fill=1), 2)
    # head with nemes headdress
    d.polygon([(44, 34), (44, 22), (48, 14), (58, 12), (64, 16), (66, 26), (64, 36)], fill=BLK)
    d.rectangle((54, 18, 61, 32), fill=WHT)                             # face
    d.point((56, 22), fill=BLK); d.point((59, 22), fill=BLK); d.line((57, 24, 58, 27), fill=BLK); d.line((56, 29, 59, 29), fill=BLK)
    for y in range(16, 34, 3): d.line((46, y, 52, y), fill=WHT)        # headdress stripes
    frame(d); return im

if __name__ == '__main__':
    for n, f in REG.items(): save(f(), CAT, n)
    print(len(REG))
