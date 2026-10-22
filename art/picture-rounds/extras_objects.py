#!/usr/bin/env python3
"""Sports gear, musical instruments, animals and famous (public-domain) paintings — 1-bit."""
import math, random
from PIL import Image, ImageDraw
from common import *

SPORT, INST, ANIM, ART = {}, {}, {}, {}
def reg(table, name):
    def deco(fn): table[name] = fn; return fn
    return deco

def floor(im, d, y=56):
    d.line((1, y, W - 2, y), fill=BLK); fill_pattern(im, (1, y + 1, W - 1, H - 1), 6)

# ================================================================== SPORTS
@reg(SPORT, 'football-soccer-ball')
def soccer():
    im, d = canvas(); floor(im, d)
    cx, cy, r = 48, 32, 22
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=WHT, outline=BLK)
    pent = lambda x, y, s: [(x + s * math.cos(math.radians(-90 + i * 72)), y + s * math.sin(math.radians(-90 + i * 72))) for i in range(5)]
    d.polygon(pent(cx, cy, 7), fill=BLK)
    for i in range(5):
        a = math.radians(-90 + i * 72); x, y = cx + 17 * math.cos(a), cy + 17 * math.sin(a)
        p = pent(x, y, 6); d.polygon(p, fill=BLK)
        d.line((cx + 7 * math.cos(a), cy + 7 * math.sin(a), x - 6 * math.cos(a), y - 6 * math.sin(a)), fill=BLK)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=BLK)
    frame(d); return im

@reg(SPORT, 'basketball')
def basketball():
    im, d = canvas(); floor(im, d)
    cx, cy, r = 48, 32, 22
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=BLK); shade(im, lambda dd: dd.ellipse((cx - r + 2, cy - r + 2, cx + r - 2, cy + r - 2), fill=1), 3)
    d.line((cx - r, cy, cx + r, cy), fill=BLK, width=2); d.line((cx, cy - r, cx, cy + r), fill=BLK, width=2)
    d.arc((cx - r - 14, cy - r, cx - 6, cy + r), -60, 60, fill=BLK, width=2); d.arc((cx + 6, cy - r, cx + r + 14, cy + r), 120, 240, fill=BLK, width=2)
    frame(d); return im

@reg(SPORT, 'american-football')
def gridiron():
    im, d = canvas(); floor(im, d)
    d.ellipse((14, 18, 82, 46), fill=BLK)
    d.polygon([(10, 32), (16, 26), (16, 38)], fill=BLK); d.polygon([(86, 32), (80, 26), (80, 38)], fill=BLK)
    d.line((32, 26, 64, 26), fill=WHT)
    for x in range(36, 62, 4): d.line((x, 23, x, 29), fill=WHT)
    for x in (22, 74): d.line((x, 21, x, 43), fill=WHT, width=2)
    frame(d); return im

@reg(SPORT, 'rugby-ball')
def rugby():
    im, d = canvas(); floor(im, d)
    d.ellipse((12, 14, 84, 50), fill=WHT, outline=BLK)
    shade(im, lambda dd: dd.ellipse((14, 16, 82, 48), fill=1), 6)
    d.arc((12, 20, 84, 44), 180, 360, fill=BLK); d.arc((12, 20, 84, 44), 0, 180, fill=BLK)
    d.line((12, 32, 84, 32), fill=BLK)
    for x in range(40, 58, 3): d.line((x, 28, x, 31), fill=BLK)
    frame(d); return im

@reg(SPORT, 'tennis-racket-and-ball')
def tennis():
    im, d = canvas(); floor(im, d)
    d.ellipse((14, 4, 50, 40), fill=WHT, outline=BLK); d.ellipse((15, 5, 49, 39), outline=BLK)
    for x in range(18, 48, 3): d.line((x, 6, x, 38), fill=BLK)
    for y in range(7, 38, 3): d.line((16, y, 48, y), fill=BLK)
    d.ellipse((16, 6, 48, 38), outline=BLK)
    d.polygon([(28, 40), (36, 40), (34, 46), (30, 46)], fill=BLK); d.rectangle((30, 46, 34, 60), fill=BLK)
    d.ellipse((64, 40, 80, 56), fill=WHT, outline=BLK); d.arc((58, 40, 72, 56), -60, 60, fill=BLK); d.arc((72, 40, 86, 56), 120, 240, fill=BLK)
    frame(d); return im

@reg(SPORT, 'cricket-bat-and-stumps')
def cricket():
    im, d = canvas(); floor(im, d)
    for x in (56, 64, 72): d.rectangle((x, 18, x + 2, 56), fill=BLK)
    d.rectangle((55, 16, 63, 17), fill=BLK); d.rectangle((65, 16, 73, 17), fill=BLK)
    d.polygon([(14, 54), (24, 22), (32, 24), (24, 56)], fill=BLK); d.polygon([(24, 22), (28, 8), (31, 9), (29, 23)], fill=BLK)
    for y in range(10, 20, 2): d.point((29, y), fill=WHT)
    d.ellipse((40, 44, 48, 52), fill=BLK); d.line((41, 48, 47, 48), fill=WHT)
    frame(d); return im

