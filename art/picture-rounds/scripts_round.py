#!/usr/bin/env python3
"""Writing systems: 'hello' written in a script, rendered as 1-bit pixel text on a little card."""
import os, sys
from PIL import Image, ImageDraw, ImageFont
from common import *
FD = os.environ.get('FONT_DIR', '/tmp/claude-0/-home-claude/5b9934e5-ccdb-525b-85de-4ba6950b4139/scratchpad/fonts')
DJ = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
CJK = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
ITEMS = {   # slug: (text, font, ttc index, direction)
    'greek': ('Γειά σου', DJ, 0, None), 'cyrillic': ('Привет', DJ, 0, None), 'hebrew': ('שלום', f'{FD}/hebrew.ttf', 0, 'rtl'),
    'arabic': ('مرحبا', f'{FD}/arabic.ttf', 0, 'rtl'), 'devanagari': ('नमस्ते', f'{FD}/devanagari.ttf', 0, None),
    'hangul': ('안녕하세요', CJK, 1, None), 'japanese-hiragana': ('こんにちは', CJK, 0, None), 'chinese-characters': ('你好', CJK, 2, None),
    'thai': ('สวัสดี', f'{FD}/thai.ttf', 0, None), 'georgian': ('გამარჯობა', DJ, 0, None), 'armenian': ('Բարեւ', DJ, 0, None),
    'geez-ethiopic': ('ሰላም', f'{FD}/ethiopic.ttf', 0, None)}

def card(text, font, idx, direction):
    SS = 8; big = Image.new('L', (W * SS, H * SS), 0); d = ImageDraw.Draw(big)
    size = 40 * SS
    while True:
        f = ImageFont.truetype(font, size, index=idx)
        box = d.textbbox((0, 0), text, font=f, direction=direction)
        if (box[2] - box[0]) <= 78 * SS and (box[3] - box[1]) <= 30 * SS: break
        size -= 8
    w, h = box[2] - box[0], box[3] - box[1]
    d.text(((W * SS - w) / 2 - box[0], (34 * SS - h / 2) - box[1]), text, font=f, fill=255, direction=direction)
    m = big.resize((W, H), Image.BOX).point(lambda v: 255 if v > 100 else 0).convert('1')
    im, dd = canvas(); fill_pattern(im, (1, 1, W - 1, H - 1), 6)
    dd.rectangle((6, 12, 90, 56), fill=WHT, outline=BLK); dd.line((8, 57, 91, 57), fill=BLK); dd.line((91, 14, 91, 57), fill=BLK)   # card with shadow
    dd.rectangle((6, 12, 90, 17), fill=BLK)
    for x in range(10, 88, 3): dd.point((x, 14), fill=WHT)
    im.paste(Image.new('1', im.size, BLK), (0, 0), m)
    frame(dd); return im

if __name__ == '__main__':
    for s in sys.argv[1:] or ITEMS: save(card(*ITEMS[s]), 'scripts', s); print(s)
