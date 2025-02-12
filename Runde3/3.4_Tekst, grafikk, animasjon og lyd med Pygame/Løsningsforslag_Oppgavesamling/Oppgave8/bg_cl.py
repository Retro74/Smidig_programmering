import pygame

class Background:
    def __init__(self, image_path, image_width, speed):
        self.image = pygame.image.load(image_path).convert()
        self.image_width = image_width
        self.speed = speed
        self.x_pos = 0

    def update(self, screen):
        self.x_pos -= self.speed
        if self.x_pos < - self.image_width:
            self.x_pos=0
        screen.blit(self.image, (self.x_pos, 0))
        screen.blit(self.image, (self.x_pos + self.image_width, 0))

