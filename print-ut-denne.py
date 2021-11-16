# Trykk på "Edit this file" og lim inn koden din.
# Lag så en PR med å trykke på "Propose changes".
# Du vil videre få mer instruksjoner om hva du må gjøre inne på PR-siden.

from solid import *
from solid.utils import *
from math import *
from numpy import *

mm = 1  # Gjøre om til millimeter (f.eks. er 5*mm = 5mm)
cm = 10  # Gjøre om til centimeter (f.eks. er 5*cm = 5cm)
deg2rad = pi / 180
rad2deg = 180 / pi
z = 0.01  # Fikse z-fighting
fn = 32  # Punkter i en sirkel (jo fler punkter jo finere, men krever mer CPU)

# Konstanter og funksjoner
r = 3*cm  # Radius på vasen


""" ⬇ SKRIV KODE HER ⬇ """
"""
Oppskrift på vase:
1. Lage en fasong/form som en funksjon (vase_form_funksjon)
2. Rotere denne formen i en sirkel
"""

# 1.
def vase_form_funksjon(x):
    y = r * 0.3
    sc_x = sqrt(x + 3) * 1
    # y += (1+sin(sc_x / 18)) * 1
    return y


tykkelse = 0.1*cm
form_på_vase = [[0, 0], [0, -tykkelse],
                [vase_form_funksjon(-tykkelse), -tykkelse]]
steg = 60

for y in linspace(1, 1*cm, steg):
    x = vase_form_funksjon(y)
    form_på_vase.append([x, y])

for [x, y] in form_på_vase[:2:-1]:
    form_på_vase.append([x - tykkelse, y])

# 2.
vase = polygon(form_på_vase)  # Lage formen som en shape
vase = rotate_extrude()(vase)  # Rotere formen rundt z-aksen

# Håndtak
handle = cube([5*cm, 1.5*cm, 0.1*cm], center = True)
handle = translate([20, 0, 9.5])(handle)
handle -= cylinder(.9*cm, 5*cm)

end = cube([1*cm, 1.7*cm, 1*cm], center = True)
end = translate([41, 0, 11])(end)
cyl = cylinder(.9*cm, 5*cm)
cyl = translate([36, 0, 0])(cyl)
end -= cyl
handle -= end

# text
txt=text("Lers", 1*cm)
txt = translate([9, -4, 10])(txt)

print((pi*(r-0.1)**2)*1)

""" ⬆ SKRIV KODE HER ⬆ """


# Skrive ut til en .scad-fil
scad_render_to_file(vase+handle+txt, __file__[:-3] + ".scad",
                    file_header='$fn = %d;' % fn)