@reg(SPORT, 'ice-hockey-stick-and-puck')
def hockey():
    im, d = canvas(); floor(im, d, 52)
    d.line((60, 4, 34, 46), fill=BLK, width=4); d.polygon([(34, 44), (16, 50), (14, 46), (32, 41)], fill=BLK)
    for y in range(8, 18, 2): d.line((56 - (y - 8) * 0.6, y, 60 - (y - 8) * 0.6, y), fill=WHT)
    d.ellipse((60, 46, 78, 54), fill=BLK); d.rectangle((60, 48, 78, 50), fill=BLK); d.ellipse((60, 44, 78, 52), fill=BLK); d.arc((60, 44, 78, 52), 180, 360, fill=WHT)
    frame(d); return im

@reg(SPORT, 'golf-ball-on-tee')
def golf():
    im, d = canvas(); fill_pattern(im, (1, 46, W - 1, H - 1), 5); d.line((1, 46, W - 2, 46), fill=BLK)
    d.ellipse((34, 8, 62, 36), fill=WHT, outline=BLK)
    for y in range(12, 34, 4):
        for x in range(38 + (y % 8) // 2, 60, 4):
            if (x - 48) ** 2 + (y - 22) ** 2 < 150: d.point((x, y), fill=BLK)
    d.polygon([(40, 36), (56, 36), (50, 40), (46, 40)], fill=BLK); d.rectangle((46, 40, 50, 58), fill=BLK)
    d.line((70, 4, 80, 50), fill=BLK, width=2); d.polygon([(78, 48), (92, 50), (92, 54), (80, 54)], fill=BLK)   # club
    frame(d); return im

@reg(SPORT, 'badminton-shuttlecock')
def shuttle():
    im, d = canvas(); floor(im, d)
    d.chord((38, 40, 58, 58), 0, 180, fill=BLK); d.rectangle((38, 46, 58, 49), fill=BLK)
    d.polygon([(38, 46), (24, 6), (72, 6), (58, 46)], fill=WHT, outline=BLK)
    for i in range(9): d.line((40 + i * 2, 46, 26 + i * 5.5, 6), fill=BLK)
    d.line((30, 20, 66, 20), fill=BLK); d.line((33, 30, 63, 30), fill=BLK)
    frame(d); return im

@reg(SPORT, 'baseball-and-bat')
def baseball():
    im, d = canvas(); floor(im, d)
    d.polygon([(12, 52), (14, 54), (66, 14), (62, 10)], fill=BLK); d.ellipse((58, 6, 70, 18), fill=BLK); d.ellipse((9, 51, 15, 57), fill=BLK)
    d.ellipse((60, 34, 84, 58), fill=WHT, outline=BLK)
    d.arc((52, 34, 70, 58), -50, 50, fill=BLK); d.arc((74, 34, 92, 58), 130, 230, fill=BLK)
    for y in range(38, 56, 3): d.point((67, y), fill=BLK); d.point((77, y), fill=BLK)
    frame(d); return im

@reg(SPORT, 'curling-stone')
def curling():
    im, d = canvas(); fill_pattern(im, (1, 46, W - 1, H - 1), 6); d.line((1, 46, W - 2, 46), fill=BLK)
    d.ellipse((20, 30, 76, 56), fill=WHT, outline=BLK); d.rectangle((20, 38, 76, 46), fill=WHT); d.line((20, 38, 20, 46), fill=BLK); d.line((76, 38, 76, 46), fill=BLK)
    d.ellipse((20, 24, 76, 50), fill=WHT, outline=BLK); shade(im, lambda dd: dd.ellipse((22, 38, 74, 54), fill=1), 2)
    d.ellipse((30, 28, 66, 44), fill=BLK)
    d.rectangle((40, 18, 46, 36), fill=BLK); d.rectangle((40, 18, 74, 23), fill=BLK)
    frame(d); return im

@reg(SPORT, 'bowling-pin-and-ball')
def bowling():
    im, d = canvas(); floor(im, d)
    pts = []
    for i in range(31):
        t = i / 30; y = 6 + 50 * t
        w = 4 + 3 * math.sin(math.pi * min(1, t / 0.25)) if t < 0.25 else (2.5 if t < 0.35 else 3 + 7 * math.sin(math.pi * (t - 0.35) / 0.9))
        pts.append((30 - w, y))
    d.polygon(pts + [(60 - x, y) for x, y in reversed(pts)], fill=WHT, outline=BLK)
    d.rectangle((26, 20, 34, 21), fill=BLK); d.rectangle((26, 23, 34, 24), fill=BLK)
    d.ellipse((50, 26, 82, 58), fill=BLK); d.ellipse((60, 32, 63, 35), fill=WHT); d.ellipse((66, 31, 69, 34), fill=WHT); d.ellipse((62, 38, 66, 42), fill=WHT)
    frame(d); return im

# ================================================================== INSTRUMENTS
@reg(INST, 'violin')
def violin():
    im, d = canvas()
    body = Image.new('1', (W, H), 0); bd = ImageDraw.Draw(body)
    bd.ellipse((30, 30, 62, 58), fill=1); bd.ellipse((33, 12, 59, 36), fill=1); bd.rectangle((38, 28, 54, 38), fill=1)
    bd.ellipse((26, 26, 38, 40), fill=0); bd.ellipse((54, 26, 66, 40), fill=0)
    d.bitmap((0, 0), body, fill=BLK); shade(im, lambda dd: dd.bitmap((0, 0), body, fill=1), 3)
    d.rectangle((44, 0, 48, 30), fill=BLK); d.ellipse((42, 0, 50, 6), fill=BLK)
    for x in (38, 54): d.arc((x - 3, 34, x + 3, 46), 270, 90 if x < 48 else 270, fill=WHT); d.point((x, 34), fill=WHT); d.point((x, 46), fill=WHT)
    d.rectangle((41, 48, 51, 50), fill=WHT)
    for x in (45, 47): d.line((x, 4, x, 50), fill=WHT)
    d.line((70, 6, 22, 60), fill=BLK, width=1); d.line((71, 7, 23, 61), fill=BLK)   # bow
    frame(d); return im

@reg(INST, 'acoustic-guitar')
def guitar():
    im, d = canvas()
    d.ellipse((8, 28, 40, 58), fill=BLK); d.ellipse((24, 22, 50, 50), fill=BLK)
    d.ellipse((26, 32, 36, 42), fill=WHT); d.ellipse((28, 34, 34, 40), fill=BLK)
    d.polygon([(40, 34), (86, 12), (88, 16), (42, 38)], fill=BLK); d.polygon([(84, 10), (94, 6), (95, 12), (88, 17)], fill=BLK)
    for t in range(3): d.line((14, 46 + t, 88, 12 + t), fill=WHT) if False else None
    for k in range(3): d.line((20, 44 + k, 86, 14 + k), fill=WHT)
    d.rectangle((14, 42, 18, 50), fill=WHT); d.rectangle((15, 43, 17, 49), fill=BLK)
    frame(d); return im

@reg(INST, 'piano-keyboard')
def piano():
    im, d = canvas()
    d.rectangle((1, 1, W - 2, 10), fill=BLK)
    for x in range(1, W - 1, 7): d.rectangle((x, 10, x + 7, 62), outline=BLK, fill=WHT)
    pattern = [1, 1, 0, 1, 1, 1, 0]
    for i, k in enumerate(pattern * 2):
        if k: x = 1 + (i + 1) * 7 - 2; d.rectangle((x, 10, x + 4, 40), fill=BLK)
    frame(d); return im

@reg(INST, 'trumpet')
def trumpet():
    im, d = canvas()
    d.polygon([(64, 24), (90, 12), (90, 44), (64, 32)], fill=BLK); d.ellipse((86, 12, 92, 44), fill=BLK)
    d.rectangle((12, 25, 64, 31), fill=BLK); d.rectangle((14, 26, 62, 30), fill=WHT); d.line((12, 28, 64, 28), fill=BLK, width=2)
    d.rounded_rectangle((20, 30, 62, 44), 6, outline=BLK, width=2)
    for x in (34, 41, 48): d.rectangle((x, 18, x + 4, 40), fill=BLK); d.rectangle((x - 1, 14, x + 5, 18), fill=BLK)
    d.rectangle((4, 26, 12, 30), fill=BLK); d.ellipse((2, 24, 6, 32), fill=BLK)
    frame(d); return im

@reg(INST, 'saxophone')
def sax():
    im, d = canvas()
    d.line((40, 4, 46, 10), fill=BLK, width=3); d.polygon([(44, 8), (50, 8), (50, 44), (44, 44)], fill=BLK)
    d.chord((44, 34, 70, 60), 0, 180, fill=BLK); d.polygon([(60, 48), (70, 48), (78, 22), (66, 22)], fill=BLK)
    d.polygon([(64, 24), (80, 24), (84, 16), (62, 16)], fill=BLK)
    for y in range(14, 42, 5): d.ellipse((50, y, 54, y + 3), fill=BLK); d.point((52, y + 1), fill=WHT)
    d.line((34, 2, 40, 6), fill=BLK, width=2)
    frame(d); return im

@reg(INST, 'harp')
def harp():
    im, d = canvas(); floor(im, d, 60)
    d.polygon([(20, 60), (26, 60), (32, 8), (26, 6)], fill=BLK)                       # pillar
    d.line((28, 8, 78, 26), fill=BLK, width=3); d.line((78, 26, 84, 58), fill=BLK, width=1)
    d.polygon([(76, 24), (86, 56), (82, 60), (72, 28)], fill=BLK)                     # soundboard
    d.chord((22, 2, 34, 12), 180, 360, fill=BLK)
    for i in range(12):
        x = 32 + i * 4; y = 10 + i * 1.4; d.line((x, y, x + 4 * (1 - i / 12) + 40 - x + i * 0.3 if False else x + (76 - x) * 0.0, 58 - i * 2.4), fill=BLK)
    frame(d); return im

@reg(INST, 'drum-kit')
def drums():
    im, d = canvas(); floor(im, d, 60)
    d.ellipse((30, 30, 62, 62), fill=WHT, outline=BLK); d.ellipse((34, 34, 58, 58), outline=BLK)
    d.ellipse((42, 42, 50, 50), fill=BLK)
    for x0 in (26, 52): d.rectangle((x0, 20, x0 + 14, 30), fill=WHT, outline=BLK); d.ellipse((x0, 17, x0 + 14, 23), fill=WHT, outline=BLK)
    d.rectangle((70, 40, 88, 58), fill=WHT, outline=BLK); d.ellipse((70, 36, 88, 44), fill=WHT, outline=BLK)
    d.rectangle((6, 38, 22, 46), fill=WHT, outline=BLK); d.ellipse((6, 34, 22, 40), fill=WHT, outline=BLK); d.line((14, 46, 14, 60), fill=BLK)
    for x, y in ((14, 12), (82, 16)):
        d.line((x, y, x, 60), fill=BLK); d.ellipse((x - 10, y - 2, x + 10, y + 2), fill=BLK)
    d.line((40, 6, 52, 18), fill=BLK); d.line((58, 4, 54, 18), fill=BLK)
    frame(d); return im

@reg(INST, 'accordion')
def accordion():
    im, d = canvas()
    d.rectangle((8, 12, 26, 56), fill=WHT, outline=BLK); d.rectangle((70, 12, 88, 56), fill=WHT, outline=BLK)
    for y in range(16, 54, 4): d.rectangle((10, y, 20, y + 2), fill=BLK)
    for y in range(16, 54, 5):
        for x in (74, 80): d.ellipse((x, y, x + 3, y + 3), fill=BLK)
    pts = []
    for i in range(12):
        x = 26 + i * 4; pts += [(x, 12 if i % 2 == 0 else 8), (x, 56 if i % 2 == 0 else 60)]
    for i in range(11):
        x = 26 + i * 4; y0, y1 = (12, 8) if i % 2 == 0 else (8, 12)
        d.line((x, y0, x + 4, y1), fill=BLK); d.line((x, 56 if i % 2 == 0 else 60, x + 4, 60 if i % 2 == 0 else 56), fill=BLK)
        d.line((x, y0, x, 56 if i % 2 == 0 else 60), fill=BLK)
    fill_pattern(im, (27, 14, 69, 54), 4)
    frame(d); return im

@reg(INST, 'bagpipes')
def bagpipes():
    im, d = canvas()
    d.ellipse((24, 26, 66, 56), fill=BLK); shade(im, lambda dd: dd.ellipse((26, 28, 64, 54), fill=1), 2)
    for k in range(3): d.line((32 + k * 3, 30, 30 + k * 10, 30 - 26 + k * 2), fill=BLK, width=2)
    d.line((30, 30, 18, 4), fill=BLK, width=3); d.line((36, 30, 34, 8), fill=BLK, width=2); d.line((42, 30, 48, 10), fill=BLK, width=2)
    for x, y in ((18, 4), (34, 8), (48, 10)): d.rectangle((x - 2, y - 2, x + 2, y), fill=BLK)
    d.line((60, 52, 68, 62), fill=BLK, width=3)                                         # chanter
    d.line((62, 30, 82, 18), fill=BLK, width=2)                                         # blowpipe
    for i in range(4): d.line((24 + i * 2, 40, 18 + i * 4, 48), fill=BLK)               # tassels
    frame(d); return im

@reg(INST, 'sitar')
def sitar():
    im, d = canvas()
    d.ellipse((8, 34, 36, 60), fill=BLK); shade(im, lambda dd: dd.ellipse((10, 36, 34, 58), fill=1), 2)
    d.polygon([(28, 40), (88, 8), (90, 12), (32, 44)], fill=BLK)
    for i in range(6): x = 40 + i * 8; d.line((x, 36 - i * 4.5, x + 2, 39 - i * 4.5), fill=WHT)   # frets
    d.ellipse((72, 4, 84, 16), fill=BLK)                                                # upper gourd
    for k in range(2): d.line((22, 46 + k, 90, 10 + k), fill=WHT)
    frame(d); return im

# ================================================================== ANIMALS (silhouettes)
def scene(level=6, y=56):
    im, d = canvas(); d.line((1, y, W - 2, y), fill=BLK); fill_pattern(im, (1, y + 1, W - 1, H - 1), level); return im, d

@reg(ANIM, 'elephant')
def elephant():
    im, d = scene()
    d.ellipse((24, 18, 70, 46), fill=BLK)
    for x in (28, 38, 54, 62): d.rectangle((x, 38, x + 6, 56), fill=BLK)
    d.ellipse((60, 12, 82, 34), fill=BLK); d.polygon([(76, 26), (84, 30), (86, 52), (90, 54), (90, 56), (82, 52), (78, 34)], fill=BLK)   # head + trunk
    d.ellipse((56, 14, 70, 34), fill=BLK); d.arc((56, 14, 70, 34), 90, 270, fill=WHT)   # ear
    d.polygon([(78, 30), (86, 32), (78, 33)], fill=WHT)                                   # tusk
    d.point((72, 20), fill=WHT); d.line((24, 26, 20, 38), fill=BLK)
    frame(d); return im

@reg(ANIM, 'giraffe')
def giraffe():
    im, d = scene()
    d.ellipse((20, 26, 54, 42), fill=BLK)
    for x in (22, 28, 44, 50): d.rectangle((x, 36, x + 3, 56), fill=BLK)
    d.polygon([(42, 30), (52, 28), (66, 8), (60, 6)], fill=BLK)                        # thick neck
    d.polygon([(58, 2), (64, 2), (76, 8), (76, 11), (66, 12), (60, 8)], fill=BLK)       # head
    d.line((60, 2, 59, -1), fill=BLK); d.line((63, 2, 63, -1), fill=BLK)               # ossicones
    for x, y in ((28, 31), (36, 30), (44, 34), (32, 37), (50, 25), (55, 18), (59, 12)): d.ellipse((x - 2, y - 1, x + 1, y + 1), fill=WHT)
    d.line((20, 30, 16, 42), fill=BLK)
    d.ellipse((82, 24, 94, 34), fill=BLK); d.rectangle((86, 32, 88, 56), fill=BLK); d.rectangle((80, 22, 95, 27), fill=BLK)
    frame(d); return im

@reg(ANIM, 'kangaroo')
def kangaroo():
    im, d = scene(1)
    d.ellipse((34, 24, 58, 52), fill=BLK)
    d.polygon([(48, 28), (54, 14), (60, 14), (58, 30)], fill=BLK)                       # neck
    d.polygon([(52, 14), (58, 8), (72, 12), (72, 15), (58, 18)], fill=BLK)              # long snout head
    d.polygon([(54, 10), (52, 0), (57, 8)], fill=BLK); d.polygon([(57, 9), (57, 0), (60, 8)], fill=BLK)   # tall ears
    d.point((62, 11), fill=WHT)
    d.polygon([(38, 46), (8, 58), (14, 58), (42, 50)], fill=BLK)                        # tail
    d.polygon([(46, 48), (54, 56), (72, 56), (72, 54), (58, 52), (54, 44)], fill=BLK)   # big hind foot
    d.line((56, 28, 62, 36), fill=BLK, width=2)
    frame(d); return im

@reg(ANIM, 'emperor-penguin')
def penguin():
    im, d = scene(6, 54)
    d.ellipse((34, 12, 62, 56), fill=BLK); d.ellipse((40, 22, 58, 54), fill=WHT)
    d.ellipse((38, 2, 56, 18), fill=BLK); d.polygon([(54, 10), (62, 12), (54, 13)], fill=BLK)
    d.ellipse((48, 10, 52, 16), fill=WHT); d.point((50, 9), fill=BLK)
    d.polygon([(36, 22), (30, 40), (36, 38)], fill=BLK)
    d.polygon([(40, 54), (48, 54), (44, 57)], fill=BLK); d.polygon([(50, 54), (58, 54), (54, 57)], fill=BLK)
    frame(d); return im

@reg(ANIM, 'camel')
def camel():
    im, d = scene(1)
    d.ellipse((28, 24, 62, 40), fill=BLK); d.ellipse((32, 16, 44, 32), fill=BLK); d.ellipse((46, 16, 58, 32), fill=BLK)
    for x in (32, 38, 52, 58): d.line((x, 36, x, 56), fill=BLK, width=3)
    d.polygon([(58, 30), (68, 18), (70, 10), (78, 10), (80, 14), (72, 14), (70, 22), (62, 34)], fill=BLK)
    d.line((28, 28, 24, 38), fill=BLK)
    sun(im, d, 16, 10, 5)
    frame(d); return im

@reg(ANIM, 'flamingo')
def flamingo():
    im, d = scene(5, 52)
    d.ellipse((30, 22, 58, 36), fill=BLK); d.polygon([(30, 28), (20, 26), (30, 32)], fill=BLK)
    pts = [(54, 26), (60, 20), (62, 14), (58, 8), (56, 4), (60, 1), (66, 2)]           # S-curved neck
    d.line(pts, fill=BLK, width=3)
    d.ellipse((62, 0, 68, 5), fill=BLK); d.polygon([(67, 2), (72, 6), (70, 9), (66, 5)], fill=BLK)   # bent beak
    d.line((44, 36, 44, 58), fill=BLK); d.line((46, 36, 50, 44), fill=BLK); d.line((50, 44, 45, 46), fill=BLK)
    frame(d); return im

@reg(ANIM, 'rhinoceros')
def rhino():
    im, d = scene()
    d.ellipse((20, 22, 66, 48), fill=BLK)
    for x in (24, 32, 52, 58): d.rectangle((x, 40, x + 7, 56), fill=BLK)
    d.polygon([(60, 26), (84, 34), (86, 44), (64, 44)], fill=BLK)
    d.polygon([(78, 34), (84, 20), (84, 34)], fill=BLK); d.polygon([(72, 32), (74, 26), (76, 32)], fill=BLK)
    d.polygon([(62, 24), (64, 18), (66, 24)], fill=BLK); d.point((72, 36), fill=WHT)
    frame(d); return im

@reg(ANIM, 'crocodile')
def croc():
    im, d = canvas(); water(im, 40)
    d.polygon([(4, 40), (20, 34), (60, 32), (78, 34), (94, 36), (94, 39), (78, 40), (60, 42), (20, 42)], fill=BLK)
    for x in range(20, 60, 4): d.polygon([(x, 33), (x + 2, 30), (x + 4, 33)], fill=BLK)
    d.ellipse((66, 30, 72, 35), fill=BLK); d.point((69, 32), fill=WHT)
    for x in range(78, 94, 3): d.point((x, 39), fill=WHT)
    frame(d); return im

@reg(ANIM, 'great-white-shark')
def shark():
    im, d = canvas(); water(im, 4, 62)
    d.polygon([(4, 30), (14, 26), (40, 22), (70, 24), (88, 30), (70, 36), (40, 38), (14, 34)], fill=BLK)
    d.polygon([(42, 22), (48, 6), (54, 23)], fill=BLK)                                # dorsal fin
    d.polygon([(4, 30), (0, 18), (10, 28)], fill=BLK); d.polygon([(4, 30), (0, 42), (10, 32)], fill=BLK)   # tail
    d.polygon([(52, 36), (46, 48), (58, 37)], fill=BLK)                               # pectoral fin
    d.point((78, 28), fill=WHT); d.line((76, 33, 86, 31), fill=WHT)
    for x in (66, 68, 70): d.line((x, 26, x - 1, 33), fill=WHT)
    frame(d); return im

@reg(ANIM, 'humpback-whale')
def whale():
    im, d = canvas(); water(im, 36)
    d.polygon([(20, 50), (30, 30), (44, 22), (70, 24), (86, 34), (82, 44), (60, 50)], fill=BLK)
    d.polygon([(62, 48), (40, 62), (50, 62), (70, 48)], fill=BLK)                     # long pectoral fin
    for y in range(36, 48, 3): d.line((68, y, 84, y - 2), fill=WHT)                    # throat grooves
    d.point((72, 30), fill=WHT)
    d.polygon([(20, 50), (8, 40), (6, 44), (14, 52), (6, 60), (10, 62), (22, 54)], fill=BLK)   # fluke
    for x, y in ((46, 8), (50, 4), (54, 8)): d.line((50, 20, x, y), fill=BLK)            # blow
    frame(d); return im

@reg(ANIM, 'tyrannosaurus-rex')
def trex():
    im, d = scene()
    d.polygon([(10, 26), (30, 24), (50, 20), (60, 18), (56, 30), (48, 40), (30, 36)], fill=BLK)    # body + tail
    d.polygon([(56, 18), (64, 8), (82, 8), (86, 14), (84, 18), (74, 18), (72, 22), (62, 24)], fill=BLK)   # head
    for x in range(74, 84, 2): d.point((x, 18), fill=WHT)
    d.point((70, 11), fill=WHT)
    d.line((60, 26, 66, 30), fill=BLK, width=2)                                         # tiny arm
    d.polygon([(44, 36), (40, 48), (34, 56), (42, 56), (46, 48), (50, 38)], fill=BLK)
    d.polygon([(52, 32), (56, 46), (54, 56), (62, 56), (60, 46), (58, 30)], fill=BLK)
    frame(d); return im

@reg(ANIM, 'stegosaurus')
def stego():
    im, d = scene()
    d.polygon([(4, 44), (20, 36), (40, 26), (60, 28), (76, 38), (88, 44), (84, 46), (70, 44), (40, 44)], fill=BLK)
    d.ellipse((82, 40, 94, 48), fill=BLK)
    for i, (x, h) in enumerate(((24, 8), (32, 12), (40, 14), (48, 14), (56, 12), (64, 9))):
        d.polygon([(x - 4, 32 - (i < 3) * 2), (x, 32 - h - (i < 3) * 2 - 4), (x + 4, 30)], fill=BLK)
    for x in (4, 8): d.line((x, 42, x - 4, 36), fill=BLK, width=2)                       # tail spikes
    for x in (30, 40, 60, 70): d.rectangle((x, 42, x + 5, 56), fill=BLK)
    frame(d); return im

@reg(ANIM, 'koala')
def koala():
    im, d = canvas()
    d.line((70, 0, 62, 64), fill=BLK, width=6)                                          # eucalyptus trunk
    for y, x in ((10, 88), (30, 90), (50, 86)): d.ellipse((x - 8, y - 3, x, y + 3), outline=BLK); d.line((x - 4, y, 68, y + 4), fill=BLK)
    d.ellipse((36, 26, 64, 58), fill=BLK); shade(im, lambda dd: dd.ellipse((40, 30, 60, 54), fill=1), 3)
    d.ellipse((30, 6, 58, 30), fill=BLK)
    d.ellipse((24, 4, 36, 16), fill=BLK); d.ellipse((52, 4, 64, 16), fill=BLK)
    d.ellipse((26, 6, 34, 14), fill=WHT); d.ellipse((54, 6, 62, 14), fill=WHT)
    d.ellipse((40, 16, 48, 26), fill=WHT); d.ellipse((41, 17, 47, 25), fill=BLK)        # big nose
    d.point((37, 16), fill=WHT); d.point((51, 16), fill=WHT)
    frame(d); return im

@reg(ANIM, 'bald-eagle')
def eagle():
    im, d = canvas(); clouds(d, [(6, 50), (70, 54)])
    # soaring, seen from below: broad wings with fingered tips
    d.polygon([(44, 22), (6, 18), (2, 24), (8, 25), (3, 29), (10, 29), (6, 33), (16, 32), (44, 32)], fill=BLK)
    d.polygon([(52, 22), (90, 18), (94, 24), (88, 25), (93, 29), (86, 29), (90, 33), (80, 32), (52, 32)], fill=BLK)
    d.ellipse((42, 18, 54, 40), fill=BLK)
    d.ellipse((43, 9, 53, 20), fill=WHT, outline=BLK); d.polygon([(46, 9), (48, 5), (50, 9)], fill=BLK)   # white head, hooked beak
    d.polygon([(43, 38), (53, 38), (56, 48), (40, 48)], fill=WHT, outline=BLK)          # white fan tail
    frame(d); return im

# ================================================================== FAMOUS PAINTINGS (public domain), 1-bit homages
def gilt(d):
    d.rectangle((0, 0, W - 1, H - 1), outline=BLK); d.rectangle((2, 2, W - 3, H - 3), outline=BLK)

@reg(ART, 'the-starry-night-van-gogh')
def starry():
    im, d = canvas(BLK)
    for cx, cy, r in ((20, 12, 4), (36, 8, 3), (58, 14, 3), (74, 8, 4), (86, 20, 5)):
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=WHT)
        for rr in (r + 2, r + 4): d.arc((cx - rr, cy - rr, cx + rr, cy + rr), 0, 300, fill=WHT)
    for k in range(3): d.arc((28 + k * 4, 18 + k * 2, 70 - k * 4, 36 - k * 2), 160, 380, fill=WHT)     # the great swirl
    d.ellipse((84, 4, 92, 12), fill=WHT); d.ellipse((86, 4, 94, 12), fill=BLK)                      # crescent moon
    for x in range(30, 92, 6):                                                                       # village
        y = 50 + (x % 12) // 4
        d.rectangle((x, y, x + 4, 60), fill=WHT); d.polygon([(x - 1, y), (x + 2, y - 3), (x + 5, y)], fill=WHT); d.point((x + 2, y + 3), fill=BLK)
    d.polygon([(62, 50), (64, 38), (66, 50)], fill=WHT)                                              # church spire
    d.line((4, 46, 92, 42), fill=WHT); d.arc((10, 40, 90, 56), 190, 350, fill=WHT)                  # hills
    d.polygon([(8, 62), (12, 30), (14, 10), (18, 30), (24, 62)], fill=WHT)                          # cypress
    d.polygon([(12, 62), (14, 34), (15, 16), (18, 34), (20, 62)], fill=BLK)
    for y in range(18, 60, 3): d.line((13, y, 18, y - 2), fill=WHT)
    gilt(d); return im

