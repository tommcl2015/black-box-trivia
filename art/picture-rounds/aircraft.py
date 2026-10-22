#!/usr/bin/env python3
"""Famous aircraft — airliners in side view, warplanes in top view (planform), 1-bit."""
import math
from PIL import Image, ImageDraw
from common import *

CAT = 'aircraft'
REG = {}
def reg(name):
    def deco(fn): REG[name] = fn; return fn
    return deco

# ================================================================== side views (airliners & classics)
def airliner(length=84, x0=6, cy=34, r=4, upper=0, upper_len=0, fin=(14, 16), ttail=False,
             wing_eng=2, tail_eng=None, rear_eng=False, rows=1):
    """Side view, nose to the right. upper: extra height of an upper deck; upper_len: its length (0 = full)."""
    im, d = canvas(); clouds(d, [(30, 4), (70, 8)])
    x1 = x0 + length
    top = cy - r; bot = cy + r
    # fuselage outline
    pts = [(x0, top - 1)]
    if upper:
        ux = x0 + 16 if not upper_len else x1 - upper_len
        pts += [(ux - 8, top), (ux, top - upper), (x1 - 14, top - upper)]
        ntop = top - upper
    else:
        pts += [(x1 - 14, top)]; ntop = top
    for i in range(9):                                   # rounded nose
        a = math.radians(-90 + i * 22.5)
        pts.append((x1 - 14 + 14 * math.cos(a), (ntop + bot) / 2 + (bot - ntop) / 2 * math.sin(a)))
    pts += [(x0 + length * 0.3, bot), (x0 + 2, top + 2)]
    d.polygon(pts, fill=BLK)
    # vertical fin, swept back (towards the tail on the left)
    fh, fb = fin; ftop = top - fh
    d.polygon([(x0 + 4 + fb, top), (x0 + 2 + fb * 0.45, ftop), (x0 + 1, ftop), (x0 + 2, top)], fill=BLK)
    # horizontal tailplane
    hy = ftop + 1 if ttail else top + 2
    d.polygon([(x0 + 18, hy), (x0 + 2, hy - 2), (x0 + 1, hy), (x0 + 14, hy + 2)], fill=BLK)
    # low wing, edge-on
    wx = x0 + length * 0.5
    d.polygon([(wx - 14, bot - 1), (wx + 8, bot - 2), (wx + 10, bot), (wx - 10, bot + 2)], fill=BLK)
    def pod(px, py, ln=11, h=5):
        d.rounded_rectangle((px, py, px + ln, py + h), 2, fill=BLK); d.line((px + ln, py + 1, px + ln, py + h - 1), fill=WHT)
    if wing_eng >= 2: pod(wx - 12, bot + 1, 10, 4); d.line((wx - 7, bot, wx - 7, bot + 1), fill=BLK)
    if wing_eng >= 1: pod(wx + 1, bot + 2); d.line((wx + 5, bot, wx + 5, bot + 2), fill=BLK)
    if tail_eng == 'dc10':                                # engine through the fin
        pod(x0 + 2, top - 7, 16, 6)
    if tail_eng == 'sduct':                               # S-duct intake hump ahead of the fin
        d.polygon([(x0 + fb + 4, top), (x0 + fb + 8, top - 4), (x0 + fb + 13, top - 4), (x0 + fb + 13, top)], fill=BLK)
        d.line((x0 + fb + 13, top - 3, x0 + fb + 13, top - 1), fill=WHT)
    if rear_eng:                                          # pods on the rear fuselage
        pod(x0 + 8, cy - 2, 14, 5)
    # windows
    for row in range(rows):
        y = cy - 1 - row * 5
        for x in range(x0 + 18 if row == 0 else (x1 - upper_len if upper_len else x0 + 18), x1 - 14, 3): d.point((x, y), fill=WHT)
    d.line((x1 - 6, (ntop + cy) // 2, x1 - 3, (ntop + cy) // 2), fill=WHT)
    # landing gear
    for gx in (wx + 2, x1 - 12): d.line((gx, bot, gx, bot + 7), fill=BLK); d.ellipse((gx - 2, bot + 6, gx + 2, bot + 10), fill=BLK)
    d.line((1, bot + 11, W - 2, bot + 11), fill=BLK); fill_pattern(im, (1, bot + 12, W - 1, H - 1), 1)
    return im, d

@reg('boeing-707')
def b707():
    im, d = airliner(length=86, r=3, fin=(15, 16), wing_eng=2)
    d.line((14, 16, 20, 13), fill=BLK)          # 707's fin-top HF antenna probe
    frame(d); return im

@reg('boeing-727')
def b727():
    im, d = airliner(length=76, x0=10, r=4, fin=(15, 14), ttail=True, wing_eng=0, rear_eng=True, tail_eng='sduct')
    frame(d); return im

@reg('boeing-737')
def b737():
    im, d = airliner(length=64, x0=16, r=4, fin=(13, 15), wing_eng=1)
    frame(d); return im

@reg('boeing-747')
def b747():
    im, d = airliner(length=86, r=5, upper=4, upper_len=34, fin=(17, 18), wing_eng=2, rows=2)
    frame(d); return im

@reg('mcdonnell-douglas-dc-10')
def dc10():
    im, d = airliner(length=84, r=5, fin=(16, 14), wing_eng=1, tail_eng='dc10')
    frame(d); return im

@reg('lockheed-l-1011-tristar')
def l1011():
    im, d = airliner(length=84, r=5, fin=(16, 14), wing_eng=1, tail_eng='sduct')
    d.rectangle((3, 28, 7, 31), fill=BLK); d.line((3, 29, 3, 30), fill=WHT)       # centre engine exhaust in the tail cone
    frame(d); return im

@reg('airbus-a380')
def a380():
    im, d = airliner(length=86, r=5, upper=6, fin=(16, 18), wing_eng=2, rows=2)
    frame(d); return im

@reg('concorde')
def concorde():
    im, d = canvas(); clouds(d, [(8, 4), (70, 6)])
    cy = 32
    d.polygon([(4, cy - 2), (80, cy - 3), (94, cy + 3), (80, cy + 2), (8, cy + 2)], fill=BLK)       # slender body, drooped nose
    d.point((84, cy - 1), fill=WHT); d.point((86, cy), fill=WHT)
    d.polygon([(8, cy - 2), (10, cy - 20), (18, cy - 20), (26, cy - 2)], fill=BLK)                   # tall fin
    d.polygon([(14, cy + 2), (52, cy + 1), (60, cy + 4), (16, cy + 5)], fill=BLK)                     # delta wing edge-on
    for x in (22, 32): d.rectangle((x, cy + 4, x + 12, cy + 8), fill=BLK); d.line((x + 12, cy + 5, x + 12, cy + 7), fill=WHT)   # paired engine boxes
    for x in range(14, 78, 3): d.point((x, cy - 1), fill=WHT)
    for gx in (38, 76): d.line((gx, cy + 2, gx, cy + 16), fill=BLK); d.ellipse((gx - 2, cy + 15, gx + 2, cy + 19), fill=BLK)   # tall gear
    d.line((1, 52, W - 2, 52), fill=BLK); fill_pattern(im, (1, 53, W - 1, H - 1), 1)
    frame(d); return im

@reg('douglas-dc-3')
def dc3():
    im, d = canvas(); clouds(d, [(8, 4), (70, 6)])
    cy = 32
    d.rounded_rectangle((20, cy - 6, 86, cy + 5), 5, fill=BLK)
    d.polygon([(20, cy - 6), (6, cy - 4), (6, cy - 2), (20, cy + 5)], fill=BLK)
    d.polygon([(6, cy - 4), (8, cy - 20), (14, cy - 20), (24, cy - 5)], fill=BLK); d.chord((7, cy - 23, 15, cy - 16), 180, 360, fill=BLK)
    d.line((4, cy - 3, 18, cy - 4), fill=BLK, width=2)
    d.polygon([(40, cy + 3), (66, cy + 2), (68, cy + 5), (42, cy + 6)], fill=BLK)
    d.rounded_rectangle((60, cy - 2, 76, cy + 6), 3, fill=BLK); d.line((77, cy - 8, 77, cy + 12), fill=BLK, width=1)   # radial engine + prop
    for x in range(26, 72, 5): d.rectangle((x, cy - 3, x + 1, cy - 1), fill=WHT)
    d.line((82, cy - 3, 85, cy - 1), fill=WHT)
    d.line((66, cy + 6, 66, cy + 16), fill=BLK); d.ellipse((63, cy + 14, 69, cy + 20), fill=BLK)    # taildragger gear
    d.ellipse((8, cy - 1, 11, cy + 2), fill=BLK)
    d.line((1, 52, W - 2, 52), fill=BLK); fill_pattern(im, (1, 53, W - 1, H - 1), 1)
    frame(d); return im

@reg('wright-flyer')
def wright():
    im, d = canvas(); clouds(d, [(70, 6)])
    fill_pattern(im, (1, 52, W - 1, H - 1), 5); d.line((1, 52, W - 2, 52), fill=BLK)
    # biplane wings seen from the front-quarter (two long planes with struts)
    for y in (20, 34):
        d.polygon([(6, y + 2), (90, y), (92, y + 2), (8, y + 4)], fill=BLK)
    for x in range(10, 90, 8): d.line((x, 23, x, 35), fill=BLK)
    d.line((10, 23, 18, 35), fill=BLK); d.line((82, 21, 74, 35), fill=BLK)
    # forward elevator and rear rudder
    d.polygon([(40, 10), (60, 10), (58, 12), (42, 12)], fill=BLK); d.line((46, 12, 46, 20), fill=BLK); d.line((54, 12, 54, 20), fill=BLK)
    d.rectangle((47, 38, 49, 48), fill=BLK); d.rectangle((47, 38, 53, 40), fill=BLK)
    # pilot lying prone + propellers
    d.rectangle((44, 30, 54, 32), fill=BLK); d.ellipse((54, 29, 57, 32), fill=BLK)
    for x in (30, 66): d.line((x, 26, x, 34), fill=BLK, width=2)
    # Wilbur running alongside
    d.ellipse((76, 40, 79, 43), fill=BLK); d.line((77, 43, 77, 48), fill=BLK); d.line((77, 48, 74, 52), fill=BLK); d.line((77, 48, 80, 52), fill=BLK)
    frame(d); return im

# ================================================================== planforms (warplanes)
def planform(half, length=56, span_scale=1.0, details=None, canopy=(0.18, 0.05)):
    """half: right-half outline as (x, y) with x in half-spans of the LENGTH (0 = centreline), y 0 nose → 1 tail."""
    im, d = canvas(); clouds(d, [(4, 4), (76, 52)])
    L = length; top = (H - L) // 2; cx = W // 2
    sx = L * span_scale
    if max(x for x, _ in half) * sx * 2 > W - 6: sx = (W - 6) / 2 / max(x for x, _ in half)
    pts = [(cx + x * sx, top + y * L) for x, y in half]
    mir = [(cx - x * sx, top + y * L) for x, y in reversed(half)]
    d.polygon(pts + mir, fill=BLK)
    # shadow
    if canopy:
        cy, ch = canopy; d.ellipse((cx - 1, top + cy * L - ch * L, cx + 1, top + cy * L + ch * L), fill=WHT)
    if details: details(d, cx, top, L, sx)
    frame(d); return im

def ell(cx, cy, rx, ry, a0, a1, n=12):
    return [(cx + rx * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + ry * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

@reg('supermarine-spitfire')
def spitfire():
    half = [(0, 0), (0.035, 0.02), (0.06, 0.08), (0.065, 0.24)] + \
           [(0.065 + x, y) for x, y in ell(0, 0.36, 0.56, 0.12, -90, 90, 16)] + \
           [(0.06, 0.5), (0.045, 0.8)] + [(0.04 + x, y) for x, y in ell(0, 0.89, 0.17, 0.06, -90, 90, 8)] + [(0.02, 1.0), (0, 1.0)]
    def det(d, cx, top, L, sx): d.line((cx - 30, top + 0.02 * L, cx + 30, top + 0.02 * L), fill=BLK)   # propeller disc
    return planform(half, 54, details=det, canopy=(0.3, 0.04))

@reg('p-51-mustang')
def p51():
    half = [(0, 0), (0.04, 0.02), (0.06, 0.1), (0.065, 0.28), (0.58, 0.35), (0.58, 0.41), (0.065, 0.47), (0.05, 0.8), (0.21, 0.85), (0.21, 0.92), (0.04, 0.95), (0.02, 1.0), (0, 1.0)]
    def det(d, cx, top, L, sx):
        d.line((cx - 26, top + 1, cx + 26, top + 1), fill=BLK)
        d.ellipse((cx - 3, top + 0.5 * L, cx + 3, top + 0.62 * L), fill=BLK)   # belly radiator scoop
    return planform(half, 54, details=det, canopy=(0.33, 0.05))

@reg('avro-lancaster')
def lancaster():
    half = [(0, 0), (0.04, 0.03), (0.05, 0.1), (0.05, 0.27), (0.74, 0.31), (0.74, 0.36), (0.05, 0.45), (0.045, 0.85), (0.25, 0.86), (0.27, 0.92), (0.25, 0.95), (0.04, 0.95), (0.03, 1.0), (0, 1.0)]
    def det(d, cx, top, L, sx):
        for f in (0.16, 0.33):
            for s in (-1, 1):
                x = cx + s * f * sx; d.rectangle((x - 2, top + 0.18 * L, x + 2, top + 0.44 * L), fill=BLK)
                d.line((x - 5, top + 0.18 * L, x + 5, top + 0.18 * L), fill=BLK)
        for s in (-1, 1): d.ellipse((cx + s * 0.26 * sx - 2, top + 0.84 * L, cx + s * 0.26 * sx + 2, top + 0.97 * L), fill=BLK)   # twin fins
    return planform(half, 44, details=det, canopy=(0.13, 0.04))

@reg('mig-21')
def mig21():
    half = [(0, 0), (0.02, 0.04), (0.05, 0.1), (0.05, 0.42), (0.24, 0.78), (0.24, 0.8), (0.05, 0.8), (0.05, 0.83), (0.14, 0.95), (0.13, 0.97), (0.05, 0.96), (0.045, 1.0), (0, 1.0)]
    def det(d, cx, top, L, sx): d.ellipse((cx - 1, top + 0.02 * L, cx + 1, top + 0.07 * L), fill=WHT)   # intake shock cone
    return planform(half, 58, span_scale=1.3, details=det, canopy=(0.24, 0.04))

@reg('mig-29')
def mig29():
    half = [(0, 0), (0.025, 0.05), (0.045, 0.18), (0.07, 0.26), (0.14, 0.42), (0.33, 0.62), (0.33, 0.66), (0.14, 0.7), (0.14, 0.78), (0.26, 0.9), (0.26, 0.95), (0.13, 0.95), (0.12, 1.0), (0.04, 1.0), (0.03, 0.95), (0, 0.95)]
    def det(d, cx, top, L, sx):
        for s in (-1, 1): d.line((cx + s * 0.1 * sx, top + 0.72 * L, cx + s * 0.11 * sx, top + 0.93 * L), fill=WHT)   # twin fins
        d.line((cx, top + 0.45 * L, cx, top + 0.9 * L), fill=WHT)
    return planform(half, 56, details=det, canopy=(0.17, 0.04))

@reg('f-14-tomcat')
def f14():
    half = [(0, 0), (0.03, 0.05), (0.06, 0.2), (0.07, 0.3), (0.2, 0.45), (0.5, 0.58), (0.5, 0.61), (0.2, 0.56), (0.2, 0.8), (0.36, 0.94), (0.33, 0.98), (0.15, 0.95), (0.12, 1.0), (0.03, 1.0), (0.03, 0.95), (0, 0.95)]
    def det(d, cx, top, L, sx):
        for s in (-1, 1): d.line((cx + s * 0.1 * sx, top + 0.7 * L, cx + s * 0.1 * sx, top + 0.95 * L), fill=WHT)
        d.line((cx - 0.04 * sx, top + 0.4 * L, cx - 0.04 * sx, top + 0.95 * L), fill=WHT); d.line((cx + 0.04 * sx, top + 0.4 * L, cx + 0.04 * sx, top + 0.95 * L), fill=WHT)
    return planform(half, 58, details=det, canopy=(0.2, 0.05))

@reg('f-16-fighting-falcon')
def f16():
    half = [(0, 0), (0.03, 0.06), (0.06, 0.25), (0.09, 0.4), (0.32, 0.67), (0.33, 0.73), (0.09, 0.74), (0.07, 0.8), (0.18, 0.92), (0.18, 0.96), (0.06, 0.96), (0.04, 1.0), (0, 1.0)]
    def det(d, cx, top, L, sx): d.line((cx, top + 0.7 * L, cx, top + 0.98 * L), fill=WHT)
    return planform(half, 58, details=det, canopy=(0.2, 0.05))

@reg('f-22-raptor')
def f22():
    half = [(0, 0), (0.03, 0.08), (0.06, 0.2), (0.11, 0.32), (0.11, 0.4), (0.36, 0.66), (0.36, 0.7), (0.14, 0.75), (0.14, 0.78), (0.3, 0.92), (0.28, 0.97), (0.12, 0.93), (0.08, 1.0), (0, 0.98)]
    def det(d, cx, top, L, sx):
        for s in (-1, 1): d.line((cx + s * 0.08 * sx, top + 0.68 * L, cx + s * 0.13 * sx, top + 0.85 * L), fill=WHT)
    return planform(half, 56, details=det, canopy=(0.15, 0.05))

@reg('sr-71-blackbird')
def sr71():
    half = [(0, 0), (0.02, 0.08), (0.05, 0.25), (0.08, 0.4), (0.15, 0.48), (0.26, 0.84), (0.26, 0.9), (0.19, 0.9), (0.19, 1.0), (0.13, 1.0), (0.13, 0.9), (0.04, 0.9), (0.02, 0.97), (0, 0.97)]
    def det(d, cx, top, L, sx):
        for s in (-1, 1):
            x = cx + s * 0.16 * sx; d.line((x, top + 0.42 * L, x, top + 1.0 * L), fill=WHT)
            d.polygon([(x - 1, top + 0.44 * L), (x, top + 0.38 * L), (x + 1, top + 0.44 * L)], fill=BLK)   # inlet spikes
            d.line((x - 2, top + 0.84 * L, x - 1, top + 0.95 * L), fill=WHT)
    return planform(half, 60, span_scale=1.25, details=det, canopy=(0.12, 0.03))

@reg('b-2-spirit')
def b2():
    half = [(0, 0), (1.0, 0.65), (1.0, 0.72), (0.62, 0.5), (0.38, 0.78), (0.18, 0.6), (0, 0.8)]
    def det(d, cx, top, L, sx):
        for s in (-1, 1): d.polygon([(cx + s * 4, top + 0.2 * L), (cx + s * 8, top + 0.26 * L), (cx + s * 4, top + 0.28 * L)], fill=WHT)   # intakes
    return planform([(x, y * 0.7) for x, y in half], 52, span_scale=0.85, details=det, canopy=(0.1, 0.03))

@reg('b-52-stratofortress')
def b52():
    half = [(0, 0), (0.03, 0.03), (0.04, 0.1), (0.04, 0.3), (0.58, 0.6), (0.57, 0.65), (0.04, 0.48), (0.04, 0.82), (0.24, 0.93), (0.23, 0.97), (0.04, 0.95), (0.02, 1.0), (0, 1.0)]
    def det(d, cx, top, L, sx):
        for f, y0 in ((0.17, 0.36), (0.33, 0.45)):
            for s in (-1, 1):
                x = cx + s * f * sx; d.rectangle((x - 2, top + (y0 - 0.06) * L, x + 2, top + (y0 + 0.04) * L), fill=BLK)
                d.line((x, top + (y0 - 0.06) * L, x, top + (y0 + 0.03) * L), fill=WHT)
    return planform(half, 52, details=det, canopy=(0.06, 0.02))

@reg('a-10-warthog')
def a10():
    half = [(0, 0), (0.035, 0.04), (0.05, 0.15), (0.05, 0.36), (0.54, 0.38), (0.54, 0.47), (0.05, 0.5), (0.04, 0.84), (0.3, 0.85), (0.3, 0.95), (0.04, 0.95), (0.02, 1.0), (0, 1.0)]
    def det(d, cx, top, L, sx):
        for s in (-1, 1):
            x = cx + s * 0.1 * sx; d.ellipse((x - 3, top + 0.52 * L, x + 3, top + 0.72 * L), fill=BLK); d.line((x - 2, top + 0.53 * L, x + 2, top + 0.53 * L), fill=WHT)
            d.rectangle((cx + s * 0.3 * sx - 1, top + 0.82 * L, cx + s * 0.3 * sx + 1, top + 0.97 * L), fill=BLK)
        d.line((cx, top - 2, cx, top + 1), fill=BLK)   # gun barrel
    return planform(half, 54, details=det, canopy=(0.12, 0.04))

@reg('eurofighter-typhoon')
def typhoon():
    half = [(0, 0), (0.035, 0.08), (0.06, 0.22), (0.15, 0.27), (0.15, 0.3), (0.07, 0.31), (0.08, 0.46), (0.36, 0.86), (0.36, 0.9), (0.07, 0.92), (0.05, 1.0), (0, 1.0)]
    def det(d, cx, top, L, sx): d.line((cx, top + 0.66 * L, cx, top + 0.97 * L), fill=WHT)
    return planform(half, 58, details=det, canopy=(0.16, 0.04))

@reg('avro-arrow')
def arrow():
    half = [(0, 0), (0.03, 0.08), (0.06, 0.24), (0.1, 0.3), (0.1, 0.36), (0.14, 0.4), (0.13, 0.42), (0.33, 0.86), (0.33, 0.9), (0.06, 0.92), (0.04, 1.0), (0, 1.0)]
    def det(d, cx, top, L, sx): d.line((cx, top + 0.62 * L, cx, top + 0.99 * L), fill=WHT)
    return planform(half, 58, details=det, canopy=(0.17, 0.04))

if __name__ == '__main__':
    for n, f in REG.items(): save(f(), CAT, n)
    print(len(REG))
