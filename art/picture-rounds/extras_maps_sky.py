#!/usr/bin/env python3
"""US state outlines, constellations and planets."""
import json, math, os, random
from PIL import Image, ImageDraw
from common import *

# ------------------------------------------------------------------ US states
def state_outlines():
    sts = json.load(open(os.path.join(ROOT, 'states.json')))
    n = 0
    for s in sts:
        if s['name'] in ('District of Columbia', 'Puerto Rico', 'Guam', 'United States Virgin Islands', 'American Samoa', 'Commonwealth of the Northern Mariana Islands'): continue
        g = s['geom']; cs = g['coordinates']
        rs = [p[0] for p in (cs if g['type'] == 'MultiPolygon' else [cs])]
        rs = [[(x + 360 if x < 0 and s['name'] == 'Alaska' and x < -170 else x, y) for x, y in r] for r in rs]
        if s['name'] == 'Alaska': rs = [[(x - 360 if x > 180 else x, y) for x, y in r] for r in rs]
        if s['name'] == 'Alaska': rs = [[(x + 360 if x < -150 and min(q[0] for q in r) < -170 else x, y) for x, y in r] for r in rs]
        area = lambda r: abs(sum(r[i][0] * r[i - 1][1] - r[i - 1][0] * r[i][1] for i in range(len(r)))) / 2
        A = max(area(r) for r in rs); rs = [r for r in rs if area(r) > A * 0.004]
        pts = [p for r in rs for p in r]
        lat0 = (max(p[1] for p in pts) + min(p[1] for p in pts)) / 2; k = math.cos(math.radians(lat0))
        P = [[(x * k, -y) for x, y in r] for r in rs]
        xs = [x for r in P for x, _ in r]; ys = [y for r in P for _, y in r]
        sc = min((W - 12) / (max(xs) - min(xs)), (H - 10) / (max(ys) - min(ys)))
        ox = (W - (max(xs) - min(xs)) * sc) / 2; oy = (H - (max(ys) - min(ys)) * sc) / 2
        im, d = canvas(); fill_pattern(im, (1, 1, W - 1, H - 1), 1)
        for r in P:
            p = [(ox + (x - min(xs)) * sc, oy + (y - min(ys)) * sc) for x, y in r]
            d.polygon([(x + 1, y + 1) for x, y in p], fill=BLK)
        for r in P:
            p = [(ox + (x - min(xs)) * sc, oy + (y - min(ys)) * sc) for x, y in r]
            d.polygon(p, fill=BLK)
        frame(d)
        save(im, 'us-states', s['name'].lower().replace(' ', '-')); n += 1
    return n