@reg(ART, 'the-scream-munch')
def scream():
    im, d = canvas()
    for k in range(6): d.arc((-20, -6 + k * 5, 116, 30 + k * 5), 190, 350, fill=BLK)               # swirling sky bands
    fill_pattern(im, (1, 1, W - 1, 14), 6)
    d.polygon([(1, 64), (96, 22), (96, 30), (1, 64)], fill=BLK)                                    # bridge railing (diagonal)
    for x in range(10, 96, 8): d.line((x, 64 - x * 0.44, x, 64 - x * 0.44 - 6), fill=BLK)
    d.line((1, 50, 96, 18), fill=BLK)
    d.line((70, 30, 74, 18), fill=BLK, width=2); d.line((78, 28, 80, 18), fill=BLK, width=2)       # two distant figures
    # the screaming figure
    d.polygon([(26, 64), (30, 44), (34, 38), (44, 38), (48, 44), (46, 64)], fill=BLK)
    d.ellipse((28, 12, 48, 38), fill=WHT, outline=BLK)
    d.ellipse((32, 20, 36, 26), fill=BLK); d.ellipse((40, 20, 44, 26), fill=BLK); d.ellipse((35, 28, 41, 35), fill=BLK)
    d.polygon([(28, 22), (22, 30), (24, 40), (30, 30)], fill=BLK); d.polygon([(48, 22), (54, 30), (52, 40), (46, 30)], fill=BLK)   # hands on face
    gilt(d); return im

