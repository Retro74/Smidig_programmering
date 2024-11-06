nesoddensBefolkning =[]
ant_Nesodden =0
ant_menn_Nesodden =0
ant_kvinner_Nesodden =0

with open("Runde1/Nesodden_2024_Alder_Ant_Menn_Kvinner.txt", encoding='utf-8') as fil:
    overskrift = fil.readline().split(";")
    for linje in fil:
        tmp = linje.split(";")
        nesoddensBefolkning.append([tmp[0].strip(), int(tmp[1].strip()), int(tmp[2].strip())]  )
        ant_menn_Nesodden +=int(tmp[1].strip())
        ant_kvinner_Nesodden += int(tmp[2].strip()) 

ant_Nesodden = ant_menn_Nesodden + ant_kvinner_Nesodden

#print(nesoddensBefolkning)
prosent_menn_nesodden = round(ant_menn_Nesodden/ant_Nesodden,2)*100
prosent_kvinner_nesodden = round(ant_kvinner_Nesodden/ant_Nesodden,2)*100
print(f"Det bor {ant_Nesodden} på Nesodden. Menn utgjør {prosent_menn_nesodden} %, kvinner utgjør {prosent_kvinner_nesodden} %.")

sum = 0
teller = 0
for rad in nesoddensBefolkning:
    sum += rad[1]+ rad[2]
    if (teller) % 10 == 9:
        print("Aldersgruppen", teller-9, "-", teller , "år :", sum)
        #print(rad[0]) #Sjekker at det tar siste i hver gruppe, X9 år
        sum = 0
    teller+=1
print("Aldersgruppen", 100, "-", 110 , "år :", sum)

    