# ------------------------------------------------------------------ constellations (real star positions)
def hm(h, m): return (h + m / 60) * 15     # RA hours/minutes → degrees
CONST = {
    'orion': ({'Betelgeuse': (hm(5, 55.2), 7.41, 3), 'Rigel': (hm(5, 14.5), -8.2, 3), 'Bellatrix': (hm(5, 25.1), 6.35, 2), 'Saiph': (hm(5, 47.8), -9.67, 2),
               'Alnitak': (hm(5, 40.8), -1.94, 2), 'Alnilam': (hm(5, 36.2), -1.2, 2), 'Mintaka': (hm(5, 32.0), -0.3, 2), 'Meissa': (hm(5, 35.1), 9.93, 1)},
              [('Betelgeuse', 'Alnitak'), ('Alnitak', 'Alnilam'), ('Alnilam', 'Mintaka'), ('Mintaka', 'Bellatrix'), ('Bellatrix', 'Betelgeuse'),
               ('Alnitak', 'Saiph'), ('Mintaka', 'Rigel'), ('Betelgeuse', 'Meissa'), ('Bellatrix', 'Meissa')]),
    'big-dipper': ({'Dubhe': (hm(11, 3.7), 61.75, 3), 'Merak': (hm(11, 1.8), 56.38, 2), 'Phecda': (hm(11, 53.8), 53.69, 2), 'Megrez': (hm(12, 15.4), 57.03, 1),
                    'Alioth': (hm(12, 54.0), 55.96, 3), 'Mizar': (hm(13, 23.9), 54.93, 2), 'Alkaid': (hm(13, 47.5), 49.31, 2)},
                   [('Dubhe', 'Merak'), ('Merak', 'Phecda'), ('Phecda', 'Megrez'), ('Megrez', 'Dubhe'), ('Megrez', 'Alioth'), ('Alioth', 'Mizar'), ('Mizar', 'Alkaid')]),
    'cassiopeia': ({'Caph': (hm(0, 9.2), 59.15, 2), 'Schedar': (hm(0, 40.5), 56.54, 2), 'Gamma': (hm(0, 56.7), 60.72, 2), 'Ruchbah': (hm(1, 25.8), 60.24, 2), 'Segin': (hm(1, 54.4), 63.67, 1)},
                   [('Caph', 'Schedar'), ('Schedar', 'Gamma'), ('Gamma', 'Ruchbah'), ('Ruchbah', 'Segin')]),
    'southern-cross': ({'Acrux': (hm(12, 26.6), -63.1, 3), 'Mimosa': (hm(12, 47.7), -59.69, 3), 'Gacrux': (hm(12, 31.2), -57.11, 2), 'Delta': (hm(12, 15.1), -58.75, 2),
                        'Epsilon': (hm(12, 21.4), -60.4, 1), 'AlphaCen': (hm(14, 39.6), -60.83, 3), 'BetaCen': (hm(14, 3.8), -60.37, 3)},
                       [('Acrux', 'Gacrux'), ('Mimosa', 'Delta')]),
    'cygnus': ({'Deneb': (hm(20, 41.4), 45.28, 3), 'Sadr': (hm(20, 22.2), 40.26, 2), 'Albireo': (hm(19, 30.7), 27.96, 2), 'Gienah': (hm(20, 46.2), 33.97, 2), 'Delta': (hm(19, 45.0), 45.13, 2)},
               [('Deneb', 'Sadr'), ('Sadr', 'Albireo'), ('Gienah', 'Sadr'), ('Sadr', 'Delta')]),
    'leo': ({'Regulus': (hm(10, 8.4), 11.97, 3), 'Denebola': (hm(11, 49.1), 14.57, 2), 'Algieba': (hm(10, 20.0), 19.84, 2), 'Zosma': (hm(11, 14.1), 20.52, 2),
             'Chertan': (hm(11, 14.2), 15.43, 1), 'Eta': (hm(10, 7.3), 16.76, 1), 'Adhafera': (hm(10, 16.7), 23.42, 1), 'Rasalas': (hm(9, 52.8), 26.0, 1), 'Epsilon': (hm(9, 45.9), 23.77, 2)},
            [('Regulus', 'Eta'), ('Eta', 'Algieba'), ('Algieba', 'Adhafera'), ('Adhafera', 'Rasalas'), ('Rasalas', 'Epsilon'), ('Algieba', 'Zosma'),
             ('Zosma', 'Denebola'), ('Denebola', 'Chertan'), ('Chertan', 'Regulus'), ('Chertan', 'Zosma')]),
    'scorpius': ({'Antares': (hm(16, 29.4), -26.43, 3), 'Graffias': (hm(16, 5.4), -19.8, 2), 'Dschubba': (hm(16, 0.3), -22.62, 2), 'Pi': (hm(15, 58.9), -26.11, 1),
                  'Sigma': (hm(16, 21.2), -25.59, 1), 'Tau': (hm(16, 35.9), -28.22, 1), 'Eps': (hm(16, 50.2), -34.29, 2), 'Mu': (hm(16, 51.9), -38.05, 1),
                  'Zeta': (hm(16, 54.6), -42.36, 1), 'Eta': (hm(17, 12.2), -43.24, 1), 'Theta': (hm(17, 37.3), -43.0, 2), 'Iota': (hm(17, 47.6), -40.13, 1),
                  'Kappa': (hm(17, 42.5), -39.03, 1), 'Shaula': (hm(17, 33.6), -37.1, 2), 'Lesath': (hm(17, 30.8), -37.3, 1)},
                 [('Graffias', 'Dschubba'), ('Dschubba', 'Pi'), ('Dschubba', 'Sigma'), ('Sigma', 'Antares'), ('Antares', 'Tau'), ('Tau', 'Eps'), ('Eps', 'Mu'),
                  ('Mu', 'Zeta'), ('Zeta', 'Eta'), ('Eta', 'Theta'), ('Theta', 'Iota'), ('Iota', 'Kappa'), ('Kappa', 'Shaula'), ('Shaula', 'Lesath')]),
    'lyra': ({'Vega': (hm(18, 36.9), 38.78, 3), 'Eps': (hm(18, 44.3), 39.61, 1), 'Zeta': (hm(18, 44.8), 37.6, 1), 'Delta': (hm(18, 54.5), 36.9, 1),
              'Gamma': (hm(18, 59.0), 32.69, 2), 'Beta': (hm(18, 50.1), 33.36, 2)},
             [('Vega', 'Eps'), ('Vega', 'Zeta'), ('Eps', 'Zeta'), ('Zeta', 'Beta'), ('Beta', 'Gamma'), ('Gamma', 'Delta'), ('Delta', 'Zeta')]),
    'pegasus': ({'Markab': (hm(23, 4.8), 15.2, 2), 'Scheat': (hm(23, 3.8), 28.08, 2), 'Algenib': (hm(0, 13.2), 15.18, 2), 'Alpheratz': (hm(0, 8.4), 29.09, 2),
                 'Homam': (hm(22, 41.5), 10.83, 1), 'Biham': (hm(22, 10.0), 6.2, 1), 'Enif': (hm(21, 44.2), 9.88, 2)},
                [('Markab', 'Scheat'), ('Scheat', 'Alpheratz'), ('Alpheratz', 'Algenib'), ('Algenib', 'Markab'), ('Markab', 'Homam'), ('Homam', 'Biham'), ('Biham', 'Enif')]),
    'taurus': ({'Aldebaran': (hm(4, 35.9), 16.51, 3), 'Elnath': (hm(5, 26.3), 28.61, 2), 'Zeta': (hm(5, 37.6), 21.14, 2), 'Gamma': (hm(4, 19.8), 15.63, 1),
                'Delta': (hm(4, 22.9), 17.54, 1), 'Eps': (hm(4, 28.6), 19.18, 1), 'Theta': (hm(4, 28.7), 15.87, 1),
                'P1': (hm(3, 47.5), 24.1, 1), 'P2': (hm(3, 45.8), 24.4, 1), 'P3': (hm(3, 49.2), 24.05, 1), 'P4': (hm(3, 46.3), 23.95, 1), 'P5': (hm(3, 44.9), 24.1, 1)},
               [('Elnath', 'Eps'), ('Eps', 'Delta'), ('Delta', 'Gamma'), ('Gamma', 'Theta'), ('Theta', 'Aldebaran'), ('Aldebaran', 'Zeta')]),
    'gemini': ({'Castor': (hm(7, 34.6), 31.89, 3), 'Pollux': (hm(7, 45.3), 28.03, 3), 'Alhena': (hm(6, 37.7), 16.4, 2), 'Mebsuta': (hm(6, 43.9), 25.13, 1),
                'Tejat': (hm(6, 23.0), 22.51, 1), 'Wasat': (hm(7, 20.1), 21.98, 1), 'Xi': (hm(6, 45.3), 12.9, 1), 'Propus': (hm(6, 14.9), 22.5, 1)},
               [('Castor', 'Pollux'), ('Castor', 'Mebsuta'), ('Mebsuta', 'Tejat'), ('Tejat', 'Propus'), ('Pollux', 'Wasat'), ('Wasat', 'Alhena'), ('Wasat', 'Xi')]),
    'little-dipper': ({'Polaris': (hm(2, 31.8), 89.26, 3), 'Yildun': (hm(17, 32.2), 86.59, 1), 'Eps': (hm(16, 46.0), 82.04, 1), 'Zeta': (hm(15, 44.1), 77.79, 1),
                       'Eta': (hm(16, 17.5), 75.76, 1), 'Kochab': (hm(14, 50.7), 74.16, 3), 'Pherkad': (hm(15, 20.7), 71.83, 2)},
                      [('Polaris', 'Yildun'), ('Yildun', 'Eps'), ('Eps', 'Zeta'), ('Zeta', 'Eta'), ('Eta', 'Pherkad'), ('Pherkad', 'Kochab'), ('Kochab', 'Zeta')]),
}

