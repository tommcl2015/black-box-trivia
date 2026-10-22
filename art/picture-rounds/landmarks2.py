#!/usr/bin/env python3
"""World landmarks — Europe, Americas, Asia, Africa, Oceania — 1-bit pixel art."""
import math
from PIL import Image, ImageDraw
from common import *
from landmarks1 import greek_temple

CAT = 'landmarks'
REG = {}
def reg(name):
    def deco(fn): REG[name] = fn; return fn
    return deco

# ================================================================== EUROPE
@reg('eiffel-tower')
def eiffel():
    im, d = canvas(); ground(im, d)
    cx = 48; L, R = [], []
    for i in range(41):
        t = i / 40; y = 58 - t * 52; half = 2 + 26 * (1 - t) ** 2.4
        L.append((cx - half, y)); R.append((cx + half, y))
    d.polygon(L + R[::-1], fill=BLK)
    d.chord((cx - 14, 46, cx + 14, 70), 180, 360, fill=WHT)
    d.rectangle((cx - 14, 58, cx + 14, 58), fill=BLK)
    for y in range(36, 46, 3):
        half = 2 + 26 * (1 - (58 - y) / 52) ** 2.4
        for x in range(int(cx - half + 2), int(cx + half - 1), 3):
            if abs(x - cx) > 2: im.putpixel((x, y), WHT)
    d.rectangle((cx - 13, 44, cx + 13, 45), fill=BLK); d.rectangle((cx - 8, 30, cx + 8, 31), fill=BLK)
    d.rectangle((cx - 3, 12, cx + 3, 13), fill=BLK); d.line((cx, 1, cx, 6), fill=BLK)
    clouds(d, [(14, 12), (74, 18)])
    frame(d); return im

@reg('big-ben')
def bigben():
    im, d = canvas(); ground(im, d)
    cx = 50
    d.rectangle((cx - 8, 22, cx + 8, 58), outline=BLK, fill=WHT)
    for y in range(36, 56, 4): d.line((cx - 6, y, cx + 6, y), fill=BLK)
    for x in (cx - 4, cx, cx + 4): d.line((x, 35, x, 57), fill=BLK)
    d.rectangle((cx - 9, 10, cx + 9, 23), outline=BLK, fill=WHT)
    d.ellipse((cx - 6, 11, cx + 6, 22), outline=BLK, fill=WHT)
    d.line((cx, 16, cx, 13), fill=BLK); d.line((cx, 16, cx + 3, 16), fill=BLK)
    d.rectangle((cx - 7, 24, cx + 7, 33), fill=WHT, outline=BLK)
    for x in range(cx - 5, cx + 6, 3): d.line((x, 26, x, 31), fill=BLK)
    d.polygon([(cx - 9, 10), (cx, -2), (cx + 9, 10)], fill=BLK)
    for x in (cx - 9, cx + 9): d.line((x, 4, x, 10), fill=BLK)
    d.rectangle((1, 40, cx - 9, 58), outline=BLK, fill=WHT)
    for x in range(4, cx - 9, 5): d.line((x, 36, x, 40), fill=BLK); d.line((x + 2, 43, x + 2, 55), fill=BLK)
    d.rectangle((cx + 9, 46, W - 2, 58), outline=BLK, fill=WHT)
    for x in range(cx + 12, W - 2, 5): d.line((x, 49, x, 56), fill=BLK)
    d.rectangle((70, 50, 90, 57), fill=BLK)
    for x in range(72, 89, 4): d.rectangle((x, 51, x + 2, 52), fill=WHT)
    d.ellipse((72, 56, 76, 60), fill=WHT, outline=BLK); d.ellipse((84, 56, 88, 60), fill=WHT, outline=BLK)
    frame(d); return im

