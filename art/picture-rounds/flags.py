#!/usr/bin/env python3
"""8-bit colour flags for every country, rendered small and snapped to a fixed retro palette."""
import io, json, os
import cairosvg
from PIL import Image, ImageDraw
from common import ROOT, OUT, W, H, S

PALETTE = [  # a fixed 18-colour "8-bit" palette tuned for flags
    (255, 255, 255), (0, 0, 0), (206, 17, 38), (140, 20, 40), (240, 120, 20), (252, 209, 22), (200, 160, 40),
    (0, 160, 80), (0, 110, 50), (120, 200, 90), (100, 180, 230), (0, 90, 190), (0, 40, 104), (120, 50, 140),
    (0, 135, 65), (128, 128, 128), (200, 200, 200), (255, 150, 160)]

def snap(c):
    return min(PALETTE, key=lambda p: (p[0] - c[0]) ** 2 * 2 + (p[1] - c[1]) ** 2 * 3 + (p[2] - c[2]) ** 2)

SQUARE = {'CH', 'VA'}
FW, FH = 72, 48

def render(a2):
    if a2 in SQUARE:
        src = os.path.join(ROOT, 'node_modules/flag-icons/flags/1x1', a2.lower() + '.svg'); w = h = 48
    elif a2 == 'NP':
        src = os.path.join(ROOT, 'node_modules/flag-icons/flags/1x1', 'np.svg'); w, h = 40, 48
    else:
        src = os.path.join(ROOT, 'node_modules/country-flag-icons/3x2', a2 + '.svg'); w, h = FW, FH
    if not os.path.exists(src): return None
    png = cairosvg.svg2png(url=src, output_width=w * 4, output_height=h * 4)
    big = Image.open(io.BytesIO(png)).convert('RGBA')
    bg = Image.new('RGBA', big.size, (255, 255, 255, 255)); bg.alpha_composite(big)
    small = bg.convert('RGB').resize((w, h), Image.BOX)
    px = small.load()
    for y in range(h):
        for x in range(w): px[x, y] = snap(px[x, y])
    can = Image.new('RGB', (W, H), (255, 255, 255)); ox, oy = (W - w) // 2, (H - h) // 2
    can.paste(small, (ox, oy)); d = ImageDraw.Draw(can)
    if a2 != 'NP': d.rectangle((ox - 1, oy - 1, ox + w, oy + h), outline=(0, 0, 0))
    d.rectangle((0, 0, W - 1, H - 1), outline=(0, 0, 0))
    return can

if __name__ == '__main__':
    from common import sheet, save
    meta = json.load(open(os.path.join(ROOT, 'countries-meta.json')))
    n = 0
    for m in meta:
        im = render(m['a2'])
        if im is None: print('no flag', m['name']); continue
        save(im, 'flags', m['slug']); n += 1
    print(n, sheet('flags', cols=12))
