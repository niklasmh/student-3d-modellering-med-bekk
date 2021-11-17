from solid import *
from solid.utils import *
from math import *
from numpy import *

mm = 1  # Gjøre om til millimeter (f.eks. er 5*mm = 5mm)
cm = 10  # Gjøre om til centimeter (f.eks. er 5*cm = 5cm)
z = 0.01  # Fikse z-fighting
# Punkter i en sirkel (jo fler punkter jo finere, men krever mer CPU)
dets = 70
fn = dets


def deg2rad(x):
    return x * pi / 180


def rad2deg(x):
    return x * 180 / pi


def torus(radius, bredde, detaljer=10):
    return rotate_extrude(360, segments=detaljer)(translate([radius, 0, 0])(circle(bredde, segments=detaljer)))


def kurve(punkter, bredde=1*cm, detaljer=fn):
    dott = sphere(bredde / 2, segments=detaljer)
    model = translate(punkter[0])(dott)
    for (punkt1, punkt2) in zip(punkter, punkter[1:]):
        model += hull()(translate(punkt1)(dott), translate(punkt2)(dott))
    return model


""" ⬇ SKRIV KODE HER ⬇ """
"""
Oppskrift på en helt rund julekule:
1. Lage hanke å tre tråd gjennom
2. Lage selve kula
"""
# TODO

# 1. lag kropp

# 1.3 lag ansikt


def pokemon_face(width=1*cm, details=30, trans=[0, 0, 0]):
    mouth = sphere(width / 3, segments=details*5)
    mouth = scale([0.8, 1.4, 0.3])(mouth)
    mouth = translate([-10, 0, 0])(mouth)
    eye = cylinder(width / 12, 9, segments=details*3)
    eye_white = scale([0.8, 0.8, 0.8])(eye)
    eye_white = translate([0, 0, 8.5])(eye_white)

    eye_black = scale([0.25, 0.25, 1])(eye)
    eye -= eye_white
    eye += eye_black
    eye = rotate([0, 90, 0])(eye)
    eye = translate([-1.2*cm, 0, 0])(eye)
    right_eye = eye
    right_eye = rotate([0, -15, 30])(right_eye)
    right_eye = translate([0, 3.8*cm, 2.5*cm])(right_eye)
    left_eye = eye
    left_eye = rotate([0, -15, -30])(left_eye)
    left_eye = translate([0, -3.8*cm, 2.5*cm])(left_eye)
    face = mouth + right_eye + left_eye
    face = translate(trans)(face)
    return face


def pokemon_torso(width=1*cm, details=30, z=1.2):
    body = sphere(width / 2, segments=details*5)
    body = scale(v=[2, 1.7, z])(body)
    body = translate([0, 0, width*z/2-8])(body)
    body += pokemon_face(width*1.3, trans=[9*cm, 0, (width*z/2-8/2)-1*cm])
    return body


# 1.2 lag bein

def pokemon_leg(x, y, z, radius=5*mm, details=30, rotate_angles=[0, 0, 0]):
    leg = cylinder(r=radius, h=radius*3)
    feet = sphere(r=radius, segments=details)
    leg += feet
    leg = translate([x, y, z])(leg)
    leg = rotate(rotate_angles)(leg)
    return leg

# 2. lag hatt


def pokemon_hat(r=12*cm, h=2*cm, w=3*mm, details=30):
    hat = cylinder(r, h, segments=details*10)
    minus_hat = cylinder(r=r-w, h=h, segments=details*10)
    minus_hat = translate([0, 0, w])(minus_hat)
    triangle = cube([r, r, w])
    triangle = translate([0, 0, w])(triangle)
    triangle = rotate([0, 0, 45])(triangle)
    triangle = scale([1, 1.8, 1])(triangle)

    right_tri1 = translate([4*cm, 4*cm, 0])(triangle)
    right_tri2 = translate([-4*cm, 4*cm, 0])(triangle)

    right_tri = right_tri1 + right_tri2

    left_tri = translate([0, -(2*cm + r*3), 0])(right_tri)

    tris = left_tri + right_tri

    minus_hat -= tris

    hat = scale([1.2, 1, 1])(hat - minus_hat)
    return hat


def pokemon():
    pokemon = pokemon_body()
    pokemon += translate([0, 0, 10*cm-8])(pokemon_hat(details=dets))
    return pokemon


def pokemon_body():
    pokemon = pokemon_torso(width=10*cm, details=dets)
    top = cylinder(10*cm, 4*cm)
    top = translate([0, 0, 10*cm-8])(top)

    pokemon -= top

    # right legs
    pokemon += translate([4.5*cm, 6*cm, 9*mm])(pokemon_leg(x=0, y=0,
                                                           z=0, radius=1.3*cm, rotate_angles=[-15, -45, 90], details=dets))
    pokemon += translate([0, 7*cm, 9*mm])(pokemon_leg(x=0, y=0, z=0,
                                                      radius=1.3*cm, rotate_angles=[0, -45, 90], details=dets))
    pokemon += translate([-4.5*cm, 6*cm, 9*mm])(pokemon_leg(x=0, y=0,
                                                            z=0, radius=1.3*cm, rotate_angles=[15, -45, 90], details=dets))

    # left legs
    pokemon += translate([4.5*cm, -6*cm, 9*mm])(pokemon_leg(x=0, y=0,
                                                            z=0, radius=1.3*cm, rotate_angles=[-15, -45, -90], details=dets))
    pokemon += translate([0, -6.5*cm, 9*mm])(pokemon_leg(x=0, y=0,
                                                         z=0, radius=1.3*cm, rotate_angles=[0, -45, -90], details=dets))
    pokemon += translate([-4.5*cm, -6*cm, 9*mm])(pokemon_leg(x=0, y=0,
                                                             z=0, radius=1.3*cm, rotate_angles=[15, -45, -90], details=dets))
    bottom = cylinder(10*cm, 2*cm)
    bottom = translate([0, 0, -2*cm])(bottom)

    pokemon -= bottom
    return pokemon


pokemon_ = scale([0.51, 0.51, 0.51])(pokemon())
# Skrive ut til en .scad-fil
scad_render_to_file(pokemon_, "pokemon" + ".scad",
                    file_header='$fn = %d;' % fn)

pokemon_body = scale([0.51, 0.51, 0.51])(pokemon_body())
scad_render_to_file(pokemon_body, "pokemonbody" + ".scad",
                    file_header='$fn = %d;' % fn)

pokemon_hat = scale([0.51, 0.51, 0.51])(pokemon_hat(details=dets))
scad_render_to_file(pokemon_hat, "pokemonhat" + ".scad",
                    file_header='$fn = %d;' % fn)
