#!/usr/bin/env python3
"""Famous ships: side profiles drawn to real dimensions (metres), bow to the right, sitting in the water."""
import sys, math
from silhouette import *

class Ship:
    def __init__(self, L): self.p = []; self.h = []; self.k = L / 88.0        # metres per output pixel (approx.)
    def px(self, n): return n * self.k
    def add(self, *ps): self.p.extend(ps)
    def hole(self, *ps): self.h.extend(ps)
    def mast(self, x, y0, y1, w=1.0, rake=0.0): self.add(line(x, y0, x - rake, y1, max(self.px(w), 0.1)))
    def funnel(self, c, y0, y1, w, rake=0.0):
        r = (y1 - y0) * math.tan(math.radians(rake))
        self.add([(c - w / 2, y0), (c + w / 2, y0), (c + w / 2 - r, y1), (c - w / 2 - r, y1)])
    def turret(self, c, y, l, h, gun, facing=1):
        self.add([(c - l / 2, y), (c + l / 2, y), (c + l / 2 - 1, y + h), (c - l / 2 + 1, y + h)])
        gx = c + facing * l / 2; self.add(line(gx - facing * 1, y + h * 0.55, gx + facing * gun, y + h * 0.65, self.px(1.0)))

def titanic():
    s = Ship(269)
    s.add([(6, 0), (264, 0), (269, 14), (230, 12.5), (60, 12), (1, 13), (0, 10), (3, 4)])          # hull with counter stern
    s.add(rect(30, 12, 215, 19.5), rect(196, 19.5, 214, 22.5), rect(60, 19.5, 190, 21))              # decks, bridge
    for c in (192, 165, 138, 111): s.funnel(c, 19.5, 43, 7.3, rake=9)
    s.mast(238, 13, 56, rake=4); s.mast(48, 12, 54, rake=4)
    return s

def queen_mary():
    s = Ship(311)
    s.add([(8, 0), (305, 0), (311, 16), (260, 14), (40, 13.5), (2, 14), (0, 10), (4, 3)])             # cruiser stern
    s.add(rect(40, 13.5, 250, 22), rect(70, 22, 236, 27), rect(220, 27, 238, 31))
    for c in (205, 165, 125): s.funnel(c, 27, 52, 11, rake=7)
    s.mast(270, 16, 58, w=1.2, rake=3); s.mast(52, 14, 52, w=1.2, rake=3)
    return s

def bismarck():
    s = Ship(251)
    s.add([(5, 0), (247, 0), (251, 11), (200, 9), (60, 8.5), (1, 8.5), (0, 6), (2, 2)])
    s.turret(196, 9, 14, 5.5, 18, 1); s.add(rect(176, 9, 186, 13)); s.turret(180, 13, 14, 5.5, 18, 1)   # Anton, Bruno (superfiring)
    s.turret(56, 9, 14, 5.5, 18, -1); s.add(rect(66, 9, 76, 13)); s.turret(72, 13, 14, 5.5, 18, -1)      # Dora, Caesar
    s.add(rect(84, 9, 168, 15), rect(140, 15, 166, 22), [(146, 22), (162, 22), (159, 33), (149, 33)], rect(151, 33, 157, 37))  # forward tower
    s.funnel(122, 15, 29, 11, rake=0); s.add(rect(115, 28, 129, 30))
    s.mast(103, 15, 40, w=1.2); s.add(rect(88, 15, 100, 22))
    return s

def missouri():
    s = Ship(270)
    s.add([(5, 0), (262, 0), (270, 14), (230, 11), (160, 8.5), (40, 7.5), (1, 7.5), (0, 5), (2, 2)])     # rising bow sheer
    s.turret(205, 10.3, 16, 6, 20, 1); s.add(rect(184, 9, 196, 15)); s.turret(188, 15, 16, 6, 20, 1)
    s.turret(70, 7.5, 16, 6, 20, -1)
    s.add(rect(88, 8.5, 176, 15), rect(150, 15, 174, 24), [(154, 24), (171, 24), (168, 36), (158, 36)], rect(160, 36, 166, 40))
    s.funnel(140, 15, 28, 8, rake=0); s.funnel(117, 15, 27, 8, rake=0)
    s.mast(128, 15, 44, w=1.2); s.add(rect(96, 15, 108, 22))
    return s

def carrier():
    s = Ship(333)
    s.add([(10, 0), (318, 0), (333, 20), (0, 20), (4, 6)])                     # hull + flight deck
    s.add(rect(-4, 19, 337, 21.5))
    s.add(rect(120, 21.5, 150, 33), rect(124, 33, 146, 40), rect(132, 40, 138, 55))            # island and mast
    for x in (40, 70, 180, 230, 265, 295):
        s.add([(x, 21.5), (x + 15, 21.5), (x + 17, 22.5), (x + 8, 24), (x + 2, 24), (x, 26)])  # parked jets
    return s

