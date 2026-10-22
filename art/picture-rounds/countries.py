#!/usr/bin/env python3
"""Every country: a 1-bit outline ('What country is this?') and a locator map ('Which country is highlighted?')."""
import json, math, os
from PIL import Image, ImageDraw
from common import *

# UN members + observer/partially recognised states commonly asked about
UN = """AF AL DZ AD AO AG AR AM AU AT AZ BS BH BD BB BY BE BZ BJ BT BO BA BW BR BN BG BF BI CV KH CM CA CF TD CL CN CO KM CG CD CR CI HR CU CY CZ
DK DJ DM DO EC EG SV GQ ER EE SZ ET FJ FI FR GA GM GE DE GH GR GD GT GN GW GY HT HN HU IS IN ID IR IQ IE IL IT JM JP JO KZ KE KI KP KR KW KG LA LV
LB LS LR LY LI LT LU MG MW MY MV ML MT MH MR MU MX FM MD MC MN ME MA MZ MM NA NR NP NL NZ NI NE NG MK NO OM PK PW PA PG PY PE PH PL PT QA RO RU RW
KN LC VC WS SM ST SA SN RS SC SL SG SK SI SB SO ZA SS ES LK SD SR SE CH SY TJ TZ TH TL TG TO TT TN TR TM TV UG UA AE GB US UY UZ VU VE VN YE ZM ZW
VA PS TW XK""".split()

NAMES = {'US': 'United States', 'GB': 'United Kingdom', 'CD': 'DR Congo', 'CG': 'Republic of the Congo', 'CF': 'Central African Republic',
         'BA': 'Bosnia and Herzegovina', 'DO': 'Dominican Republic', 'SZ': 'Eswatini', 'SS': 'South Sudan', 'SB': 'Solomon Islands',
         'GQ': 'Equatorial Guinea', 'MH': 'Marshall Islands', 'VC': 'Saint Vincent and the Grenadines', 'KN': 'Saint Kitts and Nevis',
         'AG': 'Antigua and Barbuda', 'ST': 'Sao Tome and Principe', 'MK': 'North Macedonia', 'CI': 'Ivory Coast', 'VA': 'Vatican City',
         'CZ': 'Czechia', 'TL': 'Timor-Leste', 'XK': 'Kosovo', 'PS': 'Palestine', 'FM': 'Micronesia', 'CV': 'Cape Verde', 'TV': 'Tuvalu'}
ARCHI = {'BS','MV','CV','KM','SC','PH','ID','SB','VU','FJ','GR','JP','WS','PW'}
PACIFIC = {'KI','TV','NR','MH','FM','PW','TO','WS','VU','SB','FJ'}
NO_OUTLINE = {'KI','FM','MH','TO','TV'}
POINTS = {'TV': (179.2, -8.5)}           # not in the 50m data: shown as a marked point on the locator
MERGE = {'SO': ['Somaliland'], 'CY': ['N. Cyprus'], 'IN': ['Siachen Glacier']}

world = json.load(open(os.path.join(ROOT, 'world.json')))
by_a2 = {}
for f in world:
    k = f['a2'] or ('XK' if f['name'] == 'Kosovo' else None)
    if k and f['name'] not in ('Ashmore and Cartier Is.',): by_a2.setdefault(k, f)
by_name = {f['name']: f for f in world}

def rings(geom):
    cs = geom['coordinates']
    return [p[0] for p in (cs if geom['type'] == 'MultiPolygon' else [cs])]

def area(r): return abs(sum(r[i][0] * r[i - 1][1] - r[i - 1][0] * r[i][1] for i in range(len(r)))) / 2
def centroid(r): return (sum(p[0] for p in r) / len(r), sum(p[1] for p in r) / len(r))

def country_rings(a2):
    f = by_a2[a2]; rs = rings(f['geom'])
    for extra in MERGE.get(a2, []): rs += rings(by_name[extra]['geom'])
    lons = [p[0] for r in rs for p in r]
    if min(lons) < -150 and max(lons) > 150:            # crosses the date line
        rs = [[(x + 360 if x < 0 else x, y) for x, y in r] for r in rs]
    return rs

def main_rings(a2):
    rs = country_rings(a2)
    big = max(rs, key=area); A = area(big); cx, cy = centroid(big)
    span = max(max(p[0] for p in big) - min(p[0] for p in big), max(p[1] for p in big) - min(p[1] for p in big))
    lim = max(10, 1.2 * span)
    keep = []
    for r in rs:
        x, y = centroid(r)
        if a2 == 'US' and (x < -130 or y > 50): continue
        if math.hypot(x - cx, y - cy) > lim: continue
        if a2 == 'NO' and y > 71: continue
        if area(r) < A * (0.0002 if a2 in ARCHI else 0.002): continue
        keep.append(r)
    return keep

def project(rs, box, lat0):
    k = math.cos(math.radians(lat0))
    P = [[(x * k, -y) for x, y in r] for r in rs]
    return P

