#!/usr/bin/env python3
"""Famous inventions and road signs & symbols in chunky NES-style 8-bit pixel art (48x32 cells shown at 2x),
matching paintings_nes.py."""
import sys, math
from PIL import Image, ImageDraw
from common import W, H, save
from paintings_nes import NES, K

CW, CH = W // 2, H // 2
C = dict(wht=(252, 252, 252), lgry=(188, 188, 188), gry=(124, 124, 124), dgry=(80, 80, 80), blk=K, red=(168, 16, 0), bred=(228, 0, 88),
         rd=(248, 56, 0), org=(228, 92, 16), yel=(248, 184, 0), lyel=(248, 216, 120), brn=(136, 20, 0), dbrn=(80, 48, 0), tan=(172, 124, 0),
         skin=(240, 208, 176), sky=(60, 188, 252), lsky=(164, 228, 252), blu=(0, 88, 248), dblu=(0, 0, 188), grn=(0, 168, 0), dgrn=(0, 104, 0),
         lgrn=(88, 216, 84), teal=(0, 64, 88), gold=(248, 184, 0), cream=(252, 224, 168))
C['dgry'] = (120, 120, 120)

def finish(g):
    big = g.resize((W, H), Image.NEAREST); ImageDraw.Draw(big).rectangle((0, 0, W - 1, H - 1), outline=K); return big

def museum():
    g = Image.new('RGB', (CW, CH), C['teal']); d = ImageDraw.Draw(g)
    d.rectangle((0, 26, CW, CH), fill=C['dbrn']); d.line((0, 26, CW, 26), fill=C['tan'])
    return g, d

def road():
    g = Image.new('RGB', (CW, CH), C['sky']); d = ImageDraw.Draw(g)
    for x, y in ((4, 4), (36, 6)):
        d.rectangle((x, y, x + 6, y + 1), fill=C['wht']); d.rectangle((x + 1, y - 1, x + 4, y - 1), fill=C['wht'])
    d.rectangle((0, 27, CW, CH), fill=C['grn']); d.line((0, 27, CW, 27), fill=C['lgrn'])
    return g, d

def pole(d, x=24, top=20, bot=29): d.rectangle((x - 1, top, x, bot), fill=C['gry']); d.line((x, top, x, bot), fill=C['lgry'])

def sign_plate(cx, cy, r, sides, rot=0):
    return [(cx + r * math.cos(math.radians(rot + 360 * i / sides)), cy + r * math.sin(math.radians(rot + 360 * i / sides))) for i in range(sides)]

REG = {}
def reg(cat, name):
    def f(fn): REG[name] = (cat, fn); return fn
    return f

# ================= Road signs & symbols =================
@reg('signs', 'stop-sign')
def stop():
    g, d = road(); pole(d)
    d.polygon(sign_plate(24, 12, 10.5, 8, 22.5), fill=C['wht']); d.polygon(sign_plate(24, 12, 9.5, 8, 22.5), fill=C['red'])
    # S T O P in 3x5 cell letters
    L = {'S': ['111', '100', '111', '001', '111'], 'T': ['111', '010', '010', '010', '010'], 'O': ['111', '101', '101', '101', '111'], 'P': ['111', '101', '111', '100', '100']}
    for i, ch in enumerate('STOP'):
        for yy, row in enumerate(L[ch]):
            for xx, v in enumerate(row):
                if v == '1': d.point((16 + i * 4 + xx, 10 + yy), fill=C['wht'])
    return finish(g)

@reg('signs', 'yield-sign')
def yield_():
    g, d = road(); pole(d, top=18)
    d.polygon([(12, 4), (36, 4), (24, 24)], fill=C['red']); d.polygon([(16, 6), (32, 6), (24, 19)], fill=C['wht'])
    return finish(g)

@reg('signs', 'no-entry-sign')
def no_entry():
    g, d = road(); pole(d)
    d.ellipse((14, 2, 34, 22), fill=C['wht']); d.ellipse((15, 3, 33, 21), fill=C['red']); d.rectangle((18, 10, 30, 14), fill=C['wht'])
    return finish(g)

