#!/usr/bin/env python3
"""National air force roundels (current markings) as NES-style 8-bit art, painted on an aircraft skin.
48x32 cells shown at 2x, like the paintings and inventions. No German markings."""
import sys, math
from PIL import Image, ImageDraw
from common import W, H, save
from paintings_nes import K

CW, CH = W // 2, H // 2
RED, WHITE, BLUE, NAVY, LBLUE = (228, 0, 88), (252, 252, 252), (0, 88, 248), (0, 0, 188), (60, 188, 252)
GREEN, DGREEN, YELLOW, ORANGE, BLACK, SAFFRON = (0, 168, 0), (0, 120, 0), (248, 184, 0), (228, 92, 16), (0, 0, 0), (252, 160, 68)
RRED = (168, 16, 0)
SKIN, SKIN_D, SKIN_L = (124, 124, 124), (80, 80, 80), (188, 188, 188)

def skin():
    g = Image.new('RGB', (CW, CH), SKIN); d = ImageDraw.Draw(g)
    for y in (4, 27): d.line((0, y, CW, y), fill=SKIN_D)                       # panel lines
    for x in (5, 42): d.line((x, 0, x, CH), fill=SKIN_D)
    for y in (2, 6, 25, 29):
        for x in range(1, CW, 3): d.point((x, y), fill=SKIN_L)                   # rivets
    for y in range(8, 25, 3): d.point((3, y), fill=SKIN_L); d.point((44, y), fill=SKIN_L)
    return g, d

CX, CY, R = 23.5, 15.5, 12.5
def rings(d, cols, r=R):
    """Concentric discs from the outside in."""
    n = len(cols)
    for i, c in enumerate(cols):
        rr = r * (1 - i / n) if n < 4 else r * [1, 0.76, 0.52, 0.22][i]
        d.ellipse((CX - rr, CY - rr, CX + rr, CY + rr), fill=c)

def star(d, cx, cy, r, col, inner=0.38, rot=-90, pts=5):
    P = []
    for i in range(pts * 2):
        rr = r if i % 2 == 0 else r * inner; a = math.radians(rot + 180 * i / pts)
        P.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d.polygon(P, fill=col)

def finish(g):
    big = g.resize((W, H), Image.NEAREST); ImageDraw.Draw(big).rectangle((0, 0, W - 1, H - 1), outline=K); return big


# ---- fine emblems: drawn at full 96x64 resolution (8x supersampled) over the chunky background, for more detail ----
import re
LEAF_PATH = ("m-90 2030 45-863a95 95 0 0 0-111-98l-859 151 116-320a65 65 0 0 0-20-73l-941-762 212-99a65 65 0 0 0 34-79l-186-572 542 115"
             "a65 65 0 0 0 73-38l105-247 423 454a65 65 0 0 0 111-57l-204-1052 327 189a65 65 0 0 0 91-27l332-652 332 652a65 65 0 0 0 91 27"
             "l327-189-204 1052a65 65 0 0 0 111 57l423-454 105 247a65 65 0 0 0 73 38l542-115-186 572a65 65 0 0 0 34 79l212 99-941 762"
             "a65 65 0 0 0-20 73l116 320-859-151a95 95 0 0 0-111 98l45 863z")   # the 11-point maple leaf (Flag of Canada outline)
def leaf_points():
    toks = re.findall(r'[a-zA-Z]|-?\d+\.?\d*', LEAF_PATH); i = 0; cmd = None; x = y = 0; pts = []
    while i < len(toks):
        t = toks[i]
        if t.isalpha(): cmd = t; i += 1; continue
        if cmd == 'm': x += float(toks[i]); y += float(toks[i + 1]); pts.append((x, y)); i += 2; cmd = 'l'
        elif cmd == 'l': x += float(toks[i]); y += float(toks[i + 1]); pts.append((x, y)); i += 2
        elif cmd == 'a': x += float(toks[i + 5]); y += float(toks[i + 6]); pts.append((x, y)); i += 7
        else: i += 1
    return pts

def fine(big, polys, col, box):
    """polys in unit coords; box = (cx, cy, size) in output pixels (96x64 frame)."""
    xs = [x for p in polys for x, _ in p]; ys = [y for p in polys for _, y in p]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys); cx, cy, size = box
    s = size / max(x1 - x0, y1 - y0); SS = 8
    m = Image.new('L', (W * SS, H * SS), 0); md = ImageDraw.Draw(m)
    for p in polys:
        md.polygon([((cx + (x - (x0 + x1) / 2) * s) * SS, (cy + (y - (y0 + y1) / 2) * s) * SS) for x, y in p], fill=255)
    m = m.resize((W, H), Image.BOX).point(lambda v: 255 if v > 120 else 0)
    big.paste(Image.new('RGB', big.size, col), (0, 0), m)

