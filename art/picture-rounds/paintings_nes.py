#!/usr/bin/env python3
"""Famous public-domain paintings as chunky NES-style 8-bit pixel art (48x32 cells, each cell = 2x2 pixels).
Photo-based where a photo of the original is available, hand-pixelled otherwise."""
import os, math
from PIL import Image, ImageDraw
from common import W, H, save

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'paintings_src')
CW, CH = W // 2, H // 2                      # 48 x 32 cell grid
NES = [  # the standard NES (2C02) palette, minus duplicate blacks
    (124,124,124),(0,0,252),(0,0,188),(68,40,188),(148,0,132),(168,0,32),(168,16,0),(136,20,0),(80,48,0),(0,120,0),(0,104,0),(0,88,0),(0,64,88),
    (188,188,188),(0,120,248),(0,88,248),(104,68,252),(216,0,204),(228,0,88),(248,56,0),(228,92,16),(172,124,0),(0,184,0),(0,168,0),(0,168,68),(0,136,136),
    (248,248,248),(60,188,252),(104,136,252),(152,120,248),(248,120,248),(248,88,152),(248,120,88),(252,160,68),(248,184,0),(184,248,24),(88,216,84),(88,248,152),(0,232,216),(120,120,120),
    (252,252,252),(164,228,252),(184,184,248),(216,184,248),(248,184,248),(248,164,192),(240,208,176),(252,224,168),(248,216,120),(216,248,120),(184,248,184),(184,248,216),(0,252,252),(216,216,216),
    (0,0,0)]
K = (0, 0, 0)
def near(c): return min(NES, key=lambda p: (p[0]-c[0])**2*3 + (p[1]-c[1])**2*4 + (p[2]-c[2])**2*2)
N = lambda r, g, b: near((r, g, b))

WALL = (0, 64, 88); FRAME = (172, 124, 0); FRAME_HI = (248, 184, 0); FRAME_LO = (80, 48, 0)

def framed(pic, label_wall=WALL):
    """pic: Image in cell units. Returns 96x64 image with a gold frame, upscaled 2x."""
    g = Image.new('RGB', (CW, CH), label_wall); d = ImageDraw.Draw(g)
    w, h = pic.size; x0, y0 = (CW - w) // 2, (CH - h) // 2
    d.rectangle((x0 - 2, y0 - 2, x0 + w + 1, y0 + h + 1), fill=FRAME)
    d.line((x0 - 2, y0 - 2, x0 + w + 1, y0 - 2), fill=FRAME_HI); d.line((x0 - 2, y0 - 2, x0 - 2, y0 + h + 1), fill=FRAME_HI)
    d.line((x0 - 2, y0 + h + 1, x0 + w + 1, y0 + h + 1), fill=FRAME_LO); d.line((x0 + w + 1, y0 - 2, x0 + w + 1, y0 + h + 1), fill=FRAME_LO)
    g.paste(pic, (x0, y0))
    big = g.resize((W, H), Image.NEAREST)
    ImageDraw.Draw(big).rectangle((0, 0, W - 1, H - 1), outline=K)
    return big

def from_photo(fn, colours=12, maxw=40, maxh=26):
    src = Image.open(os.path.join(SRC, fn)).convert('RGB')
    s = min(maxw / src.width, maxh / src.height)
    w, h = max(6, round(src.width * s)), max(6, round(src.height * s))
    from PIL import ImageEnhance
    small = src.resize((w, h), Image.LANCZOS)
    small = ImageEnhance.Contrast(ImageEnhance.Color(small).enhance(1.9)).enhance(1.25)   # punchier, like NES art
    pal = Image.new('P', (1, 1)); flat = [v for c in NES for v in c]; pal.putpalette(flat + [0] * (768 - len(flat)))
    q = small.quantize(palette=pal, dither=Image.Dither.NONE).convert('RGB')
    # keep it to a handful of colours, NES-style: merge rare colours into their nearest common one
    from collections import Counter
    px = q.load(); cnt = Counter(px[x, y] for y in range(h) for x in range(w))
    keep = [c for c, _ in cnt.most_common(colours)]
    for y in range(h):
        for x in range(w):
            c = px[x, y]
            if c not in keep: px[x, y] = min(keep, key=lambda k: sum((a - b) ** 2 for a, b in zip(k, c)))
    return framed(q)

