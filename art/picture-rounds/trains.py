#!/usr/bin/env python3
"""Famous trains: side profiles to real dimensions (metres), front to the right, on rails."""
import sys, math
from silhouette import *

def wheel(P, cx, r, spokes=True):
    y = r
    P.append(circle(cx, y, r, 24)); P.append(('h', circle(cx, y, r * 0.78, 24)))
    P.append(circle(cx, y, r * 0.22, 12))
    if spokes and r > 0.6:
        for k in range(6):
            a = math.radians(k * 30); P.append(line(cx - r * 0.8 * math.cos(a), y - r * 0.8 * math.sin(a), cx + r * 0.8 * math.cos(a), y + r * 0.8 * math.sin(a), r * 0.09))

def boiler(x0, x1, cy, r): return [(x0, cy - r), (x1, cy - r), (x1, cy + r), (x0, cy + r)]

def rocket():
    P = []
    P.append(boiler(0.6, 3.6, 1.75, 0.5)); P.append(rect(0.0, 1.15, 0.75, 2.2)); P.append(ellipse(0.38, 2.2, 0.38, 0.22))   # barrel boiler, firebox
    P.append([(3.35, 2.1), (3.75, 2.1), (3.75, 4.3), (3.95, 4.6), (3.15, 4.6), (3.35, 4.3)])          # tall chimney
    P.append(rect(0.4, 1.0, 3.7, 1.12))
    P.append(line(0.5, 1.95, 2.0, 1.05, 0.22)); P.append(line(1.9, 1.08, 3.3, 0.85, 0.08))            # inclined cylinder, con-rod
    wheel(P, 3.0, 0.72); wheel(P, 0.9, 0.39)
    P.append(rect(-3.3, 0.78, -0.3, 0.98)); P.append(ellipse(-1.8, 1.5, 1.25, 0.55)); P.append(rect(-0.3, 0.9, 0.0, 0.98))  # water-barrel tender
    wheel(P, -2.6, 0.45); wheel(P, -1.0, 0.45)
    return P

def a3(P, streamlined=False):
    if not streamlined:
        P.append(rect(9.0, 1.35, 21.0, 1.55))                                                          # running plate
        P.append(boiler(11.4, 20.3, 2.75, 0.9)); P.append(boiler(19.6, 20.9, 2.75, 0.97))
        P.append(rect(19.7, 3.5, 20.3, 4.05)); P.append(ellipse(17.0, 3.62, 0.5, 0.28))               # chimney, dome
        P.append(rect(9.4, 1.5, 11.7, 3.85)); P.append(rect(9.2, 3.8, 11.8, 4.0)); P.append(('h', rect(10.2, 2.7, 11.1, 3.4)))   # cab
        P.append(rect(21.0, 0.95, 21.35, 1.45)); P.append(rect(21.3, 1.05, 21.6, 1.3))
        P.append(rect(12.9, 1.0, 19.5, 1.35))                                                          # frames and cylinders
        P.append(rect(18.4, 0.85, 19.6, 1.55))
    else:
        nose = [(9.2, 1.0), (21.3, 1.0), (21.6, 1.25), (21.4, 1.9), (20.9, 2.7), (20.2, 3.35), (19.2, 3.75), (17.8, 3.95), (9.2, 3.95)]
        P.append(nose); P.append(('h', rect(10.2, 2.7, 11.1, 3.4)))
        P.append(('h', [(19.3, 1.0), (21.3, 1.0), (21.45, 1.25), (20.6, 1.25)]))                       # under-nose opening
    for cx, r in ((19.9, 0.48), (18.1, 0.48), (16.3, 1.02), (14.1, 1.02), (11.9, 1.02), (9.9, 0.55)):
        if streamlined: P.append(('h', circle(cx, r, r + 0.12, 20)))
        wheel(P, cx, r)
    if streamlined: P.append(rect(9.2, 1.02, 21.3, 1.7))                                               # valances over the wheels
    P.append(rect(8.6, 1.2, 9.3, 1.35))
    P.append(rect(0.4, 1.2, 8.6, 3.7) if not streamlined else [(0.4, 1.2), (8.6, 1.2), (8.6, 3.95), (0.9, 3.95), (0.4, 3.6)])  # tender
    if streamlined: P.append(rect(0.4, 1.02, 8.6, 1.7))
    for cx in (1.4, 3.2, 5.0, 6.8):
        if streamlined: P.append(('h', circle(cx, 0.6, 0.66, 16)))
        wheel(P, cx, 0.6)
    if streamlined: P.append(rect(0.4, 1.02, 8.6, 1.5))
    return P

