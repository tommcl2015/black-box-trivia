#!/usr/bin/env python3
"""Side-profile aircraft silhouettes traced from real 3D models (FlightGear aircraft, GitHub FGMEMBERS mirrors).
FlightGear frame: x aft, y right, z up. AC3D files: x aft, y up, z = -right. The side view uses (x, z)."""
import math, os, re, subprocess, sys
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw
from common import *

REPOS = os.environ.get('FG_REPOS', '/tmp/claude-0/-home-claude/5b9934e5-ccdb-525b-85de-4ba6950b4139/scratchpad/repos')
SKIP = re.compile(r'shadow|light|flame|glow|beam|halo|reheat|afterburn|strobe|beacon|nav|landing|taxi|cone|vapor|vapour|smoke|contrail|pilot|crew|interior|cockpit|panel|cabin|seat|instrument|fuel-truck|loader|stairs|container|chock|tank-placard|marker|trajectory|parachute|chute|boom|agm|drop-tank|rocket|bomb|propdisk|prop-disc|disc|blur|tug|pushback|tractor|towbar|truck|stair|gpu|ground|goldhofert|jetway|catering|services|flightdeck|seating|bulkhead|overhead|autopush|tyre-smoke|effects', re.I)

def git_file(repo, path):
    d = os.path.join(REPOS, 'FG_' + repo)
    try:
        return subprocess.run(['git', '-C', d, 'show', 'HEAD:' + path], capture_output=True, timeout=180).stdout
    except Exception:
        return b''

def parse_ac(text):
    """Returns list of polygons [(x,y,z)...] in AC coordinates with transforms applied."""
    lines = text.decode('latin-1').splitlines()
    i = 0; polys = []
    def obj(parent_loc, parent_rot, skip_parent):
        nonlocal i
        loc = [0.0, 0.0, 0.0]; rot = None; verts = []; name = ''; kids = 0; surfs = []
        while i < len(lines):
            ln = lines[i].strip(); i += 1
            if ln.startswith('name'): name = ln[5:].strip().strip('"')
            elif ln.startswith('loc'): loc = ([float(v) for v in ln.split()[1:4]] + [0.0, 0.0, 0.0])[:3]
            elif ln.startswith('rot'): rot = [float(v) for v in ln.split()[1:10]]
            elif ln.startswith('numvert'):
                n = int(ln.split()[1]); verts = [[float(v) for v in lines[i + k].split()[:3]] for k in range(n)]; i += n
            elif ln.startswith('numsurf'):
                ns = int(ln.split()[1])
                for _ in range(ns):
                    # SURF / mat / refs n / n lines
                    while not lines[i].strip().startswith('refs'): i += 1
                    nr = int(lines[i].split()[1]); i += 1
                    refs = [int(lines[i + k].split()[0]) for k in range(nr)]; i += nr
                    surfs.append(refs)
            elif ln.startswith('kids'):
                kids = int(ln.split()[1]); break
        # world transform: v_world = parent_rot * (rot * v + loc) + parent_loc
        def tf(v):
            if rot: v = [rot[0] * v[0] + rot[3] * v[1] + rot[6] * v[2], rot[1] * v[0] + rot[4] * v[1] + rot[7] * v[2], rot[2] * v[0] + rot[5] * v[1] + rot[8] * v[2]]
            v = [v[0] + loc[0], v[1] + loc[1], v[2] + loc[2]]
            return [v[0] + parent_loc[0], v[1] + parent_loc[1], v[2] + parent_loc[2]]
        skip = skip_parent or bool(SKIP.search(name))
        if not skip and verts:
            W = [tf(v) for v in verts]
            for refs in surfs:
                if len(refs) >= 2: polys.append([W[r] for r in refs if r < len(W)])
        nl = [loc[0] + parent_loc[0], loc[1] + parent_loc[1], loc[2] + parent_loc[2]]
        for _ in range(kids):
            while i < len(lines) and not lines[i].startswith('OBJECT'): i += 1
            i += 1; obj(nl, None, skip)
    while i < len(lines) and not lines[i].startswith('OBJECT'): i += 1
    i += 1
    obj([0, 0, 0], None, False)
    return polys

def load_model(repo, path, offs=(0, 0, 0, 0), depth=0):
    """path relative to repo root. offs = (x_aft, z_up, pitch_deg, y_right). Returns 3D polygons [(x_aft, y_lateral, z_up)]."""
    if depth > 5: return []
    path = re.sub(r'^Aircraft/[^/]+/', '', path)
    out = []
    if path.endswith('.ac'):
        a = math.radians(offs[2]); ca, sa = math.cos(a), math.sin(a)
        for p in parse_ac(git_file(repo, path)):
            out.append([(x * ca - y * sa + offs[0], -z + offs[3], x * sa + y * ca + offs[1]) for x, y, z in p])
        return out
    raw = git_file(repo, path)
    if not raw: return out
    try: root = ET.fromstring(raw)
    except ET.ParseError: return out
    base = os.path.dirname(path)
    resolve = lambda p: re.sub(r'^Aircraft/[^/]+/', '', p) if p.startswith('Aircraft/') else os.path.normpath(os.path.join(base, p))
    p = root.findtext('path')
    if p:
        ro = root.find('offsets')                               # top-level offsets move this file's own model
        g0 = lambda k: float((ro.findtext(k) if ro is not None else None) or 0)
        out += load_model(repo, resolve(p.strip()), (offs[0] + g0('x-m'), offs[1] + g0('z-m'), offs[2] + g0('pitch-deg'), offs[3] + g0('y-m')), depth + 1)
    models = list(root.findall('model'))
    for el in root.iter():                                     # <foo include="x.xml"/> pulls in more <model> entries
        inc = el.attrib.get('include')
        if inc and inc.endswith('.xml'):
            try:
                sub = ET.fromstring(git_file(repo, resolve(inc)))
                models += list(sub.findall('model'))
            except Exception: pass
    for m in models:
        mp = (m.findtext('path') or '').strip(); nm = (m.findtext('name') or '') + mp
        if not mp or SKIP.search(nm) or 'Airport' in mp: continue
        o = m.find('offsets')
        g = lambda k: float((o.findtext(k) if o is not None else None) or 0)
        no = (offs[0] + g('x-m'), offs[1] + g('z-m'), offs[2] + g('pitch-deg'), offs[3] + g('y-m'))
        out += load_model(repo, resolve(mp), no, depth + 1)
    return out