def canvas_cells(w, h, bg):
    im = Image.new('RGB', (w, h), bg); return im, ImageDraw.Draw(im)

# ---------------- hand-pixelled additions ----------------
def pearl_earring():
    im, d = canvas_cells(20, 26, (0, 0, 0))
    d.polygon([(3, 26), (5, 19), (9, 17), (14, 18), (18, 22), (19, 26)], fill=(172, 124, 0))       # ochre jacket
    d.line((9, 18, 12, 26), fill=(80, 48, 0))
    d.ellipse((5, 7, 14, 20), fill=(240, 208, 176))                                                  # face (turned)
    d.rectangle((9, 16, 12, 19), fill=(240, 208, 176))                                               # neck
    d.pieslice((4, 2, 15, 13), 180, 360, fill=(0, 88, 248)); d.rectangle((4, 7, 9, 10), fill=(0, 88, 248))   # blue turban
    d.rectangle((6, 3, 12, 5), fill=(60, 188, 252))
    d.polygon([(13, 4), (17, 5), (18, 13), (15, 14), (14, 8)], fill=(248, 216, 120))               # yellow cloth falling behind
    d.point((8, 12), fill=K); d.point((11, 12), fill=K)                                               # eyes
    d.point((7, 11), fill=(124, 124, 124))
    d.line((9, 16, 10, 16), fill=(228, 0, 88))                                                        # lips
    d.point((6, 17), fill=(252, 252, 252)); d.point((6, 16), fill=(188, 188, 188))                    # the pearl
    return framed(im)

def american_gothic():
    im, d = canvas_cells(22, 26, (164, 228, 252))
    d.polygon([(4, 10), (11, 3), (18, 10)], fill=(248, 248, 248)); d.rectangle((5, 10, 17, 16), fill=(248, 248, 248))   # house
    d.polygon([(9, 9), (11, 6), (13, 9), (13, 12), (9, 12)], fill=(124, 124, 124))                     # gothic window
    d.line((11, 6, 11, 12), fill=(248, 248, 248))
    d.rectangle((0, 14, 22, 15), fill=(0, 120, 0))                                                    # trees/bushes
    # woman (left)
    d.ellipse((3, 11, 8, 17), fill=(240, 208, 176)); d.rectangle((3, 11, 8, 12), fill=(136, 20, 0))
    d.rectangle((2, 17, 9, 26), fill=K); d.rectangle((4, 17, 7, 19), fill=(248, 248, 248)); d.rectangle((4, 20, 7, 26), fill=(80, 48, 0))
    d.point((4, 14), fill=K); d.point((7, 14), fill=K)
    # man (right) with pitchfork
    d.ellipse((12, 8, 18, 15), fill=(240, 208, 176)); d.rectangle((12, 8, 18, 9), fill=(80, 48, 0))
    d.point((13, 11), fill=K); d.point((16, 11), fill=K); d.line((14, 13, 15, 13), fill=K)
    d.rectangle((11, 15, 19, 26), fill=K); d.rectangle((14, 15, 16, 26), fill=(0, 88, 248))             # dungarees
    d.line((20, 13, 20, 26), fill=(124, 124, 124))
    for x in (19, 20, 21): d.line((x, 10, x, 13), fill=(124, 124, 124))
    d.line((19, 13, 21, 13), fill=(124, 124, 124))
    return framed(im)

def sunflowers():
    im, d = canvas_cells(20, 26, (248, 216, 120))
    d.rectangle((0, 18, 20, 26), fill=(252, 160, 68))                                                 # table
    d.polygon([(6, 15), (14, 15), (15, 24), (5, 24)], fill=(252, 224, 168)); d.line((5, 19, 15, 19), fill=(0, 88, 248))  # vase
    for (x, y, r) in ((5, 6, 3), (11, 4, 3), (16, 7, 3), (8, 11, 3), (14, 12, 2), (3, 12, 2), (11, 9, 2)):
        d.ellipse((x - r, y - r, x + r, y + r), fill=(248, 184, 0))
        d.ellipse((x - r + 1, y - r + 1, x + r - 1, y + r - 1), fill=(172, 124, 0))
        d.point((x, y), fill=(80, 48, 0))
    for x in (6, 9, 12, 14): d.line((x, 12, 10, 16), fill=(0, 120, 0))
    return framed(im)

