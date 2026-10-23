#!/usr/bin/env python3
"""Export picture questions for the game: data/pictures.json + public/pics/<round>/<slug>.png (96x64).
Run after the drawing scripts:  python3 build_pictures.py /path/to/trivia"""
import json, math, os, random, sys, io
from PIL import Image
import landmarks1, landmarks2, skylines_world, skylines_china, aircraft
import extras_maps_sky as sky, extras_objects as objs
from countries import main_rings, by_a2
from build_gallery import nice

GAME = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/trivia'
PICS = os.path.join(GAME, 'public', 'pics')
OUT = 'out'
rnd = random.Random(20261022)

SMALL_ISLANDS = set('AG BB CV KM DM FJ GD KI MV MH MU FM NR PW KN LC VC WS ST SC SB TO TV VU BH MT SG BS TT'.split())
FAME = set('''US CA MX BR AR CL PE CO VE CU GB IE FR DE IT ES PT NL BE CH AT SE NO FI DK IS PL GR TR RU UA EG ZA NG KE ET MA DZ SA IL IR IQ IN PK CN JP KR KP VN TH ID PH AU NZ MG MN AF'''.split())
ALT = {'United States': ['USA', 'US', 'America', 'United States of America'], 'United Kingdom': ['UK', 'Britain', 'Great Britain'],
       'DR Congo': ['Democratic Republic of the Congo', 'Congo-Kinshasa', 'DRC'], 'Republic of the Congo': ['Congo-Brazzaville', 'Congo'],
       'Ivory Coast': ["Cote d'Ivoire"], 'Czechia': ['Czech Republic'], 'Eswatini': ['Swaziland'], 'North Macedonia': ['Macedonia'],
       'Myanmar': ['Burma'], 'Timor-Leste': ['East Timor'], 'Vatican City': ['Vatican', 'Holy See'], 'Netherlands': ['Holland'],
       'Bosnia and Herzegovina': ['Bosnia'], 'Central African Republic': ['CAR'], 'United Arab Emirates': ['UAE'], 'South Korea': ['Korea'],
       'Russia': ['Russian Federation'], 'Equatorial Guinea': [], 'Palestine': ['Palestinian territories']}

meta = json.load(open('countries-meta.json'))
os.makedirs(PICS, exist_ok=True)

