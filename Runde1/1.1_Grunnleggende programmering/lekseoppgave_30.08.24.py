maaneder = "JanFebMarAprMaiJunJulAugSepOktNovDes"

#Henter inn månednummer fra bruker 
maaned_nummer_input = input("Skriv inn ett månednummer (1-12): ")
#Tar vare på det orginale input
maaned_nummer = maaned_nummer_input

if maaned_nummer.isnumeric():
    #Det er et tall fra brukeren
    #Gjør det som er skrevet inn om til et tall og trekker fra 1 siden vi starter å telle på 0
    maaned_nummer = int(maaned_nummer )-1
    if 0<=maaned_nummer <=11:
        maaned_nummer*=3
        print(f"Måned nummer {maaned_nummer_input} kan forkortet skrives som {maaneder[maaned_nummer:maaned_nummer+3]}")
    else:
        #Ikke et gyldig månednummer
        print(f"Ikke et gyldig tall mellom 1-12: {maaned_nummer_input}" )        
else:
    #Ikke et tall fra brukeren
    print(f"Dette er ikke et tall: {maaned_nummer_input}")