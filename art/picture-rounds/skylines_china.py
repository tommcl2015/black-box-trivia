#!/usr/bin/env python3
"""Skylines of China's biggest cities (5 million+) — 1-bit pixel art."""
import math, random
from PIL import Image, ImageDraw
from common import *
from skylines_world import back, front, needle, setback, lit

CAT = 'skylines'
REG = {}
def reg(name):
    def deco(fn): REG[name] = fn; return fn
    return deco

@reg('shanghai')
def shanghai():
    im, d = canvas(); water(im, 56)
    back(im, d, 54, seed=201, hmax=14)
    # Oriental Pearl Tower: three legs, big and small spheres
    cx = 20
    d.line((cx - 6, 54, cx - 1, 30), fill=BLK, width=2); d.line((cx + 6, 54, cx + 1, 30), fill=BLK, width=2)
    d.rectangle((cx - 1, 6, cx + 1, 54), fill=BLK)
    d.ellipse((cx - 7, 34, cx + 7, 48), fill=BLK); d.ellipse((cx - 5, 18, cx + 5, 28), fill=BLK); d.ellipse((cx - 2, 10, cx + 2, 14), fill=BLK)
    d.point((cx - 3, 38), fill=WHT); d.point((cx - 2, 21), fill=WHT); d.line((cx, 0, cx, 6), fill=BLK)
    # Jin Mao (pagoda-like setbacks)
    y = 54
    for i, w in enumerate((5, 5, 4, 4, 3, 3, 2)):
        d.rectangle((40 - w, y - 6, 40 + w, y), fill=BLK); d.point((40 - w, y - 6), fill=WHT); d.point((40 + w, y - 6), fill=WHT); y -= 6
    d.polygon([(38, y), (40, y - 6), (42, y)], fill=BLK)
    # Shanghai World Financial Center: the "bottle opener"
    d.polygon([(54, 54), (55, 6), (61, 6), (62, 54)], fill=BLK)
    d.rectangle((56, 8, 60, 12), fill=WHT)
    # Shanghai Tower: tall, twisting taper
    for y in range(2, 55):
        t = (y - 2) / 52; w = 2 + 5 * t; off = math.sin(t * 3) * 1.2
        d.line((76 - w + off, y, 76 + w + off, y), fill=BLK)
    for y in range(6, 54, 5): d.point((76 + math.sin(y / 9) * 3, y), fill=WHT)
    front(im, d, 54, 202, 2, 6, x0=84)
    frame(d); return im

@reg('beijing')
def beijing():
    im, d = canvas(); ground(im, d, 58)
    back(im, d, 56, seed=211, hmax=12)
    # CCTV Headquarters: the leaning loop
    d.polygon([(10, 56), (16, 18), (22, 18), (18, 56)], fill=BLK)
    d.polygon([(34, 56), (40, 28), (46, 28), (42, 56)], fill=BLK)
    d.polygon([(16, 18), (44, 14), (46, 28), (40, 28), (40, 22), (22, 24)], fill=BLK)
    d.rectangle((10, 50, 42, 56), fill=BLK)
    for y in range(22, 54, 4): d.point((17, y), fill=WHT); d.point((41, y + 2), fill=WHT)
    # CITIC Tower "China Zun" (ancient wine-vessel shape)
    pts = []
    for i in range(21):
        t = i / 20; y = 56 - 52 * t; w = 6 - 2.2 * math.sin(math.pi * t) + (1.5 if t > 0.9 else 0)
        pts.append((64 - w, y))
    d.polygon(pts + [(128 - x, y) for x, y in reversed(pts)], fill=BLK)
    for y in range(8, 56, 4): d.line((60, y, 68, y), fill=WHT)
    # Gate tower with double-eave roof (Tiananmen-style)
    d.rectangle((76, 44, 94, 56), fill=WHT, outline=BLK); d.rectangle((83, 48, 87, 56), fill=BLK)
    d.polygon([(74, 44), (77, 40), (93, 40), (96, 44)], fill=BLK); d.rectangle((79, 36, 91, 40), fill=WHT, outline=BLK)
    d.polygon([(76, 36), (79, 32), (91, 32), (94, 36)], fill=BLK)
    frame(d); return im