def finish_fine(g, draw):
    big = g.resize((W, H), Image.NEAREST); draw(big); ImageDraw.Draw(big).rectangle((0, 0, W - 1, H - 1), outline=K); return big

KANGAROO = [(2, 14), (8, 9), (13, 6), (15, 4), (16, -5), (18, -5), (21, 3), (23, 8), (30, 12), (42, 14), (54, 19), (64, 27), (71, 36), (75, 43),
            (86, 49), (100, 56), (100, 60), (88, 58), (77, 54), (75, 56), (72, 60), (67, 63), (80, 66), (88, 68), (88, 71), (63, 70), (58, 66),
            (54, 60), (46, 53), (38, 45), (31, 39), (27, 41), (21, 45), (19, 44), (24, 39), (28, 35), (24, 26), (17, 20), (9, 17), (3, 16)]

REG = {}
def reg(slug, country):
    def f(fn): REG[slug] = (fn, country); return fn
    return f

def simple(slug, country, cols, r=R):
    def fn():
        g, d = skin(); rings(d, cols, r); return finish(g)
    REG[slug] = (fn, country)

simple('united-kingdom', 'United Kingdom', [NAVY, WHITE, RED])
simple('france', 'France', [RED, WHITE, BLUE])
simple('italy', 'Italy', [GREEN, WHITE, RED])
simple('belgium', 'Belgium', [RED, YELLOW, BLACK])
simple('india', 'India', [SAFFRON, WHITE, GREEN])
simple('greece', 'Greece', [BLUE, WHITE, BLUE])
simple('argentina', 'Argentina', [LBLUE, WHITE, LBLUE])
simple('denmark', 'Denmark', [RED, WHITE, RED])
simple('spain', 'Spain', [RED, YELLOW, RED])

@reg('netherlands', 'Netherlands')
def nl():
    g, d = skin(); rings(d, [RED, WHITE, BLUE, ORANGE]); return finish(g)

@reg('canada', 'Canada')
def canada():
    g, d = skin(); d.ellipse((CX - R, CY - R, CX + R, CY + R), fill=NAVY); r = R * 0.7; d.ellipse((CX - r, CY - r, CX + r, CY + r), fill=WHITE)
    return finish_fine(g, lambda big: fine(big, [leaf_points()], RRED, (CX * 2 + 1, CY * 2 + 1.5, 27)))

@reg('australia', 'Australia')
def australia():
    g, d = skin(); d.ellipse((CX - R, CY - R, CX + R, CY + R), fill=NAVY); r = R * 0.7; d.ellipse((CX - r, CY - r, CX + r, CY + r), fill=WHITE)
    return finish_fine(g, lambda big: fine(big, [KANGAROO], RED, (CX * 2 + 1, CY * 2 + 1, 31)))

@reg('germany', 'Germany')
def germany():
    g, d = skin()
    def cross(r, w0, w1):            # cross pattee: arms widen from w0 at the centre to w1 at the tips
        P = []
        for k in range(4):
            a = math.radians(90 * k); ca, sa = math.cos(a), math.sin(a)
            def T(x, y): return (CX * 2 + 1 + x * ca - y * sa, CY * 2 + 1 + x * sa + y * ca)
            P.append([T(w0, -w0), T(r, -w1), T(r, w1), T(w0, w0), T(-w0, w0), T(-w0, -w0)])
        return P
    def draw(big):
        fine_raw(big, cross(22, 5.0, 10.0), WHITE); fine_raw(big, cross(20.2, 3.4, 8.2), BLACK)
    return finish_fine(g, draw)

def fine_raw(big, polys, col):
    SS = 8; m = Image.new('L', (W * SS, H * SS), 0); md = ImageDraw.Draw(m)
    for p in polys: md.polygon([(x * SS, y * SS) for x, y in p], fill=255)
    m = m.resize((W, H), Image.BOX).point(lambda v: 255 if v > 120 else 0); big.paste(Image.new('RGB', big.size, col), (0, 0), m)

@reg('new-zealand', 'New Zealand')
def nz():
    g, d = skin(); rings(d, [NAVY, WHITE])
    d.ellipse((CX - 5, CY - 3, CX + 4, CY + 4), fill=RED); d.ellipse((CX + 2, CY - 5, CX + 6, CY - 1), fill=RED)   # kiwi body and head
    d.line((CX + 6, CY - 3, CX + 10, CY + 2), fill=RED); d.line((CX - 1, CY + 4, CX - 2, CY + 7), fill=RED); d.line((CX + 1, CY + 4, CX + 2, CY + 7), fill=RED)
    return finish(g)

@reg('japan', 'Japan')
def japan():
    g, d = skin(); d.ellipse((CX - 11, CY - 11, CX + 11, CY + 11), fill=WHITE); d.ellipse((CX - 9.5, CY - 9.5, CX + 9.5, CY + 9.5), fill=RED); return finish(g)

