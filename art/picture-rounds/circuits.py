#!/usr/bin/env python3
"""Famous motor-racing circuits as 1-bit track outlines (data: github.com/bacinger/f1-circuits, MIT licence)."""
import json, math, os, sys
from PIL import Image, ImageDraw
from common import *
SRC = os.environ.get('F1_GEO', '/tmp/claude-0/-home-claude/5b9934e5-ccdb-525b-85de-4ba6950b4139/scratchpad/f1/f1.geojson')
PICK = {'Circuit de Monaco': 'monaco', 'Silverstone Circuit': 'silverstone', 'Autodromo Nazionale Monza': 'monza', 'Circuit de Spa-Francorchamps': 'spa-francorchamps',
        'Suzuka International Racing Course': 'suzuka', 'Autódromo José Carlos Pace - Interlagos': 'interlagos', 'Circuit Gilles-Villeneuve': 'circuit-gilles-villeneuve',
        'Circuit of the Americas': 'circuit-of-the-americas', 'Albert Park Circuit': 'albert-park', 'Marina Bay Street Circuit': 'marina-bay', 'Hungaroring': 'hungaroring',
        'Circuit Zandvoort': 'zandvoort', 'Baku City Circuit': 'baku', 'Las Vegas Street Circuit': 'las-vegas', 'Indianapolis Motor Speedway': 'indianapolis',
        'Nürburgring': 'nurburgring', 'Bahrain International Circuit': 'bahrain', 'Yas Marina Circuit': 'yas-marina', 'Autodromo Enzo e Dino Ferrari': 'imola', 'Red Bull Ring': 'red-bull-ring'}

def draw(coords):
    lat0 = sum(c[1] for c in coords) / len(coords); k = math.cos(math.radians(lat0))
    P = [(x * k, -y) for x, y in coords]
    xs = [p[0] for p in P]; ys = [p[1] for p in P]
    sw, sh = max(xs) - min(xs), max(ys) - min(ys); s = min((W - 16) / sw, (H - 14) / sh)
    ox = (W - sw * s) / 2; oy = (H - sh * s) / 2
    T = [((x - min(xs)) * s + ox, (y - min(ys)) * s + oy) for x, y in P]
    SS = 8; big = Image.new('L', (W * SS, H * SS), 0); bd = ImageDraw.Draw(big)
    pts = [(x * SS, y * SS) for x, y in T]
    bd.line(pts + [pts[0]], fill=255, width=int(2.4 * SS), joint='curve')
    for x, y in pts[::max(1, len(pts) // 400)]: bd.ellipse((x - 1.2 * SS, y - 1.2 * SS, x + 1.2 * SS, y + 1.2 * SS), fill=255)
    m = big.resize((W, H), Image.BOX).point(lambda v: 255 if v > 90 else 0).convert('1')
    im, d = canvas(); fill_pattern(im, (1, 1, W - 1, H - 1), 6)
    im.paste(Image.new('1', im.size, BLK), (0, 0), m)
    x, y = T[0]                                                          # chequered start/finish marker
    for i in range(3):
        for j in range(3):
            d.point((int(x) - 1 + i, int(y) - 5 + j), fill=BLK if (i + j) % 2 == 0 else WHT)
    d.rectangle((int(x) - 2, int(y) - 6, int(x) + 2, int(y) - 2), outline=BLK); d.line((int(x), int(y) - 2, int(x), int(y)), fill=BLK)
    frame(d); return im

if __name__ == '__main__':
    for f in json.load(open(SRC))['features']:
        n = f['properties']['Name']
        if n in PICK:
            g = f['geometry']; cs = g['coordinates'] if g['type'] == 'LineString' else max(g['coordinates'], key=len)
            save(draw(cs), 'circuits', PICK[n]); print(PICK[n])
