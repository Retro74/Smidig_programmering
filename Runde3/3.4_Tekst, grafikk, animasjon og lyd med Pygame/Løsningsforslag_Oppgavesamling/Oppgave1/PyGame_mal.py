import pygame as pg
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
while fortsett:
    clock.tick(60)
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
    # Farger bakgrunnen hvit
    vindu.fill((255, 255, 255))

#################### Spillogikk ########################


#################### /Spillogikk ########################

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
