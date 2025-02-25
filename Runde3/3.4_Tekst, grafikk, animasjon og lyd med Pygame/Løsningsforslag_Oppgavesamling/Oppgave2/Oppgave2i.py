import pygame as pg
import datetime
import math
# Initialiserer/starter pygame
pg.init()
# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
pg.display.set_caption("Klokke")

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)

#################### INIT ########################
clock = pg.time.Clock()

#################### /INIT ########################
fortsett = True
center_x =VINDU_BREDDE/2
center_y=VINDU_HOYDE/2
sekundviser_lengde = 220
sekundviser_tykkelse = 1
minuttviser_lengde = 220
minuttviser_tykkelse = 3
timeviser_lengde = 120
timeviser_tykkelse = 8

while fortsett:
    clock.tick(1)

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

#################### Spillogikk ########################
    now = datetime.datetime.now()
    tid = now.time()
    time = tid.hour
    minutt = tid.minute
    sekund = tid.second

    vindu.fill((255, 255, 255))
    pg.draw.circle(vindu, (0, 0, 0), (center_x, center_y), center_x-10, 3)
    # Tegn sekundviser
    sekundviser_vinkel = sekund * 6
#    print(sekund)
    sekundviser_x = math.cos(math.radians(sekundviser_vinkel)-math.pi/2) * sekundviser_lengde + center_x
    sekundviser_y = math.sin(math.radians(sekundviser_vinkel)-math.pi/2) * sekundviser_lengde + center_y

    pg.draw.line(vindu, (0, 0, 0), (center_x,center_y), (sekundviser_x, sekundviser_y), sekundviser_tykkelse)


    # Tegn minuttviser
    minuttviser_vinkel = minutt * 6
    minuttviser_x = math.cos(math.radians(minuttviser_vinkel)-math.pi/2) * minuttviser_lengde + center_x
    minuttviser_y = math.sin(math.radians(minuttviser_vinkel)-math.pi/2) * minuttviser_lengde + center_y
    pg.draw.line(vindu, (0, 0, 0), (center_x,center_y), (minuttviser_x, minuttviser_y), minuttviser_tykkelse)

    # Tegn timeviser
    timeviser_vikel = (time % 12) * 30 + minutt * 0.5
    timeviser_x = math.cos(math.radians(timeviser_vikel) - math.pi/2) * timeviser_lengde + center_x
    timeviser_y = math.sin(math.radians(timeviser_vikel) - math.pi/2) * timeviser_lengde + center_y
    pg.draw.line(vindu, (0, 0, 0), (center_x,center_y), (timeviser_x, timeviser_y), timeviser_tykkelse)


#################### /Spillogikk ########################

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
