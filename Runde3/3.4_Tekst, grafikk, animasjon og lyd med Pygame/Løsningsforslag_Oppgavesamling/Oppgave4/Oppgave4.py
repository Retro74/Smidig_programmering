import pygame as pg
import keyboard
# Initialiserer/starter pygame
pg.init()
# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

controllKeysDict ={39:{"left shift": "*", "left ctrl": "", "right ctrl": "", "left alt": "", "right alt": ""},
                   43:{"left shift":"?", "left ctrl":"", "right ctrl":"", "left alt":"", "right alt":""},
                   44:{"left shift":";", "left ctrl":"", "right ctrl":"", "left alt":"", "right alt":""},
                   45:{"left shift":"_", "left ctrl":"", "right ctrl":"", "left alt":"", "right alt":""},
                   46:{"left shift":":", "left ctrl":"", "right ctrl":"", "left alt":"", "right alt":""},
                   48:{"left shift":"=", "left ctrl":"}", "right ctrl":"", "left alt":"", "right alt":""},
                   49:{"left shift":"!", "left ctrl":"", "right ctrl":"", "left alt":"", "right alt":""},
                   50:{"left shift":"\"", "left ctrl":"@", "right ctrl":"", "left alt":"", "right alt":""},
                   51:{"left shift":"#", "left ctrl":"£", "right ctrl":"", "left alt":"", "right alt":""},
                   52:{"left shift":"¤", "left ctrl":"$", "right ctrl":"", "left alt":"", "right alt":""},
                   53:{"left shift":"%", "left ctrl":"€", "right ctrl":"", "left alt":"", "right alt":""},
                   54:{"left shift":"&", "left ctrl":"", "right ctrl":"", "left alt":"", "right alt":""},
                   55:{"left shift":"/", "left ctrl":"{", "right ctrl":"", "left alt":"", "right alt":""},
                   56:{"left shift":"(", "left ctrl":"[", "right ctrl":"", "left alt":"", "right alt":""},
                   57:{"left shift":")", "left ctrl":"]", "right ctrl":"", "left alt":"", "right alt":""},
                   60:{"left shift":">", "left ctrl":"}", "right ctrl":"", "left alt":"", "right alt":""},
                   92:{"left shift":"`", "left ctrl":"´", "right ctrl":"", "left alt":"", "right alt":""},
                   124:{"left shift":"§", "left ctrl":"", "right ctrl":"", "left alt":"", "right alt":""},
                   }

controllKeysStates = {"left shift":False, "right shift":False,  "left ctrl":False, "left alt":False, "right alt":False, "right ctrl":False}


# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)
brukerTekst = [""]
currentLine =0
cursorPos = 0
fortsett = True
while fortsett:
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

        if event.type == pg.KEYDOWN:
            key_name = pg.key.name(event.key) # Hent navnet på tasten
            if key_name =="": ## Som ved ÆØÅ
                key_name = keyboard.read_key()
            print(key_name)
            if len(key_name) ==1:
                print(ord(key_name))
#            print("Shift settes fra", controllKeysStates[key_name])
            if controllKeysStates.get(key_name)==False:
                controllKeysStates[key_name]=True
#                print("Shift settes til", controllKeysStates[key_name])
                break

            if key_name == "space":
                key_name =" "

            if key_name == "backspace":
                if brukerTekst[currentLine]== "" and currentLine>0:
                    #Hvis tom inje, men ikke på første,--> fjern linjen
                    brukerTekst.pop(currentLine)
                    currentLine-=1
                    cursorPos=len(brukerTekst[currentLine])
                else:
                    #Hvis linjen ikke er tom og ikke å første linje
                    #--> Trekk linjen opp på den over
                    if cursorPos==0 and currentLine>0:
                        cursorPos=len(brukerTekst[currentLine-1])
                        brukerTekst[currentLine-1]+= brukerTekst[currentLine]
                        brukerTekst.pop(currentLine)
                        currentLine -=1
                    else:
                        #Bare fjern ett tegn
                        brukerTekst[currentLine] = brukerTekst[currentLine][0:cursorPos-1] + brukerTekst[currentLine][cursorPos::]
                        cursorPos-=1
                break
            if key_name == "return" or key_name == "enter" :
                if currentLine == len(brukerTekst)-1 and cursorPos==len(brukerTekst[currentLine]):
                    print("Sist på siste linje")
                    #Sist på siste linje
                    currentLine+=1
                    brukerTekst.append("")
                    cursorPos=0
                elif cursorPos==len(brukerTekst[currentLine]):
                    print("Sist på en linje")
                    # Sist på linje
                    brukerTekst.insert(currentLine+1,"")
                    cursorPos=0
                    currentLine+=1
                else:
                    #Ikke sist
                    print("Ikke sist på en linje")
                    brukerTekst.insert(currentLine+1,brukerTekst[currentLine][cursorPos::])
                    brukerTekst[currentLine] = brukerTekst[currentLine][0:cursorPos]
                    cursorPos=0
                    currentLine+=1
            if key_name =="up":
                if currentLine>0:
                    currentLine-=1
                    if cursorPos> len(brukerTekst[currentLine]):
                        cursorPos = len(brukerTekst[currentLine])

            if key_name =="down":
                if currentLine < len(brukerTekst)-1:
                    currentLine+=1
                    if cursorPos> len(brukerTekst[currentLine]):
                        cursorPos = len(brukerTekst[currentLine])
            if key_name == "left":
                if cursorPos>0:
                    cursorPos -=1
                elif currentLine>0:
                    currentLine-=1
                    cursorPos=len(brukerTekst[currentLine])
            if key_name == "right":
                if cursorPos<len(brukerTekst[currentLine]):
                    cursorPos +=1
                elif currentLine<len(brukerTekst):
                    currentLine+=1
                    cursorPos=0

            if "[" in key_name:
                key_name=key_name.replace("[", "").replace("]","")

            if len(key_name)>1:
                print("Stops: ", key_name)
                break
#            print("Tester for:", key_name, "Med order:" , ord(key_name))
#            print("Skulle bli:", shiftCtrlKeyDict[ord(key_name)]["left shift"] , " Siden shift er: ", controllKeysStates["left shift"])

            if controllKeysDict.get(ord(key_name)) and controllKeysStates["left shift"]:
                key_name= controllKeysDict[ord(key_name)]["left shift"]
            if controllKeysDict.get(ord(key_name)) and controllKeysStates["left ctrl"]:
                key_name= controllKeysDict[ord(key_name)]["left  ctrl"]

            if controllKeysStates["left shift"]:
                key_name=key_name.upper()


            brukerTekst[currentLine] =  brukerTekst[currentLine][0:cursorPos] + key_name + brukerTekst[currentLine][cursorPos::]

            cursorPos+=1

        if event.type == pg.KEYUP:
            key_name = pg.key.name(event.key) # Hent navnet på tasten
            if controllKeysStates.get(key_name):
                controllKeysStates[key_name]=False


     # Lag tekstobjektet
    vindu.fill((0, 0, 0)) # Fyll skjermen med svart
    for i in range(len(brukerTekst)):
        if i == currentLine:
            tekstlinje =font.render(brukerTekst[i][0:cursorPos] + "|" + brukerTekst[i][cursorPos::], True, (255, 255, 255))
            vindu.blit(tekstlinje, (100, 25*(i+1)))
        else:
            vindu.blit(font.render(brukerTekst[i], True, (255, 255, 255)), (100, 25*(i+1))) # Skriv ut teksten på skjermen

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
