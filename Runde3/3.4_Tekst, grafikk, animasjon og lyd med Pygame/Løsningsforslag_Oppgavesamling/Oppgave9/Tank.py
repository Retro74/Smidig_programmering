import math
import pygame
from pathlib import Path
pyFilePath = Path(__file__).resolve().parent

class Tank:
    def __init__(self, x, y, size=1):
        #print("Tank made")
        self.tank_image = pygame.image.load(pyFilePath.joinpath("tank.png")) # bilde av tanken
        self.turret_image = pygame.image.load(pyFilePath.joinpath("turret.png")) # bilde av kanontårnet
        self.rect = self.tank_image.get_rect() # rektangel rundt bilde av tanken
        self.rect.x = x
        self.rect.y = y
        self.speed = 3 # fart i piksler per frame
        self.angle_speed = 2 # vinkelhastighet i grader per frame
        self.angle = 0 # startvinkel for tanks
        self.turret_angle = 0 # startvinkel for kanontårnet
        self.size = size # størrelse på tanken

    def move(self, keys):
        if keys[pygame.K_w]:
            self.rect.x -= self.speed * math.sin(math.radians(self.angle))
            self.rect.y -= self.speed * math.cos(math.radians(self.angle))

        elif keys[pygame.K_s]:
            self.rect.x += self.speed * math.sin(math.radians(self.angle))
            self.rect.y += self.speed * math.cos(math.radians(self.angle))

        if keys[pygame.K_a]:
            self.angle += self.angle_speed
        elif keys[pygame.K_d]:
            self.angle -= self.angle_speed

        # begrens vinkelen til et område mellom 0 og 360 grader
        self.angle %= 360
        #print(self.angle)


    def rotate_turret(self, keys):
        if keys[pygame.K_LEFT]:
            self.turret_angle += self.angle_speed
        elif keys[pygame.K_RIGHT]:
            self.turret_angle -= self.angle_speed

        # begrens vinkelen til et område mellom -180 og 180 grader
        self.turret_angle %= 360
        if self.turret_angle > 180:
            self.turret_angle -= 360
        elif self.turret_angle < -180:
            self.turret_angle += 360

        # roter bilde av kanontårnet rundt midten
        turret_center = (self.rect.x, self.rect.y)
        self.turret_image = pygame.transform.rotate(pygame.image.load(pyFilePath.joinpath("turret.png")), self.angle)
        self.rect = self.tank_image.get_rect()
        self.rect.x, self.rect.y = turret_center[0], turret_center[1]

    def draw(self, screen):
        tank_size = (int(self.rect.width * self.size), int(self.rect.height * self.size))
        tank_image = pygame.transform.scale(self.tank_image, tank_size)
        turret_size = (int(self.turret_image.get_width() * self.size), int(self.turret_image.get_height() * self.size))
        turret_image = pygame.transform.scale(self.turret_image, turret_size)
        rotated_tank = pygame.transform.rotate(tank_image, self.angle)
        rotated_turret = pygame.transform.rotate(turret_image, self.turret_angle)

       # sentrer rotasjonen rundt midten av tanken
        tank_rect = rotated_tank.get_rect(center=self.rect.center)
        turret_rect = rotated_turret.get_rect(center=tank_rect.center)

        # tegn bilde av tanken og kanontårnet på skjermen
        screen.blit(rotated_tank, tank_rect)
        screen.blit(rotated_turret, turret_rect)
        #print("tegner Tank her ", tank_rect)