@reg(ART, 'the-great-wave-hokusai')
def wave():
    im, d = canvas()
    fill_pattern(im, (1, 1, W - 1, 30), 6)
    d.polygon([(56, 50), (66, 38), (70, 38), (80, 50)], fill=BLK); d.polygon([(64, 41), (66, 38), (70, 38), (72, 41)], fill=WHT)   # Fuji, small
    pts = [(0, 64), (0, 40)] + [(10 + 30 * math.sin(a / 20 * math.pi) + a, 40 - 30 * math.sin(a / 20 * math.pi)) for a in range(0, 21)] + [(50, 30), (46, 20), (40, 14), (34, 16), (40, 22), (36, 30), (44, 40), (60, 64)]
    d.polygon([(0, 64), (0, 44), (8, 30), (20, 12), (34, 4), (48, 6), (56, 14), (52, 12), (44, 12), (38, 18), (42, 26), (36, 30), (30, 26), (28, 36), (40, 48), (56, 64)], fill=BLK)
    for x, y in ((50, 8), (54, 12), (46, 10), (40, 16), (44, 20), (36, 26)):                        # claw-like foam
        d.ellipse((x - 1, y - 1, x + 1, y + 1), fill=WHT)
    for k in range(4): d.arc((6 + k * 4, 14 + k * 5, 60 - k * 4, 70), 200, 300, fill=WHT)
    d.polygon([(48, 54), (90, 48), (92, 52), (50, 58)], fill=BLK)                                  # boat
    for x in range(56, 88, 5): d.ellipse((x, 49 - (x - 56) // 8, x + 2, 51 - (x - 56) // 8), fill=WHT)
    for x in range(64, 96, 6): d.arc((x, 56, x + 12, 66), 180, 360, fill=BLK)
    gilt(d); return im

@reg(ART, 'mona-lisa-da-vinci')
def mona():
    im, d = canvas()
    fill_pattern(im, (1, 1, W - 1, 40), 6)
    d.line((20, 30, 34, 26), fill=BLK); d.line((62, 26, 80, 30), fill=BLK)                       # landscape horizon
    d.arc((60, 30, 90, 46), 180, 270, fill=BLK)
    # figure
    d.polygon([(28, 64), (32, 44), (40, 36), (56, 36), (64, 44), (68, 64)], fill=BLK)
    d.ellipse((38, 8, 58, 34), fill=BLK)                                                         # hair + veil
    d.ellipse((41, 11, 55, 31), fill=WHT)                                                         # face
    d.point((45, 19), fill=BLK); d.point((51, 19), fill=BLK); d.line((48, 21, 48, 24), fill=BLK)
    d.arc((45, 22, 51, 28), 20, 160, fill=BLK)                                                    # the smile
    d.rectangle((44, 32, 52, 38), fill=WHT); d.chord((42, 34, 54, 42), 0, 180, fill=WHT)         # neck & neckline
    d.ellipse((38, 52, 58, 60), fill=WHT); d.line((44, 54, 52, 58), fill=BLK); d.line((40, 56, 56, 56), fill=BLK)   # folded hands
    gilt(d); return im

@reg({}, 'girl-with-a-pearl-earring-vermeer')
def pearl():
    im, d = canvas(BLK)
    d.polygon([(30, 64), (36, 46), (50, 42), (68, 48), (74, 64)], fill=WHT); fill_pattern(im, (30, 46, 74, 64), 5)
    d.ellipse((38, 14, 62, 44), fill=WHT)                                                        # face (turned)
    d.polygon([(34, 12), (54, 6), (64, 12), (60, 22), (38, 24)], fill=WHT); fill_pattern(im, (34, 6, 64, 24), 4)   # turban
    d.polygon([(50, 8), (58, 2), (56, 12)], fill=WHT); d.polygon([(56, 10), (58, 30), (54, 30)], fill=WHT)     # turban tail
    d.point((44, 26), fill=BLK); d.point((52, 26), fill=BLK); d.arc((44, 33, 52, 39), 20, 160, fill=BLK)
    d.ellipse((60, 34, 64, 38), fill=WHT); d.point((61, 35), fill=BLK)                           # the pearl
    gilt(d); return im

@reg(ART, 'american-gothic-grant-wood-1930')
def gothic():
    # Grant Wood's 1930 painting is public domain in the US only from 2026? — kept out of export by default
    return None

if __name__ == '__main__':
    for table, cat in ((SPORT, 'sports-gear'), (INST, 'instruments'), (ANIM, 'animals'), (ART, 'paintings')):
        for n, f in table.items():
            im = f()
            if im is not None: save(im, cat, n)
    for c in ('sports-gear', 'instruments', 'animals', 'paintings'): print(sheet(c, cols=6, scale_down=1))
