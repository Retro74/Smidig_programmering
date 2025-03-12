import pygame
from Tank import Tank
from pathlib import Path
pyFilePath = Path(__file__).resolve().parent

pygame.init()
screen = pygame.display.set_mode((1600, 800))
clock = pygame.time.Clock()
clock = pygame.time.Clock()
landscape = pygame.image.load(pyFilePath.joinpath("landscape.jpg"))

tank = Tank(400, 100, 0.1)
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