def flying_scotsman(): return a3([], False)
def mallard(): return a3([], True)

def shinkansen():
    P = []
    car = [(4.0, 0.95), (27.0, 0.95), (29.6, 1.25), (30.0, 1.6), (29.5, 2.3), (28.2, 3.05), (26.2, 3.45), (24.0, 3.55), (4.0, 3.55)]
    P.append(car); P.append(('h', [(27.6, 2.6), (28.9, 2.35), (28.4, 2.9), (27.4, 3.15)]))            # windscreen
    P.append(rect(-8.0, 0.95, 3.6, 3.55))
    for i in range(10): P.append(('h', rect(5.5 + i * 2.0, 2.35, 6.6 + i * 2.0, 2.9)))
    for i in range(5): P.append(('h', rect(-7.0 + i * 2.0, 2.35, -5.9 + i * 2.0, 2.9)))
    P.append(('h', rect(4.0, 1.25, 29.0, 1.4)))                                                     # stripe
    P.append(('h', rect(3.6, 1.0, 4.0, 3.55)))
    for cx in (7.0, 24.5, -1.0):
        P.append(rect(cx - 1.6, 0.55, cx + 1.6, 1.0))
        for dx in (-1.25, 1.25): wheel(P, cx + dx, 0.43, False)
    return P

def eurostar():
    P = []
    pc = [(0.0, 0.9), (17.5, 0.9), (21.6, 1.05), (22.1, 1.35), (21.2, 2.05), (18.0, 3.25), (15.5, 3.75), (0.0, 3.85)]
    P.append(pc); P.append(('h', [(17.2, 2.85), (19.9, 2.0), (19.0, 2.55), (17.0, 3.25)]))
    for i in range(6): P.append(('h', rect(2.0 + i * 1.6, 2.55, 2.9 + i * 1.6, 3.2)))                 # power-car grilles
    P.append(line(6.0, 3.85, 9.0, 4.7, 0.12)); P.append(line(9.0, 4.7, 11.0, 4.6, 0.12))              # pantograph
    P.append(rect(-18.7, 0.9, -0.4, 3.9))
    for i in range(8): P.append(('h', rect(-17.6 + i * 2.2, 2.3, -16.2 + i * 2.2, 3.0)))
    for cx in (3.2, 15.0, -0.2):
        P.append(rect(cx - 1.6, 0.55, cx + 1.6, 0.95))
        for dx in (-1.3, 1.3): wheel(P, cx + dx, 0.46, False)
    return P