def last_supper():
    im, d = canvas_cells(40, 22, (240, 208, 176))
    d.polygon([(0, 0), (40, 0), (30, 6), (10, 6)], fill=(172, 124, 0))                               # ceiling coffers
    d.rectangle((10, 6, 30, 13), fill=(136, 20, 0))
    for x in (13, 19, 25): d.rectangle((x, 7, x + 3, 12), fill=(164, 228, 252))                     # three windows
    d.polygon([(0, 0), (10, 6), (10, 16), (0, 22)], fill=(80, 48, 0)); d.polygon([(40, 0), (30, 6), (30, 16), (40, 22)], fill=(80, 48, 0))
    d.rectangle((2, 15, 38, 18), fill=(252, 252, 252))                                                # table
    d.rectangle((2, 18, 38, 22), fill=(124, 124, 124))
    cols = [(168, 16, 0), (0, 120, 0), (0, 88, 248), (248, 120, 88), (172, 124, 0), (148, 0, 132)]
    xs = [4, 7, 10, 13, 16, 24, 27, 30, 33, 36]
    for i, x in enumerate(xs[:3] + xs[3:5] + xs[5:]):
        d.rectangle((x - 1, 11, x + 1, 15), fill=cols[i % len(cols)]); d.point((x, 10), fill=(240, 208, 176))
    d.polygon([(18, 15), (20, 9), (22, 15)], fill=(228, 0, 88)); d.rectangle((19, 12, 21, 15), fill=(0, 88, 248))   # Jesus in red & blue
    d.point((20, 8), fill=(240, 208, 176)); d.point((20, 9), fill=(240, 208, 176))
    return framed(im)

def creation_of_adam():
    im, d = canvas_cells(40, 22, (164, 228, 252))
    d.rectangle((0, 16, 20, 22), fill=(0, 104, 0))                                                    # Adam's hill
    d.polygon([(2, 16), (10, 12), (18, 12), (18, 14), (10, 15)], fill=(240, 208, 176))               # Adam's arm, limp hand
    d.polygon([(18, 12), (20, 13), (18, 14)], fill=(240, 208, 176))
    d.ellipse((24, 2, 40, 18), fill=(228, 92, 16)); d.ellipse((26, 4, 40, 16), fill=(248, 120, 88))   # God's red cloak
    d.polygon([(22, 10), (30, 8), (30, 11)], fill=(240, 208, 176)); d.polygon([(21, 10), (23, 9), (23, 11)], fill=(240, 208, 176))   # pointing hand
    d.rectangle((30, 6, 34, 9), fill=(252, 252, 252))                                                 # white beard
    return framed(im)

def mondrian():
    im, d = canvas_cells(24, 24, (252, 252, 252))
    d.rectangle((0, 0, 7, 9), fill=(248, 248, 248)); d.rectangle((8, 0, 24, 15), fill=(228, 0, 88))   # big red block
    d.rectangle((0, 17, 7, 24), fill=(0, 88, 248))                                                    # blue
    d.rectangle((21, 21, 24, 24), fill=(248, 184, 0))                                                 # yellow
    for x in (7, 21): d.line((x, 0, x, 24), fill=K)
    d.line((8, 15, 8, 24), fill=K); d.line((0, 9, 7, 9), fill=K); d.line((0, 16, 24, 16), fill=K); d.line((21, 20, 24, 20), fill=K)
    d.line((0, 16, 7, 16), fill=K); d.line((7, 16, 7, 24), fill=K)
    return framed(im)

def whistlers_mother():
    im, d = canvas_cells(40, 24, (124, 124, 124))
    d.rectangle((0, 18, 40, 24), fill=(80, 48, 0))                                                    # floor
    d.rectangle((0, 0, 7, 24), fill=(0, 0, 0)); d.line((2, 0, 2, 24), fill=(120, 120, 120))          # curtain
    d.rectangle((16, 3, 26, 10), fill=K); d.rectangle((17, 4, 25, 9), fill=(188, 188, 188))           # framed picture
    d.polygon([(20, 22), (22, 12), (26, 10), (30, 12), (31, 22)], fill=K)                             # seated, black dress
    d.rectangle((18, 22, 34, 23), fill=K)
    d.ellipse((24, 8, 28, 12), fill=(240, 208, 176)); d.polygon([(24, 8), (28, 8), (28, 10), (25, 10)], fill=(252, 252, 252))   # face + white cap
    d.rectangle((25, 15, 27, 16), fill=(252, 252, 252))                                               # hands, handkerchief
    d.rectangle((32, 16, 35, 22), fill=(80, 48, 0))                                                   # footstool/chair
    return framed(im)

