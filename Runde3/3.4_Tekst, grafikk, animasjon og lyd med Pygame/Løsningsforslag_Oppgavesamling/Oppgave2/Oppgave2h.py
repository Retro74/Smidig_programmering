import pygame as pg
from tkinter import *
from tkinter import simpledialog

VINDU_BREDDE = 500
VINDU_HOYDE  = 500
tegne_radius = 3
farger = {"r":(255,0,0), "b":(0,0,255), "g":(0,255,0), "y":(255,255,0), "t":(0,255,255), "p":(255,0,255), "d":(0,0,0)}
valgtFarge = farger["b"]

#################### INIT ########################
# Initialiserer/starter pygame
pg.init()
# Oppretter et vindu der vi skal "tegne" innholdet vårt
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

vindu.fill((255,255,255))
#################### /INIT ########################
fortsett = True
tegn = False
while fortsett:
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

#################### Spillogikk ########################
        if event.type == pg.KEYDOWN:
            key_name = pg.key.name(event.key) # Hent navnet på tasten
            if farger.get(key_name):
                valgtFarge=farger[key_name]
            elif key_name=="s":
                Tk().wm_withdraw()
                answer = simpledialog.askstring("Input", "Lagre bildet som?")
                if answer:
                    while answer.strip() == "":
                        answer = simpledialog.askstring("Input", "Lagre bildet som?")
                    pg.image.save(vindu, answer +'.jpeg')
            elif key_name=="c":
                vindu.fill((255,255,255))
        if event.type == pg.MOUSEBUTTONDOWN:
            tegn = True
        if event.type == pg.MOUSEBUTTONUP:
            tegn=False
        if event.type == pg.MOUSEMOTION and tegn:
            pos = pg.mouse.get_pos() # Hent musposisjonen
            pg.draw.circle(vindu, valgtFarge, pos, tegne_radius)

#################### /Spillogikk ########################

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