@reg('guangzhou')
def guangzhou():
    im, d = canvas(); water(im, 56)
    back(im, d, 54, seed=221, hmax=14)
    # Canton Tower: twisted hourglass lattice
    for y in range(6, 55):
        t = (y - 6) / 48; w = 2 + 6 * abs(t - 0.6) ** 1.1 * (1.6 if t > 0.6 else 1)
        d.point((30 - w, y), fill=BLK); d.point((30 + w, y), fill=BLK)
        if y % 3 == 0: d.line((30 - w, y, 30 + w, y), fill=BLK)
    for y in range(8, 54, 6): d.line((30 - 4, y, 30 + 4, y + 6), fill=BLK)
    d.line((30, 0, 30, 6), fill=BLK, width=2)
    # Guangzhou IFC and CTF Finance Centre
    d.polygon([(54, 54), (55, 10), (59, 8), (63, 10), (64, 54)], fill=BLK)
    for y in range(12, 54, 6): d.line((55, y, 63, y + 3), fill=WHT); d.line((63, y, 55, y + 3), fill=WHT)
    setback(d, 76, 54, [(5, 28), (4, 8), (3, 6)]); d.line((76, 8, 76, 12), fill=BLK)
    for y in range(14, 54, 3): d.line((73, y, 73, y + 1), fill=WHT)
    front(im, d, 54, 222, 2, 8, x0=84)
    frame(d); return im

@reg('shenzhen')
def shenzhen():
    im, d = canvas(); water(im, 58)
    back(im, d, 56, seed=231, hmax=16)
    # Ping An Finance Centre: tall, tapered, with a spire
    d.polygon([(38, 56), (40, 10), (44, 6), (48, 10), (50, 56)], fill=BLK)
    d.line((44, 0, 44, 6), fill=BLK)
    for x in (40, 44, 48): d.line((x, 14, x, 54), fill=WHT)
    # KK100 (rounded crown)
    d.rectangle((62, 16, 70, 56), fill=BLK); d.chord((62, 10, 70, 24), 180, 360, fill=BLK)
    for y in range(18, 56, 3): d.line((63, y, 69, y), fill=WHT)
    # China Resources "Spring Bamboo" tower
    d.rectangle((16, 18, 24, 56), fill=BLK); d.polygon([(16, 18), (20, 8), (24, 18)], fill=BLK)
    for x in range(17, 24, 2): d.line((x, 18, x, 54), fill=WHT)
    front(im, d, 56, 232, 3, 9, x0=74)
    frame(d); return im

@reg('chongqing')
def chongqing():
    im, d = canvas(); water(im, 54)
    # hills
    d.polygon([(0, 54), (0, 34), (20, 28), (50, 32), (80, 26), (96, 30), (96, 54)], fill=WHT, outline=BLK)
    fill_pattern(im, (1, 30, W - 1, 54), 6)
    back(im, d, 50, seed=241, hmax=14)
    # Raffles City: row of towers bridged by the horizontal "Crystal"
    for i, x in enumerate((36, 46, 56, 66)):
        h = 36 if i in (1, 2) else 30
        d.polygon([(x - 3, 50), (x - 3, 50 - h), (x + 3, 50 - h - 2), (x + 3, 50)], fill=BLK)
        for y in range(50 - h + 2, 50, 4): d.line((x - 2, y, x + 2, y), fill=WHT)
    d.rectangle((40, 14, 62, 18), fill=BLK); d.line((41, 16, 61, 16), fill=WHT)
    for x in (28, 74): d.polygon([(x - 3, 50), (x - 3, 10), (x, 6), (x + 3, 10), (x + 3, 50)], fill=BLK)
    # Hongyadong stilted houses at the river
    d.rectangle((2, 40, 22, 50), fill=WHT, outline=BLK)
    for y in (40, 45): d.polygon([(0, y), (4, y - 3), (20, y - 3), (24, y)], fill=BLK)
    for x in range(4, 22, 3): d.rectangle((x, 46, x + 1, 48), fill=BLK)
    # river cable car
    d.line((1, 22, W - 2, 30), fill=BLK); d.rectangle((84, 28, 88, 32), fill=BLK)
    frame(d); return im

