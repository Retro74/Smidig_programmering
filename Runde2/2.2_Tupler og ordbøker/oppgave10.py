from pathlib import Path
import re
from itertools import chain
fileName = 'Miljøutfordringer er et av vår tids.txt' 
filePath = Path(__file__).resolve().parent
fullPath =f"{filePath}\\{fileName}"

with open(fullPath, encoding="utf8") as fil:
    #Leser inn alt og splitter det i ord med små bokstaver uten linjeskift 
    data_fil = fil.read().lower().strip().split(" ")

#Gjennomløper alle ord og tar bort spesialtegn
for i in range(len(data_fil)):
    data_fil[i] = re.sub(r'[^a-zA-Z0-9æøåÆØÅ\s]', '', data_fil[i])

#print(len(data_fil))

##Oppretter ordliste for å telle antall forekomster
ordliste = {}
for ord in data_fil:
    if ord in ordliste:
        ordliste[ord]+=1
    else:
        ordliste[ord]=1

#Sorterer orlisten etter antall forekomster i synkende rekkefølge
ordliste = dict(sorted(ordliste.items(),reverse=True, key=lambda item: item[1]))
print(ordliste)