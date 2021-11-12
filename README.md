# 3D-modellering med Bekk (for studenter)

Her kan du finne noen eksempler på hva du kan lage.

- [/julekule](julekule)

## Verktøy

- [VSCode](https://code.visualstudio.com/) (Anbefalt)
- [Python 3](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/en/)
- [OpenSCAD](https://openscad.org/)

## Installere pakker

Nå som du har satt opp både Python 3 og Node.js, må du installere noen pakker:

```bash
pip3 install solidpython numpy pillow
npm install -g nodemon # For å få auto-refresh på 3D-modellen
```

## Sette opp kodemiljøet

1. Åpne en terminal, f.eks. i VSCode, og kjør:

   ```bash
   nodemon julekule/julekule.py
   # Eller
   nodemon --exec python3 julekule/julekule.py # om du bruker python 2
   ```

   Husk å naviger til riktig mappe (altså hit denne readme'en er). I VSCode skal dette skje automatisk.

2. Neste steg er å åpne OpenSCAD og åpne `.scad`-filen som nå ble generert. _Når du gjør kode endringer nå vil du se 3D-modellen med en gang. Dette er supernyttig om man skal kode 3D-modeller!_

3. (Anbefalt) Plasser vinduene ved siden av hverandre, slik:
   ![Kodemiljø](https://user-images.githubusercontent.com/8504538/141381286-7e681745-31bb-47b6-8467-7f6b9853dbf9.png)
