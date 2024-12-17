from pathlib import Path
import matplotlib.pyplot as plt

#a) Denne delen av  løsningsforslaget leser inn filen i en liste med lister
print(f"\na) Leser inn data\n")

fileName = 'BeregnedeSkatterOgAvgifterPrKommuneViken2023.csv'
pyFilePath = Path(__file__).resolve().parent
fullFilePath = pyFilePath.joinpath(fileName)

list_Viken_kommuner_skatt = []
with open(fullFilePath, encoding="utf8") as fil:
    overskrift = fil.readline().strip().split(";")
    for linje in fil:
        temp_kommune = linje.strip().split(";")
        temp_kommune[1] = int(temp_kommune[1].replace(" ", "")) 
        temp_kommune[2] = int(temp_kommune[2].replace(" ", "")) 
        list_Viken_kommuner_skatt.append(temp_kommune)

#b) 
print(f"\nb) Skriver ut sortert liste\n")
list_Viken_kommuner_skatt.sort(reverse=True, key = lambda kommune: kommune[1])

print(f"{'Kommune':15}{'Skattepliktige':>20} {'Inntekter':>22}")
for kommune, antall, inntekt in list_Viken_kommuner_skatt:
    print(f"{kommune:15} {round(antall/1000,1):15.1f} k {round(inntekt/1000000,1):20.1f} mill.")


#c)
print(f"\nc) Søke-funksjon\n")
soketerm = input("Søk etter kommune: ").strip()
#soketerm = "Nes*" #Debug
print(f"Søker etter: {soketerm}")

if len(soketerm) > 0:
    if soketerm[0]==soketerm[-1]=="*":
        soketerm=soketerm[1:-1]
        for kommune, antall, skatt in list_Viken_kommuner_skatt:
            if soketerm in kommune:
                print(f"{kommune:<20} {antall:6} {skatt:15}")
    if soketerm[-1]=="*":
        #    Nes*
        soketerm=soketerm[0:-1]
        for kommune, antall, skatt in list_Viken_kommuner_skatt:
            if len(soketerm)<= len(kommune):
                if kommune[0:len(soketerm)]== soketerm:
                    print(f"{kommune:<20} {antall:6} {skatt:15}")

    elif soketerm[0]=="*":
        #    *er
        soketerm = soketerm[1:]
        for kommune, antall, skatt in list_Viken_kommuner_skatt:
            if len(soketerm)<= len(kommune):
                if kommune[-(len(soketerm)):]== soketerm:
                    print(f"{kommune:<20} {antall:6} {skatt:15}")
    
    else:
        for kommune, antall, skatt in list_Viken_kommuner_skatt:
            if kommune== soketerm:
                print(f"{kommune:<20} {antall:6} {skatt:15}")


#d)
print(f"\nd) Finner kommuner med skatte og avgifts-inntekt over: ", end="")
while True:
    try:
        skatteinntekt = int(input("Skriv inn ett skatteinntektbeløp i mill:"))*1000000
        #skatteinntekt = 100 * 1000000  #Debug
        print(f"Disse kommune har en skatte og avgiftsinntekt over {skatteinntekt/1000000:.0f} mill kr: \n")
        print(f"{'Kommune':<20}{'Skattepliktige':15}{'Skatt':>20}")
        for kommune, antall, skatt in list_Viken_kommuner_skatt:
            if skatt>= skatteinntekt:
                print(f"{kommune:<20} {round(antall/1000,1):15} k {round(skatt/1000000,1):20} mill. kr")
        break
    except:
        print("Du må skrive inn et tall")

print(f"\ne) Legger til felt i data for gjennomsnitt\n")

for i in range(len(list_Viken_kommuner_skatt)):
    list_Viken_kommuner_skatt[i].append(list_Viken_kommuner_skatt[i][2]/list_Viken_kommuner_skatt[i][1])

#print(list_Viken_kommuner_skatt)