def big_boy():
    P = []
    L0 = 15.5      # tender 0..14.5, locomotive 15.5..40.5
    P.append(rect(L0 + 1.0, 2.0, 40.2, 2.2))
    P.append(boiler(L0 + 6.0, 38.6, 3.25, 1.2)); P.append(boiler(38.0, 39.6, 3.25, 1.25))
    P.append(rect(38.3, 4.3, 39.0, 4.95)); P.append(ellipse(33.0, 4.45, 0.9, 0.35)); P.append(ellipse(28.0, 4.45, 0.9, 0.3))
    P.append(rect(L0 + 1.2, 1.7, L0 + 5.6, 4.85)); P.append(rect(L0 + 1.0, 4.8, L0 + 5.8, 5.0)); P.append(('h', rect(L0 + 2.6, 3.3, L0 + 4.0, 4.2)))
    P.append(rect(36.4, 1.0, 38.0, 1.95)); P.append(rect(24.6, 1.0, 26.6, 1.95))   # two sets of cylinders
    P.append(rect(40.2, 0.9, 40.6, 1.6)); P.append([(40.2, 0.3), (41.3, 0.3), (40.6, 1.0), (40.2, 1.0)])
    for cx in (38.6, 37.4): wheel(P, cx, 0.46)
    for cx in (35.6, 33.8, 32.0, 30.2, 27.4, 25.6, 23.8, 22.0): wheel(P, cx, 0.86)
    for cx in (20.2, 18.9): wheel(P, cx, 0.53)
    P.append([(0.2, 1.3), (14.5, 1.3), (14.5, 4.2), (13.0, 4.5), (0.2, 4.5)])                       # huge tender
    P.append(rect(14.5, 1.4, 15.6, 1.6))
    for cx in (1.2, 2.9, 4.6, 6.3, 8.0, 9.7, 11.4, 13.1)[:7]: wheel(P, cx + 0.8, 0.53)
    return P

def the_general():
    P = []
    P.append(rect(4.6, 1.45, 14.3, 1.62))
    P.append(boiler(8.0, 13.4, 2.4, 0.62)); P.append([(10.2, 2.9), (11.4, 2.9), (11.2, 3.45), (10.4, 3.45)])   # boiler, sand dome
    P.append(ellipse(10.8, 3.45, 0.5, 0.2)); P.append(ellipse(8.9, 3.25, 0.4, 0.3))
    P.append([(12.9, 2.9), (13.3, 2.9), (13.3, 3.4), (13.9, 4.6), (12.3, 4.6), (12.9, 3.4)])          # diamond stack
    P.append(rect(13.3, 3.0, 14.2, 3.8)); P.append(rect(13.45, 3.8, 14.05, 4.0))                    # oil headlamp
    P.append(rect(5.4, 1.6, 8.0, 3.75)); P.append([(5.0, 3.75), (8.4, 3.75), (8.1, 4.15), (5.3, 4.15)]); P.append(('h', rect(6.1, 2.7, 7.4, 3.4)))   # wooden cab
    P.append([(14.3, 1.5), (14.3, 0.3), (16.3, 0.18)]); P.append(rect(14.1, 1.4, 14.6, 1.7))       # cowcatcher
    P.append(rect(11.6, 1.0, 13.4, 1.45))
    for cx in (12.9, 11.6): wheel(P, cx, 0.46)
    for cx in (9.4, 7.2): wheel(P, cx, 0.76)
    P.append(rect(0.0, 1.2, 4.6, 2.3)); P.append(rect(4.6, 1.3, 5.4, 1.45))                         # tender with stacked wood
    for i in range(7): P.append(ellipse(0.4 + i * 0.6, 2.55, 0.32, 0.25))
    for i in range(6): P.append(ellipse(0.7 + i * 0.6, 2.95, 0.32, 0.25))
    for cx in (0.8, 1.9, 2.8, 3.9): wheel(P, cx, 0.45, False)
    return P

ITEMS = {'stephensons-rocket': rocket, 'flying-scotsman': flying_scotsman, 'mallard': mallard,
         'shinkansen-bullet-train': shinkansen, 'eurostar': eurostar, 'big-boy': big_boy, 'the-general': the_general}

CROP = {'flying-scotsman': 4.5, 'mallard': 4.5, 'shinkansen-bullet-train': 13.0, 'eurostar': 5.0, 'big-boy': 17.0, 'the-general': 0.0}

if __name__ == '__main__':
    for slug in sys.argv[1:] or ITEMS:
        save(fit_draw(ITEMS[slug](), scene='rails', pad=3, ground_h=9, xmin=CROP.get(slug)), 'trains', slug); print(slug)
