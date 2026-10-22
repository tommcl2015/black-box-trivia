"""Shared 1-bit pixel-art helpers for Black Box Trivia picture questions."""
import os, math
from PIL import Image, ImageDraw

W, H, S = 96, 64, 4
BLK, WHT = 0, 1
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'out')

def canvas(bg=WHT, w=W, h=H):
    im = Image.new('1', (w, h), bg)
    return im, ImageDraw.Draw(im)

def save(im, cat, name, scale=S):
    d = os.path.join(OUT, cat); os.makedirs(d, exist_ok=True)
    big = im.convert('RGB' if im.mode in ('RGB', 'P') else 'L').resize((im.width * scale, im.height * scale), Image.NEAREST)
    big.save(os.path.join(d, name + '.png'))

def pattern_on(level, x, y):
    if level == 0: return False
    if level == 1: return (x % 4 == 0 and y % 4 == 0) or (x % 4 == 2 and y % 4 == 2)   # light dots
    if level == 2: return (x + y) % 2 == 0                                              # 50% grey
    if level == 3: return not (x % 2 == 0 and y % 2 == 0)                               # dark grey
    if level == 4: return y % 3 == 0                                                    # horizontal hatch
    if level == 5: return (x + y) % 4 == 0                                              # diagonal hatch
    if level == 6: return x % 4 == 0 and y % 4 == 0                                     # very light
    if level == 7: return (x - y) % 4 == 0                                              # other diagonal
    return True

def fill_pattern(im, box, level):
    x0, y0, x1, y1 = [int(round(v)) for v in box]
    px = im.load()
    for y in range(max(0, y0), min(im.height, y1)):
        for x in range(max(0, x0), min(im.width, x1)):
            if pattern_on(level, x, y): px[x, y] = BLK

def shade(im, draw_fn, level):
    """Fill a shape (drawn by draw_fn onto a mask) with a pattern."""
    m = Image.new('1', im.size, 0); draw_fn(ImageDraw.Draw(m))
    full = Image.new('1', im.size, WHT); fill_pattern(full, (0, 0, im.width, im.height), level)
    im.paste(full, (0, 0), m)

def frame(d, w=W, h=H):
    d.rectangle((0, 0, w - 1, h - 1), outline=BLK)

def water(im, y0, y1=None, x0=1, x1=None):
    y1 = y1 or im.height - 1; x1 = x1 or im.width - 1
    px = im.load()
    for y in range(y0, y1):
        for x in range(x0, x1):
            if y % 3 == 0 and (x + y) % 6 < 3: px[x, y] = BLK

def ground(im, d, y=58, level=1):
    d.line((1, y, im.width - 2, y), fill=BLK)
    fill_pattern(im, (1, y + 1, im.width - 1, im.height - 1), level)

def clouds(d, spots):
    for x, y in spots:
        d.ellipse((x, y, x + 10, y + 5), outline=BLK, fill=WHT)
        d.ellipse((x + 5, y - 2, x + 14, y + 4), outline=BLK, fill=WHT)
        d.rectangle((x + 4, y + 1, x + 10, y + 4), fill=WHT)

def sun(im, d, x, y, r=5):
    d.ellipse((x - r, y - r, x + r, y + r), outline=BLK, fill=WHT)
    fill_pattern(im, (x - r + 2, y - r + 2, x + r - 1, y + r - 1), 2)

def windows(im, box, rng=None, density=0.35, step=(2, 3)):
    import random
    r = rng or random.Random(1)
    x0, y0, x1, y1 = box
    for y in range(y0, y1, step[1]):
        for x in range(x0, x1, step[0]):
            if 0 < x < im.width - 1 and 0 < y < im.height - 1 and r.random() < density:
                im.putpixel((x, y), WHT)

def city_fill(im, d, y=56, seed=1, hmin=6, hmax=18, x0=1, x1=None, wmin=4, wmax=9):
    """Generic blocks of buildings with lit windows."""
    import random
    r = random.Random(seed); x1 = x1 or im.width - 2
    x = x0
    while x < x1:
        w = r.randint(wmin, wmax); h = r.randint(hmin, hmax)
        d.rectangle((x, y - h, min(x + w, x1), y), fill=BLK)
        windows(im, (x + 1, y - h + 2, min(x + w, x1), y - 1), r)
        x += w + r.randint(0, 2)

def tower(d, cx, top, bottom, wb, wt=None, fill=BLK):
    wt = wb if wt is None else wt
    d.polygon([(cx - wb, bottom), (cx - wt, top), (cx + wt, top), (cx + wb, bottom)], fill=fill)

def pagoda(d, cx, base, tiers, w0, th=5, shrink=1, fill=BLK):
    """Chinese/Japanese pagoda: tiers of upturned roofs."""
    y = base; w = w0
    for i in range(tiers):
        d.rectangle((cx - w + 2, y - th + 1, cx + w - 2, y), fill=WHT, outline=fill)
        d.polygon([(cx - w - 2, y - th + 1), (cx - w, y - th - 1), (cx + w, y - th - 1), (cx + w + 2, y - th + 1)], fill=fill)
        y -= th + 1; w -= shrink
    d.line((cx, y, cx, y - 4), fill=fill)
    return y

def onion(d, cx, base, r, fill=BLK, outline=None):
    """Onion dome (St Basil's, Taj style)."""
    pts = []
    for i in range(0, 21):
        t = i / 20; a = math.pi * t
        rr = r * math.sin(a) * (1.15 - 0.6 * t)
        pts.append((cx - rr, base - t * 2.3 * r))
    pts += [(2 * cx - x, y) for x, y in reversed(pts)]
    d.polygon(pts, fill=fill, outline=outline)
    d.line((cx, base - 2.3 * r, cx, base - 2.3 * r - 3), fill=BLK)

def arches(d, x0, x1, y0, y1, step=4, fill=BLK):
    for x in range(x0, x1 - 1, step):
        d.rectangle((x + 1, y0 + 1, x + step - 2, y1), fill=fill)
        d.point((x + 1, y0 + 1), fill=WHT); d.point((x + step - 2, y0 + 1), fill=WHT)

def sheet(cat, cols=8, label=True, out=None, scale_down=2):
    d = os.path.join(OUT, cat)
    fs = sorted(f for f in os.listdir(d) if f.endswith('.png'))
    tiles = [Image.open(os.path.join(d, f)).convert('RGB') for f in fs]
    w = tiles[0].width // scale_down; h = tiles[0].height // scale_down; pad = 8; lab = 12 if label else 0
    rows = (len(tiles) + cols - 1) // cols
    sh = Image.new('RGB', (cols * (w + pad) + pad, rows * (h + pad + lab) + pad), 'white'); dd = ImageDraw.Draw(sh)
    for i, (f, t) in enumerate(zip(fs, tiles)):
        x = pad + (i % cols) * (w + pad); y = pad + (i // cols) * (h + pad + lab)
        sh.paste(t.resize((w, h), Image.NEAREST), (x, y))
        if label: dd.text((x, y + h + 1), f[:-4][:30], fill=0)
    p = out or os.path.join(ROOT, 'sheets', cat + '.png'); os.makedirs(os.path.dirname(p), exist_ok=True)
    sh.save(p); return p, len(fs)
