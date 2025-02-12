import pygame as pg
import random

def hit_encounter(bullet_pos, target_x, target_y, target_width, target_height):
    if target_x < bullet_pos[0] <target_x+target_width and target_y< bullet_pos[1] < target_y+ target_height:
        return True
    else:
        return False

# Initialiserer/starter pygame
pg.init()
# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 1600
VINDU_HOYDE  = 900
HORISONT = 350
AIM_DIAMETER = 50
BADGUY_WIDTH= 50
BADGUY_HEIGHT = 90
BADGUY_SCALE = 0.01
BADGUY_x = random.randint(0,VINDU_BREDDE-BADGUY_WIDTH)
BADGUY_y = random.randint(HORISONT,VINDU_HOYDE-BADGUY_HEIGHT)

vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
bg = pg.image.load("desser.jpg")
bg = pg.transform.scale(bg, (VINDU_BREDDE,VINDU_HOYDE))
aim = pg.image.load("sniper_aim.png").convert_alpha()
aim = pg.transform.scale(aim, (AIM_DIAMETER,AIM_DIAMETER))
badGuy = pg.image.load("badGuy.png").convert_alpha()
badGuy = pg.transform.scale(badGuy, (BADGUY_WIDTH*(BADGUY_y-HORISONT)*BADGUY_SCALE,BADGUY_HEIGHT*(BADGUY_y-HORISONT)*BADGUY_SCALE))

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)
#################### INIT ########################

#################### /INIT ########################

fortsett = True
pos =(0,0)
shot_pos =(0,0)
hit_count = 0

while fortsett:
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
        if event.type == pg.MOUSEMOTION:
            pos = pg.mouse.get_pos()
        elif event.type == pg.MOUSEBUTTONDOWN:
            button = event.button # Hent knappen som ble trykket på
            shot_pos = pg.mouse.get_pos() # Hent musposisjonen

    # Farger bakgrunnen hvit
    vindu.fill((255, 255, 255))

#################### Spillogikk ########################
    vindu.blit(bg, (0, 0))
    badGuy = pg.image.load("badGuy.png").convert_alpha()
    badGuy = pg.transform.scale(badGuy, (BADGUY_WIDTH*(BADGUY_y-HORISONT)*BADGUY_SCALE,BADGUY_HEIGHT*(BADGUY_y-HORISONT)*BADGUY_SCALE))
    vindu.blit(badGuy, (BADGUY_x,BADGUY_y))
    print(BADGUY_x,BADGUY_y)
    vindu.blit(aim, (pos[0]-AIM_DIAMETER/2,pos[1]-AIM_DIAMETER/2))
    if hit_encounter(shot_pos, BADGUY_x, BADGUY_y, BADGUY_WIDTH*(BADGUY_y-HORISONT)*BADGUY_SCALE, BADGUY_HEIGHT*(BADGUY_y-HORISONT)*BADGUY_SCALE):
        hit_count +=1
        BADGUY_x = random.randint(0,VINDU_BREDDE-BADGUY_WIDTH)
        BADGUY_y = random.randint(HORISONT,VINDU_HOYDE-BADGUY_HEIGHT*3)

    text = font.render(f"Hits: {hit_count}",True, (255, 255, 255))
    vindu.blit(text, (10, 10)) # Skriv ut teksten på skjermen

#################### /Spillogikk ########################

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()


