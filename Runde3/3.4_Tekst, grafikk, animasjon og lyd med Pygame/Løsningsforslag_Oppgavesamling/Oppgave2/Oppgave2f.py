import pygame as pg
import math

# Variabler til programmet
VINDU_BREDDE = 700
VINDU_HOYDE  = 700

antall_runder = 20
radius = 0
center_x, center_y = VINDU_BREDDE//2, VINDU_HOYDE//2
clock = pg.time.Clock()

#################### INIT PYGAME VINDU ########################
# Initialiserer/starter pygame
pg.init()
# Oppretter et vindu der vi skal "tegne" innholdet vårt
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])


while radius < VINDU_BREDDE//2:
    pos_x = math.cos(math.radians(radius*antall_runder))*radius+center_x
    pos_y = math.sin(math.radians(radius*antall_runder))*radius+center_y
    pg.draw.circle(vindu, (255, 0, 0), (pos_x,pos_y), 1)
    radius+=0.01

#################### /INIT ########################
fortsett = True
while fortsett:
    clock.tick(60)
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

#################### SPILL-LOGIKK (Animasjon) ########################
# Denne oppgaven tegner bare en spiral en gang og har ingen utvikling/animasjon

#################### /SPILL-LOGIKK (Animasjon) ########################

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
