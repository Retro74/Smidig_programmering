import math
import pygame

class Tank:
    def __init__(self, x, y, size=1):
        self.tank_image = pygame.image.load("tank.png") # bilde av tanken
        self.turret_image = pygame.image.load("turret.png") # bilde av kanontårnet
        self.turret_offset = (25, 25) # offset for å plassere kanontårnet på riktig sted
        self.rect = self.tank_image.get_rect() # rektangel rundt bilde av tanken
        self.rect.x = x
        self.rect.y = y
        self.speed = 5 # fart i piksler per frame
        self.angle_speed = 5 # vinkelhastighet i grader per frame
        self.angle = 0 # startvinkel for tanks
        self.turret_angle = 0 # startvinkel for kanontårnet
        self.size = size # størrelse på tanken

    def move(self, keys):
        if keys[pygame.K_w]:
            self.rect.y -= self.speed * math.cos(self.angle*math.pi/180)
            self.rect.x -= self.speed * math.sin(self.angle*math.pi/180)

        elif keys[pygame.K_s]:
            self.rect.y += self.speed * math.cos(self.angle*math.pi/180)
            self.rect.x += self.speed * math.sin(self.angle*math.pi/180)
        if keys[pygame.K_a]:
            self.angle += self.angle_speed
        elif keys[pygame.K_d]:
            self.angle -= self.angle_speed

        # begrens vinkelen til et område mellom -180 og 180 grader
        self.angle %= 360
        if self.angle > 180:
            self.angle -= 360
        elif self.angle < -180:
            self.angle += 360

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
        old_center = self.rect.center
        turret_center = (self.rect.x + self.turret_offset[0], self.rect.y + self.turret_offset[1])
        self.turret_image = pygame.transform.rotate(pygame.image.load("turret.png"), self.angle)
        self.rect = self.tank_image.get_rect()
        self.rect.center = old_center
        self.rect.x, self.rect.y = turret_center[0] - self.turret_offset[0], turret_center[1] - self.turret_offset[1]

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
