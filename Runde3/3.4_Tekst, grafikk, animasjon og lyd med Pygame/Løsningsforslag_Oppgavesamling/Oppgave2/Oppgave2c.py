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
clock = pg.time.Clock()

#################### /INIT ########################
fortsett = True
end_x=VINDU_BREDDE
end_y=VINDU_HOYDE
linepunkter=[(random.randint(0,VINDU_BREDDE), random.randint(0,VINDU_HOYDE))]

while fortsett:
    clock.tick(5)
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

#################### Spillogikk ########################
    linepunkter.append((random.randint(0,VINDU_BREDDE), random.randint(0,VINDU_HOYDE)))
    for i in range(len(linepunkter)-1):
        pg.draw.line(vindu, (255, 0, 0), (linepunkter[i]), linepunkter[i+1], 2)




#################### /Spillogikk ########################

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
