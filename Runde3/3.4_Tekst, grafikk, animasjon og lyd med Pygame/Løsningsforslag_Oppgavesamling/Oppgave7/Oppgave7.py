import pygame as pg
from Ball import Ball
import pylab as m

NUMBER_OF_BALLS = 10
BALL_RADIUS=20
BALLVEKT = 1
TOPPFART = 10

def finnAvstand(obj1, obj2):
  xAvstand = (obj1.x - obj2.x)**2  # x-avstand i andre
  yAvstand = (obj1.y - obj2.y)**2  # y-avstand i andre
  return  m.sqrt(xAvstand + yAvstand)

colors=[]
for i in range(NUMBER_OF_BALLS):
    colors.append((m.randint(0,255), m.randint(0,255), m.randint(0,255)))

clock = pg.time.Clock()

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])


# Lager et Ball-objekt
baller=[]
for color in colors:
    baller.append(Ball(float(m.randint(20,VINDU_BREDDE-20)), float(m.randint(20, VINDU_HOYDE-20)), float(m.randint(-10,10)*TOPPFART/10), float(m.randint(-10,10)*TOPPFART/10),BALLVEKT, BALL_RADIUS,color, vindu))

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:
    clock.tick(60)
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Farger bakgrunnen lyseblå
    vindu.fill((135, 206, 235))

    # Tegner og flytter ballen
    for ball in baller:
        ball.tegn()
        ball.flytt()
    for i in range(len(baller)-1):
        for j in range(i+1, len(baller)):
            baller[i].kollisjon(baller[j])

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
