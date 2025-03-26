from pathlib import Path
fileName = 'offentlige_utgifter.csv'
pyFilePath = Path(__file__).resolve().parent
fullFilePath = pyFilePath.joinpath(fileName)
fileData = []
with open(fullFilePath, encoding="utf-8") as fil:
    for linje in fil:
        tmp_linje = linje.strip().split(";")
        for i in range(len(tmp_linje)):
            if i>0:
                tmp_linje[i] = int(tmp_linje[i])
        fileData.append(tmp_linje)


while True:
    try:
        aar = 2020 #int(input(f"Skriv inn ett år mellom {fileData[0][1]}-{fileData[0][-1]}: "))
        if fileData[0][1] <= aar <= fileData[0][-1]:
            break
        else:
            print("Ugyldig år")
    except:
        print("Skriv året på nytt")
    
aar_index = aar - fileData[0][1] + 1

total = fileData[1][aar_index]
utskrift = []
for i in range(1, len(fileData)):
    utskrift.append([fileData[i][0], fileData[i][aar_index]])

utskrift.sort(reverse=True, key = lambda utgift: utgift[1])

for i in range(1, len(utskrift)):
    print(f'{utskrift[i][0]:40}: {utskrift[i][1]:7} mill. kr. som utgjør {utskrift[i][1]*100/total:.2f}% \t av utgiftene')

import matplotlib.pyplot as plt
formaal =[]
pietall = []
for i in range(2,len(fileData)):
    formaal.append(fileData[i][0])
    pietall.append(fileData[i][aar_index])

plt.pie(pietall, labels=formaal, autopct='%1.1f%%') #
plt.title(f"Offentlige utgifter for {aar} i millioner kroner")
plt.show()