def small_png(src, dst, colour=False):
    im = Image.open(src); im = im.resize((im.width // 4, im.height // 4), Image.NEAREST)
    im = im.convert('RGB').quantize(colors=18, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE) if colour else im.convert('1', dither=Image.Dither.NONE)
    os.makedirs(os.path.dirname(dst), exist_ok=True); im.save(dst, optimize=True)

def centroid(a2):
    rs = main_rings(a2); pts = [p for r in rs for p in r]
    return (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))

def area(a2):
    rs = main_rings(a2)
    def ar(r): return abs(sum(r[i][0] * r[i - 1][1] - r[i - 1][0] * r[i][1] for i in range(len(r)))) / 2
    lat = centroid(a2)[1]
    return sum(ar(r) for r in rs) * math.cos(math.radians(lat))

Q = []
def add(round_, rname, cat, slug, folder, d, q, a, wrong, alt=(), fib=False, colour=False):
    src = os.path.join(OUT, folder, slug + '.png')
    if not os.path.exists(src): return
    dst = os.path.join(PICS, round_, slug + '.png'); small_png(src, dst, colour)
    Q.append({'pr': round_, 'prn': rname, 'c': cat, 'd': max(1, min(5, d)), 'q': q, 'a': a, 'w': wrong, 'alt': list(alt), 'fib': fib,
              'img': f'/pics/{round_}/{slug}.png'})

# ---------------- countries: flags, shapes, maps ----------------
countries = [m for m in meta if m['a2'] not in SMALL_ISLANDS and m['a2'] in by_a2]
cent = {m['a2']: centroid(m['a2']) for m in countries}
areas = {m['a2']: area(m['a2']) for m in countries}
def near(a2, k=7):
    cx, cy = cent[a2]
    tiny = areas[a2] < 1
    others = sorted((m for m in countries if m['a2'] != a2 and (tiny or areas[m['a2']] >= 1)), key=lambda m: (cent[m['a2']][0] - cx) ** 2 + (cent[m['a2']][1] - cy) ** 2)
    return [m['name'] for m in others[:k]]
for m in countries:
    a2, name, slug = m['a2'], m['name'], m['slug']
    big = areas[a2] > 60; mid = areas[a2] > 8
    fame = a2 in FAME
    w = near(a2)
    alt = ALT.get(name, [])
    add('flags', 'Flags', 'geo', slug, 'flags', 1 if fame else (3 if mid else 4), "Which country's flag is this?", name, w, alt, True, True)
    add('shapes', 'Country shapes', 'geo', slug, 'countries-outline', 2 if fame else (3 if big else 4), 'Which country has this shape?', name, w, alt, True)
    add('maps', 'Find the country', 'geo', slug, 'countries-locator', (2 if big else 3 if mid else 4) - (1 if fame else 0), 'Which country is shown in black on this map?', name, w, alt, True)

# ---------------- landmarks & wonders ----------------
LM_D = {'eiffel-tower': 1, 'statue-of-liberty': 1, 'big-ben': 1, 'taj-mahal': 1, 'pyramids-of-giza': 1, 'leaning-tower-of-pisa': 1, 'colosseum': 1,
        'sydney-opera-house': 1, 'great-wall-of-china': 1, 'christ-the-redeemer': 1, 'golden-gate-bridge': 1, 'mount-fuji': 2, 'tower-bridge': 2,
        'stonehenge': 2, 'great-sphinx-of-giza': 2, 'machu-picchu': 2, 'mount-rushmore': 2, 'arc-de-triomphe': 2, 'white-house': 2, 'cn-tower': 2,
        'moai-easter-island': 2, 'parthenon': 2, 'burj-khalifa': 2, 'niagara-falls': 2, 'uluru': 2, 'st-basils-cathedral': 2, 'petronas-towers': 3,
        'sagrada-familia': 3, 'brandenburg-gate': 3, 'chichen-itza': 3, 'petra-treasury': 3, 'angkor-wat': 3, 'neuschwanstein-castle': 3,
        'burj-al-arab': 3, 'us-capitol': 3, 'gateway-arch': 3, 'hagia-sophia': 3, 'matterhorn': 3, 'notre-dame-de-paris': 3, 'marina-bay-sands': 3,
        'windmills-of-kinderdijk': 3, 'itsukushima-torii': 3, 'temple-of-heaven': 4, 'table-mountain': 3, 'atomium': 4, 'st-peters-basilica': 3,
        'mont-saint-michel': 3, 'golden-temple-amritsar': 4, 'kremlin-spasskaya-tower': 3, 'taipei-101': 3}
ANCIENT = {'hanging-gardens-of-babylon', 'colossus-of-rhodes', 'lighthouse-of-alexandria', 'temple-of-artemis', 'statue-of-zeus-at-olympia', 'mausoleum-at-halicarnassus'}
lm = sorted(set(landmarks1.REG) | set(landmarks2.REG))
lm_names = {s: nice(s, 'landmarks') for s in lm}
for s in lm:
    if s in ANCIENT:
        pool = [lm_names[x] for x in ANCIENT if x != s] + ['Great Pyramid of Giza']
        add('landmarks', 'Landmarks & wonders', 'his', s, 'landmarks', 4, 'Which ancient wonder of the world is this?', lm_names[s], pool)
    else:
        pool = [lm_names[x] for x in lm if x != s and x not in ANCIENT]
        rnd.shuffle(pool)
        add('landmarks', 'Landmarks & wonders', 'geo', s, 'landmarks', LM_D.get(s, 3), 'Name this famous landmark.', lm_names[s], pool[:7])

# ---------------- skylines ----------------
SK_D = {'new-york': 2, 'london': 2, 'paris': 1, 'sydney': 2, 'dubai': 2, 'toronto': 2, 'seattle': 2, 'rio-de-janeiro': 2, 'san-francisco': 3,
        'las-vegas': 2, 'singapore': 3, 'hong-kong': 3, 'tokyo': 3, 'shanghai': 3, 'beijing': 3, 'kuala-lumpur': 3, 'chicago': 3, 'rome': 2,
        'venice': 2, 'berlin': 3, 'moscow': 3, 'istanbul': 3, 'cairo': 3, 'athens': 3, 'amsterdam': 3, 'barcelona': 3}
world = sorted(skylines_world.REG); china = sorted(skylines_china.REG)
cityname = lambda s: nice(s, 'skylines').replace(' (night)', '')
for s in world + china:
    if s == 'hong-kong-victoria-harbour': continue
    if s in china:
        pool = [cityname(x) for x in china if x != s and x != 'hong-kong-victoria-harbour']
        q = 'Which Chinese city is this?'; d = SK_D.get(s, 4)
    else:
        pool = [cityname(x) for x in world if x != s]; q = 'Which city is this?'; d = SK_D.get(s, 3)
    rnd.shuffle(pool)
    add('skylines', 'City skylines', 'geo', s, 'skylines', d, q, cityname(s), pool[:7], (), True)

# ---------------- aircraft ----------------
AIRLINERS = ['boeing-707', 'boeing-727', 'boeing-737', 'boeing-747', 'mcdonnell-douglas-dc-10', 'lockheed-l-1011-tristar', 'airbus-a380', 'concorde', 'douglas-dc-3', 'wright-flyer']
AC_D = {'boeing-747': 2, 'concorde': 2, 'supermarine-spitfire': 2, 'wright-flyer': 2, 'airbus-a380': 3, 'b-2-spirit': 2, 'sr-71-blackbird': 3,
        'f-14-tomcat': 3, 'p-51-mustang': 3, 'boeing-737': 3, 'douglas-dc-3': 3, 'b-52-stratofortress': 3, 'a-10-warthog': 4, 'avro-arrow': 4}
ac = sorted(aircraft.REG); acn = {s: nice(s, 'aircraft') for s in ac}
ALT_AC = {'boeing-747': ['747', 'Jumbo Jet'], 'boeing-707': ['707'], 'boeing-727': ['727'], 'boeing-737': ['737'], 'mcdonnell-douglas-dc-10': ['DC-10', 'DC10'],
          'lockheed-l-1011-tristar': ['L-1011', 'TriStar', 'Tristar'], 'airbus-a380': ['A380'], 'douglas-dc-3': ['DC-3', 'Dakota'], 'supermarine-spitfire': ['Spitfire'],
          'p-51-mustang': ['Mustang', 'P-51'], 'avro-lancaster': ['Lancaster'], 'mig-21': ['MiG 21'], 'mig-29': ['MiG 29', 'Fulcrum'], 'f-14-tomcat': ['Tomcat', 'F-14'],
          'f-16-fighting-falcon': ['F-16', 'Fighting Falcon'], 'f-22-raptor': ['Raptor', 'F-22'], 'sr-71-blackbird': ['SR-71', 'Blackbird'], 'b-2-spirit': ['B-2', 'Stealth bomber'],
          'b-52-stratofortress': ['B-52'], 'a-10-warthog': ['A-10', 'Warthog', 'Thunderbolt II'], 'eurofighter-typhoon': ['Typhoon', 'Eurofighter'], 'avro-arrow': ['Arrow', 'CF-105'],
          'wright-flyer': ['Wright Flyer', 'Flyer']}
for s in ac:
    grp = [x for x in ac if (x in AIRLINERS) == (s in AIRLINERS) and x != s]
    pool = [acn[x] for x in grp]; rnd.shuffle(pool)
    add('aircraft', 'Famous aircraft', 'sci', s, 'aircraft3d', AC_D.get(s, 3), 'Name this aircraft.', acn[s], pool[:7], ALT_AC.get(s, []), True)

# ---------------- US states ----------------
sts = json.load(open('states.json'))
stc = {}
for st in sts:
    g = st['geom']; cs = g['coordinates']; rs = [p[0] for p in (cs if g['type'] == 'MultiPolygon' else [cs])]
    big = max(rs, key=len); stc[st['name']] = (sum(p[0] for p in big) / len(big), sum(p[1] for p in big) / len(big))
ST_D = {'Texas': 1, 'Florida': 1, 'California': 1, 'Alaska': 2, 'Hawaii': 2, 'Michigan': 2, 'Louisiana': 2, 'Oklahoma': 2, 'Idaho': 3, 'New York': 2,
        'Maine': 3, 'Tennessee': 3, 'Nevada': 3, 'Utah': 3, 'Massachusetts': 3, 'Maryland': 3, 'Ohio': 3, 'Kentucky': 3, 'Virginia': 3, 'West Virginia': 3,
        'Colorado': 4, 'Wyoming': 4, 'Kansas': 4, 'North Dakota': 4, 'South Dakota': 4, 'Iowa': 4, 'Arkansas': 4, 'Missouri': 4, 'Nebraska': 4, 'Montana': 3}
names = [n for n in stc if os.path.exists(os.path.join(OUT, 'us-states', n.lower().replace(' ', '-') + '.png'))]
for n in names:
    cx, cy = stc[n]
    pool = sorted((x for x in names if x != n and x not in ('Alaska', 'Hawaii')), key=lambda x: (stc[x][0] - cx) ** 2 + (stc[x][1] - cy) ** 2)[:7]
    add('states', 'US states', 'geo', n.lower().replace(' ', '-'), 'us-states', ST_D.get(n, 3), 'Which US state is this?', n, pool, (), True)

# ---------------- constellations ----------------
CO_D = {'orion': 2, 'big-dipper': 2, 'cassiopeia': 3, 'southern-cross': 3, 'little-dipper': 3}
CO_ALT = {'big-dipper': ['The Plough', 'Plough', 'Ursa Major'], 'little-dipper': ['Ursa Minor'], 'southern-cross': ['Crux'], 'cygnus': ['Northern Cross', 'The Swan'],
          'leo': ['The Lion'], 'scorpius': ['Scorpio', 'The Scorpion'], 'gemini': ['The Twins'], 'taurus': ['The Bull'], 'orion': ['The Hunter']}
cos = sorted(sky.CONST); con = {s: nice(s, 'constellations') for s in cos}
for s in cos:
    pool = [con[x] for x in cos if x != s]; rnd.shuffle(pool)
    add('stars', 'Constellations', 'sci', s, 'constellations', CO_D.get(s, 4), 'Name this constellation.', con[s], pool[:7], CO_ALT.get(s, []), True)

# Animals round removed (Oct 2026): the drawings weren't good enough.

# ---------------- paintings (NES-style 8-bit colour) ----------------
# slug: (kind, answer, difficulty, alternatives)  kind 'name' = name the painting, 'artist' = name the painter
PT = {
    'mona-lisa': ('name', 'Mona Lisa', 1, ['La Gioconda', 'The Mona Lisa']),
    'the-starry-night': ('name', 'The Starry Night', 1, ['Starry Night']),
    'the-scream': ('name', 'The Scream', 1, ['Scream']),
    'the-great-wave-off-kanagawa': ('name', 'The Great Wave off Kanagawa', 2, ['The Great Wave', 'Great Wave']),
    'water-lilies-monet': ('name', 'Water Lilies', 3, ['Nympheas', 'Waterlilies']),
    'girl-with-a-pearl-earring': ('name', 'Girl with a Pearl Earring', 2, ['The Girl with a Pearl Earring']),
    'american-gothic': ('name', 'American Gothic', 2, []),
    'sunflowers-van-gogh': ('name', 'Sunflowers', 2, ['The Sunflowers']),
    'the-last-supper': ('name', 'The Last Supper', 2, ['Last Supper']),
    'the-creation-of-adam': ('name', 'The Creation of Adam', 2, ['Creation of Adam']),
    'whistlers-mother': ('name', "Whistler's Mother", 3, ['Arrangement in Grey and Black']),
    'wanderer-above-the-sea-of-fog': ('name', 'Wanderer above the Sea of Fog', 4, ['Wanderer above the Sea of Mist']),
    'the-kiss-klimt': ('name', 'The Kiss', 3, ['Kiss']),
    'impression-sunrise-monet': ('name', 'Impression, Sunrise', 4, ['Impression Sunrise']),
    'a-sunday-on-la-grande-jatte': ('name', 'A Sunday on La Grande Jatte', 4, ['Sunday on La Grande Jatte', 'La Grande Jatte']),
    'liberty-leading-the-people': ('name', 'Liberty Leading the People', 3, []),
    'woman-with-a-hat-matisse': ('artist', 'Henri Matisse', 4, ['Matisse']),
    'composition-vii-kandinsky': ('artist', 'Wassily Kandinsky', 4, ['Kandinsky']),
    'self-portrait-van-gogh': ('artist', 'Vincent van Gogh', 2, ['Van Gogh']),
    'shipwreck-of-the-minotaur-turner': ('artist', 'J. M. W. Turner', 5, ['Turner', 'JMW Turner', 'William Turner']),
    'still-life-with-apples-cezanne': ('artist', 'Paul Cezanne', 4, ['Cezanne', 'Paul Cézanne']),
    'composition-mondrian': ('artist', 'Piet Mondrian', 3, ['Mondrian']),
}
NAMES = [v[1] for v in PT.values() if v[0] == 'name'] + ['The Birth of Venus', 'The Night Watch', 'The Persistence of Memory', 'Las Meninas']
ARTISTS = ['Claude Monet', 'Pablo Picasso', 'Vincent van Gogh', 'Henri Matisse', 'Wassily Kandinsky', 'Paul Cezanne', 'J. M. W. Turner', 'Piet Mondrian',
           'Pierre-Auguste Renoir', 'Rembrandt', 'Gustav Klimt', 'Edvard Munch', 'Salvador Dali', 'Paul Gauguin', 'Edgar Degas']
for s, (kind, ans, d, alt) in PT.items():
    if kind == 'name':
        pool = [x for x in NAMES if x != ans]; q = 'Name this famous painting.'
    else:
        pool = [x for x in ARTISTS if x != ans]; q = "Whose self-portrait is this?" if s == 'self-portrait-van-gogh' else 'Which artist painted this?'
    rnd.shuffle(pool)
    add('paintings', 'Famous paintings', 'art', s, 'paintings-nes', d, q, ans, pool[:7], alt, True, True)

json.dump(Q, open(os.path.join(GAME, 'data', 'pictures.json'), 'w'), indent=0, ensure_ascii=False)
from collections import Counter
print(len(Q), Counter(q['pr'] for q in Q))