def constellation(name):
    stars, lines = CONST[name]
    # tangent-plane projection about the mean direction
    vecs = {k: (math.cos(math.radians(de)) * math.cos(math.radians(ra)), math.cos(math.radians(de)) * math.sin(math.radians(ra)), math.sin(math.radians(de))) for k, (ra, de, _) in stars.items()}
    cx = sum(v[0] for v in vecs.values()); cy = sum(v[1] for v in vecs.values()); cz = sum(v[2] for v in vecs.values())
    n = math.sqrt(cx * cx + cy * cy + cz * cz); c = (cx / n, cy / n, cz / n)
    ra0 = math.atan2(c[1], c[0]); de0 = math.asin(c[2])
    def proj(ra, de):
        ra, de = math.radians(ra), math.radians(de)
        cosc = math.sin(de0) * math.sin(de) + math.cos(de0) * math.cos(de) * math.cos(ra - ra0)
        x = math.cos(de) * math.sin(ra - ra0) / cosc
        y = (math.cos(de0) * math.sin(de) - math.sin(de0) * math.cos(de) * math.cos(ra - ra0)) / cosc
        return -x, -y                    # east to the left, north up
    P = {k: proj(ra, de) for k, (ra, de, _) in stars.items()}
    xs = [p[0] for p in P.values()]; ys = [p[1] for p in P.values()]
    sc = min((W - 20) / max(1e-6, max(xs) - min(xs)), (H - 16) / max(1e-6, max(ys) - min(ys)))
    ox = (W - (max(xs) - min(xs)) * sc) / 2; oy = (H - (max(ys) - min(ys)) * sc) / 2
    S2 = {k: (ox + (x - min(xs)) * sc, oy + (y - min(ys)) * sc) for k, (x, y) in P.items()}
    im, d = canvas(BLK)
    r = random.Random(hash(name) % 1000)
    for _ in range(40): im.putpixel((r.randint(1, W - 2), r.randint(1, H - 2)), WHT)       # faint background stars
    for a, b in lines:
        (x0, y0), (x1, y1) = S2[a], S2[b]; L = int(max(abs(x1 - x0), abs(y1 - y0)))
        for i in range(0, L + 1, 2):
            t = i / max(1, L); im.putpixel((int(round(x0 + (x1 - x0) * t)), int(round(y0 + (y1 - y0) * t))), WHT)
    for k, (x, y) in S2.items():
        mag = stars[k][2]; x, y = int(round(x)), int(round(y))
        if mag >= 3:
            d.rectangle((x - 1, y - 1, x + 1, y + 1), fill=WHT); d.point((x - 2, y), fill=WHT); d.point((x + 2, y), fill=WHT); d.point((x, y - 2), fill=WHT); d.point((x, y + 2), fill=WHT)
        elif mag == 2: d.rectangle((x - 1, y - 1, x + 1, y + 1), fill=WHT); d.point((x - 1, y - 1), fill=BLK); d.point((x + 1, y + 1), fill=BLK)
        else: d.rectangle((x, y, x + 1, y + 1), fill=WHT)
    d.rectangle((0, 0, W - 1, H - 1), outline=BLK)
    return im

