import pygame as pg
import random
# Initialiserer/starter pygame
pg.init()
# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)

#################### INIT ########################

#################### /INIT ########################
fortsett = True
start_x =0
start_y=0
end_x=VINDU_BREDDE
end_y=VINDU_HOYDE

while fortsett:
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

#################### Spillogikk ########################
    pg.draw.line(vindu, (200, 0, 200), (start_x,start_y), (end_x, end_y), 2)
    if start_x < VINDU_BREDDE:
        start_x+=10
    elif start_y< VINDU_HOYDE:
        start_y +=10
    if end_x >0:
        end_x -=10
    elif end_y > 0:
        end_y-=10


#################### /Spillogikk ########################

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
