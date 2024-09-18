## Hovedliste over bilmerker og modeller ("Database")
bilmerker_modeller = [["Volvo", "CX90", "ex30", "ex40"],
            ["Tesla", "Modell 3", "Modell Y", "Modell X"],
            ["Toyota", "Supra", "Corolla", "RAV4"],
            ["Nissan", "X-trail", "Leaf", "Arya", "Yaris"]]

##Legge inn elementer i listen, inntil brukeren skriver "q"
brukerinput_merke_modell = input("Skriv inn ett bilmerke eller bilmodell (q=quit): ")
while brukerinput_merke_modell != "q":
    funnet = False
    for merke_modell in bilmerker_modeller:
        #Finne ut om det som er skrevet inn finnes som merke eller modell
        if  brukerinput_merke_modell == merke_modell[0]:
            ##Funnet som merke
            print(f"Bilmerket, {brukerinput_merke_modell} er registert i listen, med {len(merke_modell)-1} modeller.")
            funnet=True
        elif brukerinput_merke_modell in merke_modell:
            ##Funnet som modell
            print(f"{merke_modell[0]}, er registert med bilmodellen {brukerinput_merke_modell}, i listen.") 
            funnet=True
    
    if not funnet:
        er_merke = input(f"Er {brukerinput_merke_modell} et bilmerke (Skriv 1) eller en modell (Skriv 2)? ")=="1"
        if er_merke:
            ##Hvis ikke funnet i listen, men er et merke legg det inn
            bilmerker_modeller.append([brukerinput_merke_modell])
            print(f"Bilmerket: {brukerinput_merke_modell} er lagt inn med 0 modeller.")
        else:
            ##Hvis ikke funnet i listen, men er en modell. 
            # Spør om merke og legg inn som eksisterende merke eller merke og modell.
            brukerinput_merke = input(f"Hvilket bilmerke er {brukerinput_merke_modell}? ")
            merke_funnet = False
            #Sjekke om det merket brukeren har skrevet inn finnes
            for merke_modell in bilmerker_modeller:
                if merke_modell[0]==brukerinput_merke:
                    merke_funnet=True
                    merke_modell.append(brukerinput_merke_modell)
                    print(f"Bilmerket: {brukerinput_merke}, modell {brukerinput_merke_modell} er registert i listen, med {len(merke_modell)-1} modeller.")
                    break
            if not merke_funnet:    
                bilmerker_modeller.append([brukerinput_merke, brukerinput_merke_modell])
                print(f"Bilmerket {brukerinput_merke}, modell {brukerinput_merke_modell} er registert, med 1 modell.")

    brukerinput_merke_modell = input("Skriv inn ett bilmerke eller bilmodell (q=quit): ")

### Utskrift og beregninger
antall_modeller = 0
for merke_modell in bilmerker_modeller:
    antall_modeller+=len(merke_modell)-1
    print(f"{merke_modell[0]}: ", end="")
    for merke in merke_modell[1:]:
        print(f"{merke}, ", end="") 
    print("")

print(f"Det er registert {len(bilmerker_modeller)} bilmerker og {antall_modeller} modeller i listen")