def uboat():
    s = Ship(67)
    s.add([(1, 0), (64, 0), (67, 1.4), (40, 1.6), (6, 1.4), (0, 0.9)])
    s.add([(28, 1.5), (38, 1.5), (37.5, 5.0), (29, 5.2), (27, 3.2)])                         # conning tower
    s.mast(33, 5, 9, w=0.8); s.mast(35, 5, 8, w=0.8)                                         # periscopes
    s.add(rect(44, 1.5, 45, 2.6), line(44.5, 2.5, 49, 2.8, s.px(0.8)))                      # deck gun
    return s

def sail(x0, x1, y0, y1, belly=0.6):
    return [(x0, y0), (x1, y0), (x1 + belly, (y0 + y1) / 2), (x1, y1), (x0, y1), (x0 + belly, (y0 + y1) / 2)]

def mayflower():
    s = Ship(36)
    s.add([(3, 0), (27, 0), (31, 4.5), (24, 4.0), (8, 4.0), (5, 7.5), (1, 8), (0, 5)])            # hull, high stern castle
    s.add(line(29, 4.2, 36, 7.5, s.px(1)))                                                    # bowsprit
    for x, h, n in ((24, 24, 2), (15.5, 29, 3), (7, 17, 0)): s.mast(x, 4, h, w=0.9)
    s.add(sail(21, 27, 8, 14, 0.7), sail(21.5, 26.5, 15, 21, 0.6))                            # fore course, topsail
    s.add(sail(11.5, 19.5, 7, 15, 0.8), sail(12.5, 18.5, 16, 23, 0.7), sail(13.5, 17.5, 24, 27.5, 0.5))
    s.add([(7, 6), (7, 16), (2.5, 7)])                                                         # mizzen lateen
    s.add(sail(31.5, 35, 2.5, 5.5, 0.3))                                                      # spritsail
    return s

def victory():
    s = Ship(69)
    s.add([(5, 0), (58, 0), (63, 9), (57, 11), (12, 12), (4, 16), (1, 16), (0, 9), (2, 3)])
    s.add(line(60, 9, 69, 14, s.px(1.2)))
    for x, h in ((52, 50), (33, 60), (15, 42)):
        s.mast(x, 11, h, w=1.0)
        for k, f in enumerate((0.42, 0.62, 0.8)):
            y = 11 + (h - 11) * f; half = (h - 11) * (0.42 - 0.17 * k)
            s.add(line(x - half, y, x + half, y, s.px(0.8)))                                     # yards
    for row, y in enumerate((3.2, 6.3, 9.2)):
        for i in range(10 - row): s.hole(rect(14 + i * 4.5, y, 15.8 + i * 4.5, y + 1.5))         # three rows of gun ports
    return s

def cutty_sark():
    s = Ship(80)
    s.add([(5, 0), (60, 0), (64, 4.5), (8, 4.0), (1, 4.6), (0, 3.2), (2, 1)])
    s.add(line(62, 4.2, 76, 8.5, s.px(1)))
    for x, h in ((50, 44), (35, 47), (19, 40)):
        s.mast(x, 4, h, w=0.9); hh = h - 6; w0 = 8 if x != 19 else 6.5
        for k in range(4):
            y0 = 6 + k * (hh / 4); y1 = y0 + hh / 4 - 0.8; w = w0 * (1 - 0.16 * k)
            s.add(sail(x - w, x + w, y0, y1, 0.5))
    s.add([(52, 26), (72, 7.5), (58, 7)], [(53, 34), (75, 9), (70, 8.8)])                     # jibs
    s.add([(4, 6), (17, 6), (17, 24)])                                                         # spanker
    return s

def longship():
    s = Ship(25)
    s.add([(3, 0), (20, 0), (23, 2.2), (24.4, 5.5), (24.8, 7.2), (24, 7.8), (23, 6.5), (21.5, 2.6), (4, 2.6), (2, 6.5), (1, 7.8), (0.2, 7.2), (0.6, 5.5), (1.8, 2.2)])
    for i in range(11):
        x = 4.6 + i * 1.55; s.add(circle(x, 2.7, 0.62, 14))                                    # shields
        s.add(line(x + 0.4, 2.3, x - 1.6, -0.6, s.px(0.6)))                                      # oars
    s.mast(12.4, 2.6, 13.5, w=1.0)
    s.add(sail(7.6, 17.2, 5, 12.5, 0.6))
    for k in range(4): s.hole(rect(7.9 + k * 2.4, 5.3, 8.9 + k * 2.4, 12.2))                    # striped sail
    return s

def junk():
    s = Ship(32)
    s.add([(4, 0), (26, 0), (30, 3.5), (31, 5), (24, 4), (8, 4.2), (2, 7.5), (0, 7.5), (0.5, 4), (2, 1)])
    for x, h, w, sh in ((24.5, 15, 6.5, 6.5), (15, 21, 9, 8.5), (5.5, 14.5, 5.5, 8.0)):
        s.mast(x, 4, h + 0.5, w=0.8)
        y0, y1 = sh, h
        s.add([(x - w * 0.55, y0), (x + w * 0.45, y0), (x + w * 0.35, y1), (x - w * 0.05, y1 + 0.5), (x - w * 0.6, y1 - 1)])
        n = 5
        for k in range(1, n): s.hole(line(x - w * 0.7, y0 + (y1 - y0) * k / n, x + w * 0.6, y0 + (y1 - y0) * k / n + 0.3, s.px(0.5)))   # battens
    return s