def render(polys3, flip=False, view='side'):
    if view == 'top':
        polys = [[(-y, x) for x, y, z in p] for p in polys3]          # nose up: lateral across, length down
    else:
        polys = [[(x, z) for x, y, z in p] for p in polys3]
    xs = [x for p in polys for x, _ in p]; zs = [z for p in polys for _, z in p]
    x0, x1, z0, z1 = min(xs), max(xs), min(zs), max(zs)
    SC = 8; BW, BH = W * SC, H * SC
    GY = H - 12 if view != 'top' else H                          # ground line
    s = min((W - 8) * SC / (x1 - x0), (GY - 6) * SC / (z1 - z0))
    ox = (BW - (x1 - x0) * s) / 2; oy = ((GY - 1) * SC - (z1 - z0) * s) if view != 'top' else (BH - (z1 - z0) * s) / 2
    big = Image.new('L', (BW, BH), 0); bd = ImageDraw.Draw(big)
    for p in polys:
        if view == 'top': q = [((x - x0) * s + ox, (z - z0) * s + oy) for x, z in p]
        else: q = [((x1 - x) * s + ox if not flip else (x - x0) * s + ox, (z1 - z) * s + oy) for x, z in p]   # nose to the right
        if len(q) >= 3: bd.polygon(q, fill=255)
    small = big.resize((W, H), Image.BOX)
    im, d = canvas(); clouds(d, [(6, 5), (72, 9)])
    px = im.load(); sp = small.load()
    for y in range(H):
        for x in range(W):
            if sp[x, y] > 70: px[x, y] = BLK
    if view != 'top': d.line((1, GY, W - 2, GY), fill=BLK); fill_pattern(im, (1, GY + 1, W - 1, H - 1), 6)
    frame(d)
    return im

TOP = {'b-2-spirit', 'avro-lancaster'}   # these read best from above
AIRCRAFT = {   # slug: (repo, model path, flip)
    'boeing-707': ('707', 'Models/707.xml', False),
    'boeing-727': ('727-230', 'Models/727-230.xml', False),
    'boeing-737': ('737-300', 'Models/737-300.xml', False),
    'boeing-747': ('747-400', 'Models/747-400.xml', False),
    'mcdonnell-douglas-dc-10': ('DC-10-30', 'Models/DC-10-30.xml', False),
    'lockheed-l-1011-tristar': ('L1011', 'Models/L1011-1.xml', False),
    'airbus-a380': ('A380', 'XML/A380.xml', False),
    'concorde': ('Concorde', 'Models/concorde.ac', False),
    'douglas-dc-3': ('dc3', 'Models/dc3-dpm.ac', False),
    'wright-flyer': ('wrightFlyer1903', 'Models/WrightFlyer-pb-jw.ac', False),
    'supermarine-spitfire': ('SpitfireIX', 'Models/spitfire9.ac', False),
    'p-51-mustang': ('p51d', 'Models/P-51D-25NA.ac', False),
    'mig-21': ('MiG-21bis', 'Models/MiG-21bis.ac', False),
    'mig-29': ('MiG-29', 'Models/Mig-29.ac', False),
    'f-14-tomcat': ('f-14b', 'Models/f-14b.ac', False),
    'f-16-fighting-falcon': ('f16', 'Models/f16.ac', False),
    'f-22-raptor': ('F-22', 'Models/F-22.ac', False),
    'sr-71-blackbird': ('SR71-BlackBird', 'Models/SR-71-Blackbird-Base.ac', False),
    'b-2-spirit': ('B-2', 'Models/spirit.ac', False),
    'b-52-stratofortress': ('B-52F', 'Models/B-52F-002-027e.ac', False),
    'a-10-warthog': ('A-10', 'Models/A-10-model.xml', False),
    'eurofighter-typhoon': ('EF2000', 'Models/EF2000.ac', False),
    'avro-arrow': ('Avro-Arrow', 'Models/arrow.ac', False),
    'avro-lancaster': ('Avro-Lancaster', 'Models/lancaster.xml', False),
}

if __name__ == '__main__':
    only = sys.argv[1:] or list(AIRCRAFT)
    for slug in only:
        repo, path, flip = AIRCRAFT[slug]
        try: polys = load_model(repo, path)
        except Exception as e: print('ERROR', slug, e); continue
        if not polys: print('NO GEOMETRY', slug, path); continue
        if slug == 'airbus-a380': polys = [q for q in polys if min(v[0] for v in q) < 46.5]   # a tailplane part placed behind the aircraft
        save(render(polys, flip, 'top' if slug in TOP else 'side'), 'aircraft3d', slug)
        print(slug, len(polys))