@reg('tower-bridge')
def tower_bridge():
    im, d = canvas(); water(im, 50)
    d.line((1, 49, W - 2, 49), fill=BLK)
    for cx in (30, 66):
        d.rectangle((cx - 7, 14, cx + 7, 52), fill=WHT, outline=BLK)       # tower
        d.rectangle((cx - 5, 24, cx + 5, 30), fill=BLK); d.polygon([(cx - 3, 30), (cx, 26), (cx + 3, 30)], fill=WHT)
        d.rectangle((cx - 3, 36, cx + 3, 44), fill=BLK)
        d.polygon([(cx - 7, 14), (cx, 4), (cx + 7, 14)], fill=BLK)         # pyramidal roof
        for x in (cx - 7, cx + 7):
            d.rectangle((x - 1, 8, x + 1, 14), fill=BLK); d.line((x, 4, x, 8), fill=BLK)
        d.rectangle((cx - 8, 48, cx + 8, 54), fill=BLK)                    # pier
    d.rectangle((37, 16, 59, 20), fill=BLK)                                 # high walkways
    for x in range(39, 58, 3): d.point((x, 18), fill=WHT)
    d.line((37, 40, 47, 37), fill=BLK, width=2); d.line((59, 40, 49, 37), fill=BLK, width=2)   # raised bascules
    d.line((1, 40, 23, 40), fill=BLK, width=2); d.line((73, 40, 94, 40), fill=BLK, width=2)    # side spans
    d.line((23, 16, 1, 34), fill=BLK); d.line((73, 16, 94, 34), fill=BLK)                       # chains
    for x in range(4, 23, 4): d.line((x, 40, x, 34 - (x - 1) * 18 // 22 + 0), fill=BLK)
    for x in range(76, 94, 4): d.line((x, 40, x, 16 + (x - 73) * 18 // 21), fill=BLK)
    frame(d); return im

@reg('stonehenge')
def stonehenge():
    im, d = canvas()
    fill_pattern(im, (1, 46, W - 1, H - 1), 5); d.line((1, 46, W - 2, 46), fill=BLK)
    sun(im, d, 48, 14, 6)
    def tri(x, y, w=12, h=20, shaded=True):
        d.rectangle((x, y, x + 4, y + h), fill=BLK); d.rectangle((x + w - 4, y, x + w, y + h), fill=BLK)
        d.rectangle((x - 1, y - 4, x + w + 1, y), fill=BLK)
    tri(10, 30); tri(30, 28, 14); tri(60, 28, 14); tri(80, 31, 10, 17)
    d.rectangle((50, 36, 54, 52), fill=BLK)                                  # lone upright
    d.polygon([(22, 56), (40, 52), (41, 56), (23, 60)], fill=BLK)           # fallen stone
    d.rectangle((6, 50, 10, 56), fill=BLK); d.rectangle((86, 50, 90, 55), fill=BLK)
    for x0 in (11, 31, 61, 81): fill_pattern(im, (x0, 31, x0 + 3, 48), 0)
    frame(d); return im

@reg('leaning-tower-of-pisa')
def pisa():
    big = Image.new('1', (W, H), WHT); d = ImageDraw.Draw(big)
    cx, w = 48, 10
    for i in range(7):
        y0 = 54 - (i + 1) * 6; y1 = 54 - i * 6; ww = w if i < 6 else w - 3
        d.rectangle((cx - ww, y0, cx + ww, y1), outline=BLK, fill=WHT); d.line((cx - ww - 1, y1, cx + ww + 1, y1), fill=BLK)
        for x in range(cx - ww + 2, cx + ww - 1, 3): d.line((x, y0 + 2, x, y1 - 1), fill=BLK)
    d.rectangle((cx - w, 54, cx + w, 57), fill=BLK)
    im = big.rotate(-5, resample=Image.NEAREST, center=(cx, 57), fillcolor=WHT); d = ImageDraw.Draw(im)
    ground(im, d, 58)
    d.rectangle((4, 46, 26, 58), outline=BLK, fill=WHT); d.chord((8, 38, 22, 54), 180, 360, outline=BLK, fill=WHT)
    for x in range(7, 25, 4): d.line((x, 50, x, 56), fill=BLK)
    d.point((76, 52), fill=BLK); d.line((76, 53, 76, 57), fill=BLK); d.line((76, 54, 72, 50), fill=BLK)   # tourist "holding it up"
    frame(d); return im

@reg('arc-de-triomphe')
def arc():
    im, d = canvas(); ground(im, d)
    d.rectangle((22, 12, 74, 58), fill=WHT, outline=BLK)
    d.rectangle((20, 8, 76, 12), fill=BLK); d.line((22, 20, 74, 20), fill=BLK); d.line((22, 22, 74, 22), fill=BLK)
    for x in range(24, 74, 3): d.point((x, 21), fill=BLK)
    d.chord((38, 26, 58, 46), 180, 360, fill=BLK); d.rectangle((38, 36, 58, 58), fill=BLK)     # main arch
    for x0 in (26, 62):                                                     # relief panels
        d.rectangle((x0, 34, x0 + 8, 46), outline=BLK); fill_pattern(im, (x0 + 2, 36, x0 + 7, 45), 2)
    d.rectangle((26, 24, 70, 25), fill=BLK)
    # flag + cars
    d.rectangle((6, 52, 14, 56), fill=BLK); d.rectangle((80, 52, 89, 56), fill=BLK)
    d.ellipse((7, 55, 9, 57), fill=WHT); d.ellipse((86, 55, 88, 57), fill=WHT)
    frame(d); return im

@reg('sagrada-familia')
def sagrada():
    im, d = canvas(); ground(im, d)
    def spire(cx, top, base=58, w=4):
        pts = []
        for i in range(21):
            t = i / 20; y = top + (base - top) * t
            ww = 1 + w * min(1, t * 1.6) * (1.2 - 0.3 * t)
            pts.append((cx - ww, y))
        d.polygon(pts + [(2 * cx - x, y) for x, y in reversed(pts)], fill=BLK)
        for y in range(top + 10, base - 6, 4): d.point((cx, y), fill=WHT)
        d.ellipse((cx - 1, top - 3, cx + 1, top - 1), fill=BLK)
    for cx, top in ((24, 18), (32, 12), (40, 10), (56, 10), (64, 12), (72, 18)):
        spire(cx, top)
    spire(48, 2, w=6)                                                      # central tower of Jesus
    d.rectangle((16, 40, 80, 58), fill=BLK)
    d.chord((38, 44, 58, 66), 180, 360, fill=WHT); d.chord((41, 47, 55, 66), 180, 360, fill=BLK)
    fill_pattern(im, (18, 42, 36, 56), 2); fill_pattern(im, (60, 42, 78, 56), 2)
    # construction crane
    d.line((86, 58, 86, 6), fill=BLK); d.line((60, 6, 94, 6), fill=BLK)
    d.line((86, 2, 70, 6), fill=BLK); d.line((86, 2, 94, 6), fill=BLK); d.line((66, 6, 66, 14), fill=BLK)
    frame(d); return im

@reg('brandenburg-gate')
def brandenburg():
    im, d = canvas(); ground(im, d)
    d.rectangle((10, 22, 86, 28), fill=BLK); d.rectangle((14, 28, 82, 30), fill=BLK)
    for i in range(6):
        x = 16 + i * 13; d.rectangle((x - 2, 30, x + 2, 58), fill=BLK); d.line((x, 32, x, 56), fill=WHT)
    d.rectangle((6, 34, 12, 58), fill=WHT, outline=BLK); d.rectangle((84, 34, 90, 58), fill=WHT, outline=BLK)
    d.rectangle((30, 16, 66, 22), fill=WHT, outline=BLK)                    # attic
    for x in range(33, 64, 3): d.point((x, 19), fill=BLK)
    # quadriga
    for x in (38, 44, 50, 56):
        d.rectangle((x, 10, x + 4, 13), fill=BLK); d.line((x, 13, x, 16), fill=BLK); d.line((x + 4, 13, x + 4, 16), fill=BLK)
        d.rectangle((x + 4, 7, x + 5, 10), fill=BLK)
    d.rectangle((46, 2, 49, 10), fill=BLK); d.polygon([(47, 2), (49, -1), (51, 2)], fill=BLK); d.line((51, 0, 51, 8), fill=BLK)
    frame(d); return im

@reg('neuschwanstein-castle')
def neuschwanstein():
    im, d = canvas()
    # mountains
    d.polygon([(0, 30), (14, 12), (26, 22), (40, 6), (58, 24), (74, 10), (96, 28), (96, 64), (0, 64)], fill=WHT, outline=BLK)
    for x, y in ((14, 12), (40, 6), (74, 10)): d.polygon([(x - 4, y + 5), (x, y), (x + 4, y + 5)], fill=BLK)
    # forested hill
    d.polygon([(0, 64), (0, 48), (20, 44), (40, 42), (70, 46), (96, 52), (96, 64)], fill=BLK)
    for x in range(2, 96, 4): d.polygon([(x - 2, 47 + (x % 8) // 3), (x, 42 + (x % 8) // 3), (x + 2, 47 + (x % 8) // 3)], fill=BLK)
    # castle
    d.rectangle((30, 26, 64, 46), fill=WHT, outline=BLK)
    d.polygon([(30, 26), (47, 18), (64, 26)], fill=BLK)
    for x in range(33, 62, 4):
        d.rectangle((x, 30, x + 1, 33), fill=BLK); d.rectangle((x, 37, x + 1, 40), fill=BLK)
    def turret(x, top, base, r=2):
        d.rectangle((x - r, top, x + r, base), fill=WHT, outline=BLK)
        d.polygon([(x - r - 1, top), (x, top - 7), (x + r + 1, top)], fill=BLK)
        d.point((x, top + 3), fill=BLK)
    turret(26, 22, 46, 3); turret(68, 16, 46, 3); turret(36, 18, 26); turret(58, 14, 26); turret(47, 10, 20, 2)
    frame(d); return im

@reg('st-basils-cathedral')
def st_basil():
    im, d = canvas(); ground(im, d)
    d.rectangle((14, 40, 82, 58), fill=WHT, outline=BLK)
    for x in range(18, 80, 6): d.chord((x, 44, x + 4, 52), 180, 360, fill=BLK); d.rectangle((x, 48, x + 4, 54), fill=BLK)
    # central tent spire
    d.polygon([(42, 40), (46, 10), (50, 10), (54, 40)], fill=WHT, outline=BLK)
    for y in range(14, 40, 4): d.line((44, y, 52, y), fill=BLK)
    onion(d, 48, 10, 2.5)
    domes = [(22, 40, 6, 3), (34, 38, 7, 2), (62, 38, 7, 5), (74, 40, 6, 4), (28, 30, 5, 7), (68, 30, 5, 2)]
    for cx, base, r, pat in domes:
        d.rectangle((cx - r + 2, base - 4, cx + r - 2, base), fill=WHT, outline=BLK)
        onion(d, cx, base - 4, r, fill=WHT, outline=BLK)
        shade(im, lambda dd, cx=cx, base=base, r=r: onion(dd, cx, base - 5, r - 1, fill=1), pat)
    frame(d); return im

@reg('parthenon')
def parthenon():
    im, d = canvas()
    # Acropolis hill
    d.polygon([(0, 64), (0, 52), (12, 46), (84, 46), (96, 52), (96, 64)], fill=BLK)
    shade(im, lambda dd: dd.polygon([(0, 64), (0, 54), (12, 48), (84, 48), (96, 54), (96, 64)], fill=1), 3)
    greek_temple(d, im, 16, 80, 46, 22, 8, pediment=8)
    # ruined pediment: knock a gap out of the roof
    d.polygon([(58, 14), (72, 21), (58, 21)], fill=WHT); d.line((58, 14, 58, 21), fill=BLK)
    clouds(d, [(4, 6), (76, 4)])
    frame(d); return im

@reg('atomium')
def atomium():
    im, d = canvas(); ground(im, d)
    pts = {'t': (48, 8), 'b': (48, 48), 'c': (48, 28), 'l1': (28, 18), 'r1': (68, 18), 'l2': (28, 38), 'r2': (68, 38), 'f1': (38, 22), 'f2': (58, 34)}
    edges = [('t', 'l1'), ('t', 'r1'), ('b', 'l2'), ('b', 'r2'), ('l1', 'l2'), ('r1', 'r2'), ('t', 'c'), ('c', 'b'), ('l1', 'c'), ('r2', 'c'), ('l2', 'c'), ('r1', 'c')]
    for a, b in edges: d.line(pts[a] + pts[b], fill=BLK, width=2)
    for k, (x, y) in pts.items():
        if k[0] == 'f': continue
        d.ellipse((x - 5, y - 5, x + 5, y + 5), fill=WHT, outline=BLK)
        shade(im, lambda dd, x=x, y=y: dd.ellipse((x - 1, y - 3, x + 4, y + 4), fill=1), 2)
        d.point((x - 2, y - 2), fill=BLK)
    for x in (38, 58): d.line((48, 52, x, 58), fill=BLK, width=2)
    d.line((48, 53, 48, 58), fill=BLK, width=2)
    frame(d); return im

@reg('notre-dame-de-paris')
def notre_dame():
    im, d = canvas(); ground(im, d)
    d.rectangle((20, 14, 76, 58), fill=WHT, outline=BLK)
    d.rectangle((20, 14, 38, 20), fill=WHT, outline=BLK); d.rectangle((58, 14, 76, 20), fill=WHT, outline=BLK)
    d.rectangle((38, 22, 58, 58), outline=BLK)
    for x0 in (22, 60):                                                      # tower openings
        for x in (x0 + 3, x0 + 10): d.rectangle((x, 6 + 10, x + 2, 26), fill=BLK); d.point((x, 16), fill=WHT); d.point((x + 2, 16), fill=WHT)
    d.rectangle((18, 12, 40, 14), fill=BLK); d.rectangle((56, 12, 78, 14), fill=BLK)
    d.ellipse((40, 24, 56, 40), fill=WHT, outline=BLK)                       # rose window
    for a in range(0, 360, 30):
        r = math.radians(a); d.line((48, 32, 48 + 7 * math.cos(r), 32 + 7 * math.sin(r)), fill=BLK)
    d.line((20, 42, 76, 42), fill=BLK)
    for x in range(22, 76, 3): d.rectangle((x, 40, x + 1, 42), fill=BLK)   # gallery of kings
    for cx in (29, 48, 67):                                                  # three portals
        d.chord((cx - 6, 44, cx + 6, 60), 180, 360, fill=BLK); d.rectangle((cx - 6, 52, cx + 6, 58), fill=BLK)
        d.line((cx, 50, cx, 58), fill=WHT)
    d.line((48, 2, 48, 14), fill=BLK)                                        # spire behind
    frame(d); return im

@reg('windmills-of-kinderdijk')
def windmill():
    im, d = canvas(); water(im, 54)
    d.line((1, 52, W - 2, 52), fill=BLK)
    def mill(cx, base, s=1.0, ang=20):
        h = int(26 * s); bw = int(8 * s); tw = int(4 * s)
        d.polygon([(cx - bw, base), (cx - tw, base - h), (cx + tw, base - h), (cx + bw, base)], fill=BLK)
        d.chord((cx - tw - 1, base - h - 4, cx + tw + 1, base - h + 3), 180, 360, fill=BLK)
        d.rectangle((cx - 1, base - 6, cx + 1, base), fill=WHT)
        hub = (cx, base - h - 1); L = int(18 * s)
        for k in range(4):
            a = math.radians(ang + k * 90)
            ex, ey = hub[0] + L * math.cos(a), hub[1] + L * math.sin(a)
            d.line(hub + (ex, ey), fill=BLK)
            px, py = -math.sin(a) * 3 * s, math.cos(a) * 3 * s
            d.polygon([(hub[0] + 5 * math.cos(a), hub[1] + 5 * math.sin(a)), (ex, ey), (ex + px, ey + py), (hub[0] + 5 * math.cos(a) + px, hub[1] + 5 * math.sin(a) + py)], outline=BLK)
    mill(30, 52, 1.0, 20); mill(70, 52, 0.75, 45); mill(88, 52, 0.45, 10)
    frame(d); return im

@reg('st-peters-basilica')
def st_peters():
    im, d = canvas(); ground(im, d)
    d.rectangle((14, 34, 82, 58), fill=WHT, outline=BLK)
    d.rectangle((12, 32, 84, 36), fill=BLK)
    for x in range(18, 80, 6): d.rectangle((x, 37, x + 2, 58), fill=BLK)
    d.polygon([(36, 32), (48, 26), (60, 32)], fill=WHT, outline=BLK)
    for x in range(16, 82, 4): d.point((x, 31), fill=BLK)
    # drum + dome + lantern
    d.rectangle((36, 18, 60, 26), fill=WHT, outline=BLK)
    for x in range(38, 60, 3): d.line((x, 19, x, 25), fill=BLK)
    d.chord((34, 2, 62, 34), 180, 360, fill=WHT, outline=BLK)
    for a in range(200, 341, 20):
        r = math.radians(a); d.line((48 + 6 * math.cos(r), 18 + 6 * math.sin(r), 48 + 14 * math.cos(r), 18 + 15 * math.sin(r)), fill=BLK)
    d.rectangle((46, 0, 50, 4), fill=BLK)
    # colonnade arms
    for side in (-1, 1):
        for i in range(5):
            x = 48 + side * (36 + i * 2); d.line((x, 44, x, 58), fill=BLK)
    frame(d); return im

@reg('mont-saint-michel')
def mont_st_michel():
    im, d = canvas(); water(im, 52)
    d.polygon([(10, 56), (22, 44), (34, 34), (48, 28), (62, 34), (74, 44), (86, 56)], fill=BLK)     # rock
    for y in range(46, 56, 3):
        for x in range(16 + (y % 6), 80, 5): d.rectangle((x, y, x + 1, y + 1), fill=WHT)              # town windows
    d.rectangle((38, 18, 60, 30), fill=BLK)                                                           # abbey
    for x in range(40, 59, 3): d.rectangle((x, 21, x, 26), fill=WHT)
    d.polygon([(46, 18), (48, 2), (50, 18)], fill=BLK); d.line((48, 0, 48, 2), fill=BLK)             # spire
    d.rectangle((44, 14, 52, 18), fill=BLK)
    d.line((86, 56, 96, 60), fill=BLK)                                                                 # causeway
    frame(d); return im

@reg('hagia-sophia')
def hagia_sophia():
    im, d = canvas(); ground(im, d)
    d.rectangle((18, 36, 78, 58), fill=WHT, outline=BLK)
    for x in range(22, 76, 5): d.rectangle((x, 44, x + 2, 50), fill=BLK)
    d.chord((22, 24, 46, 48), 180, 360, fill=WHT, outline=BLK); d.chord((50, 24, 74, 48), 180, 360, fill=WHT, outline=BLK)   # half domes
    d.rectangle((34, 22, 62, 30), fill=WHT, outline=BLK)
    for x in range(36, 61, 3): d.point((x, 26), fill=BLK)
    d.chord((32, 6, 64, 38), 180, 360, fill=WHT, outline=BLK)
    shade(im, lambda dd: dd.chord((48, 8, 62, 36), 270, 360, fill=1), 2)
    d.line((48, 2, 48, 6), fill=BLK); d.point((48, 1), fill=BLK)
    for x in (8, 16, 80, 88):                                                 # minarets
        d.rectangle((x - 1, 14, x + 1, 58), fill=BLK); d.polygon([(x - 2, 14), (x, 4), (x + 2, 14)], fill=BLK)
        d.rectangle((x - 2, 24, x + 2, 25), fill=BLK); d.rectangle((x - 2, 36, x + 2, 37), fill=BLK)
    frame(d); return im

@reg('matterhorn')
def matterhorn():
    im, d = canvas()
    clouds(d, [(6, 10), (74, 4)])
    d.polygon([(0, 64), (24, 40), (38, 30), (46, 10), (50, 6), (56, 14), (62, 26), (76, 36), (96, 50), (96, 64)], fill=WHT, outline=BLK)
    shade(im, lambda dd: dd.polygon([(50, 6), (56, 14), (62, 26), (76, 36), (96, 50), (96, 64), (52, 64), (54, 30)], fill=1), 3)
    d.polygon([(46, 10), (50, 6), (54, 12), (50, 18), (48, 14)], fill=WHT, outline=BLK)
    for x, y in ((40, 28), (44, 22), (36, 34)): d.line((x, y, x + 3, y + 4), fill=BLK)
    # pine trees + chalet
    for x in range(4, 40, 6): d.polygon([(x - 3, 62), (x, 52), (x + 3, 62)], fill=BLK)
    d.rectangle((70, 56, 80, 62), fill=WHT, outline=BLK); d.polygon([(68, 56), (75, 51), (82, 56)], fill=BLK)
    frame(d); return im

# ================================================================== AMERICAS
@reg('statue-of-liberty')
def liberty():
    im, d = canvas(); water(im, 52)
    cx = 48
    d.rectangle((cx - 14, 46, cx + 14, 52), fill=BLK)
    d.polygon([(cx - 9, 46), (cx - 8, 34), (cx + 8, 34), (cx + 9, 46)], fill=WHT, outline=BLK)
    for y in (37, 41): d.line((cx - 8, y, cx + 8, y), fill=BLK)
    d.polygon([(cx - 5, 34), (cx - 4, 18), (cx + 4, 18), (cx + 6, 34)], fill=BLK)
    d.polygon([(cx + 2, 20), (cx + 5, 12), (cx + 7, 3), (cx + 9, 3), (cx + 7, 13), (cx + 4, 21)], fill=BLK)
    d.polygon([(cx + 6, 3), (cx + 8, -1), (cx + 10, 3)], fill=BLK)
    d.rectangle((cx - 7, 21, cx - 4, 26), fill=BLK)
    d.ellipse((cx - 3, 11, cx + 3, 18), fill=BLK)
    for ang in (-70, -40, -10, 20, 50):
        a = math.radians(ang - 90); d.line((cx, 12, cx + 6 * math.cos(a), 12 + 6 * math.sin(a)), fill=BLK)
    frame(d); return im

@reg('golden-gate-bridge')
def golden_gate():
    im, d = canvas(); water(im, 46)
    d.polygon([(0, 46), (0, 32), (10, 30), (18, 40), (24, 46)], fill=BLK)          # Marin headlands
    d.polygon([(76, 46), (84, 38), (96, 36), (96, 46)], fill=BLK)
    deck = 38
    d.line((1, deck, W - 2, deck), fill=BLK, width=2)
    for tx in (26, 70):
        d.rectangle((tx - 2, 6, tx - 1, 50), fill=BLK); d.rectangle((tx + 1, 6, tx + 2, 50), fill=BLK)
        for y in (8, 16, 24, 32): d.line((tx - 2, y, tx + 2, y), fill=BLK)
        d.rectangle((tx - 3, 48, tx + 3, 52), fill=BLK)
    pts = [(26 + i, 7 + ((i - 22) / 22) ** 2 * 28) for i in range(0, 45)]
    d.line(pts, fill=BLK)
    d.line([(1, 30), (26, 7)], fill=BLK); d.line([(70, 7), (94, 30)], fill=BLK)
    for x in range(28, 70, 3):
        y = 7 + ((x - 48) / 22) ** 2 * 28; d.line((x, y, x, deck), fill=BLK)
    for x in range(4, 26, 3): d.line((x, 30 - (x - 1) * 23 / 25, x, deck), fill=BLK)
    for x in range(72, 94, 3): d.line((x, 7 + (x - 70) * 23 / 24, x, deck), fill=BLK)
    # fog
    for x0 in (34, 54): d.ellipse((x0, 2, x0 + 14, 8), fill=WHT, outline=BLK)
    frame(d); return im

@reg('mount-rushmore')
def rushmore():
    im, d = canvas()
    clouds(d, [(70, 4)])
    d.polygon([(0, 64), (0, 22), (12, 12), (30, 8), (60, 6), (82, 12), (96, 20), (96, 64)], fill=WHT, outline=BLK)
    fill_pattern(im, (1, 46, W - 1, H - 1), 2)
    for x in range(1, 95, 5): d.polygon([(x - 2, 64), (x, 54 + (x % 10) // 3), (x + 2, 64)], fill=BLK)   # pines
    faces = [(18, 22, 9), (38, 18, 9), (54, 24, 7), (72, 20, 9)]
    for i, (cx, cy, r) in enumerate(faces):
        d.ellipse((cx - r, cy - r, cx + r, cy + r + 6), fill=WHT, outline=BLK)
        shade(im, lambda dd, cx=cx, cy=cy, r=r: dd.chord((cx - r, cy - r, cx + r, cy + r + 6), 300, 60, fill=1), 6)
        d.line((cx - 4, cy - 1, cx - 1, cy - 1), fill=BLK); d.line((cx + 2, cy - 1, cx + 5, cy - 1), fill=BLK)      # brows/eyes
        d.point((cx - 2, cy + 1), fill=BLK); d.point((cx + 3, cy + 1), fill=BLK)
        d.line((cx, cy + 1, cx + 1, cy + 5), fill=BLK); d.line((cx - 2, cy + 8, cx + 3, cy + 8), fill=BLK)
    d.line((64, 16, 66, 30), fill=BLK)    # Lincoln's beard edge
    for x in range(66, 82, 2): d.point((x, 30), fill=BLK)
    frame(d); return im

@reg('gateway-arch')
def gateway_arch():
    im, d = canvas(); water(im, 56)
    d.line((1, 54, W - 2, 54), fill=BLK)
    pts_o = [(48 + 34 * t, 54 - 50 * (1 - abs(t) ** 1.8)) for t in [i / 40 - 1 for i in range(81)]]
    pts_i = [(48 + 30 * t, 54 - 44 * (1 - abs(t) ** 1.8)) for t in [i / 40 - 1 for i in range(81)]]
    d.polygon(pts_o + pts_i[::-1], fill=BLK)
    shade(im, lambda dd: dd.polygon(pts_o[40:] + pts_i[40:][::-1], fill=1), 2)
    city_fill(im, d, 54, seed=3, hmin=3, hmax=8, x0=2, x1=12); city_fill(im, d, 54, seed=4, hmin=3, hmax=9, x0=84)
    frame(d); return im

@reg('white-house')
def white_house():
    im, d = canvas(); ground(im, d, 56, 5)
    d.rectangle((10, 30, 86, 56), fill=WHT, outline=BLK)
    d.rectangle((8, 28, 88, 30), fill=BLK)
    for x in range(14, 84, 7):
        if 36 < x < 60: continue
        for y in (34, 44): d.rectangle((x, y, x + 3, y + 5), fill=BLK); d.polygon([(x - 1, y), (x + 1.5, y - 2), (x + 4, y)], fill=BLK)
    # portico
    d.chord((36, 22, 60, 40), 180, 360, fill=WHT, outline=BLK)
    d.rectangle((36, 30, 60, 32), fill=BLK)
    for x in range(38, 60, 4): d.rectangle((x, 33, x + 1, 56), fill=BLK)
    d.line((48, 22, 48, 10), fill=BLK)                                       # flag
    d.rectangle((49, 10, 56, 14), fill=BLK); fill_pattern(im, (49, 10, 52, 12), 0)
    for y in (11, 13): d.line((53, y, 56, y), fill=WHT)
    d.rectangle((44, 58, 52, 62), outline=BLK); fill_pattern(im, (45, 59, 52, 62), 1)   # fountain
    frame(d); return im

@reg('us-capitol')
def capitol():
    im, d = canvas(); ground(im, d, 56, 5)
    d.rectangle((4, 40, 92, 56), fill=WHT, outline=BLK)
    for x in range(6, 91, 4): d.line((x, 44, x, 56), fill=BLK)
    d.rectangle((2, 38, 94, 40), fill=BLK)
    d.polygon([(38, 38), (48, 32), (58, 38)], fill=WHT, outline=BLK)
    d.rectangle((34, 26, 62, 32), fill=WHT, outline=BLK)                    # drum
    for x in range(36, 62, 3): d.line((x, 27, x, 31), fill=BLK)
    d.chord((36, 8, 60, 38), 180, 360, fill=WHT, outline=BLK)
    for y in (14, 18): d.line((40, y + 4, 56, y + 4), fill=BLK)
    for x in range(40, 58, 3): d.point((x, 21), fill=BLK)
    d.rectangle((45, 4, 51, 10), fill=WHT, outline=BLK); d.rectangle((47, 0, 49, 4), fill=BLK)
    frame(d); return im

@reg('moai-easter-island')
def moai():
    im, d = canvas(); water(im, 52)
    sun(im, d, 82, 10, 5)
    d.rectangle((1, 46, W - 2, 52), fill=BLK)                                # ahu platform
    for i, x in enumerate((10, 28, 46, 64)):
        h = 30 - i % 2 * 3
        top = 46 - h
        d.polygon([(x, 46), (x + 1, top + 6), (x + 3, top), (x + 11, top), (x + 12, top + 6), (x + 13, 46)], fill=BLK)
        d.rectangle((x + 3, top + 6, x + 10, top + 9), fill=WHT)              # heavy brow shadow line
        d.line((x + 3, top + 7, x + 10, top + 7), fill=BLK)
        d.polygon([(x + 6, top + 9), (x + 8, top + 18), (x + 5, top + 18)], fill=WHT)   # long nose
        d.line((x + 4, top + 21, x + 9, top + 21), fill=WHT)
        d.rectangle((x + 1, top + 12, x + 2, top + 18), fill=WHT)            # ear
    frame(d); return im

@reg('cn-tower')
def cn_tower():
    im, d = canvas(); water(im, 58)
    city_fill(im, d, 56, seed=4, hmin=6, hmax=16)
    cx = 40
    d.polygon([(cx - 3, 56), (cx - 1, 6), (cx + 1, 6), (cx + 3, 56)], fill=BLK)
    d.polygon([(cx - 6, 56), (cx - 2, 30), (cx - 1, 30)], fill=BLK); d.polygon([(cx + 6, 56), (cx + 2, 30), (cx + 1, 30)], fill=BLK)
    d.ellipse((cx - 7, 18, cx + 7, 25), fill=BLK); d.rectangle((cx - 6, 21, cx + 6, 22), fill=WHT)
    d.ellipse((cx - 3, 13, cx + 3, 17), fill=BLK); d.line((cx, 0, cx, 6), fill=BLK)
    d.chord((58, 40, 80, 56), 180, 360, fill=BLK)                            # Rogers Centre dome
    frame(d); return im

def falls(lip, gorge=None):
    im, d = canvas()
    clouds(d, [(70, 4)])
    d.rectangle((1, 14, W - 2, 22), fill=WHT); fill_pattern(im, (1, 15, W - 1, 22), 7); d.line((1, 14, W - 2, 14), fill=BLK)
    for x in range(1, W - 1):
        top = lip(x); d.point((x, top), fill=BLK)
        for y in range(22, top):
            if (x - y) % 4 == 0: d.point((x, y), fill=BLK)
        if x % 2: d.line((x, top, x, 48), fill=BLK)
    if gorge:
        for x0, x1 in gorge: d.rectangle((x0, 22, x1, 48), fill=BLK); fill_pattern(im, (x0 + 1, 23, x1, 48), 0)
    for x0, y0 in ((-4, 42), (14, 38), (34, 42), (54, 38), (74, 42)): d.ellipse((x0, y0, x0 + 24, y0 + 12), fill=WHT, outline=BLK)
    water(im, 54)
    return im, d

@reg('niagara-falls')
def niagara():
    im, d = falls(lambda x: 22 + int(12 * math.sqrt(max(0, 1 - ((x - 52) / 30) ** 2))) if 22 < x < 82 else 22)
    d.polygon([(60, 56), (78, 56), (75, 60), (63, 60)], fill=BLK); d.rectangle((66, 53, 72, 56), fill=BLK)   # Maid of the Mist
    frame(d); return im

# ================================================================== ASIA, AFRICA, OCEANIA
@reg('mount-fuji')
def fuji():
    im, d = canvas()
    sun(im, d, 16, 12, 7)
    d.polygon([(0, 58), (30, 32), (42, 14), (54, 14), (66, 32), (96, 58)], fill=BLK)
    d.polygon([(42, 14), (54, 14), (61, 25), (57, 24), (53, 29), (49, 23), (45, 29), (41, 24), (35, 25)], fill=WHT, outline=BLK)
    # Chureito pagoda on the right
    pagoda(d, 80, 60, 5, 8, 5, 1)
    # cherry blossom clusters
    for x, y in ((6, 50), (14, 54), (60, 52)):
        d.ellipse((x - 5, y - 4, x + 5, y + 4), fill=WHT, outline=BLK); fill_pattern(im, (x - 4, y - 3, x + 4, y + 3), 1)
    frame(d); return im

@reg('angkor-wat')
def angkor():
    im, d = canvas(); water(im, 52)
    sun(im, d, 82, 8, 4)
    d.rectangle((6, 42, 90, 52), fill=WHT, outline=BLK)
    for x in range(8, 90, 4): d.rectangle((x, 45, x + 1, 50), fill=BLK)
    def bud(cx, base, h, w):
        pts = []
        for i in range(21):
            t = i / 20; y = base - h * t
            ww = w * (1 - t ** 1.6) + 0.5
            pts.append((cx - ww, y))
        d.polygon(pts + [(2 * cx - x, y) for x, y in reversed(pts)], fill=BLK)
        for y in range(base - h + 6, base - 2, 3): d.line((cx - w * (1 - ((base - y) / h) ** 1.6) + 1, y, cx + w * (1 - ((base - y) / h) ** 1.6) - 1, y), fill=WHT)
    d.rectangle((24, 32, 72, 42), fill=WHT, outline=BLK)
    for x in range(26, 72, 4): d.rectangle((x, 35, x + 1, 40), fill=BLK)
    bud(30, 34, 16, 5); bud(66, 34, 16, 5); bud(39, 33, 20, 5); bud(57, 33, 20, 5); bud(48, 32, 28, 7)
    frame(d); return im

@reg('petronas-towers')
def petronas():
    im, d = canvas(); city_fill(im, d, 60, seed=8, hmin=4, hmax=10)
    for cx in (34, 62):
        for i, (y0, y1, w) in enumerate(((20, 60, 7), (14, 20, 6), (10, 14, 5), (7, 10, 4), (5, 7, 3))):
            d.rectangle((cx - w, y0, cx + w, y1), fill=BLK)
            if i == 0:
                for x in range(cx - w + 2, cx + w - 1, 2): d.line((x, y0 + 2, x, y1 - 2), fill=WHT)
                for y in range(y0 + 4, y1, 6): d.line((cx - w, y, cx + w, y), fill=BLK)
        d.line((cx, 0, cx, 5), fill=BLK)
    d.rectangle((41, 30, 55, 32), fill=BLK); d.line((44, 32, 41, 38), fill=BLK); d.line((52, 32, 55, 38), fill=BLK)   # skybridge
    frame(d); return im

@reg('burj-al-arab')
def burj_al_arab():
    im, d = canvas(); water(im, 52)
    sun(im, d, 20, 12, 5)
    d.rectangle((54, 52, 70, 56), fill=BLK)                                  # island
    d.line((54, 54, 1, 58), fill=BLK, width=2)                              # causeway
    d.polygon([(58, 52), (58, 6), (64, 6), (64, 52)], fill=BLK)             # mast spine
    sail = [(64, 8)] + [(64 + 22 * math.sin(math.pi * t) * (1 - t * 0.4), 8 + 44 * t) for t in [i / 20 for i in range(21)]]
    d.polygon(sail, fill=WHT, outline=BLK)
    for t in [i / 8 for i in range(1, 8)]:
        y = 8 + 44 * t; d.line((64, y, 64 + 22 * math.sin(math.pi * t) * (1 - t * 0.4), y), fill=BLK)
    d.ellipse((54, 16, 60, 20), fill=BLK)                                    # helipad
    d.line((60, 0, 60, 8), fill=BLK)
    frame(d); return im

@reg('temple-of-heaven')
def temple_of_heaven():
    im, d = canvas()
    for i, (y, w) in enumerate(((58, 44), (54, 38), (50, 32))):              # marble terraces
        d.rectangle((48 - w, y - 4, 48 + w, y), fill=WHT, outline=BLK)
        for x in range(48 - w + 2, 48 + w - 1, 3): d.point((x, y - 3), fill=BLK)
    d.rectangle((1, 58, W - 2, 62), fill=BLK)
    y = 46
    for i, (w, h) in enumerate(((22, 8), (16, 7), (11, 7))):
        d.rectangle((48 - w + 4, y - h + 2, 48 + w - 4, y), fill=WHT, outline=BLK)
        for x in range(48 - w + 6, 48 + w - 4, 3): d.line((x, y - h + 3, x, y - 1), fill=BLK)
        d.polygon([(48 - w - 2, y - h + 2), (48 - w + 4, y - h - 3), (48 + w - 4, y - h - 3), (48 + w + 2, y - h + 2)], fill=BLK)
        y -= h + 3
    d.ellipse((46, y - 1, 50, y + 3), fill=BLK); d.line((48, y - 4, 48, y), fill=BLK)
    frame(d); return im

@reg('itsukushima-torii')
def torii():
    im, d = canvas(); water(im, 44)
    sun(im, d, 70, 12, 8)
    d.polygon([(0, 30), (16, 22), (30, 28), (44, 20), (60, 32), (60, 44), (0, 44)], fill=BLK)       # Miyajima hills
    fill_pattern(im, (1, 30, 40, 43), 0)
    shade(im, lambda dd: dd.polygon([(0, 30), (16, 22), (30, 28), (44, 20), (60, 32), (60, 44), (0, 44)], fill=1), 3)
    cx = 48
    d.rectangle((cx - 17, 16, cx - 13, 56), fill=BLK); d.rectangle((cx + 13, 16, cx + 17, 56), fill=BLK)
    d.polygon([(cx - 26, 12), (cx - 22, 16), (cx + 22, 16), (cx + 26, 12), (cx + 20, 13), (cx - 20, 13)], fill=BLK)   # kasagi
    d.rectangle((cx - 22, 20, cx + 22, 22), fill=BLK)                        # nuki
    d.rectangle((cx - 2, 16, cx + 2, 20), fill=BLK)
    for x in (cx - 22, cx + 18): d.rectangle((x, 26, x + 4, 56), fill=BLK)  # support posts
    d.line((cx - 22, 30, cx - 13, 30), fill=BLK); d.line((cx + 13, 30, cx + 22, 30), fill=BLK)
    frame(d); return im

@reg('sydney-opera-house')
def opera():
    im, d = canvas()
    d.arc((54, 14, 120, 66), 200, 340, fill=BLK); d.arc((54, 17, 120, 69), 200, 340, fill=BLK)
    d.line((52, 38, W - 2, 38), fill=BLK)
    for x in range(60, W - 2, 5): d.line((x, 38, x, 30 + abs(x - 87) // 4), fill=BLK)
    water(im, 52)
    d.rectangle((4, 46, 74, 51), fill=BLK)
    for (xr, r) in ((22, 26), (38, 24), (50, 18), (62, 14), (70, 9)):
        d.pieslice((xr - r, 46 - r, xr + r, 46 + r), 180, 270, fill=WHT, outline=BLK)
        d.line((xr - r // 3, 46 - r + 3, xr - 1, 45), fill=BLK)
    frame(d); return im

@reg('uluru')
def uluru():
    im, d = canvas()
    sun(im, d, 80, 10, 6)
    fill_pattern(im, (1, 50, W - 1, H - 1), 1); d.line((1, 50, W - 2, 50), fill=BLK)
    rock = [(4, 50), (10, 36), (20, 30), (50, 28), (74, 30), (86, 36), (92, 50)]
    d.polygon(rock, fill=BLK)
    shade(im, lambda dd: dd.polygon([(10, 36), (20, 30), (50, 28), (74, 30), (86, 36), (60, 34), (30, 34)], fill=1), 3)
    for x in range(16, 88, 7): d.line((x, 36, x + 2, 50), fill=WHT)        # erosion gullies
    for x in (14, 40, 70): d.polygon([(x - 3, 58), (x, 53), (x + 3, 58)], fill=BLK); d.line((x, 58, x, 60), fill=BLK)   # spinifex
    frame(d); return im

@reg('burj-khalifa')
def burj_khalifa():
    im, d = canvas(); fill_pattern(im, (1, 58, W - 1, H - 1), 1)
    city_fill(im, d, 58, seed=21, hmin=6, hmax=16)
    cx = 50
    steps = [(58, 9), (46, 7), (36, 6), (27, 5), (19, 4), (12, 3), (7, 2)]
    for (y, w), (y2, _) in zip(steps, steps[1:] + [(2, 0)]):
        d.rectangle((cx - w, y2, cx + w, y), fill=BLK)
        d.rectangle((cx - w - 2, y - 3, cx - w, y), fill=BLK); d.rectangle((cx + w, y - 6, cx + w + 2, y), fill=BLK)
    d.line((cx, 0, cx, 4), fill=BLK)
    for y in range(10, 56, 4): d.point((cx, y), fill=WHT)
    frame(d); return im

@reg('marina-bay-sands')
def marina_bay():
    im, d = canvas(); water(im, 52)
    for x in (24, 46, 68):
        d.polygon([(x - 6, 52), (x - 5, 18), (x + 5, 18), (x + 6, 52)], fill=BLK)
        for y in range(22, 50, 4): d.line((x - 4, y, x + 4, y), fill=WHT)
    d.polygon([(10, 16), (88, 14), (90, 18), (12, 19)], fill=BLK)             # SkyPark "ship"
    d.polygon([(80, 14), (90, 14), (88, 18), (80, 18)], fill=BLK)
    # ArtScience Museum lotus
    for i in range(5): d.line((6 + i * 2, 52, 2 + i * 3, 42 - abs(i - 2) * 2), fill=BLK)
    frame(d); return im

@reg('taipei-101')
def taipei101():
    im, d = canvas(); city_fill(im, d, 60, seed=14, hmin=4, hmax=10)
    cx = 48
    d.rectangle((cx - 7, 44, cx + 7, 60), fill=BLK)
    y = 44
    for i in range(8):
        d.polygon([(cx - 5, y), (cx - 7, y - 4), (cx + 7, y - 4), (cx + 5, y)], fill=BLK)
        d.line((cx - 6, y - 4, cx + 6, y - 4), fill=WHT); y -= 4
    d.rectangle((cx - 3, y - 4, cx + 3, y), fill=BLK); d.line((cx, y - 12, cx, y - 4), fill=BLK)
    d.ellipse((cx - 2, 48, cx + 2, 52), fill=WHT)                            # coin motif
    frame(d); return im

@reg('golden-temple-amritsar')
def golden_temple():
    im, d = canvas(); water(im, 44)
    d.rectangle((1, 38, W - 2, 44), fill=WHT, outline=BLK)
    d.rectangle((18, 22, 78, 40), fill=BLK)
    fill_pattern(im, (20, 24, 77, 39), 2)
    for x in range(22, 76, 5): d.chord((x, 28, x + 3, 36), 180, 360, fill=WHT); d.rectangle((x, 32, x + 3, 36), fill=WHT)
    d.rectangle((16, 20, 80, 22), fill=BLK)
    d.rectangle((38, 14, 58, 20), fill=BLK)
    onion(d, 48, 14, 6, fill=BLK)
    for x in (22, 74, 30, 66): onion(d, x, 20, 2.2, fill=BLK)
    d.rectangle((1, 52, 30, 54), fill=BLK); d.rectangle((66, 52, 95, 54), fill=BLK)   # causeway & reflection hint
    frame(d); return im

@reg('table-mountain')
def table_mountain():
    im, d = canvas(); water(im, 54)
    d.polygon([(0, 46), (8, 30), (14, 18), (20, 16), (24, 22), (30, 20), (34, 14), (74, 14), (78, 20), (86, 30), (96, 40), (96, 52), (0, 52)], fill=BLK)
    d.polygon([(30, 13), (78, 13), (76, 9), (62, 10), (46, 8), (32, 10)], fill=WHT, outline=BLK)     # tablecloth cloud
    for x in range(36, 76, 4): d.line((x, 14, x + 1, 18), fill=WHT)
    city_fill(im, d, 54, seed=11, hmin=2, hmax=7, x0=6, x1=90, wmin=2, wmax=5)
    frame(d); return im

@reg('kremlin-spasskaya-tower')
def kremlin():
    im, d = canvas(); ground(im, d)
    d.rectangle((1, 40, W - 2, 58), fill=WHT, outline=BLK)
    for x in range(2, W - 2, 4): d.rectangle((x, 37, x + 2, 40), fill=BLK); d.polygon([(x, 37), (x + 1, 35), (x + 2, 37)], fill=BLK)   # swallowtail merlons
    cx = 48
    d.rectangle((cx - 8, 24, cx + 8, 58), fill=WHT, outline=BLK)
    d.rectangle((cx - 4, 46, cx + 4, 58), fill=BLK); d.chord((cx - 4, 42, cx + 4, 50), 180, 360, fill=BLK)
    d.rectangle((cx - 6, 14, cx + 6, 24), fill=WHT, outline=BLK)
    d.ellipse((cx - 4, 15, cx + 4, 23), fill=WHT, outline=BLK); d.line((cx, 19, cx, 16), fill=BLK); d.line((cx, 19, cx + 2, 20), fill=BLK)
    d.polygon([(cx - 6, 14), (cx, 0 + 4), (cx + 6, 14)], fill=BLK)
    d.polygon([(cx, 0), (cx - 2, 3), (cx + 2, 3)], fill=BLK); d.point((cx, 4), fill=WHT)   # star
    for x in (cx - 8, cx + 8): d.polygon([(x - 2, 24), (x, 19), (x + 2, 24)], fill=BLK)
    onion(d, 18, 40, 4, fill=WHT, outline=BLK); onion(d, 78, 40, 4, fill=WHT, outline=BLK)
    frame(d); return im

if __name__ == '__main__':
    for n, f in REG.items(): save(f(), CAT, n)
    print(len(REG))