@reg('tianjin')
def tianjin():
    im, d = canvas(); water(im, 54)
    back(im, d, 50, seed=251, hmax=12)
    # Goldin Finance 117: diamond-topped
    d.polygon([(64, 50), (66, 14), (74, 14), (76, 50)], fill=BLK)
    d.polygon([(64, 14), (70, 4), (76, 14)], fill=WHT, outline=BLK); d.line((70, 4, 70, 14), fill=BLK)
    for y in range(18, 50, 4): d.line((67, y, 73, y), fill=WHT)
    # Tianjin Eye: a Ferris wheel on a bridge
    d.ellipse((12, 8, 44, 40), outline=BLK, fill=WHT)
    for a in range(0, 360, 30):
        r = math.radians(a); x, y = 28 + 16 * math.cos(r), 24 + 16 * math.sin(r)
        d.line((28, 24, x, y), fill=BLK); d.rectangle((x - 1, y, x + 1, y + 2), fill=BLK)
    d.line((28, 24, 20, 46), fill=BLK, width=2); d.line((28, 24, 36, 46), fill=BLK, width=2)
    d.rectangle((1, 46, 60, 48), fill=BLK)
    for x in (4, 52): d.chord((x, 48, x + 10, 58), 180, 360, fill=BLK)
    frame(d); return im

@reg('wuhan')
def wuhan():
    im, d = canvas(); water(im, 54)
    back(im, d, 50, seed=261, hmax=12)
    # Yellow Crane Tower: five tiers of flying eaves
    cx = 26
    pagoda(d, cx, 50, 5, 14, 7, 2)
    # Wuhan Yangtze River Bridge
    d.rectangle((44, 44, W - 2, 47), fill=BLK)
    for x in range(48, 95, 12): d.rectangle((x, 47, x + 3, 56), fill=BLK); d.chord((x + 3, 47, x + 12, 55), 180, 360, fill=WHT)
    for x in range(44, 95, 4): d.line((x, 40, x + 2, 44), fill=BLK)
    d.line((44, 40, W - 2, 40), fill=BLK)
    # Wuhan Center tower
    d.polygon([(74, 40), (76, 10), (80, 6), (84, 10), (86, 40)], fill=BLK)
    for y in range(12, 40, 4): d.line((77, y, 83, y), fill=WHT)
    frame(d); return im

@reg('xian')
def xian():
    im, d = canvas(); ground(im, d, 58)
    # City wall with gate tower
    d.rectangle((1, 44, W - 2, 58), fill=WHT, outline=BLK)
    for x in range(2, W - 2, 4): d.rectangle((x, 42, x + 2, 44), fill=BLK)
    d.chord((60, 48, 72, 64), 180, 360, fill=BLK)
    d.rectangle((54, 32, 78, 44), fill=WHT, outline=BLK)
    for x in range(57, 77, 3): d.line((x, 35, x, 43), fill=BLK)
    d.polygon([(50, 33), (54, 28), (78, 28), (82, 33)], fill=BLK); d.rectangle((58, 24, 74, 28), fill=WHT, outline=BLK)
    d.polygon([(54, 24), (58, 20), (74, 20), (78, 24)], fill=BLK)
    # Giant Wild Goose Pagoda: square, stepped brick tiers
    cx = 22; y = 44
    for i in range(7):
        w = 10 - i; h = 5
        d.rectangle((cx - w, y - h, cx + w, y), fill=WHT, outline=BLK)
        d.rectangle((cx - w - 1, y - h, cx + w + 1, y - h + 1), fill=BLK)
        d.rectangle((cx - 1, y - h + 2, cx + 1, y - 1), fill=BLK)
        y -= h
    d.polygon([(cx - 3, y), (cx, y - 5), (cx + 3, y)], fill=BLK)
    frame(d); return im