@reg('signs', 'railway-crossing-sign')
def crossbuck():
    g, d = road(); pole(d, top=8)
    for a, b in (((13, 3), (35, 17)), ((35, 3), (13, 17))):
        d.line((*a, *b), fill=C['blk'], width=5); d.line((*a, *b), fill=C['wht'], width=3)
    d.line((15, 4, 33, 16), fill=C['blk']); d.line((33, 4, 15, 16), fill=C['blk'])
    for x, y, t in ((17, 8, 'R'), (31, 8, 'R')): pass
    d.rectangle((19, 20, 29, 23), fill=C['blk']); d.ellipse((18, 19, 22, 23), fill=C['rd']); d.ellipse((26, 19, 30, 23), fill=C['rd'])
    return finish(g)

@reg('signs', 'pedestrian-crossing-sign')
def ped():
    g, d = road(); pole(d)
    d.rectangle((13, 1, 35, 23), fill=C['blu']); d.polygon([(14, 22), (34, 22), (24, 3)], fill=C['wht'])
    d.rectangle((23, 7, 25, 9), fill=C['blk'])                                  # head
    d.line((24, 10, 23, 15), fill=C['blk'], width=2)                            # body
    d.line((23, 15, 20, 20), fill=C['blk'], width=1); d.line((23, 15, 27, 19), fill=C['blk'], width=1); d.line((27, 19, 28, 20), fill=C['blk'])
    d.line((24, 11, 21, 14), fill=C['blk']); d.line((24, 11, 27, 13), fill=C['blk'])
    for x in range(17, 32, 3): d.rectangle((x, 20, x + 1, 21), fill=C['blk'])   # zebra stripes
    return finish(g)

@reg('signs', 'roundabout-sign')
def roundabout():
    g, d = road(); pole(d)
    d.ellipse((14, 2, 34, 22), fill=C['wht']); d.ellipse((15, 3, 33, 21), fill=C['blu'])
    d.arc((18, 6, 30, 18), 200, 520, fill=C['wht'], width=2)
    for a in (90, 210, 330):
        x = 24 + 6 * math.cos(math.radians(a)); y = 12 + 6 * math.sin(math.radians(a))
        d.polygon([(x - 1.5, y - 1.5), (x + 1.5, y - 1.5), (x, y + 1.5)] if a == 90 else [(x - 1.5, y), (x + 1.5, y - 1.5), (x + 1.5, y + 1.5)] if a == 210 else [(x - 1.5, y - 1.5), (x - 1.5, y + 1.5), (x + 1.5, y)], fill=C['wht'])
    return finish(g)

@reg('signs', 'no-u-turn-sign')
def no_u():
    g, d = road(); pole(d)
    d.ellipse((14, 2, 34, 22), fill=C['red']); d.ellipse((16, 4, 32, 20), fill=C['wht'])
    d.line((21, 18, 21, 10), fill=C['blk'], width=2); d.arc((21, 6, 28, 14), 180, 360, fill=C['blk'], width=2); d.line((27, 10, 27, 13), fill=C['blk'], width=2)
    d.polygon([(25, 13), (30, 13), (27, 16)], fill=C['blk'])
    d.line((17, 19, 31, 5), fill=C['red'], width=2)
    return finish(g)

def warning(d, top=2):
    d.polygon([(24, top), (36, top + 21), (12, top + 21)], fill=C['red']); d.polygon([(24, top + 3), (33, top + 19), (15, top + 19)], fill=C['wht'])

@reg('signs', 'slippery-road-sign')
def slippery():
    g, d = road(); pole(d); warning(d)
    d.rectangle((21, 11, 27, 14), fill=C['blk']); d.point((22, 15), fill=C['blk']); d.point((26, 15), fill=C['blk'])
    d.line((19, 19, 21, 16), fill=C['blk']); d.line((21, 16, 23, 19), fill=C['blk']); d.line((25, 19, 27, 16), fill=C['blk']); d.line((27, 16, 29, 19), fill=C['blk'])
    return finish(g)

