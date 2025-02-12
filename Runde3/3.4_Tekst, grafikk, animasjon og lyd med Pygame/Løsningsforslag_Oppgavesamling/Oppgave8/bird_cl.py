import pygame
ACCELRATION = 0.1
GRAVITY = 0.05
class Bird:
    def __init__(self, image_path, image_width, image_height, x_pos, y_pos, x_speed=0, y_speed=0):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image_width = image_width
        self.image_height = image_height
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.image = pygame.transform.scale(self.image, (self.image_width,self.image_height))

    def update(self, screen):
        self.y_speed += GRAVITY
        self.y_pos += self.y_speed
        blitImage = pygame.transform.rotate(self.image, -self.y_speed*10)
        screen.blit(blitImage, (self.x_pos, self.y_pos))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y_speed = -1.5

