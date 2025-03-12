import pygame as pg
import math

# Variabler i spillet
VINDU_BREDDE = 600
VINDU_HOYDE  = 600
clock = pg.time.Clock()
center_x, center_y = VINDU_BREDDE // 2, VINDU_HOYDE // 2
radius = 250



#################### INIT ########################
# Initialiserer/starter pygame
pg.init()
# Oppretter et vindu der vi skal "tegne" innholdet vårt
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
vindu.fill((255, 255, 255))

# Tegner en gradert kule ved hjelp av sirkeler i ulike farger
for i in range(radius):
    farge = (i, i, i) #Grå
#    farge = (i, 0, 0) #Rød
#    farge = (0, 0, i) #Blå
#    farge = (0, i, 0) #Grønn
#    farge = (i, i, 0) #Gul
#    farge = (0, i, i) #Turkis
#    farge = (i, 0, i) #Rosa
    pg.draw.circle(vindu, farge, (center_x, center_y), 255-i)


#################### /INIT ########################
fortsett = True
while fortsett:
    clock.tick(60)
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

#################### Spillogikk ########################
# Denne oppgaven har ingen utvikling/animasjon

#################### /Spillogikk ########################

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
