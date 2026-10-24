#!/usr/bin/env python3
"""Tanks and war machines: side profiles to real dimensions (metres), front to the right."""
import sys, math
from silhouette import *

def track_loop(x0, x1, y0, h, wheels, r, holes):
    """Track run as a stadium shape with the road wheels showing as rings."""
    rr = h / 2; poly = []
    for i in range(13): a = math.pi / 2 + math.pi * i / 12; poly.append((x0 + rr + rr * math.cos(a), y0 + rr + rr * math.sin(a)))
    for i in range(13): a = -math.pi / 2 + math.pi * i / 12; poly.append((x1 - rr + rr * math.cos(a), y0 + rr + rr * math.sin(a)))
    for cx in wheels:
        holes.append(circle(cx, y0 + r + 0.08, r * 0.78, 18))
    return poly

def hubs(wheels, y, r): return [circle(cx, y, r, 10) for cx in wheels]

def mark_i():
    P, H = [], []
    outer = [(1.8, 0), (7.0, 0), (9.9, 1.55), (9.5, 2.45), (1.0, 2.45), (0.0, 1.45)]
    inner = [(2.3, 0.38), (6.9, 0.38), (9.15, 1.55), (8.9, 2.07), (1.35, 2.07), (0.55, 1.45)]
    inner2 = [(2.4, 0.5), (6.85, 0.5), (8.95, 1.55), (8.75, 1.95), (1.45, 1.95), (0.7, 1.45)]
    P.append(outer); P.append(('h', inner)); P.append(inner2)
    P.append([(3.6, 0.55), (6.6, 0.55), (6.9, 1.25), (6.6, 2.07), (3.6, 2.07), (3.3, 1.25)])      # sponson
    P.append(line(6.6, 1.35, 8.3, 1.45, 0.16))                                                  # 6-pounder
    P.append(('h', rect(4.0, 1.45, 6.2, 1.6)))
    P.append(line(0.3, 1.2, -1.6, 0.75, 0.18)); P.append(circle(-1.5, 0.55, 0.55, 16)); P.append(('h', circle(-1.5, 0.55, 0.35, 12)))   # steering tail
    return P, H

def renault_ft():
    P, H = [], []
    P.append([(0.4, 0.15), (3.9, 0.15), (4.55, 0.85), (4.45, 1.45), (3.4, 1.55), (1.2, 1.6), (0.4, 1.25), (0.1, 0.7)])
    P.append([(1.9, 1.55), (3.1, 1.55), (3.0, 1.95), (2.75, 2.08), (2.25, 2.08), (2.0, 1.95)])   # cast turret
    P.append(rect(2.35, 2.05, 2.65, 2.14)); P.append(line(3.0, 1.82, 3.55, 1.84, 0.1))
    P.append(line(0.5, 0.95, -0.65, 0.35, 0.12)); P.append(line(0.55, 0.45, -0.6, 0.3, 0.1))      # tail skid
    H.append(circle(4.0, 1.05, 0.28, 14)); H.extend(hubs([1.0, 1.55, 2.1, 2.65, 3.2], 0.33, 0.14))
    return P, H

def tiger():
    P, H = [], []
    P.append(track_loop(0.0, 6.3, 0.0, 1.05, [0.75, 1.55, 2.35, 3.15, 3.95, 4.75, 5.5], 0.4, H))
    P.append([(0.05, 0.95), (6.3, 0.95), (6.35, 1.6), (6.0, 1.95), (0.15, 1.95), (0.0, 1.5)])
    P.append([(1.8, 1.95), (5.1, 1.95), (5.35, 2.25), (5.2, 2.9), (2.0, 2.95), (1.7, 2.5)])          # turret
    P.append(rect(2.3, 2.9, 2.9, 3.1))                                                          # cupola
    P.append(line(5.2, 2.45, 8.25, 2.45, 0.2)); P.append(rect(8.15, 2.33, 8.5, 2.57))          # 88 mm gun with muzzle brake
    return P, H

def t34():
    P, H = [], []
    P.append(track_loop(0.0, 5.9, 0.0, 0.95, [0.6, 1.75, 2.9, 4.05, 5.2], 0.42, H))
    P.append([(0.1, 0.85), (5.6, 0.85), (6.1, 0.95), (5.0, 1.55), (0.9, 1.55), (0.0, 1.05)])       # sloped glacis and rear
    P.append([(2.6, 1.55), (4.6, 1.55), (4.35, 2.3), (3.6, 2.4), (2.75, 2.35), (2.45, 1.9)])
    P.append(line(4.4, 2.0, 6.75, 2.05, 0.16))
    return P, H

def sherman():
    P, H = [], []
    P.append(track_loop(0.0, 5.6, 0.0, 0.85, [], 0.3, H))
    for cx in (1.0, 2.5, 4.0):                                                                  # volute bogies
        P.append(rect(cx - 0.5, 0.35, cx + 0.5, 0.85)); H.append(circle(cx - 0.32, 0.36, 0.22, 12)); H.append(circle(cx + 0.32, 0.36, 0.22, 12))
    P.append([(0.1, 0.8), (5.0, 0.8), (5.84, 1.1), (5.7, 1.5), (5.0, 2.0), (0.4, 2.0), (0.0, 1.5)])
    P.append([(2.0, 2.0), (4.1, 2.0), (4.25, 2.4), (3.9, 2.7), (2.4, 2.74), (1.85, 2.45)])
    P.append(line(4.1, 2.32, 6.3, 2.35, 0.15))
    return P, H

