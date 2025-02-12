import pygame as pg
import random
import math
class Ball:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, fart_x, fart_y, vekt, radius, color,  vindusobjekt):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.fart_x = fart_x
    self.fart_y = fart_y
    self.vekt = vekt
    self.radius = radius
    self.color = color
    self.vindusobjekt = vindusobjekt

  def tegn(self):
    """Metode for å tegne ballen"""
    pg.draw.circle(self.vindusobjekt, self.color , (self.x, self.y), self.radius)

  def flytt(self):
    """Metode for å flytte ballen"""
    # Sjekker om ballen er utenfor høyre/venstre kant
    if ((self.x - self.radius) <= 1) or ((self.x + self.radius) >= self.vindusobjekt.get_width()-1):
      self.fart_x = -self.fart_x

    if ((self.y - self.radius) <= 1) or ((self.y + self.radius) >= self.vindusobjekt.get_height()-1):
      self.fart_y = -self.fart_y

    # Flytter ballen
    self.x += self.fart_x
    self.y += self.fart_y

  def kollisjon(self, annen_ball):
        avstand = ((self.x - annen_ball.x)**2 + (self.y - annen_ball.y)**2)**0.5
        if avstand < self.radius + annen_ball.radius:
            self.fart_x, annen_ball.fart_x =  annen_ball.fart_x, self.fart_x
            self.fart_y, annen_ball.fart_y =  annen_ball.fart_y, self.fart_y