@reg('signs', 'deer-crossing-sign')
def deer():
    g, d = road(); pole(d)
    d.polygon([(24, 1), (36, 13), (24, 25), (12, 13)], fill=C['blk']); d.polygon([(24, 2), (35, 13), (24, 24), (13, 13)], fill=C['yel'])
    d.rectangle((20, 12, 27, 15), fill=C['blk']); d.line((21, 16, 19, 19), fill=C['blk']); d.line((26, 16, 28, 19), fill=C['blk'])
    d.line((27, 12, 29, 9), fill=C['blk']); d.rectangle((28, 8, 30, 10), fill=C['blk']); d.line((29, 7, 28, 5), fill=C['blk']); d.line((30, 7, 31, 5), fill=C['blk'])
    return finish(g)

@reg('signs', 'radiation-symbol')
def radiation():
    g, d = road(); pole(d)
    d.polygon([(24, 1), (37, 23), (11, 23)], fill=C['blk']); d.polygon([(24, 3), (35, 22), (13, 22)], fill=C['yel'])
    cx, cy = 24, 15
    for a in (90, 210, 330): d.pieslice((cx - 7, cy - 7, cx + 7, cy + 7), a - 30, a + 30, fill=C['blk'])
    d.ellipse((cx - 3, cy - 3, cx + 3, cy + 3), fill=C['yel']); d.ellipse((cx - 1.5, cy - 1.5, cx + 1.5, cy + 1.5), fill=C['blk'])
    return finish(g)

@reg('signs', 'biohazard-symbol')
def biohazard():
    g, d = road(); pole(d)
    d.polygon([(24, 1), (37, 23), (11, 23)], fill=C['blk']); d.polygon([(24, 3), (35, 22), (13, 22)], fill=C['yel'])
    cx, cy = 24, 15
    for a in (270, 30, 150):
        x = cx + 3.2 * math.cos(math.radians(a)); y = cy + 3.2 * math.sin(math.radians(a))
        d.ellipse((x - 3, y - 3, x + 3, y + 3), outline=C['blk'], width=2)
        x2 = cx + 4.6 * math.cos(math.radians(a)); y2 = cy + 4.6 * math.sin(math.radians(a)); d.ellipse((x2 - 1, y2 - 1, x2 + 1, y2 + 1), fill=C['yel'])
    d.ellipse((cx - 1, cy - 1, cx + 1, cy + 1), fill=C['yel'])
    return finish(g)

@reg('signs', 'high-voltage-sign')
def voltage():
    g, d = road(); pole(d)
    d.polygon([(24, 1), (37, 23), (11, 23)], fill=C['blk']); d.polygon([(24, 3), (35, 22), (13, 22)], fill=C['yel'])
    d.polygon([(25, 7), (21, 15), (24, 15), (22, 21), (28, 12), (25, 12), (27, 7)], fill=C['blk'])
    return finish(g)

@reg('signs', 'poison-symbol')
def poison():
    g, d = museum()
    d.rectangle((17, 5, 31, 25), fill=C['grn']); d.rectangle((20, 2, 28, 5), fill=C['dgrn']); d.rectangle((21, 0, 27, 2), fill=C['brn'])
    d.rectangle((18, 9, 30, 22), fill=C['cream'])
    d.ellipse((21, 10, 27, 16), fill=C['blk']); d.rectangle((22, 15, 26, 17), fill=C['blk'])
    d.point((23, 12), fill=C['cream']); d.point((25, 12), fill=C['cream']); d.point((23, 16), fill=C['cream']); d.point((25, 16), fill=C['cream'])
    d.line((19, 18, 29, 21), fill=C['blk']); d.line((29, 18, 19, 21), fill=C['blk'])
    return finish(g)

@reg('signs', 'recycling-symbol')
def recycle():
    g = Image.new('RGB', (CW, CH), C['wht']); d = ImageDraw.Draw(g)
    T = [(24, 3), (37, 26), (11, 26)]                                            # three chasing arrows around a triangle
    for k in range(3):
        p0, p1 = T[k], T[(k + 1) % 3]
        a = (p0[0] + (p1[0] - p0[0]) * 0.18, p0[1] + (p1[1] - p0[1]) * 0.18); b = (p0[0] + (p1[0] - p0[0]) * 0.70, p0[1] + (p1[1] - p0[1]) * 0.70)
        d.line((*a, *b), fill=C['grn'], width=3)
        ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0]); n = (-math.sin(ang), math.cos(ang))
        tip = (b[0] + 5 * math.cos(ang), b[1] + 5 * math.sin(ang))
        d.polygon([tip, (b[0] + 4 * n[0], b[1] + 4 * n[1]), (b[0] - 4 * n[0], b[1] - 4 * n[1])], fill=C['grn'])
    return finish(g)

