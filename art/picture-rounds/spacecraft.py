#!/usr/bin/env python3
"""Rockets & spacecraft silhouettes. Real NASA 3D models (github.com/nasa/NASA-3D-Resources) where available,
otherwise outlines drawn to real dimensions."""
import os, sys, math, warnings
warnings.filterwarnings('ignore')
import numpy as np
from silhouette import *
D = os.environ.get('NASA_DIR', '/tmp/claude-0/-home-claude/5b9934e5-ccdb-525b-85de-4ba6950b4139/scratchpad/nasa')

def mesh_polys(name, a, b, flipx=False, flipy=False, scale=1.0, rot=0, xr=None):
    import trimesh
    m = trimesh.load(os.path.join(D, name + '.glb'), force='scene').dump(concatenate=True)
    faces = m.faces
    if xr:                                   # keep only part of a model (e.g. one craft of a docked pair) by position along x
        cx = m.vertices[faces].mean(1)[:, 0]; faces = faces[(cx > xr[0]) & (cx < xr[1])]
    p = m.vertices[:, [a, b]].copy() * scale
    if flipx: p[:, 0] *= -1
    if flipy: p[:, 1] *= -1
    if rot:
        c, s = math.cos(math.radians(rot)), math.sin(math.radians(rot))
        p = p @ np.array([[c, s], [-s, c]])
    return [[tuple(p[i]) for i in f] for f in faces]

def ogive(r, L, n=10, base=0):
    """nose cone profile points (r, h) from base up"""
    return [(r * math.cos(math.pi / 2 * i / n) ** 0.8, base + L * math.sin(math.pi / 2 * i / n)) for i in range(n + 1)]

def falcon9_landing():
    # first-stage booster (41 m x 3.7 m) touching down on a drone ship, legs and grid fins out
    b = rect(-1.83, 3.0, 1.83, 44.0)
    eng = [[(-1.6, 3.0), (1.6, 3.0), (1.9, 1.8), (-1.9, 1.8)]]
    fins = [rect(1.83, 40.5, 3.6, 42.5), rect(-3.6, 40.5, -1.83, 42.5)]
    legs = [line(1.6, 11.0, 8.5, 0.4, 0.7), line(-1.6, 11.0, -8.5, 0.4, 0.7), line(1.7, 5.0, 7.6, 1.6, 0.45), line(-1.7, 5.0, -7.6, 1.6, 0.45)]
    deck = [rect(-16, -2.2, 16, 0.4), rect(-16, 0.4, -15, 2.5), rect(15, 0.4, 16, 2.5)]
    return [b] + eng + fins + legs + deck

def falcon9():
    P = [(1.83, 0), (1.83, 47.7), (1.83, 52.0), (2.6, 55.0), (2.6, 62.0)] + ogive(2.6, 8.0, base=62.0)[1:]
    body = revolve(P)
    legs = [line(1.7, 1, 2.3, 10, 0.5), line(-1.7, 1, -2.3, 10, 0.5)]
    return [body] + legs

def soyuz():
    core = revolve([(1.47, 0), (1.47, 27), (1.3, 28), (1.33, 28.5), (1.33, 36), (1.5, 36.5), (1.5, 40), (1.0, 44), (0.5, 46), (0.0, 46.5)])
    boost = []
    for sgn in (1, -1):
        boost.append([(sgn * 1.2, 0), (sgn * 4.2, 0), (sgn * 3.3, 6), (sgn * 1.7, 18.5), (sgn * 1.3, 20.5), (sgn * 1.2, 20.5)])
    tower = [line(0, 46.5, 0, 50, 0.25)]
    return [core] + boost + tower

def v2():
    body = revolve([(0.0, 0.3), (0.55, 0.4), (0.82, 2.0), (0.83, 7.0)] + ogive(0.83, 7.0, base=7.0)[1:])
    fins = [[(0.6, 0.2), (1.78, -0.2), (1.78, 0.9), (0.8, 3.6)], [(-0.6, 0.2), (-1.78, -0.2), (-1.78, 0.9), (-0.8, 3.6)]]
    return [body] + fins

def sputnik():
    polys = [circle(0, 0, 0.29, 40)]
    for ang, L in [(168, 2.4), (178, 2.9), (186, 2.9), (196, 2.4)]:
        a = math.radians(ang); x0, y0 = 0.27 * math.cos(a), 0.27 * math.sin(a)
        polys.append(line(x0, y0, x0 + L * math.cos(a), y0 + L * math.sin(a), 0.045))
    return polys

FX = True
def shuttle_stack():
    # External tank 46.9 m x 8.4 m, SRB 45.5 m x 3.7 m, orbiter (traced model) riding on the tank's side
    et = revolve([(4.2, 0), (4.2, 38.0)] + ogive(4.2, 8.9, base=38.0)[1:])
    srb = [ [(x + 0.0, y) for x, y in revolve([(1.85, 0.0), (1.85, 41.0)] + ogive(1.85, 4.5, base=41.0)[1:])] ]
    noz = [[(-1.5, 0), (1.5, 0), (1.9, -3.0), (-1.9, -3.0)]]
    orb = mesh_polys('Space Shuttle (A)', 1, 2, flipx=FX, flipy=True, scale=37.24 / 41.9)
    xs = [v[0] for p in orb for v in p]; ys = [v[1] for p in orb for v in p]
    dx = 4.2 - min(xs) - 0.5; dy = 2.0 - min(ys)
    orb = [[(x + dx, y + dy) for x, y in p] for p in orb]
    return [et] + srb + noz + orb

ITEMS = {   # slug: (builder, scene)
    'space-shuttle': (lambda: mesh_polys('Space Shuttle (C)', 0, 2), 'sky'),
    'apollo-lunar-module': (lambda: mesh_polys('Apollo Lunar Module', 0, 1), 'moon'),
    'hubble-space-telescope': (lambda: mesh_polys('Hubble Space Telescope (A)', 0, 1), 'space'),
    'international-space-station': (lambda: mesh_polys('International Space Station (ISS) (A)', 0, 1), 'space'),
    'skylab': (lambda: mesh_polys('Skylab', 0, 2), 'space'),
    'voyager': (lambda: mesh_polys('Voyager Probe (A)', 2, 1), 'space'),
    'viking-lander': (lambda: mesh_polys('Viking Lander', 2, 1), 'moon'),
    'perseverance-rover': (lambda: mesh_polys('Mars 2020 Perseverance Rover', 2, 1), 'moon'),
    'sputnik-1': (sputnik, 'space'),
    'falcon-9': (falcon9_landing, 'water'),
    'apollo-command-module': (lambda: mesh_polys('Apollo Soyuz', 0, 1, xr=(-99, -0.95)), 'space'),
    'soyuz-spacecraft': (lambda: mesh_polys('Apollo Soyuz', 0, 1, flipx=True, xr=(1.25, 99)), 'space'),
    'v-2-rocket': (v2, 'pad'),
}

if __name__ == '__main__':
    for slug in sys.argv[1:] or ITEMS:
        fn, scene = ITEMS[slug]
        polys = fn()
        sc = 'sky' if scene == 'pad' else ('moonground' if scene == 'moon' else scene)
        im = fit_draw(polys, scene=sc, ground_h=8 if scene == 'pad' else 12, pad=4 if scene == 'pad' else (14 if slug == 'apollo-command-module' else 6), vpad=2 if scene == 'pad' else None)
        save(im, 'spacecraft', slug); print(slug, len(polys))
