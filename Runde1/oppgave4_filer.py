videregaandeskoler = []
with open("Runde1/AkerhusVGS_22-23_og_23-24.txt", encoding='utf-8') as fil:
    for linje in fil:
        tmp = linje.split(";")
        prosenttall = (int(tmp[2])- int(tmp[1]))/int(tmp[1])
        videregaandeskoler.append([tmp[0], int(tmp[1]), int(tmp[2]),round(prosenttall*100,1)]  )

sortertListe = sorted(videregaandeskoler,key=lambda l:(l[3]))[::-1]

#print(videregaandeskoler)
print(f"Skolene emd størst øksning er:")
for skole in sortertListe:
#    print(f"{skole[0]}, med {skole[3]} % endring")
    print(f"{skole[0]}, med {skole[3]} % {'økning' if skole[3]>=0 else 'nedgang'}")