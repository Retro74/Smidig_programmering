import kontakter as kontaktfil
app_modes = {"a": "Søke etter en kontakt med et gitt navn",
             "b": "Søke etter kontakter med navn som starter på en gitt kombinasjon",
             "c": "Søke etter kontakter med navn som inneholder en gitt bokstavkombinasjon",
             "d": "Søke etter kontakter etter nasjonalt telefonnummer",
             "e": "Søke opp kontakter som er en gitt alder, eldre eller yngre enn en gitt verdi"}
#print(kontaktfil.kontakter)
def sok_navn(): #a
    navn = input("Hvilket navn vil du søke etter? ")
    for kontakt in kontaktfil.kontakter:
        if kontakt["navn"] == navn: 
            print(f"Vi fant {kontakt["navn"]}, {kontakt["alder"]} år, med tlfnr. {kontakt["telefonnummer"]}")

def sok_navn_start(): #b
    navn = input("Hvilket navn som starter med vil du søke etter? ")
    for kontakt in kontaktfil.kontakter:
        if kontakt["navn"][:len(navn)] == navn: 
            print(f"Vi fant {kontakt["navn"]}, {kontakt["alder"]} år, med tlfnr. {kontakt["telefonnummer"]}")

def sok_navn_med(): #c
    navn = input("Hvilket navn som starter med vil du søke etter? ")
    for kontakt in kontaktfil.kontakter:
        if navn in kontakt["navn"]: 
            print(f"Vi fant {kontakt["navn"]}, {kontakt["alder"]} år, med tlfnr. {kontakt["telefonnummer"]}")

def sok_telefonnummer_nasjon(): #d
    nasjoner_antall = {}
    for kontakt in kontaktfil.kontakter:
        kontakt_tlf_prefiks = kontakt["telefonnummer"][:3]
        if kontakt_tlf_prefiks in nasjoner_antall:
            nasjoner_antall[kontakt_tlf_prefiks]+=1
        else:
            nasjoner_antall[kontakt_tlf_prefiks]=1

    for nokkel, verdi in nasjoner_antall.items():
        print(f"Det finnes {verdi} kontakter med telefonnumer {nokkel}")
    tlfstart = input("Hvilke kontakter vil du se? (skriv en av de ovenfor)")
    for kontakt in kontaktfil.kontakter:
        if kontakt["telefonnummer"][:3]==tlfstart:
            print(f"Vi fant {kontakt["navn"]}, {kontakt["alder"]} år, med tlfnr. {kontakt["telefonnummer"]}")
def sok_alder():
    alder = input("Skriv inn øvre og nedre alder for kontakter du vil se. eks. 33-36: ").split("-")
    for kontakt in kontaktfil.kontakter:
        if kontakt["alder"]>= int(alder[0]) and kontakt["alder"]<= int(alder[1]): 
            print(f"Vi fant {kontakt["navn"]}, {kontakt["alder"]} år, med tlfnr. {kontakt["telefonnummer"]}")

while True:
    print("Velg:")
    for nokkel , verdi in app_modes.items():
          print(f"{nokkel}) {verdi}")    
    valg = input()
    if valg in app_modes:
        print(f"Du valgte: {app_modes[valg]}")
    elif valg == "":
        print("Avslutter")
        break
    else:
        print("Feil valg. Prøv igjen")

    if valg == "a":
        sok_navn()
    elif valg == "b":
        sok_navn_start()
    elif valg == "c":
        sok_navn_med()
    elif valg == "d":
        sok_telefonnummer_nasjon()
    elif valg == "e":
        sok_alder()

    