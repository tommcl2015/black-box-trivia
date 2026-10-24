#!/usr/bin/env python3
"""Famous trains as NES-style 8-bit pixel art (48x32 cells at 2x), digitised from freely licensed photos
on Wikimedia Commons (see CREDITS). Same look as the photo-based paintings."""
import os, sys
from collections import Counter
from PIL import Image, ImageEnhance, ImageDraw
from common import W, H, save
from paintings_nes import NES, K

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'trains_src')
CW, CH = W // 2, H // 2
CREDITS = {
    'stephensons-rocket': ('Replica of Robert Stephenson Famous Rocket, National Railway Museum', 'Barry Marsh', 'Public domain'),
    'flying-scotsman': ('Flying Scotsman in Doncaster.JPG', '', 'Public domain'),
    'mallard': ('Number 4468 Mallard in York.jpg', 'PTG Dudva', 'CC BY-SA 3.0'),
    'shinkansen-bullet-train': ('JRC Shinkansen Series N700 Z13', 'Scfema', 'CC BY-SA 3.0'),
    'eurostar': ('Eurostars 373 210 and 373 205 Brussels-South', 'Bahnfrend', 'CC BY-SA 4.0'),
    'big-boy': ('Union Pacific Big Boy 4000 1941.JPG', 'Association of American Railroads', 'Public domain'),
    'the-general': ('The General, Western & Atlantic RR Locomotive', 'Gary Todd', 'CC0'),
}
# crop (fractions of the source: x0, y0, x1, y1), colour boost, contrast, colours kept
SET = {
    'stephensons-rocket': ((0.02, 0.22, 0.98, 0.98), 1.7, 1.25, 10),
    'flying-scotsman': ((0.12, 0.10, 0.98, 0.83), 1.8, 1.2, 10),
    'mallard': ((0.0, 0.12, 1.0, 0.92), 1.6, 1.2, 10),
    'shinkansen-bullet-train': ((0.0, 0.08, 0.82, 0.84), 1.4, 1.25, 8),
    'eurostar': ((0.12, 0.08, 0.96, 0.95), 1.6, 1.2, 10),
    'big-boy': ((0.0, 0.12, 1.0, 0.95), 1.0, 1.35, 6),
    'the-general': ((0.05, 0.05, 0.98, 0.93), 1.5, 1.2, 10),
}

def despeckle(img):
    """Replace lone pixels with the most common colour around them (keeps the art clean, NES-like)."""
    px = img.load(); w, h = img.size; out = img.copy(); po = out.load()
    for y in range(h):
        for x in range(w):
            nb = [px[x + dx, y + dy] for dx in (-1, 0, 1) for dy in (-1, 0, 1) if (dx or dy) and 0 <= x + dx < w and 0 <= y + dy < h]
            if px[x, y] not in nb:
                po[x, y] = Counter(nb).most_common(1)[0][0]
    return out

def convert(slug):
    (x0, y0, x1, y1), col, con, ncol = SET[slug]
    src = Image.open(os.path.join(SRC, slug + '.png')).convert('RGB')
    w, h = src.size; box = (x0 * w, y0 * h, x1 * w, y1 * h)
    bw, bh = box[2] - box[0], box[3] - box[1]
    if bw / bh > CW / CH: c = (box[0] + box[2]) / 2; bw = bh * CW / CH; box = (c - bw / 2, box[1], c + bw / 2, box[3])
    else: c = (box[1] + box[3]) / 2; bh = bw * CH / CW; box = (box[0], c - bh / 2, box[2], c + bh / 2)
    small = src.crop(tuple(int(round(v)) for v in box)).resize((CW, CH), Image.LANCZOS)
    small = ImageEnhance.Contrast(ImageEnhance.Color(small).enhance(col)).enhance(con)
    pal = Image.new('P', (1, 1)); flat = [v for c in NES for v in c]; pal.putpalette(flat + [0] * (768 - len(flat)))
    q = small.quantize(palette=pal, dither=Image.Dither.NONE).convert('RGB')
    px = q.load(); cnt = Counter(px[x, y] for y in range(CH) for x in range(CW)); keep = [c for c, _ in cnt.most_common(ncol)]
    for y in range(CH):
        for x in range(CW):
            c = px[x, y]
            if c not in keep: px[x, y] = min(keep, key=lambda k: sum((a - b) ** 2 for a, b in zip(k, c)))
    q = despeckle(q)
    big = q.resize((W, H), Image.NEAREST); ImageDraw.Draw(big).rectangle((0, 0, W - 1, H - 1), outline=K)
    return big

# rectangle around each train in the 217x143 source, for GrabCut to cut it out of its background
RECT = {'big-boy': (0, 36, 217, 136), 'eurostar': (40, 18, 178, 141), 'flying-scotsman': (0, 30, 217, 140), 'mallard': (8, 8, 216, 128),
        'shinkansen-bullet-train': (0, 28, 216, 141), 'stephensons-rocket': (24, 30, 200, 142), 'the-general': (14, 14, 202, 142)}

def cutout(slug):
    import cv2, numpy as np
    src = Image.open(os.path.join(SRC, slug + '.png')).convert('RGB'); a = np.asarray(src)[:, :, ::-1].copy()
    mask = np.zeros(a.shape[:2], np.uint8); bg = np.zeros((1, 65), np.float64); fg = np.zeros((1, 65), np.float64)
    x0, y0, x1, y1 = RECT[slug]
    cv2.grabCut(a, mask, (x0, y0, x1 - x0, y1 - y0), bg, fg, 8, cv2.GC_INIT_WITH_RECT)
    m = np.where((mask == 1) | (mask == 3), 255, 0).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(m)
    if n > 1:                                                       # keep the biggest piece (the train)
        big = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA])); keepl = [i for i in range(1, n) if st[i, cv2.CC_STAT_AREA] > 0.08 * st[big, cv2.CC_STAT_AREA]]
        m = np.isin(lab, keepl).astype(np.uint8) * 255
    return src, Image.fromarray(m)