# ------------------------------------------------------------------ planets
def planet_base(r=24, cx=48, cy=32):
    im, d = canvas(BLK)
    rr = random.Random(r)
    for _ in range(30): im.putpixel((rr.randint(1, W - 2), rr.randint(1, H - 2)), WHT)
    return im, d

def disc_mask(cx, cy, r):
    m = Image.new('1', (W, H), 0); ImageDraw.Draw(m).ellipse((cx - r, cy - r, cx + r, cy + r), fill=1); return m

def shaded_disc(im, d, cx, cy, r, level=0):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=WHT)
    if level: shade(im, lambda dd: dd.ellipse((cx - r, cy - r, cx + r, cy + r), fill=1), level)
    # terminator shadow on the right
    m = disc_mask(cx, cy, r); md = Image.new('1', (W, H), 0); ImageDraw.Draw(md).ellipse((cx - r + r // 3, cy - r - 2, cx + r + r, cy + r + 2), fill=1)
    shadow = Image.new('1', (W, H), 0); shadow.paste(md, (0, 0), m)
    darker = Image.new("1", (W, H), WHT); fill_pattern(darker, (0, 0, W, H), 5)
    im.paste(darker, (0, 0), shadow)

def planets():
    out = {}
    im, d = planet_base(); shaded_disc(im, d, 48, 32, 22, 2)                                   # Mercury: cratered grey
    for x, y, r in ((40, 24, 4), (52, 38, 3), (36, 38, 2), (46, 46, 2), (56, 22, 2)): d.ellipse((x - r, y - r, x + r, y + r), outline=BLK)
    out['mercury'] = im
    im, d = planet_base(); shaded_disc(im, d, 48, 32, 24, 6)                                   # Venus: bright, swirled clouds
    for y in range(14, 52, 6): d.arc((20, y - 8, 76, y + 8), 200, 340, fill=BLK)
    out['venus'] = im
    im, d = planet_base(); shaded_disc(im, d, 48, 32, 24, 0)                                   # Earth: oceans + continents + clouds
    m = disc_mask(48, 32, 24); sea = Image.new('1', (W, H), WHT); fill_pattern(sea, (0, 0, W, H), 1); im.paste(sea, (0, 0), m)
    land = [(34, 14), (44, 12), (50, 18), (46, 26), (52, 34), (48, 48), (42, 52), (40, 40), (34, 32), (30, 22)]
    d.polygon(land, fill=BLK); d.polygon([(56, 14), (66, 18), (64, 26), (58, 24)], fill=BLK)
    for x0, y0 in ((52, 40), (30, 34), (58, 30)): d.ellipse((x0, y0, x0 + 10, y0 + 3), fill=WHT)
    d.chord((38, 6, 58, 14), 180, 360, fill=WHT)
    out['earth'] = im
    im, d = planet_base(); shaded_disc(im, d, 48, 32, 22, 2)                                   # Mars: rust disc, polar cap, Valles
    d.chord((38, 9, 58, 18), 180, 360, fill=WHT); d.line((36, 30, 56, 34), fill=BLK, width=2)
    for x, y in ((42, 40), (52, 24)): d.ellipse((x - 3, y - 2, x + 3, y + 2), fill=BLK)
    out['mars'] = im
    im, d = planet_base(); shaded_disc(im, d, 48, 32, 26, 0)                                   # Jupiter: bands + Great Red Spot
    m = disc_mask(48, 32, 26); bands = Image.new('1', (W, H), WHT); bd = ImageDraw.Draw(bands)
    for y0, y1, lv in ((8, 14, 2), (18, 22, 3), (27, 29, 1), (34, 38, 3), (42, 46, 2), (50, 56, 1)): fill_pattern(bands, (0, y0, W, y1), lv)
    im.paste(bands, (0, 0), m); d.ellipse((50, 36, 62, 43), fill=WHT, outline=BLK); fill_pattern(im, (53, 38, 60, 42), 3)
    out['jupiter'] = im
    im, d = planet_base(); shaded_disc(im, d, 48, 32, 17, 1)                                   # Saturn: rings
    d.ellipse((10, 24, 86, 40), outline=WHT); d.ellipse((14, 26, 82, 38), outline=WHT); d.ellipse((18, 27, 78, 37), outline=WHT)
    d.chord((31, 15, 65, 49), 200, 340, fill=WHT); fill_pattern(im, (32, 16, 64, 26), 1)
    d.line((31, 32, 65, 32), fill=BLK)
    out['saturn'] = im
    im, d = planet_base(); shaded_disc(im, d, 48, 32, 20, 6)                                   # Uranus: tilted on its side, faint vertical rings
    d.ellipse((42, 4, 54, 60), outline=WHT)
    out['uranus'] = im
    im, d = planet_base(); shaded_disc(im, d, 48, 32, 20, 2)                                   # Neptune: deep blue + Great Dark Spot
    d.ellipse((38, 24, 48, 30), fill=BLK); d.arc((40, 18, 60, 30), 200, 320, fill=WHT)
    out['neptune'] = im
    im, d = planet_base(); shaded_disc(im, d, 48, 32, 18, 1)                                   # Pluto: the "heart"
    d.polygon([(48, 44), (40, 36), (40, 30), (44, 28), (48, 32), (52, 28), (56, 30), (56, 36)], fill=WHT)
    out['pluto'] = im
    im, d = planet_base(); shaded_disc(im, d, 48, 32, 24, 1)                                   # the Moon: maria + craters
    for x, y, r in ((40, 22, 7), (52, 26, 6), (44, 36, 5), (54, 40, 3)): d.ellipse((x - r, y - r, x + r, y + r), fill=BLK)
    d.ellipse((44, 46, 50, 52), outline=BLK); d.line((47, 52, 47, 56), fill=BLK)
    out['the-moon'] = im
    return out

if __name__ == '__main__':
    print('states', state_outlines())
    for k in CONST: save(constellation(k), 'constellations', k)
    for k, im in planets().items(): save(im, 'planets', k)
    print(sheet('us-states', cols=10), sheet('constellations', cols=6, scale_down=1), sheet('planets', cols=5, scale_down=1))
