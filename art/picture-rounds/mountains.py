#!/usr/bin/env python3
"""Famous mountains & volcanoes as 1-bit silhouettes in the landmark style. Profiles in a 0-100 x 0-60 box (y up)."""
import sys, math
from PIL import Image, ImageDraw
from common import *

def smooth(pts, n=6):
    """Catmull-Rom through the points (keeps sharp peaks reasonably sharp with low n)."""
    out = []
    P = [pts[0]] + pts + [pts[-1]]
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        for k in range(n):
            t = k / n; t2, t3 = t * t, t * t * t
            out.append(tuple(.5 * ((2 * p1[j]) + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t2 + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t3) for j in (0, 1)))
    out.append(pts[-1]); return out

BASE = 56
def P(x, y): return (1 + x * .94, BASE - y * .82)
def poly(pts, sm=True): return [P(*p) for p in (smooth(pts) if sm else pts)]

def scene(profile, snow=None, sm=True, water_y=None, lit_side=None, extra=None, cloud_spots=((6, 8), (70, 6))):
    im, d = canvas()
    if cloud_spots: clouds(d, cloud_spots)
    body = poly(profile, sm) + [P(100, -5), P(0, -5)]
    d.polygon(body, fill=BLK)
    if lit_side:                                         # dithered sunlit face: polygon in profile units
        shade(im, lambda dd: dd.polygon(poly(lit_side, False), fill=1), 3)
    if snow:
        for s in snow: d.polygon(poly(s, False), fill=WHT)
        d.line(poly(profile, sm), fill=BLK)                 # keep the skyline crisp against white snow
    if extra: extra(im, d)
    if water_y is not None:
        y = int(BASE - water_y * .8); d.rectangle((1, y, W - 2, H - 2), fill=WHT); water(im, y + 1)
        d.line((1, y, W - 2, y), fill=BLK)
    else:
        d.rectangle((1, BASE, W - 2, H - 2), fill=BLK)
    frame(d); return im

def matterhorn():
    prof = [(0, 6), (14, 12), (26, 20), (36, 30), (44, 40), (50, 50), (54, 58), (56, 62), (59, 63), (62, 61), (62.5, 56), (64, 50), (68, 44), (74, 36), (82, 28), (92, 20), (100, 15)]
    snow = [[(55, 59), (56, 62), (59, 63), (61, 60), (58, 56), (57, 50), (55, 54)],
            [(62.5, 55), (64, 50), (68, 44), (70, 41), (66, 43), (63, 48)], [(46, 42), (49, 47), (50, 42), (48, 36)], [(76, 34), (80, 30), (74, 32)]]
    return scene(prof, snow, sm=False)

def fuji():
    prof = [(0, 4), (14, 9), (26, 17), (35, 28), (41, 39), (45, 48), (47, 50), (50, 49), (53, 50), (55, 48), (59, 39), (65, 28), (74, 17), (86, 9), (100, 4)]
    snow = [[(45, 48), (47, 50), (50, 49), (53, 50), (55, 48), (59, 39), (61.5, 34), (59, 36), (58, 31), (56, 37), (54, 30), (52, 37), (50, 29), (48, 37), (46, 31), (44, 37), (42, 32), (41, 38), (39.5, 35), (41, 39)]]
    return scene(prof, snow, sm=False, water_y=4)

def kilimanjaro():
    prof = [(0, 4), (10, 10), (20, 19), (30, 30), (38, 37), (44, 40), (52, 41), (60, 41), (66, 39), (71, 35), (75, 32), (78, 36), (80, 33), (82, 37), (84, 33), (88, 24), (94, 14), (100, 9)]
    snow = [[(38, 37), (44, 40), (52, 41), (60, 41), (66, 39), (64, 35), (61, 37), (58, 34), (55, 37), (52, 33), (49, 37), (46, 34), (43, 37), (41, 34)]]
    def acacia(im, d):
        for x, h in ((12, 10), (86, 8), (30, 6)):
            px, py = P(x, 0); d.line((px, py, px, py - h), fill=BLK); d.line((px, py - h + 3, px - 3, py - h), fill=BLK)
            d.ellipse((px - 8, py - h - 3, px + 6, py - h + 1), fill=BLK)
    return scene(prof, snow, sm=False, extra=acacia, cloud_spots=((4, 14), (74, 12)))