def paddle_steamer():
    s = Ship(80)
    s.add([(8, 0), (74, 0), (80, 2.2), (6, 2.2)])
    s.add(rect(10, 2.2, 66, 6), rect(14, 6, 60, 9.5), rect(30, 9.5, 52, 12), rect(40, 12, 48, 15))    # wedding-cake decks, pilot house
    s.hole(*[rect(16 + i * 3.2, 7, 17.4 + i * 3.2, 8.6) for i in range(13)])
    s.hole(*[rect(12 + i * 3.6, 3.2, 13.6 + i * 3.6, 5) for i in range(15)])
    for x in (54, 59): s.add(rect(x, 9.5, x + 1.6, 27), [(x - 0.9, 27), (x + 2.5, 27), (x + 2.0, 28.5), (x - 0.4, 28.5)])   # twin stacks
    s.add(circle(5, 4.5, 5.2, 30)); s.hole(circle(5, 4.5, 4.0, 30))                             # stern wheel
    for a in range(0, 180, 30):
        r = math.radians(a); s.add(line(5 - 4 * math.cos(r), 4.5 - 4 * math.sin(r), 5 + 4 * math.cos(r), 4.5 + 4 * math.sin(r), s.px(0.7)))
    return s

def trireme():
    s = Ship(40)
    s.add([(4, 0), (34, 0), (39, -0.2), (39.5, 0.6), (35, 1.0), (34, 3.2), (6, 3.2), (2, 5.5), (0.5, 7.0), (0, 6.5), (1.2, 4.5), (2.5, 1.5)])
    for i in range(17): s.add(line(8 + i * 1.5, 2.0, 5.5 + i * 1.5, -1.0, s.px(0.6)))
    s.mast(20, 3.2, 14, w=1.0); s.add(sail(15, 25, 7, 13, 0.5))
    s.hole(*[circle(36.5, 1.8, 0.5, 10)])                                                       # painted eye
    return s

SHIPS = {'titanic': titanic, 'queen-mary': queen_mary, 'bismarck': bismarck, 'uss-missouri': missouri,
         'aircraft-carrier': carrier, 'u-boat': uboat, 'mayflower': mayflower, 'hms-victory': victory,
         'cutty-sark': cutty_sark, 'viking-longship': longship, 'chinese-junk': junk,
         'paddle-steamer': paddle_steamer, 'greek-trireme': trireme}

EXAG = {'titanic': 1.4, 'queen-mary': 1.4, 'bismarck': 1.5, 'uss-missouri': 1.5, 'aircraft-carrier': 1.4, 'u-boat': 1.6, 'greek-trireme': 1.2}

# Traced from real profile drawings on Wikimedia Commons (thresholded to a silhouette, waterline up):
#   bismarck: "Bb bismarck sideview.png" (CC BY-SA 4.0); uss-missouri: "Iowa classe battleships drawing.jpg" (public domain)
TRACED = {'bismarck': 1.45, 'uss-missouri': 1.45}

def traced(slug, ex):
    import os
    from PIL import Image as I
    m = I.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ships_src', slug + '.png')).convert('L')
    m = m.crop(m.getbbox()); m = m.resize((m.width, int(m.height * ex)), I.BOX)
    GY = H - 9; s = min((W - 6) / m.width, (GY - 4) / m.height)
    w, h = max(1, round(m.width * s)), max(1, round(m.height * s))
    small = m.resize((w, h), I.BOX).point(lambda v: 255 if v > 60 else 0).convert('1')
    im = fit_draw([[(0, 0), (1, 0), (1, 0.0001)]], scene='water', pad=3, ground_h=9)     # empty scene: sky, clouds, water
    im.paste(I.new('1', (w, h), BLK), ((W - w) // 2, GY + 1 - h), small)
    return im

if __name__ == '__main__':
    import sys as _s
    for slug in [a for a in (_s.argv[1:] or TRACED) if a in TRACED]: save(traced(slug, TRACED[slug]), 'ships', slug); print('traced', slug)
    if _s.argv[1:] and all(a in TRACED for a in _s.argv[1:]): raise SystemExit
    for slug in [a for a in (sys.argv[1:] or SHIPS) if a not in TRACED]:
        s = SHIPS[slug]()
        ex = EXAG.get(slug, 1.0)                     # long, low hulls get a little extra height, as pixel artists do
        f = lambda ps: [[(x, y * ex) for x, y in q] for q in ps]
        save(fit_draw(f(s.p), scene='water', holes=f(s.h), pad=3, ground_h=9), 'ships', slug); print(slug)