def scene():
    g = Image.new('RGB', (CW, CH), (60, 188, 252)); d = ImageDraw.Draw(g)
    for x, y in ((3, 3), (34, 5)):
        d.rectangle((x, y, x + 7, y + 1), fill=(252, 252, 252)); d.rectangle((x + 2, y - 1, x + 5, y - 1), fill=(252, 252, 252))
    d.rectangle((0, 22, CW, 23), fill=(0, 168, 0)); d.rectangle((0, 24, CW, CH), fill=(172, 124, 0))
    for x in range(0, CW, 3): d.rectangle((x, 27, x + 1, 28), fill=(80, 48, 0))
    d.line((0, 26, CW, 26), fill=(188, 188, 188)); d.line((0, 29, CW, 29), fill=(188, 188, 188))
    return g

def convert2(slug):
    src, m = cutout(slug)
    bb = m.getbbox(); src = src.crop(bb); m = m.crop(bb)
    (_, col, con, ncol) = SET[slug]
    s = min((CW - 2) / src.width, 27 / src.height)
    w, h = max(1, round(src.width * s)), max(1, round(src.height * s))
    small = ImageEnhance.Contrast(ImageEnhance.Color(src.resize((w, h), Image.LANCZOS)).enhance(col)).enhance(con)
    ms = m.resize((w, h), Image.BOX).point(lambda v: 255 if v > 110 else 0)
    pal = Image.new('P', (1, 1)); flat = [v for c in NES for v in c]; pal.putpalette(flat + [0] * (768 - len(flat)))
    q = small.quantize(palette=pal, dither=Image.Dither.NONE).convert('RGB')
    px = q.load(); mp = ms.load()
    cnt = Counter(px[x, y] for y in range(h) for x in range(w) if mp[x, y]); keep = [c for c, _ in cnt.most_common(ncol)]
    for y in range(h):
        for x in range(w):
            c = px[x, y]
            if c not in keep: px[x, y] = min(keep, key=lambda k: sum((a - b) ** 2 for a, b in zip(k, c)))
    q = despeckle(q)
    g = scene(); ox = (CW - w) // 2; oy = 28 - h
    g.paste(q, (ox, oy), ms)
    big = g.resize((W, H), Image.NEAREST); ImageDraw.Draw(big).rectangle((0, 0, W - 1, H - 1), outline=K)
    return big

# Final settings: full 96x64 resolution (1 cell = 1 pixel) reads far better for busy machinery than 48x32.
FULL = {   # slug: (colour boost, contrast, colours kept)
    'stephensons-rocket': (1.5, 1.15, 14), 'flying-scotsman': (1.9, 1.1, 16), 'mallard': (1.5, 1.15, 14),
    'shinkansen-bullet-train': (1.5, 1.15, 14), 'eurostar': (1.5, 1.15, 14), 'big-boy': (1.0, 1.4, 6), 'the-general': (1.5, 1.15, 14)}

BRIGHT = {'flying-scotsman': 1.45, 'big-boy': 1.15}
NO_TEAL = [(0, 64, 88), (0, 136, 136), (0, 0, 188), (68, 40, 188)]

def convert_full(slug):
    col, con, ncol = FULL[slug]
    src = Image.open(os.path.join(SRC, slug + '.png')).convert('RGB')
    x0, y0, x1, y1 = RECT[slug]; bw, bh = x1 - x0, y1 - y0
    if bw / bh > 1.5: c = (y0 + y1) / 2; bh = bw / 1.5; box = (x0, c - bh / 2, x1, c + bh / 2)
    else: c = (x0 + x1) / 2; bw = bh * 1.5; box = (c - bw / 2, y0, c + bw / 2, y1)
    small = src.crop(tuple(int(round(v)) for v in box)).resize((W, H), Image.LANCZOS)
    small = ImageEnhance.Brightness(small).enhance(BRIGHT.get(slug, 1.0))
    small = ImageEnhance.Contrast(ImageEnhance.Color(small).enhance(col)).enhance(con)
    P = [c for c in NES if c not in NO_TEAL] if slug == 'flying-scotsman' else NES          # LNER green, not teal
    if slug == 'big-boy': P = [(0, 0, 0), (80, 80, 80), (124, 124, 124), (188, 188, 188), (216, 216, 216), (252, 252, 252)]   # a black-and-white 1941 photo
    pal = Image.new('P', (1, 1)); flat = [v for c in P for v in c]; pal.putpalette(flat + [0] * (768 - len(flat)))
    q = small.quantize(palette=pal, colors=len(P), dither=Image.Dither.NONE).convert('RGB')
    px = q.load(); cnt = Counter(px[x, y] for y in range(H) for x in range(W)); keep = [c for c, _ in cnt.most_common(ncol)]
    for y in range(H):
        for x in range(W):
            c = px[x, y]
            if c not in keep: px[x, y] = min(keep, key=lambda k: sum((a - b) ** 2 for a, b in zip(k, c)))
    q = despeckle(q); ImageDraw.Draw(q).rectangle((0, 0, W - 1, H - 1), outline=K)
    return q

if __name__ == '__main__':
    for slug in sys.argv[1:] or FULL: save(convert_full(slug), 'trains', slug); print(slug)
    raise SystemExit
    for slug in sys.argv[1:] or SET: save(convert(slug), 'trains', slug); print(slug)