@reg('signs', 'no-smoking-sign')
def no_smoking():
    g = Image.new('RGB', (CW, CH), C['wht']); d = ImageDraw.Draw(g)
    d.rectangle((14, 14, 32, 17), fill=C['blk']); d.rectangle((30, 14, 32, 17), fill=C['org'])
    d.line((33, 12, 34, 9), fill=C['lgry']); d.line((34, 9, 33, 6), fill=C['lgry'])
    d.ellipse((12, 4, 36, 28), outline=C['red'], width=3); d.line((15, 7, 33, 25), fill=C['red'], width=3)
    return finish(g)

@reg('signs', 'peace-symbol')
def peace():
    g = Image.new('RGB', (CW, CH), C['blu']); d = ImageDraw.Draw(g)
    d.ellipse((13, 5, 35, 27), outline=C['wht'], width=3)
    d.line((24, 6, 24, 26), fill=C['wht'], width=3); d.line((24, 16, 17, 23), fill=C['wht'], width=3); d.line((24, 16, 31, 23), fill=C['wht'], width=3)
    return finish(g)

@reg('signs', 'power-symbol')
def power():
    g = Image.new('RGB', (CW, CH), C['blk']); d = ImageDraw.Draw(g)
    d.arc((14, 6, 34, 26), -60, 240, fill=C['lgrn'], width=3); d.line((24, 3, 24, 15), fill=C['lgrn'], width=3)
    return finish(g)

@reg('signs', 'wheelchair-symbol')
def access():
    g = Image.new('RGB', (CW, CH), C['blu']); d = ImageDraw.Draw(g)
    d.ellipse((21, 4, 25, 8), fill=C['wht']); d.line((22, 9, 21, 17), fill=C['wht'], width=2); d.line((21, 17, 28, 17), fill=C['wht'], width=2)
    d.line((28, 17, 31, 24), fill=C['wht'], width=2); d.line((22, 12, 27, 12), fill=C['wht'], width=2)
    d.arc((13, 13, 27, 27), 100, 400, fill=C['wht'], width=2)
    return finish(g)

# ================= Famous inventions =================
@reg('inventions', 'enigma-machine')
def enigma():
    g, d = museum()
    d.rectangle((8, 6, 40, 27), fill=C['dbrn']); d.rectangle((9, 7, 39, 26), fill=C['brn']); d.rectangle((10, 8, 38, 25), fill=C['blk'])
    for i in range(3): d.rectangle((18 + i * 4, 9, 20 + i * 4, 11), fill=C['lgry'])       # rotors
    for row, n in enumerate((9, 8, 9)):
        for i in range(n): d.ellipse((12 + i * 3 + (row % 2), 13 + row * 2, 13 + i * 3 + (row % 2), 14 + row * 2), fill=C['lyel'])   # lamps
    for row, n in enumerate((9, 8, 9)):
        for i in range(n): d.point((12 + i * 3 + (row % 2), 20 + row * 2), fill=C['wht'])   # keys
    d.rectangle((10, 25, 38, 25), fill=C['gry'])
    return finish(g)

@reg('inventions', 'gramophone')
def gramophone():
    g, d = museum()
    d.rectangle((10, 18, 26, 26), fill=C['brn']); d.rectangle((10, 18, 26, 19), fill=C['tan'])
    d.ellipse((11, 16, 25, 19), fill=C['blk'])
    d.line((22, 17, 26, 12), fill=C['gold'], width=1)
    d.polygon([(26, 13), (40, 1), (44, 6), (45, 14), (42, 20), (28, 15)], fill=C['gold'])
    d.polygon([(28, 14), (40, 3), (43, 8), (43, 14), (40, 18)], fill=C['yel'])
    d.ellipse((38, 2, 46, 19), outline=C['tan'])
    return finish(g)

