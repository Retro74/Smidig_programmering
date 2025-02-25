import pygame as pg
pg.init()

VINDU_BREDDE = 600
VINDU_HOYDE = 700
FPS = 60

klokke = pg.time.Clock()
font = pg.font.SysFont("Arial", 24)
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

kjorer = True
while kjorer:
    klokke.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            kjorer = False
    ### Tegne ting på vinduet  ###
    vindu.fill((255, 255, 255))

    bilde = font.render("Hei på deg!", True, (50, 50, 50))
    vindu.blit(bilde, (200, 400))

    pg.draw.circle(vindu, (255, 0, 0), (150, 250), 30)
    pg.draw.circle(vindu, (0, 255, 0), (250, 350), 35)
    pg.draw.circle(vindu, (255, 255, 0), (450, 150), 45)

    pg.draw.rect(vindu, (129,33,89), (320,250, 50, 180))
    pg.draw.ellipse(vindu, (11,222,78), (320,250, 50, 180))
    pg.draw.line(vindu, (111,33, 189), (0, VINDU_HOYDE), (VINDU_BREDDE, 0), 5)



    pg.display.flip() #tegn det som skal være på vinduet på vinduet/skjermen.
    
pg.quit()

