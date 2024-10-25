
with open("Rogers Øvingsoppgaver/Prøve2/Norskstil Miljøutfordringer i fremtiden.txt", encoding="utf8") as fil:
    antAvsnitt = 1
    antOrd = 0
    antTegn = 0
    antSetninger =0
    for linje in fil:
        if linje.strip() =="":
            antAvsnitt+=1
        else:
            antOrd += len(linje.split(" "))
            antTegn += len(linje.strip()) #Hvis linjeskift skal telles med, tas strip() bort
            antSetninger += len(linje.split("."))-1 #Deler opp en for mye på siste punktum


print(f'a) Antall avsnitt: {antAvsnitt}')
print(f'b) Antall ord: {antOrd}')
print(f'c) Antall tegn: {antTegn}')
print(f'd) Antall setninger: {antSetninger}')