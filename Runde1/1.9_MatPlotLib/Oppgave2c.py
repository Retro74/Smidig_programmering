import matplotlib.pyplot as plt
#import pandas as pd
farger = ['#f3f3f3', '#e8e8e8', '#dddddd', '#d2d2d2', '#c7c7c7','#bfbfbf', 
 '#bcbcbc', '#b1b1b1', '#a6a6a6', '#9b9b9b', '#909090', '#858585', 
 '#797979', '#6e6e6e', '#636363', '#585858', '#4d4d4d', '#424242', 
 '#373737', '#2c2c2c', '#212121', '#161616','#090909', '#0b0b0b', '#000000']


months = ["Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Des"]
#vaerdata = pd.read_csv("Runde1/1.9_MatPlotLib/vaerdata.csv")
vaerdata =[]
with open("Runde1/1.9_MatPlotLib/vaerdata.csv") as fil:
    for linje in fil:
        tmp_linje = linje.strip().split(";")
        for i in range(len(tmp_linje)):
            if i == 0:
                tmp_linje[i] = int(tmp_linje[i])
            else:
                tmp_linje[i] =  float(tmp_linje[i])
        vaerdata.append(tmp_linje)
print(vaerdata)

for i in range(len(vaerdata)):
    plt.plot(months, vaerdata[i][1:], color=farger[i], label= vaerdata[i][0]) # blir mye...
    

plt.xlabel("Måneder")
plt.ylabel("Temperatur (C)")
plt.title(f"Gjennomsnittlig temperatur i Oslo gjennom årene  {vaerdata[-1][0]}-{vaerdata[0][0]}")

#d)
gjenomsnittMndTemp = [0]*12
for aar in vaerdata:
    for i in range(1, len(aar)):
        gjenomsnittMndTemp[i-1]+=aar[i]/len(vaerdata)


plt.plot(months, gjenomsnittMndTemp, color="red", label="Gjennomsnitt")

plt.gca().set_facecolor("#bbbbff")

plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0.)

plt.show()

