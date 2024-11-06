nedboerNesooden = []
with open("Runde1/Nedbør_Nesodden_2015-2024.txt", encoding='utf-8') as fil:
    overskrift = fil.readline().split(";")
    for linje in fil:
        tmp = linje.strip().split(";")
        nedboerNesooden.append([tmp[0], float(tmp[1].replace(",","."))])

#print(nedboerNesooden)

##Oppgave a)
maks_nedboer =0
maks_nedboer_dato = ""
for dag in nedboerNesooden:
    if dag[1]>maks_nedboer:
        maks_nedboer=dag[1]
        maks_nedboer_dato = dag[0]

print("Nesodden hadde mest nedbør den", maks_nedboer_dato, "med", maks_nedboer, "mm nedbør")

##Oppgave b)
maks_5_dagers_nedboer = 0
maks_5_dagers_nedboer_slutt_indeks = 0
for i in range(len(nedboerNesooden)-4):
    tmp_5_dagers =0
    for j in range(5):
        tmp_5_dagers += nedboerNesooden[i+j][1]
    if (tmp_5_dagers > maks_5_dagers_nedboer):
        maks_5_dagers_nedboer =tmp_5_dagers
        maks_5_dagers_nedboer_slutt_indeks = i
print(f"5-dagersperioden med mest nedbør på Nesodden var {nedboerNesooden[maks_5_dagers_nedboer_slutt_indeks][0]}-{nedboerNesooden[maks_5_dagers_nedboer_slutt_indeks+4][0]}, med {maks_5_dagers_nedboer}mm nedbør")

##Oppgave c)
sommere=[]
sommre_nedboer=[]
for dag in nedboerNesooden:
    if ".05." in dag[0] or ".06." in dag[0] or ".07." in dag[0] or ".08." in dag[0]:
        if not dag[0][-4:] in sommere:
            sommere.append(dag[0][-4:])
            sommre_nedboer.append(dag[1])
        else:
            sommre_nedboer[-1]+=dag[1]

for i in range(len(sommere)):
    print(f"Sommeren {sommere[i]}, kom det {round(sommre_nedboer[i],0)}mm nedbør")


##Oppgave d)
mnd_aar=[]
mnd_aar_nedboer_mm=[]
for dag in nedboerNesooden:
    if not dag[0][-7:] in mnd_aar:
        mnd_aar.append(dag[0][-7:])
        mnd_aar_nedboer_mm.append(dag[1])
    else:
        mnd_aar_nedboer_mm[-1]+= dag[1]

maks_nedboar_mnd=""
maks_nedboar_mnd_mm=0

for i in range(len(mnd_aar)):
    if mnd_aar_nedboer_mm[i]>maks_nedboar_mnd_mm:
        maks_nedboar_mnd_mm=mnd_aar_nedboer_mm[i]
        maks_nedboar_mnd = mnd_aar[i]
    
print(f"{maks_nedboar_mnd} er den måneden med mest nedbør, med {round(maks_nedboar_mnd_mm,0)} mm nedbør")


##Oppgave f)
maks_torkeperiode_start=""
torkeperiode_start=""
maks_torkeperiode_sutt=""
torkeperiode_sutt=""
maks_torkeperiode_lengde =0
toerkeperiode_teller = 0

for dag in nedboerNesooden:   
    if dag[1]==0:
        if toerkeperiode_teller==0:
            torkeperiode_start=dag[0];
        toerkeperiode_teller+=1
        torkeperiode_sutt=dag[0]
    else:
        if toerkeperiode_teller>maks_torkeperiode_lengde:
            maks_torkeperiode_lengde=toerkeperiode_teller
            maks_torkeperiode_start=torkeperiode_start
            maks_torkeperiode_sutt=torkeperiode_sutt
        toerkeperiode_teller=0

print(f"Den lengste tørkeperioden opplevde Nesodden fra {maks_torkeperiode_start} til {maks_torkeperiode_sutt}, den varte i {maks_torkeperiode_lengde} dager.")