@reg('inventions', 'candlestick-telephone')
def candlestick():
    g, d = museum()
    d.ellipse((17, 22, 29, 27), fill=C['blk']); d.rectangle((22, 8, 24, 24), fill=C['blk'])
    d.polygon([(19, 4), (27, 4), (25, 8), (21, 8)], fill=C['blk']); d.ellipse((20, 3, 26, 5), fill=C['gry'])
    d.line((24, 12, 31, 12), fill=C['gry']); d.rectangle((31, 10, 34, 13), fill=C['blk']); d.rectangle((31, 13, 33, 20), fill=C['blk'])
    d.line((29, 24, 36, 26), fill=C['blk'])
    return finish(g)

@reg('inventions', 'rotary-phone')
def rotary():
    g, d = museum()
    d.polygon([(10, 26), (38, 26), (34, 13), (14, 13)], fill=C['red']); d.rectangle((14, 13, 34, 15), fill=C['bred'])
    d.ellipse((17, 15, 31, 26), fill=C['wht']); d.ellipse((22, 18, 26, 22), fill=C['red'])
    for k in range(10):
        a = math.radians(200 + k * 26); d.point((24 + 5 * math.cos(a), 20.5 + 4 * math.sin(a)), fill=C['blk'])
    d.rectangle((9, 8, 39, 11), fill=C['red']); d.ellipse((7, 7, 14, 14), fill=C['red']); d.ellipse((34, 7, 41, 14), fill=C['red'])
    return finish(g)

@reg('inventions', 'model-t-ford')
def model_t():
    g, d = road()
    d.rectangle((0, 25, CW, 27), fill=C['gry'])
    d.rectangle((12, 15, 34, 21), fill=C['blk']); d.rectangle((30, 16, 40, 21), fill=C['blk'])             # body, bonnet
    d.rectangle((14, 6, 28, 7), fill=C['blk']); d.line((14, 7, 14, 15), fill=C['blk']); d.line((28, 7, 28, 15), fill=C['blk']); d.line((22, 7, 22, 15), fill=C['blk'])   # roof and pillars
    d.line((29, 9, 30, 15), fill=C['lsky']); d.line((30, 9, 31, 15), fill=C['blk'])
    d.rectangle((40, 17, 41, 21), fill=C['gold'])
    for cx in (16, 36): d.ellipse((cx - 4, 18, cx + 4, 26), fill=C['blk']); d.ellipse((cx - 2, 20, cx + 2, 24), fill=C['lgry']); d.point((cx, 22), fill=C['blk'])
    d.line((8, 21, 12, 21), fill=C['blk'])
    return finish(g)

@reg('inventions', 'typewriter')
def typewriter():
    g, d = museum()
    d.polygon([(8, 26), (40, 26), (36, 15), (12, 15)], fill=C['blk'])
    d.rectangle((10, 8, 38, 11), fill=C['blk']); d.rectangle((6, 9, 9, 10), fill=C['lgry']); d.rectangle((16, 3, 32, 9), fill=C['wht'])   # platen, paper
    for i in range(4): d.line((18, 4 + i, 30 - (i % 2) * 4, 4 + i), fill=C['lgry'])
    for row in range(3):
        for i in range(8 - row % 2): d.ellipse((13 + i * 3 + row, 17 + row * 3, 14 + i * 3 + row, 18 + row * 3), fill=C['wht'])
    d.rectangle((18, 24, 30, 25), fill=C['lgry'])
    return finish(g)

@reg('inventions', 'light-bulb')
def bulb():
    g = Image.new('RGB', (CW, CH), C['blk']); d = ImageDraw.Draw(g)
    for r, c in ((13, (80, 48, 0)), (10, (136, 20, 0))): d.ellipse((24 - r, 12 - r, 24 + r, 12 + r), fill=c)
    d.ellipse((17, 4, 31, 18), fill=C['lyel']); d.polygon([(19, 16), (29, 16), (27, 21), (21, 21)], fill=C['lyel'])
    d.line((22, 18, 23, 10), fill=C['org']); d.line((26, 18, 25, 10), fill=C['org']); d.line((23, 10, 25, 10), fill=C['wht'])
    for y in range(21, 27, 2): d.rectangle((21, y, 27, y), fill=C['lgry']); d.rectangle((21, y + 1, 27, y + 1), fill=C['gry'])
    d.rectangle((23, 27, 25, 28), fill=C['dgry'])
    return finish(g)