def outline(a2):
    rs = main_rings(a2)
    allpts = [p for r in rs for p in r]
    lat0 = (max(p[1] for p in allpts) + min(p[1] for p in allpts)) / 2
    P = project(rs, None, lat0)
    xs = [x for r in P for x, _ in r]; ys = [y for r in P for _, y in r]
    sw, shh = max(xs) - min(xs), max(ys) - min(ys)
    sc = min((W - 12) / sw, (H - 10) / shh)
    ox = (W - sw * sc) / 2; oy = (H - shh * sc) / 2
    pts = [[(ox + (x - min(xs)) * sc, oy + (y - min(ys)) * sc) for x, y in r] for r in P]
    im, d = canvas(); fill_pattern(im, (1, 1, W - 1, H - 1), 1)
    for p in pts:
        if len(p) > 2: d.polygon([(x + 1, y + 1) for x, y in p], fill=BLK)
    for p in pts:
        if len(p) > 2: d.polygon(p, fill=WHT)
    for p in pts:
        if len(p) > 2: d.polygon(p, fill=BLK)
        # tiny islands still get a visible dot
        if max(x for x, _ in p) - min(x for x, _ in p) < 1.5: d.point(p[0], fill=BLK)
    frame(d)
    detail = sum(len(r) for r in rs)
    return im, detail

def unwrap(r, near):
    xs = [x for x, _ in r]
    if max(xs) - min(xs) > 180: r = [(x + 360 if x < 0 else x, y) for x, y in r]
    mx = sum(x for x, _ in r) / len(r)
    while mx - near > 180: r = [(x - 360, y) for x, y in r]; mx -= 360
    while near - mx > 180: r = [(x + 360, y) for x, y in r]; mx += 360
    return r

def locator(a2, min_span=16):
    if a2 in POINTS:
        cx, cy = POINTS[a2]; tx0 = tx1 = cx; ty0 = ty1 = cy; target = []
    else:
        target = main_rings(a2)
        pts = [p for r in target for p in r]
        tx0, tx1 = min(p[0] for p in pts), max(p[0] for p in pts); ty0, ty1 = min(p[1] for p in pts), max(p[1] for p in pts)
        cx, cy = (tx0 + tx1) / 2, (ty0 + ty1) / 2
    k = math.cos(math.radians(max(-70, min(70, cy))))
    span_x = max((tx1 - tx0) * k * 2.6, (ty1 - ty0) * 2.6 * 1.5, min_span)
    span_y = span_x / 1.5
    x0 = cx * k - span_x / 2; y0 = -cy - span_y / 2
    sc = W / span_x
    tp = lambda x, y: ((x * k - x0) * sc, (-y - y0) * sc)
    im, d = canvas()
    land = Image.new('1', (W, H), 0); ld = ImageDraw.Draw(land)
    borders = []
    for f in world:
        if f['name'] == 'Antarctica': continue
        for r in rings(f['geom']):
            p = [tp(x, y) for x, y in unwrap(r, cx)]
            xs = [q[0] for q in p]; ys = [q[1] for q in p]
            if max(xs) < -5 or min(xs) > W + 5 or max(ys) < -5 or min(ys) > H + 5: continue
            if len(p) > 2: ld.polygon(p, fill=1); borders.append(p)
    shade(im, lambda dd: dd.bitmap((0, 0), land, fill=1), 2)
    for p in borders: d.line(p + [p[0]], fill=WHT)
    mask = Image.new('1', (W, H), 0); md = ImageDraw.Draw(mask)
    for r in target:
        p = [tp(x, y) for x, y in unwrap(r, cx)]
        if len(p) > 2: d.polygon(p, fill=BLK, outline=BLK); md.polygon(p, fill=1)
    if sum(mask.get_flattened_data()) < 40:                       # tiny: zoom out for context, then ring it
        if min_span < 40: return locator(a2, 70 if a2 in PACIFIC else 40)
        mx, my = tp(cx, cy)
        d.ellipse((mx - 1, my - 1, mx + 1, my + 1), fill=BLK)
        for rr in (5, 6): d.ellipse((mx - rr, my - rr, mx + rr, my + rr), outline=BLK)
    frame(d)
    return im

if __name__ == '__main__':
    meta = []
    missing = [a for a in UN if a not in by_a2 and a not in POINTS]
    print('missing', missing)
    for a2 in UN:
        name = NAMES.get(a2) or (by_a2[a2]['name'] if a2 in by_a2 else a2)
        slug = name.lower().replace(' ', '-').replace("'", '').replace('.', '')
        if a2 in by_a2 and a2 not in NO_OUTLINE:
            im, detail = outline(a2)
            if detail >= 25: save(im, 'countries-outline', slug)
            else: print('outline too small', name, detail)
        save(locator(a2), 'countries-locator', slug)
        meta.append({'a2': a2, 'name': name, 'slug': slug})
    json.dump(meta, open(os.path.join(ROOT, 'countries-meta.json'), 'w'), indent=1)
    print(sheet('countries-outline', cols=12), sheet('countries-locator', cols=12))
