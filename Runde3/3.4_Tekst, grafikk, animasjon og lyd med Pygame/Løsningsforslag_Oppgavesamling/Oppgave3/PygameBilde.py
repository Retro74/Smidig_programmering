import pygame as pg
# Initialiserer/starter pygame
import pygame.transform

pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)
redCar = pg.image.load("car.png").convert_alpha()
redCar = pg.transform.scale(redCar, (125,50))
tree = pg.image.load("tree.png").convert_alpha()
tree = pg.transform.scale(tree, (125,120))

redCar_y = 300
redCar_x= 500
speed = -0.1
fortsett = True
while fortsett:
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
    # Farger bakgrunnen hvit
    vindu.fill((255, 255, 255))
    pg.draw.line(vindu, (50, 50, 50), (0, 350), (500, 350), 15)
    redCar_x += speed

    if redCar_x < -200 or redCar_x > 500:
        speed = -speed
        redCar = pygame.transform.flip(redCar, True, False)

    vindu.blit(tree,(70,232))
    vindu.blit(tree,(120,222))
    vindu.blit(tree,(265,235))
    vindu.blit(tree,(170,228))

    vindu.blit(redCar, (redCar_x, redCar_y))
    vindu.blit(tree,(200,277))
    vindu.blit(tree,(100,284))
    vindu.blit(tree,(260,282))

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
