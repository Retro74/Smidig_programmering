import pygame
import pygame as pg
from bg_cl import Background
from bird_cl import Bird
#################### INIT ########################
# Initialiserer/starter pygame
pg.init()
# Oppretter et vindu der vi skal "tegne" innholdet vårt

VINDU_BREDDE = 288
VINDU_HOYDE  = 384

vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

clock = pygame.time.Clock()

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)
text = font.render('Start/Pause press "p"', True, (0, 0, 0))

BG_SPEED = 2
background = Background("bg.png", 288, BG_SPEED)
bird = Bird("fugl.png", 34, 24, 10, 10)

gameRunning = True

#################### /INIT ########################

fortsett = True
while fortsett:
    clock.tick(60)
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_p]:
                gameRunning = not gameRunning
    # Farger bakgrunnen hvit
    #################### Spillogikk ########################
    if gameRunning:
        background.update(vindu)
        bird.update(vindu)
    else:
        vindu.fill((255, 255, 255))
        vindu.blit(text, (100,100) )

    if bird.y_pos > 300:
        fortsett=False

    #################### /Spillogikk ########################

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
