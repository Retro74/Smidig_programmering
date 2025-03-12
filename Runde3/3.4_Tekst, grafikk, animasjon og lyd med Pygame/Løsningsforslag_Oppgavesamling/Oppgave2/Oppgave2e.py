import pygame as pg
import math
# Initialiserer/starter pygame
pg.init()
# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
FPS = 60
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)

#################### INIT ########################
clock = pg.time.Clock()
radius=200 #Radius til sirkelen
#################### /INIT ########################
fortsett = True
kuler=255 #Maks 255 siden denne også brukes til farge
stigende=True
offset = 0
while fortsett:
    clock.tick(FPS)
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

#################### Spillogikk ########################
    for i in range(kuler):
        pos_x = math.cos(math.radians(offset+i))*radius + VINDU_BREDDE/2
        pos_y = math.sin(math.radians(offset+i))*radius + VINDU_HOYDE/2
        pg.draw.circle(vindu, (0, i, 0), (pos_x, pos_y), 8) #Tegn en prikkpå stedet gitt av pos_x og pos_y
        
    offset +=3
    



#################### /Spillogikk ########################
    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
