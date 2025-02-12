import pygame
from Tank import Tank

pygame.init()
screen = pygame.display.set_mode((1600, 800))
clock = pygame.time.Clock()
clock = pygame.time.Clock()
landscape = pygame.image.load("landscape.jpg")

tank = Tank(400, 300, 0.1)
fortsett = True
while fortsett:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fortsett = False

    keys = pygame.key.get_pressed()
    screen.blit(landscape,(0,0))

    tank.move(keys)
    tank.rotate_turret(keys)
    tank.draw(screen)

    pygame.display.flip()

