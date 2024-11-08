import matplotlib.pyplot as plt 
from pathlib import Path
fileName = 'standpunktskarakterer_R1.csv' 
filePath = Path(__file__).resolve().parent
fullPath =f"{filePath}\{fileName}"
fileData =[]
##
kar_frekvens = {1:0,2:0,3:0,4:0,5:0,6:0}
with open(fullPath, encoding="utf8") as fil:
    overskrift = fil.readline().strip().split(",")
    for linje in fil:
        tmp_linje = linje.strip().split(",")
        tmp_linje[-1] = int(tmp_linje[-1])
        kar_frekvens[tmp_linje[-1]]+=1
        fileData.append(tmp_linje)

##Lager en ordbok med relative frekvenser
kar_rel_frekvens = {}
antall_elever = sum(kar_frekvens.values())
for karakter, antall in kar_frekvens.items():
    kar_rel_frekvens[karakter] = antall / antall_elever

print(kar_frekvens)
print(kar_rel_frekvens)
#print(sum(frekvenser))
#plt.bar(kar_frekvens.keys(), kar_frekvens.values())
plt.pie(kar_frekvens.values(), labels=kar_frekvens.keys())
plt.show()
