import os, io, json, base64
from PIL import Image
import skylines_china, skylines_world, landmarks1
OUT='out'
meta={m['slug']:m['name'] for m in json.load(open('countries-meta.json'))}
SPECIAL={'mig-21':'MiG-21','mig-29':'MiG-29','f-14-tomcat':'F-14 Tomcat','f-16-fighting-falcon':'F-16 Fighting Falcon','f-22-raptor':'F-22 Raptor',
 'sr-71-blackbird':'SR-71 Blackbird','b-2-spirit':'B-2 Spirit','b-52-stratofortress':'B-52 Stratofortress','a-10-warthog':'A-10 Warthog',
 'p-51-mustang':'P-51 Mustang','boeing-707':'Boeing 707','boeing-727':'Boeing 727','boeing-737':'Boeing 737','boeing-747':'Boeing 747',
 'mcdonnell-douglas-dc-10':'McDonnell Douglas DC-10','lockheed-l-1011-tristar':'Lockheed L-1011 TriStar','airbus-a380':'Airbus A380','douglas-dc-3':'Douglas DC-3',
 'cn-tower':'CN Tower','us-capitol':'US Capitol','st-basils-cathedral':"St Basil's Cathedral",'st-peters-basilica':"St Peter's Basilica",
 'moai-easter-island':'Moai, Easter Island','kremlin-spasskaya-tower':'Kremlin, Spasskaya Tower','golden-temple-amritsar':'Golden Temple, Amritsar',
 'xian':"Xi'an",'hong-kong-victoria-harbour':'Hong Kong (night)','great-sphinx-of-giza':'Great Sphinx of Giza','petra-treasury':'Petra (the Treasury)',
 'the-starry-night-van-gogh':'The Starry Night — van Gogh','the-scream-munch':'The Scream — Munch','the-great-wave-hokusai':'The Great Wave — Hokusai',
 'mona-lisa-da-vinci':'Mona Lisa — da Vinci','football-soccer-ball':'Football (soccer) ball','the-moon':'The Moon','tyrannosaurus-rex':'Tyrannosaurus rex',
 'windmills-of-kinderdijk':'Windmills of Kinderdijk','statue-of-zeus-at-olympia':'Statue of Zeus at Olympia','mausoleum-at-halicarnassus':'Mausoleum at Halicarnassus',
 'notre-dame-de-paris':'Notre-Dame de Paris','itsukushima-torii':'Itsukushima torii'}
SMALL={'of','and','at','the','de','on'}
def nice(slug, cat):
    if cat.startswith('countries') or cat=='flags': return meta.get(slug, slug)
    if slug in SPECIAL: return SPECIAL[slug]
    w=slug.split('-'); return ' '.join(x if (i and x in SMALL) else x[:1].upper()+x[1:] for i,x in enumerate(w))
def enc(path, colour=False):
    im=Image.open(path); im=im.resize((im.width//4, im.height//4), Image.NEAREST)
    im = im.convert('RGB').quantize(colors=18, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE) if colour else im.convert('1', dither=Image.Dither.NONE)
    b=io.BytesIO(); im.save(b,'PNG',optimize=True); return 'data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
china=set(skylines_china.REG); wonders=set(landmarks1.REG)
cats=[('outline','Countries: outlines','countries-outline',None,'What country is this?'),
      ('locator','Countries: on the map','countries-locator',None,'Which country is shown in black?'),
      ('flags','Flags (8-bit colour)','flags',None,"Which country's flag is this?"),
      ('wonders','Wonders of the world','landmarks',lambda s:s in wonders,'Name this wonder'),
      ('landmarks','World landmarks','landmarks',lambda s:s not in wonders,'Name this landmark'),
      ('skylines','World skylines','skylines',lambda s:s not in china,'Which city is this?'),
      ('china','China’s 5M+ cities','skylines',lambda s:s in china,'Which Chinese city is this?'),
      ('aircraft','Famous aircraft','aircraft',None,'Name this aircraft'),
      ('states','US states','us-states',None,'Which US state is this?'),
      ('stars','Constellations','constellations',None,'Name this constellation'),
      ('planets','Planets & moons','planets',None,'Which world is this?'),
      ('animals','Animals','animals',None,'Which animal is this?'),
      ('sports','Sports gear','sports-gear',None,'Which sport uses this?'),
      ('music','Instruments','instruments',None,'Name this instrument'),
      ('art','Famous paintings','paintings',None,'Name this painting')]
data=[]; total=0
for key,label,folder,flt,q in cats:
    items=[]
    for f in sorted(os.listdir(f'{OUT}/{folder}')):
        s=f[:-4]
        if flt and not flt(s): continue
        items.append([nice(s,folder), enc(f'{OUT}/{folder}/{f}', folder=='flags')])
    items.sort(key=lambda x:x[0].lower())
    data.append({'key':key,'label':label,'q':q,'items':items}); total+=len(items)
json.dump(data, open('gallery-data.json','w'))
print(total, os.path.getsize('gallery-data.json'))