def wanderer():
    im, d = canvas_cells(20, 26, (184, 184, 248))
    for y, c in ((8, (216, 216, 216)), (12, (188, 188, 188)), (16, (252, 252, 252))):
        d.rectangle((0, y, 20, y + 4), fill=c)                                                          # sea of fog
    d.polygon([(0, 14), (4, 10), (7, 14)], fill=(124, 124, 124)); d.polygon([(13, 12), (17, 8), (20, 12)], fill=(124, 124, 124))
    d.polygon([(4, 26), (8, 19), (12, 18), (16, 26)], fill=(80, 48, 0))                              # rock
    d.rectangle((9, 11, 11, 18), fill=(0, 0, 0)); d.ellipse((9, 9, 11, 11), fill=(136, 20, 0))       # the wanderer from behind
    d.line((8, 18, 9, 15), fill=K); d.line((12, 18, 11, 15), fill=K)
    d.line((11, 14, 13, 18), fill=K)                                                                   # walking stick
    return framed(im)

def the_kiss():
    im, d = canvas_cells(24, 26, (172, 124, 0))
    for x in range(0, 24, 3):
        for y in range(0, 26, 3): d.point((x + (y % 2), y), fill=(248, 184, 0))                     # gold-leaf background
    d.rectangle((0, 21, 24, 26), fill=(0, 168, 0))                                                    # flower meadow
    for x in range(1, 24, 3): d.point((x, 22), fill=(248, 120, 248)); d.point((x + 1, 24), fill=(252, 252, 252))
    d.polygon([(5, 24), (7, 9), (12, 5), (18, 8), (19, 24)], fill=(248, 216, 120))                   # the couple's golden robe
    for (x, y) in ((13, 9), (15, 13), (13, 17), (16, 19), (14, 22)): d.rectangle((x, y, x + 1, y + 2), fill=K); d.point((x, y), fill=(252, 252, 252))   # his black-and-white rectangles
    for (x, y, c) in ((8, 13, (248, 120, 88)), (9, 18, (60, 188, 252)), (7, 21, (248, 120, 248)), (10, 15, (228, 0, 88))): d.ellipse((x, y, x + 2, y + 2), fill=c)   # her coloured circles
    d.ellipse((10, 2, 16, 8), fill=K)                                                                 # his dark head bending down
    d.ellipse((7, 6, 12, 11), fill=(240, 208, 176)); d.point((9, 8), fill=(80, 48, 0))                # her face, eyes closed
    d.rectangle((6, 5, 8, 8), fill=(136, 20, 0))                                                      # her red hair with flowers
    return framed(im)

def impression_sunrise():
    im, d = canvas_cells(40, 26, (104, 136, 252))
    d.rectangle((0, 0, 40, 12), fill=(184, 184, 248)); d.rectangle((0, 12, 40, 26), fill=(0, 88, 248))
    for x in (6, 10, 30, 34, 37): d.line((x, 4, x, 12), fill=(152, 120, 248))                         # hazy cranes and masts
    d.ellipse((20, 6, 25, 11), fill=(248, 56, 0))                                                     # the orange sun
    for y in range(13, 24, 2): d.line((22, y, 23, y), fill=(252, 160, 68))                           # its reflection
    for (x, y) in ((10, 18), (16, 21), (28, 16)): d.rectangle((x, y, x + 4, y + 1), fill=(0, 0, 188)); d.point((x + 1, y - 1), fill=(0, 0, 188))   # rowing boats
    return framed(im)