@reg('inventions', 'printing-press')
def press():
    g, d = museum()
    for x in (10, 36): d.rectangle((x, 2, x + 2, 26), fill=C['brn'])
    d.rectangle((10, 2, 38, 4), fill=C['brn']); d.rectangle((12, 10, 36, 12), fill=C['brn'])
    d.rectangle((23, 4, 25, 13), fill=C['gry']); d.line((15, 7, 33, 7), fill=C['dbrn'], width=1)       # screw and bar
    d.rectangle((17, 13, 31, 15), fill=C['tan'])                                                    # platen
    d.rectangle((8, 18, 40, 20), fill=C['dbrn']); d.rectangle((16, 16, 32, 18), fill=C['wht'])     # bed and paper
    d.line((33, 7, 42, 4), fill=C['tan'])
    return finish(g)

@reg('inventions', 'telescope')
def telescope():
    g = Image.new('RGB', (CW, CH), C['dblu']); d = ImageDraw.Draw(g)
    for x, y in ((4, 3), (40, 5), (32, 2), (8, 12), (44, 14), (14, 6)): d.point((x, y), fill=C['wht'])
    d.ellipse((34, 2, 42, 10), fill=C['lyel'])
    d.line((12, 22, 34, 10), fill=C['tan'], width=4); d.line((10, 23, 14, 21), fill=C['dbrn'], width=3)
    d.line((22, 17, 18, 28), fill=C['dbrn']); d.line((22, 17, 26, 28), fill=C['dbrn']); d.line((22, 17, 22, 28), fill=C['dbrn'])
    d.rectangle((0, 28, CW, CH), fill=C['dgrn'])
    return finish(g)

@reg('inventions', 'magnetic-compass')
def compass():
    g, d = museum()
    d.ellipse((12, 3, 36, 27), fill=C['tan']); d.ellipse((14, 5, 34, 25), fill=C['cream'])
    d.polygon([(24, 6), (26, 15), (22, 15)], fill=C['red']); d.polygon([(24, 24), (26, 15), (22, 15)], fill=C['blu'])
    d.point((24, 15), fill=C['blk'])
    for a in range(0, 360, 45):
        r = math.radians(a); d.point((24 + 9 * math.sin(r), 15 - 9 * math.cos(r)), fill=C['blk'])
    d.rectangle((22, 1, 26, 3), fill=C['tan'])
    return finish(g)

@reg('inventions', 'abacus')
def abacus():
    g, d = museum()
    d.rectangle((8, 4, 40, 26), fill=C['brn']); d.rectangle((10, 6, 38, 24), fill=C['teal'])
    d.rectangle((10, 11, 38, 11), fill=C['brn'])
    import random; r = random.Random(3)
    for i in range(9):
        x = 12 + i * 3; d.line((x, 6, x, 24), fill=C['lgry'])
        up = r.randint(0, 1); d.rectangle((x - 1, 7 + up * 2, x + 1, 8 + up * 2), fill=C['org'])
        n = r.randint(0, 4)
        for k in range(4):
            y = 13 + k * 2 + (0 if k < n else 3); d.rectangle((x - 1, y, x + 1, y + 1), fill=C['org'] if k % 2 == 0 else C['yel'])
    return finish(g)

@reg('inventions', 'sewing-machine')
def sewing():
    g, d = museum()
    d.rectangle((8, 22, 40, 26), fill=C['dbrn'])
    d.rectangle((10, 19, 34, 22), fill=C['blk']); d.rectangle((10, 8, 15, 19), fill=C['blk']); d.rectangle((10, 6, 34, 10), fill=C['blk'])
    d.rectangle((30, 10, 33, 15), fill=C['blk']); d.line((31, 15, 31, 19), fill=C['lgry'])
    d.ellipse((5, 9, 11, 15), fill=C['gry']); d.ellipse((7, 11, 9, 13), fill=C['blk'])
    for x in range(16, 30, 3): d.point((x, 7), fill=C['gold']); d.point((x + 1, 20), fill=C['gold'])
    d.rectangle((20, 3, 22, 6), fill=C['wht'])
    return finish(g)

