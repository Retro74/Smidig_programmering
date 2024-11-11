from pathlib import Path
import re
from itertools import chain
fileName = 'Miljøutfordringer er et av vår tids.txt' 
filePath = Path(__file__).resolve().parent
fullPath =f"{filePath}\{fileName}"
fileData =[]
with open(fullPath, encoding="utf8") as fil:
    for linje in fil:
        tmp_linje = linje.lower().strip().split(" ") 
        for i in range(len(tmp_linje)):
            tmp_linje[i] = re.sub(r'[^a-zA-Z0-9æøåÆØÅ\s]', '', tmp_linje[i])
        fileData.append(tmp_linje)
fileData = list(chain.from_iterable(fileData))
print(len(fileData))

ordliste = {}
for ord in fileData:
    if ord in ordliste:
        ordliste[ord]+=1
    else:
        ordliste[ord]=1

ordliste = dict(sorted(ordliste.items(),reverse=True, key=lambda item: item[1]))
print(ordliste)