import pygame as pg
import math
import numpy
# Initialiserer/starter pygame
pg.init()
# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)

#################### INIT ########################
clock = pg.time.Clock()

#################### /INIT ########################
fortsett = True
offset = 0
while fortsett:
    clock.tick(60)
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

#################### Spillogikk ########################
    for i in range(VINDU_HOYDE):
        if i<256:
            pg.draw.line(vindu, (i%256, i%256, i%256), (0, i), (VINDU_BREDDE, i), 1)
        else:
            pg.draw.line(vindu, (255-i%256, 255-i%256, 255-i%256), (0, i), (VINDU_BREDDE, i), 1)
    offset+=1

#################### /Spillogikk ########################

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
