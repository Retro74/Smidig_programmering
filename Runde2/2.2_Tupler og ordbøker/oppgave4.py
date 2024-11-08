from pathlib import Path
fileName = 'standpunktskarakterer_R1.csv' 
filePath = Path(__file__).resolve().parent
fullPath =f"{filePath}\{fileName}"
fileData =[]
frekvenser = [0]*6
karakterer = [1,2,3,4,5,6]
with open(fullPath, encoding="utf8") as fil:
    overskrift = fil.readline().strip().split(",")
    for linje in fil:
        tmp_linje = linje.strip().split(",")
        tmp_linje[-1] = int(tmp_linje[-1])
        frekvenser[tmp_linje[-1]-1]+=1
        fileData.append(tmp_linje)

print(frekvenser)
print(sum(frekvenser))
#print(fileData)

