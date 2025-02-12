import pygame as pg
import math
# Initialiserer/starter pygame
pg.init()
# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 700
VINDU_HOYDE  = 700
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)

#################### INIT ########################
clock = pg.time.Clock()

radius = 0
center_x, center_y = VINDU_BREDDE//2, VINDU_HOYDE//2

while radius < VINDU_BREDDE//2:
    pos_x = math.cos(math.radians(radius*10))*radius+center_x
    pos_y = math.sin(math.radians(radius*10))*radius+center_y
    pg.draw.circle(vindu, (255, 0, 0), (pos_x,pos_y), 1)
    radius+=0.01

#################### /INIT ########################
fortsett = True
i=0
while fortsett:
    clock.tick(60)
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

#################### Spillogikk ########################


#################### /Spillogikk ########################

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
