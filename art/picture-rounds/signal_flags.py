#!/usr/bin/env python3
"""International maritime signal flags (ICS) as NES-style 8-bit art: flag flying from a mast against the sky.
48x32 cells at 2x. O (Oscar) and Y (Yankee) left out (diagonal layouts too easy to get subtly wrong)."""
import sys
from PIL import Image, ImageDraw
from common import W, H, save
from paintings_nes import K

CW, CH = W // 2, H // 2
R, Wt, B, Y, BK = (216, 40, 0), (252, 252, 252), (0, 88, 248), (248, 184, 0), (0, 0, 0)
SKY, SKY2, POLE, POLE_D, ROPE = (164, 228, 252), (60, 188, 252), (172, 124, 0), (80, 48, 0), (240, 208, 176)
X0, Y0, FW, FH = 12, 6, 30, 20            # flag box in cells

def flag(letter):
    f = Image.new('RGB', (FW, FH), Wt); d = ImageDraw.Draw(f); w, h = FW, FH
    def vbands(cols):
        n = len(cols)
        for i, c in enumerate(cols): d.rectangle((round(i * w / n), 0, round((i + 1) * w / n) - 1, h), fill=c)
    def hbands(cols, sizes=None):
        sizes = sizes or [1] * len(cols); t = sum(sizes); y = 0
        for c, s in zip(cols, sizes):
            y1 = y + s * h / t; d.rectangle((0, round(y), w, round(y1) - 1), fill=c); y = y1
    def quarters(a, b):
        d.rectangle((0, 0, w, h), fill=b); d.rectangle((0, 0, w // 2 - 1, h // 2 - 1), fill=a); d.rectangle((w // 2, h // 2, w, h), fill=a)
    def saltire(bg, fg, t=3):
        d.rectangle((0, 0, w, h), fill=bg); d.line((0, 0, w - 1, h - 1), fill=fg, width=t); d.line((0, h - 1, w - 1, 0), fill=fg, width=t)
    def cross(bg, fg, t=4):
        d.rectangle((0, 0, w, h), fill=bg); d.rectangle((w // 2 - t // 2, 0, w // 2 + t // 2 - 1, h), fill=fg); d.rectangle((0, h // 2 - t // 2, w, h // 2 + t // 2 - 1), fill=fg)
    def centre(bg, fg, fw, fh):
        d.rectangle((0, 0, w, h), fill=bg); d.rectangle((w // 2 - fw // 2, h // 2 - fh // 2, w // 2 + fw // 2 - 1, h // 2 + fh // 2 - 1), fill=fg)
    L = letter
    if L == 'A': vbands([Wt, B])
    elif L == 'B': d.rectangle((0, 0, w, h), fill=R)
    elif L == 'C': hbands([B, Wt, R, Wt, B])
    elif L == 'D': hbands([Y, B, Y], [1, 2, 1])
    elif L == 'E': hbands([B, R])
    elif L == 'F': d.rectangle((0, 0, w, h), fill=Wt); d.polygon([(w / 2, 0), (w - 1, h / 2), (w / 2, h - 1), (0, h / 2)], fill=R)
    elif L == 'G': vbands([Y, B, Y, B, Y, B])
    elif L == 'H': vbands([Wt, R])
    elif L == 'I': d.rectangle((0, 0, w, h), fill=Y); d.ellipse((w / 2 - 6, h / 2 - 6, w / 2 + 5, h / 2 + 5), fill=BK)
    elif L == 'J': hbands([B, Wt, B])
    elif L == 'K': vbands([Y, B])
    elif L == 'L': quarters(Y, BK)
    elif L == 'M': saltire(B, Wt, 4)
    elif L == 'N':
        for i in range(4):
            for j in range(4): d.rectangle((round(i * w / 4), round(j * h / 4), round((i + 1) * w / 4) - 1, round((j + 1) * h / 4) - 1), fill=B if (i + j) % 2 == 0 else Wt)
    elif L == 'P': centre(B, Wt, 12, 8)
    elif L == 'Q': d.rectangle((0, 0, w, h), fill=Y)
    elif L == 'R': cross(R, Y, 4)
    elif L == 'S': centre(Wt, B, 12, 8)
    elif L == 'T': vbands([R, Wt, B])
    elif L == 'U': quarters(R, Wt)
    elif L == 'V': saltire(Wt, R, 4)
    elif L == 'W': d.rectangle((0, 0, w, h), fill=B); d.rectangle((4, 4, w - 5, h - 5), fill=Wt); d.rectangle((8, 7, w - 9, h - 8), fill=R)
    elif L == 'X': cross(Wt, B, 4)
    elif L == 'Z':
        c = (w / 2, h / 2)
        d.polygon([(0, 0), (w, 0), c], fill=Y); d.polygon([(w, 0), (w, h), c], fill=B)
        d.polygon([(w, h), (0, h), c], fill=R); d.polygon([(0, h), (0, 0), c], fill=BK)
    mask = Image.new('1', (FW, FH), 1)
    if L in 'AB': ImageDraw.Draw(mask).polygon([(w, 0), (w - 9, h / 2), (w, h)], fill=0)   # swallowtail
    return f, mask

def picture(letter):
    g = Image.new('RGB', (CW, CH), SKY); d = ImageDraw.Draw(g)
    for y in range(0, 9): 
        for x in range((y % 2), CW, 2):
            if y < 5 or (x + y) % 4 == 0: d.point((x, y), fill=SKY2)
    d.rectangle((0, 27, CW, CH), fill=(0, 88, 248))                                   # sea
    for x in range(0, CW, 4): d.point((x + 1, 28), fill=Wt); d.point((x + 3, 30), fill=SKY2)
    d.rectangle((8, 1, 9, 29), fill=POLE); d.line((9, 1, 9, 29), fill=POLE_D); d.rectangle((7, 0, 10, 1), fill=Y)   # mast + truck
    f, m = flag(letter)
    ol = Image.new('RGB', (FW + 2, FH + 2), BK); olm = Image.new('1', (FW + 2, FH + 2), 0)
    for dx in (0, 1, 2):
        for dy in (0, 1, 2): olm.paste(1, (dx, dy), m) if False else olm.paste(m, (dx, dy), m)
    g.paste(ol, (X0 - 1, Y0 - 1), olm); g.paste(f, (X0, Y0), m)
    d.line((10, Y0, X0 - 1, Y0), fill=ROPE); d.line((10, Y0 + FH - 1, X0 - 1, Y0 + FH - 1), fill=ROPE)   # halyard
    big = g.resize((W, H), Image.NEAREST); ImageDraw.Draw(big).rectangle((0, 0, W - 1, H - 1), outline=K); return big

LETTERS = 'ABCDEFGHIJKLMNPQRSTUVWXZ'
if __name__ == '__main__':
    for L in sys.argv[1:] or LETTERS: save(picture(L), 'signalflags', L.lower())