@reg('united-states', 'United States')
def usa():
    g, d = skin()
    d.rectangle((CX - 21, CY - 5, CX + 21, CY + 5), fill=NAVY); d.ellipse((CX - 11, CY - 11, CX + 11, CY + 11), fill=NAVY)
    d.rectangle((CX - 20, CY - 4, CX + 20, CY + 4), fill=WHITE); d.ellipse((CX - 10, CY - 10, CX + 10, CY + 10), fill=WHITE)
    d.ellipse((CX - 9, CY - 9, CX + 9, CY + 9), fill=NAVY)
    d.rectangle((CX - 19, CY - 1, CX + 19, CY + 1), fill=RED)
    d.ellipse((CX - 9, CY - 9, CX + 9, CY + 9), fill=NAVY)
    star(d, CX, CY + 0.5, 9, WHITE)
    return finish(g)

@reg('russia', 'Russia')
def russia():
    g, d = skin(); star(d, CX, CY + 1, 13.5, BLUE); star(d, CX, CY + 1, 11.5, WHITE); star(d, CX, CY + 1, 9.5, RED); return finish(g)

@reg('china', 'China')
def china():
    g, d = skin()
    d.rectangle((CX - 20, CY - 2, CX + 20, CY + 2), fill=RED)
    star(d, CX, CY + 1, 12, YELLOW); star(d, CX, CY + 1, 10.5, RED)
    d.rectangle((CX - 2, CY - 1, CX + 2, CY), fill=YELLOW); d.line((CX - 3, CY + 2, CX + 3, CY + 2), fill=YELLOW)   # the "8 1" characters, suggested
    return finish(g)

@reg('israel', 'Israel')
def israel():
    g, d = skin(); d.ellipse((CX - 12, CY - 12, CX + 12, CY + 12), fill=WHITE)
    for rot in (-90, 90):
        P = [(CX + 9.5 * math.cos(math.radians(rot + 120 * i)), CY + 9.5 * math.sin(math.radians(rot + 120 * i))) for i in range(3)]
        d.polygon(P, outline=BLUE, width=2)
    return finish(g)

@reg('poland', 'Poland')
def poland():
    g, d = skin()
    s = 6
    for i in range(4):
        for j in range(4):
            c = RED if (i + j) % 2 == 0 else WHITE
            d.rectangle((CX - 2 * s + i * s, CY - 2 * s + j * s, CX - 2 * s + (i + 1) * s - 1, CY - 2 * s + (j + 1) * s - 1), fill=c)
    d.rectangle((CX - 2 * s - 1, CY - 2 * s - 1, CX + 2 * s, CY + 2 * s), outline=RED)
    return finish(g)

@reg('sweden', 'Sweden')
def sweden():
    g, d = skin(); d.ellipse((CX - 12, CY - 12, CX + 12, CY + 12), fill=BLUE)
    for cx, cy in ((CX - 4, CY - 4), (CX + 4, CY - 4), (CX, CY + 3)):
        d.polygon([(cx - 3, cy + 2), (cx - 3, cy - 2), (cx - 1.5, cy), (cx, cy - 3), (cx + 1.5, cy), (cx + 3, cy - 2), (cx + 3, cy + 2)], fill=YELLOW)
    return finish(g)

@reg('brazil', 'Brazil')
def brazil():
    g, d = skin(); rings(d, [GREEN, YELLOW, BLUE]); star(d, CX, CY + 0.5, 3.5, WHITE); return finish(g)

@reg('mexico', 'Mexico')
def mexico():
    g, d = skin()
    for r, c in ((14, GREEN), (9.5, WHITE), (5, RED)):
        d.polygon([(CX, CY - r), (CX + r * 0.87, CY + r / 2), (CX - r * 0.87, CY + r / 2)], fill=c)
    return finish(g)

@reg('south-korea', 'South Korea')
def korea():
    g, d = skin(); d.ellipse((CX - 12, CY - 12, CX + 12, CY + 12), fill=WHITE)
    r = 8; d.pieslice((CX - r, CY - r, CX + r, CY + r), 180, 360, fill=RED); d.pieslice((CX - r, CY - r, CX + r, CY + r), 0, 180, fill=BLUE)
    d.ellipse((CX - r, CY - r / 2, CX, CY + r / 2), fill=RED); d.ellipse((CX, CY - r / 2, CX + r, CY + r / 2), fill=BLUE)
    return finish(g)

@reg('switzerland', 'Switzerland')
def swiss():
    g, d = skin(); d.rectangle((CX - 11, CY - 11, CX + 11, CY + 11), fill=RED)
    d.rectangle((CX - 2, CY - 7, CX + 2, CY + 7), fill=WHITE); d.rectangle((CX - 7, CY - 2, CX + 7, CY + 2), fill=WHITE); return finish(g)

if __name__ == '__main__':
    for n in sys.argv[1:] or REG: save(REG[n][0](), 'roundels', n); print(n)
