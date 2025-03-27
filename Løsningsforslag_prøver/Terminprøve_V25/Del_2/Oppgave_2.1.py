from pathlib import Path
fileName = 'offentlige_utgifter.csv'
pyFilePath = Path(__file__).resolve().parent
fullFilePath = pyFilePath.joinpath(fileName)

##Henter ut data fra fil til listen fileData
fileData = []
with open(fullFilePath, encoding="utf-8") as fil:
    for linje in fil:
        tmp_linje = linje.strip().split(";")
        for i in range(len(tmp_linje)):
            if i>0:
                tmp_linje[i] = int(tmp_linje[i])
        fileData.append(tmp_linje)

## Henter ut et gyldig årstall fra brukeren
while True:
    try:
        aar = 2020 #int(input(f"Skriv inn ett år mellom {fileData[0][1]}-{fileData[0][-1]}: "))
        if int(fileData[0][1]) <= aar <= int(fileData[0][-1]):
            print(f"Henter ut informasjonen fra {aar}")
            break
        else:
            print("Ugyldig år")
    except:
        print("Skriv året på nytt")

##Finner hvilken index årstallet har    
aar_index = aar - fileData[0][1] + 1

## Tar ut totalkostnader for dette året 
total = fileData[1][aar_index]

## Klargjør for utsrifts-liste
utskrift = []
for i in range(1, len(fileData)):
    utskrift.append([fileData[i][0], fileData[i][aar_index]])

## Sorterer utskiften bassert på verdein i kolonne index 1
utskrift.sort(reverse=True, key = lambda utgift: utgift[1])

##Skriver ut den sorterte listen inkl en prosent-kolonne
for i in range(1, len(utskrift)):
    print(f'{utskrift[i][0]:40}: {utskrift[i][1]:7} mill. kr. som utgjør {utskrift[i][1]*100/total:.2f}% \t av utgiftene')


## Lager et diagram to lister ett med hvert formål
import matplotlib.pyplot as plt
formaal =[]
pietall = []
for i in range(2,len(fileData)):
    formaal.append(fileData[i][0])
    pietall.append(fileData[i][aar_index])

## Lager og viser diagrammet med data fra listene
plt.pie(pietall, labels=formaal, autopct='%1.1f%%', startangle=20) #
plt.title(f"Offentlige utgifter for {aar} i millioner kroner")
plt.show()