@reg('inventions', 'penny-farthing')
def penny():
    g, d = road(); d.rectangle((0, 27, CW, CH), fill=C['gry'])
    d.ellipse((6, 2, 30, 26), outline=C['blk'], width=1); d.ellipse((7, 3, 29, 25), outline=C['dgry'])
    for a in range(0, 180, 20):
        r = math.radians(a); d.line((18 - 11 * math.cos(r), 14 - 11 * math.sin(r), 18 + 11 * math.cos(r), 14 + 11 * math.sin(r)), fill=C['dgry'])
    d.ellipse((36, 21, 42, 27), outline=C['blk']); d.point((39, 24), fill=C['blk'])
    d.line((18, 2, 22, 1), fill=C['blk']); d.line((22, 1, 38, 22), fill=C['blk'], width=1)
    d.rectangle((19, 1, 23, 1), fill=C['brn']); d.line((15, 3, 21, 3), fill=C['blk'])
    return finish(g)

@reg('inventions', 'valve-radio')
def radio():
    g, d = museum()
    d.rounded_rectangle((10, 4, 38, 26), 6, fill=C['brn']) if hasattr(d, 'rounded_rectangle') else d.rectangle((10, 4, 38, 26), fill=C['brn'])
    d.pieslice((12, 6, 36, 30), 180, 360, fill=C['tan'])
    for x in range(14, 36, 2): d.line((x, 8, x, 17), fill=C['dbrn'])
    d.rectangle((14, 19, 34, 21), fill=C['lyel']); d.point((22, 20), fill=C['red'])
    d.ellipse((14, 22, 18, 25), fill=C['dbrn']); d.ellipse((30, 22, 34, 25), fill=C['dbrn'])
    return finish(g)

@reg('inventions', 'television')
def tv():
    g, d = museum()
    d.rectangle((9, 3, 39, 24), fill=C['brn']); d.rectangle((11, 5, 31, 22), fill=C['dgry']); d.rectangle((12, 6, 30, 21), fill=C['lsky'])
    for y in range(7, 21, 2): d.line((12, y, 30, y), fill=C['sky'])
    d.ellipse((33, 7, 37, 11), fill=C['dbrn']); d.ellipse((33, 13, 37, 17), fill=C['dbrn'])
    d.line((16, 3, 12, -2), fill=C['gry']); d.line((32, 3, 36, -2), fill=C['gry'])
    d.rectangle((12, 24, 14, 27), fill=C['dbrn']); d.rectangle((34, 24, 36, 27), fill=C['dbrn'])
    return finish(g)

@reg('inventions', 'microscope')
def microscope():
    g, d = museum()
    d.rectangle((14, 23, 34, 26), fill=C['blk']); d.rectangle((24, 8, 27, 23), fill=C['blk'])
    d.line((24, 9, 18, 2), fill=C['gry'], width=3); d.rectangle((16, 0, 19, 2), fill=C['blk'])
    d.rectangle((15, 15, 26, 16), fill=C['blk']); d.rectangle((18, 14, 22, 14), fill=C['lsky'])
    d.line((20, 9, 21, 13), fill=C['lgry'], width=2); d.ellipse((26, 10, 29, 13), fill=C['gry'])
    d.ellipse((17, 18, 21, 21), fill=C['lgry'])
    return finish(g)

@reg('inventions', 'floppy-disk')
def floppy():
    g = Image.new('RGB', (CW, CH), C['lsky']); d = ImageDraw.Draw(g)
    d.polygon([(12, 2), (34, 2), (37, 5), (37, 29), (12, 29)], fill=C['dgry'])
    d.rectangle((17, 2, 31, 10), fill=C['lgry']); d.rectangle((27, 3, 29, 9), fill=C['dgry'])
    d.rectangle((15, 15, 34, 28), fill=C['wht'])
    for y in (18, 21, 24): d.line((17, y, 32, y), fill=C['blu'])
    return finish(g)

if __name__ == '__main__':
    for n in sys.argv[1:] or REG:
        cat, fn = REG[n]; save(fn(), cat, n, scale=4); print(cat, n)
