import pygame as pg
import random as rd
from Card import Card

def dealCards():
    # Tegn kortet på skjermen
    for i in range(5):
        card_surface, card_rect = cards[i].draw()
        vindu.blit(card_surface, card_rect)
def cardValueInBlackJack(kortverdi):
    kortverdi = kortverdi %13
    return kortverdi if 0 < kortverdi < 10 else 10

def cardValue(kortverdi):
    return kortverdi % 13 if kortverdi % 13 != 0 else 13

def cardColor(kortverdi):
    if kortverdi<14:
        return "Klubbs"
    elif kortverdi<27:
        return "Dimonds"
    elif kortverdi<40:
        return "Hearts"
    else:
        return "Spades"


# Initialiser Pygame
pg.init()
font = pg.font.SysFont("Arial", 24)

# Opprett et vindu
width = 900
height = 490
zoom = 1.5
vindu = pg.display.set_mode((width*zoom , height*zoom ))
table = pg.image.load("table.png").convert_alpha()
table = pg.transform.scale(table, (width*zoom ,height*zoom ))

# Last inn bilder for kortet
back_image = pg.image.load("cards/0.png")
cardWidth = 50 * zoom
cardHeight = 70* zoom
cardPositioning = [
    {"x_pos":185*zoom , "y_pos":236*zoom , "rotation":-62},
    {"x_pos":300*zoom , "y_pos":320*zoom , "rotation":-23},
    {"x_pos":450*zoom , "y_pos":350*zoom , "rotation":0},
    {"x_pos":600*zoom , "y_pos":320*zoom , "rotation":23},
    {"x_pos":715*zoom , "y_pos":235*zoom , "rotation":62}
]

cards = []
dealedCards = []
for i in range(5):
    cardnumber = rd.randint(1,53)
    while cardnumber in dealedCards:
        cardnumber = rd.randint(1,53)
    dealedCards.append(cardnumber)
    # Opprett et kortene
    front_image = pg.image.load("cards/" + str(cardnumber) + ".png")
    cards.append(
        Card(
            front_image,                    back_image,
            cardValue(cardnumber),          cardColor(cardnumber),
            x=cardPositioning[i]["x_pos"],  y=cardPositioning[i]["y_pos"],
            width=cardWidth,                height=cardHeight,
            rotation=cardPositioning[i]["rotation"])
    )

# Oppdater skjermen
#pg.display.update()
sum = 0

fortsett = True
while fortsett:
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
    # Farger bakgrunnen hvit
#    vindu.fill((255, 255, 255))


#################### Spillogikk ########################
        elif event.type == pg.MOUSEBUTTONDOWN:
            button = event.button # Hent knappen som ble trykket på
            pos = pg.mouse.get_pos() # Hent musposisjonen
            for i in range(5):
                if cards[i].is_clicked(pos):
                    sum += 0 if cards[i].is_up else cardValueInBlackJack(cards[i].value)
                    cards[i].flip()
    sum_display = font.render(str(sum), True, (255, 255, 255))
    vindu.fill((0,0,0))
    vindu.blit(table,(0,0))
    dealCards()
    vindu.blit(sum_display, (400, 20))


#################### /Spillogikk ########################

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