def grande_jatte():
    im, d = canvas_cells(40, 26, (88, 216, 84))
    d.rectangle((0, 0, 40, 8), fill=(184, 248, 184)); d.rectangle((26, 0, 40, 10), fill=(0, 168, 68))   # sky, trees
    d.polygon([(0, 8), (12, 8), (0, 14)], fill=(60, 188, 252))                                        # the river
    for x in range(0, 40, 2):
        for y in range(10, 26, 3): d.point((x + (y % 2), y), fill=(0, 168, 0))                       # pointillist dots
    d.rectangle((0, 22, 40, 26), fill=(0, 104, 0))                                                    # shadow foreground
    # the couple in profile on the right, with parasol and a monkey
    d.rectangle((30, 12, 33, 24), fill=K); d.polygon([(29, 24), (31, 16), (34, 16), (36, 24)], fill=K); d.point((31, 11), fill=(240, 208, 176))
    d.chord((26, 7, 33, 13), 180, 360, fill=(216, 0, 204)); d.line((29, 10, 29, 13), fill=K)
    d.rectangle((35, 10, 37, 24), fill=(0, 0, 0)); d.point((36, 9), fill=(240, 208, 176)); d.rectangle((35, 8, 37, 8), fill=K)
    d.rectangle((26, 22, 28, 23), fill=(80, 48, 0))
    # small figures across the park
    for (x, y, c) in ((6, 14, (252, 252, 252)), (12, 16, (228, 0, 88)), (18, 13, (0, 0, 188)), (21, 18, (248, 248, 248)), (9, 20, (248, 120, 88))):
        d.rectangle((x, y, x + 1, y + 3), fill=c); d.point((x, y - 1), fill=(240, 208, 176))
    d.chord((10, 13, 14, 16), 180, 360, fill=(248, 184, 0))
    return framed(im)

def liberty():
    im, d = canvas_cells(36, 26, (216, 216, 216))
    d.rectangle((0, 0, 36, 10), fill=(188, 188, 188)); d.ellipse((0, 4, 14, 14), fill=(124, 124, 124)); d.ellipse((22, 6, 36, 14), fill=(124, 124, 124))   # smoke
    d.line((18, 2, 17, 16), fill=(80, 48, 0))                                                          # flagpole
    d.rectangle((18, 1, 21, 6), fill=(0, 88, 248)); d.rectangle((22, 1, 24, 6), fill=(252, 252, 252)); d.rectangle((25, 1, 28, 6), fill=(228, 0, 88))   # tricolour
    d.polygon([(13, 26), (15, 14), (19, 12), (21, 14), (23, 26)], fill=(252, 224, 168))               # Liberty's dress
    d.ellipse((16, 9, 20, 13), fill=(240, 208, 176)); d.rectangle((16, 8, 20, 9), fill=(228, 0, 88))   # head with red Phrygian cap
    d.line((19, 13, 18, 8), fill=(240, 208, 176))                                                      # raised arm
    d.line((14, 16, 10, 18), fill=(80, 48, 0))                                                          # musket
    for (x, c) in ((6, K), (9, (0, 0, 188)), (26, K), (29, (136, 20, 0))):                             # revolutionaries
        d.rectangle((x, 15, x + 2, 24), fill=c); d.point((x + 1, 14), fill=(240, 208, 176))
    d.rectangle((0, 24, 36, 26), fill=(80, 48, 0))                                                     # barricade
    return framed(im)

HAND = {'girl-with-a-pearl-earring': pearl_earring, 'american-gothic': american_gothic, 'sunflowers-van-gogh': sunflowers,
        'the-last-supper': last_supper, 'the-creation-of-adam': creation_of_adam, 'composition-mondrian': mondrian,
        'whistlers-mother': whistlers_mother, 'wanderer-above-the-sea-of-fog': wanderer, 'the-kiss-klimt': the_kiss,
        'impression-sunrise-monet': impression_sunrise, 'a-sunday-on-la-grande-jatte': grande_jatte, 'liberty-leading-the-people': liberty}
PHOTO = {'mona-lisa': 'mona.png', 'the-starry-night': 'starry.jpg', 'the-scream': 'scream.jpg', 'the-great-wave-off-kanagawa': 'wave2.jpg',
         'water-lilies-monet': 'lilies.jpg', 'woman-with-a-hat-matisse': 'matisse.jpg', 'composition-vii-kandinsky': 'comp7.jpg',
         'self-portrait-van-gogh': 'gogh.jpg', 'shipwreck-of-the-minotaur-turner': 'turner.jpg', 'still-life-with-apples-cezanne': 'cezanne.jpg'}

if __name__ == '__main__':
    import shutil; shutil.rmtree(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out', 'paintings-nes'), ignore_errors=True)
    for slug, fn in PHOTO.items(): save(from_photo(fn), 'paintings-nes', slug)
    for slug, f in HAND.items(): save(f(), 'paintings-nes', slug)
    from common import sheet
    print(sheet('paintings-nes', cols=5, scale_down=1))
