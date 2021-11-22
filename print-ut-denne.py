from solid import *
from solid.utils import *
from math import *
from numpy import *

mm = 1  # Gjøre om til millimeter (f.eks. er 5*mm = 5mm)
cm = 10  # Gjøre om til centimeter (f.eks. er 5*cm = 5cm)
deg2rad = pi / 180
rad2deg = 180 / pi
z = 0.01  # Fikse z-fighting
fn = 75  # Punkter i en sirkel (jo fler punkter jo finere, men krever mer CPU)

# Konstanter og funksjoner
r = 5*cm
christmas = False

# ---

sphere_distance_from_origo = r * sin(30 * deg2rad) / sin(120 * deg2rad)

sphere1 = sphere(r, segments=fn)
sphere1 = translate([sphere_distance_from_origo, 0, 0])(sphere1)

sphere2 = sphere(r, segments=fn)
sphere2 = translate([sphere_distance_from_origo * cos(120 * deg2rad), sphere_distance_from_origo * sin(120 * deg2rad), 0])(sphere2)

sphere3 = sphere(r, segments=fn)
sphere3 = translate([sphere_distance_from_origo * cos(-120 * deg2rad), sphere_distance_from_origo * sin(-120 * deg2rad), 0])(sphere3)

height_from_origo = sqrt(r ** 2 - sphere_distance_from_origo ** 2)

sphere4 = sphere(r, segments=fn)
sphere4 = translate([0, 0, height_from_origo])(sphere4)

rt = sphere1 * sphere2 * sphere3 * sphere4

if christmas:
    cylinder_height=5*cm
    cylinder_radius=2*mm

    c = cylinder(r=cylinder_radius, h=cylinder_height)
    c = translate([0, 0, -cylinder_height/2])(c)
    c = rotate([90, 0, 0])(c)
    c = translate([0, 0, height_from_origo * 0.9])(c)

    rt -= c
# ---

# Skrive ut til en .scad-fil
scad_render_to_file(rt, __file__[:-3] + ".scad",
                    file_header='$fn = %d;' % fn)
