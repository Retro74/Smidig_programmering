import pygame as pg
pg.init()

VINDU_BREDDE = 600
VINDU_HOYDE = 700
FPS = 60

klokke = pg.time.Clock()
#font = pg.font.SysFont("Arial", 24)
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
x_pos_ball = 30
ball_motHoyre = True
ball_radius = 30

kjorer = True
while kjorer:
    klokke.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            kjorer = False
    ### Tegne ting på vinduet  ###
    if x_pos_ball > VINDU_BREDDE-ball_radius:
        ball_motHoyre = False
    
    if x_pos_ball < 0+ball_radius:
        ball_motHoyre = True
        
    if ball_motHoyre:
        x_pos_ball += 3
    else:
        x_pos_ball -= 3


    
    vindu.fill((0,0,0))
    pg.draw.circle(vindu, (255, 0, 0), (x_pos_ball, 250), ball_radius)

    pg.display.flip() #tegn det som skal være på vinduet på vinduet/skjermen.
    
pg.quit()