@reg('hangzhou')
def hangzhou():
    im, d = canvas(); water(im, 46)
    # hills around West Lake
    d.polygon([(0, 46), (0, 30), (20, 22), (40, 28), (60, 18), (80, 26), (96, 22), (96, 46)], fill=WHT, outline=BLK)
    fill_pattern(im, (1, 22, W - 1, 46), 5)
    # Leifeng Pagoda on its hill
    cx = 30
    d.rectangle((cx - 9, 40, cx + 9, 46), fill=BLK)
    pagoda(d, cx, 40, 5, 9, 5, 1)
    # Broken Bridge: a low stone arch
    d.chord((54, 38, 90, 58), 180, 360, fill=WHT, outline=BLK); d.chord((64, 44, 80, 58), 180, 360, fill=BLK)
    d.rectangle((54, 47, 90, 48), fill=WHT)
    # willow branches
    d.line((4, 46, 8, 30), fill=BLK)
    for x in range(2, 16, 2): d.line((8, 30, x, 30 + 10 + (x % 4)), fill=BLK)
    # rowing boat
    d.polygon([(40, 56), (52, 56), (50, 58), (42, 58)], fill=BLK); d.rectangle((44, 53, 48, 56), fill=BLK)
    frame(d); return im

@reg('nanjing')
def nanjing():
    im, d = canvas(); water(im, 58)
    d.polygon([(54, 40), (70, 26), (80, 30), (96, 24), (96, 56), (54, 56)], fill=WHT, outline=BLK)  # Purple Mountain
    fill_pattern(im, (55, 28, W - 1, 56), 6)
    back(im, d, 56, seed=271, hmax=12)
    # Zifeng Tower
    d.polygon([(30, 56), (31, 12), (35, 4), (39, 12), (40, 56)], fill=BLK)
    d.line((35, 0, 35, 4), fill=BLK); d.line((33, 14, 33, 54), fill=WHT)
    # Zhonghua Gate / Ming city wall
    d.rectangle((50, 46, 94, 56), fill=WHT, outline=BLK)
    for x in range(51, 94, 3): d.rectangle((x, 44, x + 1, 46), fill=BLK)
    for x in (58, 70, 82): d.chord((x, 48, x + 8, 60), 180, 360, fill=BLK)
    front(im, d, 56, 272, 3, 10, x0=1, x1=26)
    frame(d); return im