def table_mountain():
    prof = [(0, 4), (6, 14), (11, 26), (14, 34), (16, 37), (19, 32), (23, 38), (27, 40), (66, 40), (70, 36), (74, 24), (79, 18), (83, 21), (86, 27), (88, 29), (90, 27), (93, 18), (97, 10), (100, 6)]
    def city(im, d):
        city_fill(im, d, y=BASE, seed=4, hmin=2, hmax=6)
    im = scene(prof, None, sm=False, extra=city, water_y=None)
    d = ImageDraw.Draw(im)
    for x0, x1 in ((30, 40), (46, 58)):                                # the "tablecloth" of cloud on the top
        a, b = P(x0, 41), P(x1, 41); d.ellipse((a[0], a[1] - 3, b[0], b[1] + 3), fill=WHT, outline=BLK)
    return im

def sugarloaf():
    prof = [(0, 3), (6, 10), (12, 14), (18, 15), (24, 11), (28, 9), (32, 14), (35, 26), (38, 40), (42, 50), (46, 54), (50, 55), (54, 53), (57, 46), (59, 34), (60, 20), (61, 6), (62, 2), (100, 2)]
    def cable(im, d):
        a, b = P(16, 15), P(46, 54); d.line((a[0], a[1], b[0], b[1]), fill=BLK)
        m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2 + 1); d.rectangle((m[0] - 2, m[1], m[0] + 2, m[1] + 3), fill=BLK)
    return scene(prof, None, sm=True, water_y=2, extra=cable)

def half_dome():
    prof = [(0, 8), (12, 16), (26, 26), (38, 37), (48, 46), (56, 51), (62, 53), (67, 52.5), (70, 51), (71.5, 48), (72, 36), (72.5, 22), (74, 14), (82, 10), (100, 8)]
    lit = [(71.5, 48), (72, 36), (72.5, 22), (74, 14), (64, 14), (64, 44), (70, 51)]
    def pines(im, d):
        for x in range(4, 96, 7):
            px, py = P(x, 0); h = 6 + (x * 7) % 5
            d.polygon([(px - 3, py), (px, py - h), (px + 3, py)], fill=BLK)
    im = scene(prof, None, sm=True, extra=pines)
    m = Image.new('1', im.size, 0); ImageDraw.Draw(m).polygon(poly(lit, False), fill=1)
    full = Image.new('1', im.size, WHT); fill_pattern(full, (0, 0, W, H), 5); im.paste(full, (0, 0), m)   # sheer face, streaked
    return im

def uluru():
    prof = [(0, 1), (8, 2), (11, 8), (13, 15), (16, 19), (22, 21), (36, 22), (52, 22.5), (68, 21.5), (80, 20), (86, 17), (89, 11), (91, 4), (94, 1), (100, 1)]
    def scrub(im, d):
        for x in range(2, 96, 5):
            px, py = P(x, 0); d.ellipse((px - 2, py - 2 - (x % 3), px + 2, py + 1), fill=BLK)
    im = scene(prof, None, sm=True, extra=scrub, cloud_spots=((10, 10), (60, 14)))
    sun(im, ImageDraw.Draw(im), 82, 14); return im

def devils_tower():
    prof = [(0, 4), (16, 10), (26, 14), (31, 16), (33, 26), (34.5, 40), (36, 47), (38, 49), (58, 49), (60, 47), (61.5, 40), (63, 26), (64.5, 16), (70, 14), (84, 9), (100, 4)]
    im = scene(prof, None, sm=False, cloud_spots=((6, 8), (74, 10)))
    d = ImageDraw.Draw(im)
    for x in range(36, 61, 3):                                              # the famous columns
        a, b = P(x, 47), P(x + (x - 48) * .12, 18); d.line((a[0], a[1], b[0], b[1]), fill=WHT)
    talus = poly([(20, 12), (30, 15), (40, 17), (56, 17), (66, 15), (76, 12)])
    for i in range(len(talus) - 1): d.line((talus[i], talus[i + 1]), fill=WHT)
    for x in range(10, 90, 4):
        px, py = P(x, 4 + (x % 3)); d.point((px, py), fill=WHT)
    return im

def vesuvius():
    prof = [(0, 4), (10, 11), (20, 20), (27, 27), (31, 30), (34, 29), (38, 26), (42, 25), (46, 27), (51, 33), (56, 39), (60, 41), (65, 40.5), (69, 38), (75, 30), (84, 19), (94, 10), (100, 7)]
    im = scene(prof, None, sm=True, water_y=4)
    d = ImageDraw.Draw(im); y = int(BASE - 4 * .82)
    for x in range(2, 40, 4):                                              # Naples waterfront
        h = 2 + (x * 5) % 4; d.rectangle((x, y - h, x + 2, y), fill=BLK)
    d.polygon([(70, y + 5), (77, y + 5), (74, y - 3)], fill=WHT, outline=BLK)  # a sail on the bay
    return im

