#!/usr/bin/env python3
"""Big islands and famous lakes as 1-bit outline tiles, drawn the same way as the country shapes (countries.py)."""
import json, math, os, sys
from shapely.geometry import shape, Point, Polygon, MultiPolygon
from shapely.ops import unary_union
from common import *
import countries as C

NE = os.environ.get('NE_DIR', '/tmp/claude-0/-home-claude/5b9934e5-ccdb-525b-85de-4ba6950b4139/scratchpad/ne')

# island: (countries whose land it is, a point on the island)
ISLANDS = {
    'greenland': (['GL'], (-42, 72)), 'great-britain': (['GB'], (-2, 53)), 'ireland': (['IE', 'GB'], (-8, 53.3)),
    'sicily': (['IT'], (14.2, 37.5)), 'sardinia': (['IT'], (9.0, 40.1)), 'corsica': (['FR'], (9.1, 42.2)), 'crete': (['GR'], (24.9, 35.2)),
    'borneo': (['MY', 'ID', 'BN'], (114.5, 0.5)), 'new-guinea': (['PG', 'ID'], (141, -5)), 'honshu': (['JP'], (138.5, 36.5)),
    'hokkaido': (['JP'], (142.8, 43.4)), 'tasmania': (['AU'], (146.6, -42)), 'south-island-new-zealand': (['NZ'], (170.5, -44)),
    'north-island-new-zealand': (['NZ'], (175.8, -38.8)), 'sumatra': (['ID'], (101.5, 0)), 'java': (['ID'], (110, -7.3)),
    'baffin-island': (['CA'], (-72, 69)), 'vancouver-island': (['CA'], (-125.6, 49.6)), 'newfoundland': (['CA'], (-56, 48.6)),
    'hawaii-big-island': (['US'], (-155.5, 19.6)), 'tierra-del-fuego': (['AR', 'CL'], (-68.5, -54)), 'long-island': (['US'], (-73, 40.8)),
}
LAKES = {   # name in Natural Earth, file
    'lake-superior': 'Lake Superior', 'lake-michigan': 'Lake Michigan', 'lake-huron': 'Lake Huron', 'lake-erie': 'Lake Erie',
    'lake-ontario': 'Lake Ontario', 'lake-victoria': 'Lake Victoria', 'lake-baikal': 'Lake Baikal', 'lake-tanganyika': 'Lake Tanganyika',
    'lake-malawi': 'Lake Malawi', 'lake-titicaca': 'Lago Titicaca', 'great-bear-lake': 'Great Bear Lake', 'great-slave-lake': 'Great Slave Lake',
    'lake-winnipeg': 'Lake Winnipeg', 'lake-ladoga': 'Lake Ladoga', 'dead-sea': 'Dead Sea', 'great-salt-lake': 'Great Salt Lake',
    'lake-chad': 'Lake Chad', 'lake-tahoe': 'Lake Tahoe', 'sea-of-galilee': 'Sea of Galilee', 'lake-nasser': 'Lake Nasser',
    'lake-geneva': 'Lake Geneva', 'lake-como': 'Lago di Como', 'lake-garda': 'Lago di Garda', 'loch-ness': 'Loch Ness',
    'lake-turkana': 'Lake Turkana', 'lake-okeechobee': 'Lake Okeechobee', 'lake-van': 'Lake Van', 'lake-balaton': 'Lake Balaton',
}

def island_geom(a2s, pt):
    P = Point(pt); parts = []
    for a2 in a2s:
        g = shape(C.by_a2[a2]['geom'])
        for poly in (g.geoms if isinstance(g, MultiPolygon) else [g]):
            if poly.buffer(0.15).contains(P) or poly.distance(P) < 0.01: parts.append(poly)
    if not parts: raise SystemExit('no land at %s %s' % (a2s, pt))
    u = unary_union([p.buffer(0.02) for p in parts])
    if len(a2s) > 1:                                  # an island shared by countries: everything touching the first piece
        u = unary_union([p.buffer(0.03) for a2 in a2s for p in (lambda g: g.geoms if isinstance(g, MultiPolygon) else [g])(shape(C.by_a2[a2]['geom'])) if p.buffer(0.05).intersects(u)])
    return max(u.geoms, key=lambda g: g.area) if isinstance(u, MultiPolygon) else u

_lakes = {}
def lake_geom(name):
    if not _lakes:
        for f in ('ne_10m_lakes', 'ne_50m_lakes'):
            for ft in json.load(open(os.path.join(NE, f + '.geojson')))['features']:
                n = ft['properties'].get('name')
                if n and n not in _lakes: _lakes[n] = shape(ft['geometry'])
        for ft in json.load(open(os.path.join(NE, 'ne_50m_geography_marine_polys.geojson')))['features']:
            if ft['properties'].get('name') == 'Caspian Sea': _lakes['Caspian Sea'] = shape(ft['geometry'])
    g = _lakes[name]
    return max(g.geoms, key=lambda x: x.area) if isinstance(g, MultiPolygon) else g

def tile(geom):
    lat0 = (geom.bounds[1] + geom.bounds[3]) / 2; k = math.cos(math.radians(lat0))
    ext = [(x * k, -y) for x, y in geom.exterior.coords]
    holes = [[(x * k, -y) for x, y in r.coords] for r in geom.interiors]
    xs = [x for x, _ in ext]; ys = [y for _, y in ext]
    sw, sh = max(xs) - min(xs), max(ys) - min(ys)
    sc = min((W - 12) / sw, (H - 10) / sh); ox = (W - sw * sc) / 2; oy = (H - sh * sc) / 2
    T = lambda r: [(ox + (x - min(xs)) * sc, oy + (y - min(ys)) * sc) for x, y in r]
    big = 4; m = Image.new('1', (W * big, H * big), 0); md = ImageDraw.Draw(m)        # supersample for smoother coastlines
    md.polygon([(x * big, y * big) for x, y in T(ext)], fill=1)
    for h in holes:
        if Polygon(h).area * sc * sc > 4: md.polygon([(x * big, y * big) for x, y in T(h)], fill=0)
    mm = m.convert('L').resize((W, H), Image.BOX).point(lambda v: 255 if v > 110 else 0).convert('1')
    im, d = canvas(); fill_pattern(im, (1, 1, W - 1, H - 1), 1)
    sh_ = Image.new('1', (W, H), 0); sh_.paste(mm, (1, 1))
    im.paste(Image.new('1', (W, H), BLK), (0, 0), sh_)
    im.paste(Image.new('1', (W, H), WHT), (0, 0), mm.point(lambda v: 255 if v else 0))
    inner = Image.new('1', (W, H), 0); inner.paste(mm, (0, 0))
    im.paste(Image.new('1', (W, H), BLK), (0, 0), inner)
    frame(d)
    return im

if __name__ == '__main__':
    LAKES['caspian-sea'] = 'Caspian Sea'
    for slug, (a2s, pt) in ISLANDS.items(): save(tile(island_geom(a2s, pt)), 'islands', slug)
    for slug, n in LAKES.items(): save(tile(lake_geom(n)), 'lakes', slug)
    print(len(ISLANDS), len(LAKES))
