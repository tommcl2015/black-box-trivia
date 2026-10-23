#!/usr/bin/env python3
"""Famous public-domain paintings as 8-bit colour pixel art (from photographs of the originals)."""
import os
from PIL import Image, ImageDraw
from common import W, H, save

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'paintings_src')
# slug: (file, crop box as fractions or None)
PAINTINGS = {
    'mona-lisa': ('mona.png', None),
    'the-starry-night': ('starry.jpg', None),
    'the-scream': ('scream.jpg', None),
    'the-great-wave-off-kanagawa': ('wave2.jpg', None),
    'water-lilies-monet': ('lilies.jpg', None),
    'woman-with-a-hat-matisse': ('matisse.jpg', None),
    'composition-vii-kandinsky': ('comp7.jpg', None),
    'self-portrait-van-gogh': ('gogh.jpg', None),
    'shipwreck-of-the-minotaur-turner': ('turner.jpg', None),
    'still-life-with-apples-cezanne': ('cezanne.jpg', None),
}
WALL = (60, 60, 70); FRAME = (176, 128, 40); FRAME_D = (110, 72, 20)

def paint8(fn, colours=16):
    src = Image.open(os.path.join(SRC, fn)).convert('RGB')
    maxw, maxh = W - 10, H - 10
    s = min(maxw / src.width, maxh / src.height)
    w, h = max(8, round(src.width * s)), max(8, round(src.height * s))
    small = src.resize((w, h), Image.LANCZOS)
    q = small.quantize(colors=colours, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).convert('RGB')
    im = Image.new('RGB', (W, H), WALL); d = ImageDraw.Draw(im)
    x0, y0 = (W - w) // 2, (H - h) // 2
    d.rectangle((x0 - 3, y0 - 3, x0 + w + 2, y0 + h + 2), fill=FRAME)
    d.rectangle((x0 - 3, y0 - 3, x0 + w + 2, y0 + h + 2), outline=FRAME_D)
    d.rectangle((x0 - 1, y0 - 1, x0 + w, y0 + h), outline=FRAME_D)
    im.paste(q, (x0, y0))
    d.rectangle((0, 0, W - 1, H - 1), outline=(0, 0, 0))
    return im

if __name__ == '__main__':
    for slug, (fn, _) in PAINTINGS.items():
        save(paint8(fn), 'paintings8', slug)
    from common import sheet
    print(sheet('paintings8', cols=5, scale_down=1))
