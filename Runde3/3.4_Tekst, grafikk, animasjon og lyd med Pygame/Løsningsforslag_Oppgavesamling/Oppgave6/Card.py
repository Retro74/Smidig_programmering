import pygame
import math

class Card:
    def __init__(self, front_image, back_image, value, color, x, y, width, height, rotation=0):
        self.front_image = front_image
        self.back_image = back_image
        self.value = value
        self.color = color
        self.is_up = False
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotation = rotation

    def draw(self):
        if self.is_up:
            image = self.front_image
        else:
            image = self.back_image
        rotated_image = pygame.transform.rotate(image, self.rotation)
        scaled_image = pygame.transform.smoothscale(rotated_image, self.get_scaled_size())
        rect = scaled_image.get_rect(center=(self.x, self.y))
        return scaled_image, rect

    def flip(self):
        #self.is_up = not self.is_up
        self.is_up =True

    def move(self, x, y):
        self.x = x
        self.y = y

    def rotate(self, angle):
        self.rotation = (self.rotation + angle) % 360

    def get_scaled_size(self):
        angle = math.radians(self.rotation)
        w, h = self.width, self.height
        new_w = abs(w * math.cos(angle)) + abs(h * math.sin(angle))
        new_h = abs(h * math.cos(angle)) + abs(w * math.sin(angle))
        return int(new_w), int(new_h)

    def is_clicked(self, pos):
        # Get the scaled size of the card
        scaled_size = self.get_scaled_size()

        # Calculate the position of the top-left corner of the card
        x = self.x - scaled_size[0] // 2
        y = self.y - scaled_size[1] // 2

        # Rotate the click position based on the card's rotation
        angle = math.radians(-self.rotation)
        cx, cy = pos
        px, py = cx - self.x, cy - self.y
        new_x = self.x + px * math.cos(angle) - py * math.sin(angle)
        new_y = self.y + px * math.sin(angle) + py * math.cos(angle)

        # Check if the rotated click position is within the bounds of the card
        return x <= new_x <= x + scaled_size[0] and y <= new_y <= y + scaled_size[1]