@reg('suzhou')
def suzhou():
    im, d = canvas(); water(im, 54)
    back(im, d, 50, seed=281, hmax=10)
    # Gate to the East ("the big trousers")
    d.polygon([(30, 50), (34, 8), (62, 8), (66, 50), (56, 50), (52, 28), (44, 28), (40, 50)], fill=BLK)
    d.chord((44, 18, 52, 38), 180, 360, fill=WHT)
    for y in range(12, 48, 4): d.line((33 + (50 - y) // 10, y, 38, y), fill=WHT); d.line((58, y, 63 - (50 - y) // 10, y), fill=WHT)
    # Garden pavilion and humpback bridge in front
    d.polygon([(2, 44), (8, 38), (20, 38), (26, 44)], fill=BLK); d.rectangle((6, 44, 22, 50), fill=WHT, outline=BLK)
    for x in (8, 20): d.line((x, 44, x, 50), fill=BLK)
    d.chord((70, 46, 94, 66), 180, 360, fill=WHT, outline=BLK); d.chord((76, 50, 88, 66), 180, 360, fill=BLK)
    frame(d); return im

@reg('harbin')
def harbin():
    im, d = canvas()
    for x, y in ((10, 6), (30, 12), (70, 8), (86, 16), (52, 4)): d.point((x, y), fill=BLK); d.point((x + 1, y + 1), fill=BLK)   # snow
    ground(im, d, 56, 6)
    # Saint Sophia Cathedral: big green onion dome + bell tower
    d.rectangle((20, 34, 60, 56), fill=WHT, outline=BLK)
    for x in range(24, 58, 5): d.chord((x, 40, x + 3, 48), 180, 360, fill=BLK); d.rectangle((x, 44, x + 3, 50), fill=BLK)
    d.rectangle((32, 22, 48, 34), fill=WHT, outline=BLK)
    onion(d, 40, 22, 9, fill=BLK); d.line((40, 0, 40, 4), fill=BLK); d.line((38, 2, 42, 2), fill=BLK)
    d.rectangle((62, 24, 70, 56), fill=WHT, outline=BLK); onion(d, 66, 24, 4, fill=BLK)
    for y in (30, 38): d.rectangle((64, y, 67, y + 4), fill=BLK)
    # ice-sculpture castle blocks
    for x, h in ((76, 16), (84, 24), (90, 12)):
        d.rectangle((x, 56 - h, x + 6, 56), outline=BLK); fill_pattern(im, (x + 1, 57 - h, x + 6, 56), 6)
        d.polygon([(x, 56 - h), (x + 3, 50 - h), (x + 6, 56 - h)], outline=BLK)
    frame(d); return im

@reg('shenyang')
def shenyang():
    im, d = canvas(); ground(im, d, 58)
    back(im, d, 56, seed=291, hmax=12)
    # Fangyuan Building: the ancient-coin-shaped tower
    d.rectangle((48, 10, 76, 56), fill=BLK)
    d.ellipse((50, 12, 74, 36), fill=WHT); d.rectangle((58, 20, 66, 28), fill=BLK)
    for y in range(40, 56, 3):
        for x in range(50, 75, 3): d.point((x, y), fill=WHT)
    # Mukden Palace roofs
    d.polygon([(4, 46), (10, 40), (34, 40), (40, 46)], fill=BLK); d.rectangle((8, 46, 36, 56), fill=WHT, outline=BLK)
    d.polygon([(10, 40), (14, 34), (30, 34), (34, 40)], fill=BLK)
    d.rectangle((14, 30, 30, 34), fill=WHT, outline=BLK); d.polygon([(12, 30), (16, 26), (28, 26), (32, 30)], fill=BLK)
    for x in range(10, 36, 4): d.line((x, 48, x, 56), fill=BLK)
    frame(d); return im

@reg('zhengzhou')
def zhengzhou():
    im, d = canvas(); water(im, 58)
    back(im, d, 56, seed=301, hmax=14)
    # Zhengzhou Greenland Plaza: the "corn cob"
    d.rectangle((40, 14, 54, 56), fill=BLK); d.chord((40, 4, 54, 24), 180, 360, fill=BLK); d.line((47, 0, 47, 6), fill=BLK)
    for y in range(12, 56, 3):
        for x in range(41 + (y % 2), 54, 2): d.point((x, y), fill=WHT)
    # Henan Art Center pebbles + low ring buildings
    for x0, w, h in ((8, 12, 10), (20, 9, 8), (64, 14, 10), (78, 10, 7)): d.chord((x0, 56 - h * 2, x0 + w, 56), 180, 360, fill=WHT, outline=BLK)
    frame(d); return im

@reg('qingdao')
def qingdao():
    im, d = canvas(); water(im, 46)
    # Laoshan hills and red-roofed German-era houses
    d.polygon([(0, 30), (16, 18), (36, 24), (58, 14), (80, 22), (96, 18), (96, 40), (0, 40)], fill=WHT, outline=BLK)
    fill_pattern(im, (1, 18, W - 1, 40), 6)
    for x in range(4, 94, 9):
        y = 36 - (x % 18) // 3
        d.rectangle((x, y, x + 6, 40), fill=WHT, outline=BLK); d.polygon([(x - 1, y), (x + 3, y - 4), (x + 7, y)], fill=BLK)
    d.rectangle((1, 40, W - 2, 46), fill=WHT, outline=BLK)
    # Zhanqiao Pier leading to Huilan Pavilion
    d.rectangle((40, 46, 44, 60), fill=BLK); d.rectangle((40, 50, 60, 52), fill=BLK)
    d.rectangle((60, 46, 72, 56), fill=WHT, outline=BLK)
    d.polygon([(58, 46), (62, 42), (70, 42), (74, 46)], fill=BLK); d.polygon([(61, 42), (64, 38), (68, 38), (71, 42)], fill=BLK)
    d.line((66, 34, 66, 38), fill=BLK)
    frame(d); return im

@reg('chengdu')
def chengdu():
    im, d = canvas(); water(im, 54)
    back(im, d, 46, seed=311, hmax=16)
    # Anshun covered bridge
    d.rectangle((1, 40, 70, 44), fill=BLK)
    for x in (6, 30, 54): d.chord((x, 44, x + 16, 58), 180, 360, fill=WHT, outline=BLK)
    for x in range(4, 70, 10): d.polygon([(x, 40), (x + 2, 36), (x + 8, 36), (x + 10, 40)], fill=BLK)
    d.rectangle((26, 30, 44, 36), fill=WHT, outline=BLK); d.polygon([(22, 30), (28, 24), (42, 24), (48, 30)], fill=BLK)
    # giant panda sitting on the bank
    d.ellipse((76, 34, 92, 52), fill=WHT, outline=BLK)
    d.ellipse((78, 22, 90, 34), fill=WHT, outline=BLK)
    d.ellipse((77, 21, 81, 25), fill=BLK); d.ellipse((87, 21, 91, 25), fill=BLK)             # ears
    d.ellipse((80, 26, 83, 29), fill=BLK); d.ellipse((85, 26, 88, 29), fill=BLK)             # eye patches
    d.point((84, 31), fill=BLK)
    d.rectangle((76, 36, 80, 46), fill=BLK); d.rectangle((88, 36, 92, 46), fill=BLK)         # arms
    d.ellipse((76, 46, 82, 52), fill=BLK); d.ellipse((86, 46, 92, 52), fill=BLK)             # legs
    d.line((74, 20, 72, 46), fill=BLK); d.line((72, 24, 69, 22), fill=BLK)                    # bamboo
    frame(d); return im

@reg('hong-kong-victoria-harbour')
def hk_night():
    """Hong Kong at night — a second, harder view."""
    im, d = canvas(BLK)
    d.polygon([(0, 30), (20, 18), (40, 22), (60, 14), (80, 20), (96, 26), (96, 50), (0, 50)], fill=BLK, outline=WHT)
    r = random.Random(5)
    x = 1
    while x < W - 2:
        w = r.randint(3, 7); h = r.randint(8, 30)
        for y in range(50 - h, 50, 2):
            for xx in range(x, x + w, 2):
                if r.random() < 0.5: im.putpixel((xx, y), WHT)
        x += w + 1
    # Bank of China outline in lights
    d.polygon([(24, 50), (24, 18), (30, 8), (36, 18), (36, 50)], fill=BLK, outline=WHT)
    for y0 in (18, 30, 42): d.line((24, y0 + 10, 30, y0), fill=WHT); d.line((30, y0, 36, y0 + 10), fill=WHT)
    for y in range(52, H - 1, 2):
        for xx in range(1, W - 1):
            if r.random() < 0.12: im.putpixel((xx, y), WHT)
    d.rectangle((0, 0, W - 1, H - 1), outline=BLK)
    return im

if __name__ == '__main__':
    for n, f in REG.items(): save(f(), CAT, n)
    print(len(REG))