def abrams():
    P, H = [], []
    P.append(track_loop(0.0, 7.6, 0.0, 0.8, [], 0.3, H))
    P.append([(0.0, 0.55), (7.2, 0.55), (7.9, 0.95), (7.6, 1.3), (0.05, 1.32)])                   # hull with side skirts
    for cx in (1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 6.9): H.append(circle(cx, 0.3, 0.2, 12))
    P.append([(1.3, 1.32), (6.0, 1.32), (6.9, 1.7), (6.1, 2.1), (2.0, 2.2), (1.2, 1.9)])          # flat, angular turret
    P.append(rect(4.2, 2.1, 4.8, 2.44)); P.append(line(6.6, 1.82, 9.8, 1.86, 0.17))
    return P, H

def jeep():
    P, H = [], []
    P.append([(0.05, 0.5), (3.32, 0.5), (3.33, 0.95), (2.35, 1.0), (1.95, 0.98), (1.75, 0.88), (0.45, 0.9), (0.05, 0.95)])
    for cx in (0.62, 2.75):
        P.append(('h', circle(cx, 0.4, 0.47, 18))); P.append(circle(cx, 0.36, 0.37, 18)); P.append(('h', circle(cx, 0.36, 0.13, 10)))
    P.append(line(1.8, 0.95, 1.62, 1.7, 0.09)); P.append(line(1.62, 1.7, 1.66, 1.72, 0.09)); P.append(line(1.66, 1.7, 1.6, 1.72, 0.09))  # windscreen frame
    P.append(line(1.4, 0.95, 1.55, 1.25, 0.05)); P.append(line(1.45, 1.27, 1.65, 1.2, 0.05))    # steering wheel
    P.append(circle(-0.12, 0.85, 0.36, 18)); P.append(('h', circle(-0.12, 0.85, 0.12, 10)))              # spare tyre
    P.append(rect(0.35, 0.9, 1.25, 1.05))                                                       # seats
    return P, H

def zeppelin():
    P, H = [], []
    L, R = 196.0, 15.0; body = []
    for i in range(41):
        t = i / 40; x = L * t; r = R * (math.sin(math.pi * t) ** 0.55) * (1.0 if t > 0.35 else (0.55 + 0.45 * t / 0.35) ** 0.5)
        body.append((x, r))
    poly = [(x, 30 + r) for x, r in body] + [(x, 30 - r) for x, r in reversed(body)]
    P.append(poly)
    P.append([(0, 30), (34, 32), (30, 53), (3, 50)]); P.append([(0, 30), (34, 28), (30, 7), (3, 10)])   # fins
    for x0, x1 in ((138, 162), (70, 92), (42, 60)):
        P.append([(x0, 10), (x1, 10), (x1 - 3, 3.5), (x0 + 3, 3.5)]); P.append(rect(x0 + 4, 9, x1 - 4, 17))  # gondolas
    return P, H

def big_bertha():
    P, H = [], []
    a = math.radians(42)
    bx, by = 2.2, 2.0; L = 6.7
    P.append(line(bx - 1.2 * math.cos(a), by - 1.2 * math.sin(a), bx + L * math.cos(a), by + L * math.sin(a), 0.9))   # stubby 42 cm barrel
    P.append(line(bx - 0.6 * math.cos(a), by - 0.6 * math.sin(a), bx + 2.6 * math.cos(a), by + 2.6 * math.sin(a), 1.25))  # breech and recoil cylinders
    P.append([(-0.8, 0.9), (4.0, 0.9), (3.6, 2.4), (0.0, 2.0)])                                  # carriage
    P.append(line(-0.6, 1.2, -3.2, 0.25, 0.45)); P.append(rect(-3.8, 0.0, -2.6, 0.3))             # trail
    P.append(('h', circle(1.8, 1.0, 1.12, 24))); P.append(circle(1.8, 1.0, 1.0, 24)); P.append(('h', circle(1.8, 1.0, 0.8, 24))); P.append(circle(1.8, 1.0, 0.22, 10))
    for k in range(8):
        r = math.radians(k * 45 + 22.5); P.append(line(1.8, 1.0, 1.8 + 0.85 * math.cos(r), 1.0 + 0.85 * math.sin(r), 0.12))
    return P, H

ITEMS = {'mark-i-tank': mark_i, 'renault-ft': renault_ft, 'tiger-tank': tiger, 't-34': t34, 'sherman-tank': sherman,
         'm1-abrams': abrams, 'willys-jeep': jeep, 'zeppelin': zeppelin, 'big-bertha': big_bertha}

if __name__ == '__main__':
    for slug in sys.argv[1:] or ITEMS:
        P, H = ITEMS[slug]()
        save(fit_draw(P, scene='air' if slug == 'zeppelin' else 'sky', holes=H, pad=5, ground_h=10), 'tanks', slug); print(slug)