def st_helens():
    prof = [(0, 4), (14, 10), (26, 19), (36, 29), (42, 35), (45, 37), (48, 33), (52, 31), (56, 31.5), (60, 35), (63, 38), (66, 35), (74, 26), (86, 15), (100, 6)]
    snow = [[(42, 35), (45, 37), (47, 34), (44, 31), (41, 33)], [(60, 35), (63, 38), (66, 35), (64, 31), (62, 33)], [(30, 22), (33, 26), (32, 20)], [(70, 30), (72, 28), (69, 26)]]
    im = scene(prof, snow, sm=False, cloud_spots=((6, 10), (78, 8)))
    d = ImageDraw.Draw(im)
    for cx, cy, r in ((53, 26, 5), (50, 19, 6), (55, 13, 7), (48, 8, 6)):     # ash/steam column from the crater
        m = Image.new('1', im.size, 0); ImageDraw.Draw(m).ellipse((cx - r, cy - r, cx + r, cy + r), fill=1)
        full = Image.new('1', im.size, WHT); fill_pattern(full, (0, 0, W, H), 1); im.paste(full, (0, 0), m)
        d.arc((cx - r, cy - r, cx + r, cy + r), 140, 400, fill=BLK)
    return im

def mittens():
    def butte(x0, w, top):
        return [(x0 - 6, 6), (x0 - 2, 10), (x0, 20), (x0 + 1, top), (x0 + w, top), (x0 + w + 1, 20), (x0 + w + 3, 10), (x0 + w + 7, 6)]
    prof = [(0, 4)] + butte(8, 22, 42) + butte(56, 24, 40) + [(100, 4)]
    im = scene(prof, None, sm=False, cloud_spots=((40, 6), (82, 8)))
    d = ImageDraw.Draw(im)
    for x, top, w in ((33, 36, 3.5), (83, 34, 3.5)):                      # the slender "thumbs"
        d.polygon(poly([(x, 10), (x, top - 3), (x + .8, top), (x + w, top), (x + w, 10)], False), fill=BLK)
    fill_pattern(im, (1, int(BASE - 6), W - 1, BASE), 2)
    return im

def everest():
    prof = [(0, 14), (10, 20), (20, 26), (28, 32), (34, 38), (40, 46), (46, 54), (50, 59), (53, 60), (56, 57), (62, 50), (70, 42), (76, 40), (82, 44), (86, 41), (92, 34), (100, 30)]
    nuptse = [(0, 10), (14, 16), (24, 22), (32, 26), (38, 28), (44, 27), (50, 26), (58, 28), (64, 26), (72, 22), (84, 16), (100, 12)]
    im, d = canvas(); fill_pattern(im, (1, 1, W - 1, BASE), 1)              # thin high-altitude sky
    d.polygon(poly(prof, False) + [P(100, -5), P(0, -5)], fill=BLK)
    for s_ in ([(40, 46), (46, 54), (50, 59), (53, 60), (52, 52), (48, 47), (45, 42)], [(76, 40), (82, 44), (86, 41), (82, 37)]):
        d.polygon(poly(s_, False), fill=WHT)
    d.line(poly(prof, False), fill=BLK)
    pts = [P(53 + i * 7, 59 - i) for i in range(5)]                          # summit snow plume streaming east
    for i, (x, y) in enumerate(pts):
        r = 2 + i; d.ellipse((x - r, y - r / 1.6, x + r + 3, y + r / 1.6), fill=WHT)
    d.polygon(poly(nuptse, False) + [P(100, -5), P(0, -5)], fill=WHT, outline=BLK)   # snowy Nuptse ridge in front
    shade(im, lambda dd: dd.polygon(poly([(0, 10), (14, 16), (24, 22), (32, 26), (38, 28), (38, 0), (0, 0)], False), fill=1), 6)
    d.rectangle((1, BASE, W - 2, H - 2), fill=BLK); frame(d)
    return im

ITEMS = {'matterhorn': matterhorn, 'mount-fuji': fuji, 'kilimanjaro': kilimanjaro, 'table-mountain': table_mountain,
         'sugarloaf-mountain': sugarloaf, 'half-dome': half_dome, 'uluru': uluru, 'devils-tower': devils_tower,
         'vesuvius': vesuvius, 'mount-st-helens': st_helens}
if __name__ == '__main__':
    for k in sys.argv[1:] or ITEMS: save(ITEMS[k](), 'mountains', k)
