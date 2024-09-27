
videregaandeskoler =[]
sumEleverAkerhusVGS=0
storsteSkole = ""
ant_storsteSkole = 0
with open("Runde1/AkershusVGS_23-24.txt", encoding='utf-8') as fil:
    for linje in fil:
        tmp = linje.split(";")
        videregaandeskoler.append([tmp[0], int(tmp[1])])
        sumEleverAkerhusVGS += int(tmp[1])
        if int(tmp[1]) > ant_storsteSkole:
             ant_storsteSkole = int(tmp[1])
             storsteSkole =  tmp[0]

sortertListe = sorted(videregaandeskoler,key=lambda l:(l[1]))[::-1][:5]

#print(sortertListe)
#print(videregaandeskoler)
print(f"Det går {sumEleverAkerhusVGS} elever på VGS skolene i Akershus.")
print(f"Den største VGS i Akershus er {storsteSkole}, med {ant_storsteSkole} elever.")
print(f"De 5 største VGS i Akershus er:")

for skole in sortertListe:
    print(f"{skole[0]} - {str(skole[1])} elever.")
