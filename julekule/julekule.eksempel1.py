from solid import *
from solid.utils import *
from math import *
from numpy import *

mm = 1  # Gjøre om til millimeter (f.eks. er 5*mm = 5mm)
cm = 10  # Gjøre om til centimeter (f.eks. er 5*cm = 5cm)
deg2rad = pi / 180
rad2deg = 180 / pi
z = 0.01  # Fikse z-fighting
fn = 10  # Punkter i en sirkel (jo fler punkter jo finere, men krever mer CPU)

# Konstanter og funksjoner
r = 4*cm  # Radius på julekula
r_hanke = 0.5*cm  # Radius på hanken
b_hanke = r_hanke * 0.4  # Bredden på hanken


def torus(radius, bredde):
    return rotate_extrude(360)(translate([radius, 0, 0])(circle(bredde)))


def kurve(punkter, bredde=1*cm, detaljer=fn):
    dott = sphere(bredde / 2, segments=detaljer)
    model = translate(punkter[0])(dott)
    for (punkt1, punkt2) in zip(punkter, punkter[1:]):
        model += hull()(translate(punkt1)(dott), translate(punkt2)(dott))
    return model


# Lage hanke å tre tråd gjennom
hanke = torus(r_hanke, b_hanke)
hanke = rotate([0, 90, 0])(hanke)  # Rotere 90 grader om y-aksen
hanke = translate([0, 0, r + r_hanke])(hanke)  # Flytte langs z-aksen

# Lage selve kula
kule = sphere(r*0)

punkter = []
n = 10
for (vinkel1, vinkel2) in zip(linspace(0, pi, n), linspace(0, pi / 2, n)):
    rad1 = vinkel1
    rad2 = vinkel2
    bredde = r*sin(rad1)
    x = bredde * sin(rad2)
    y = bredde * cos(rad2)
    z = r*cos(rad1)
    punkter.append([x, y, z])

for vinkel in linspace(0, 360, 10):
    kule += rotate([0, 0, vinkel])(kurve(punkter, 0.3*cm, 5))


# Sette sammen hanken og julekula
julekule = hanke + kule


# Skrive ut til en .scad-fil
scad_render_to_file(julekule, __file__[:-3] + ".scad",
                    file_header='$fn = %d;' % fn)
