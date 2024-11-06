
#Oppretet liste
bilmerker = ["Volvo", "Tesla", "BMW", "Audi"]


#print(bilmerker[::-1])

#Legge til elementer
bilmerker.append("VW")
bilmerker.insert(1,"Toyota")
bilmerker.extend(["Mazda", "Fiat", "Ford"])

#print(bilmerker)

#Fjeren bassert på verdi
#bilmerker.remove("BMW")
#print(bilmerker)

#Fjeren bassert på index
#bilmerker.pop(1)
#print(bilmerker)

#Fjerne flere elementer fra listen
#del bilmerker[3:]
#print(bilmerker)

#sok_bilmerke = input("Skriv inn et bilmerke: ")

#if sok_bilmerke in bilmerker:
#    print(f"Vi har {sok_bilmerke} i listen.")
#else:
#    bilmerker.append(sok_bilmerke)
#    print (f'Vi har ikke {sok_bilmerke} i listen men har lagt den til. Takk')


#print(bilmerker)
#bilmerker.sort()
#bilmerker.reverse()
#print(sorted(bilmerker))
#print(bilmerker)

#variabel_1 = "Roger"
#variabel_2 = variabel_1
#variabel_1 = "Stian"
#print(variabel_1)
#print(variabel_2)
#print(bilmerker)
#kopi_bilmerker = bilmerker
#print(kopi_bilmerker)
#bilmerker.pop(-1)
#print(bilmerker)
#print(kopi_bilmerker)


#tallListe = list(range(3,31,3))
#tallListe.insert(3,65)
#tallListe.insert(6,2)
#tallListe[4]=17
#tallListe[6]=17
#tallListe[7]=17
#print(tallListe)
#print(f"max: {max(tallListe)}")
#print(f"min: {min(tallListe)}")
#print(f"sum: {sum(tallListe)}")
#
#from statistics import mean, median, mode
#print(f"gjennomsnitt: {mean(tallListe)}")
#print(f"median: {median(tallListe)}")
#print(f"typetall: {mode(tallListe)}")


#for bilmerke in bilmerker[::-1]:
#    print(f"Undersøker: {bilmerke}")
#    if bilmerke == "BMW":
#        bilmerker.remove(bilmerke)
#print(bilmerker)



bilmerker = [   ["Volvo", "CX90", "ex30", "ex40"], 
                ["Tesla", "Modell 3", "Modell Y", "Modell X"], 
                ["Toyota", "Supra", "Corolla", "RAV4"], 
                ["Nissan", "X-trail", "Leaf", "Arya", "Yaris"]]

#print(bilmerker[1][0])

for merke_modell in bilmerker:
    print(f"{merke_modell[0]}: ", end="")
    for modell in merke_modell[1:]:
        print(f"{modell}, ", end="")
    print("")


