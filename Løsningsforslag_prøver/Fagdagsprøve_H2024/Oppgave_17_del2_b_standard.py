from pathlib import Path
import matplotlib.pyplot as plt
from tkinter import *

#a)
print(f"\na) Leser inn data\n")

fileName = 'BeregnedeSkatterOgAvgifterPrKommuneViken2023.csv'
pyFilePath = Path(__file__).resolve().parent
fullFilePath = pyFilePath.joinpath(fileName)
dict_Viken_kommuner_skatt = {}

with open(fullFilePath, encoding="utf8") as fil:
    overskrift = fil.readline().strip().split(";")
    for linje in fil:
        temp_kommune = linje.strip().split(";")
        temp_kommune[1] = int(temp_kommune[1].replace(" ", "")) 
        temp_kommune[2] = int(temp_kommune[2].replace(" ", "")) 
        dict_Viken_kommuner_skatt[temp_kommune[0]]=temp_kommune[1:]
print(dict_Viken_kommuner_skatt)

print(f"\ne) Legger til felt i data for gjennomsnitt\n")

for kommune, verdier in dict_Viken_kommuner_skatt.items():
    dict_Viken_kommuner_skatt[kommune].append(dict_Viken_kommuner_skatt[kommune][1]/dict_Viken_kommuner_skatt[kommune][0])

def resulat_utskrift(kommune, antall, skatt, gjennomsnitt):
    tmp_resultat_txt = f"Kommune: {kommune}\n"
    tmp_resultat_txt+= f"Antall Skattepliktige: {round(antall/1000,1)} k\n"
    tmp_resultat_txt+= f"Skatte- og avgiftinntekter: {round(skatt/1000000, 1)} mill.\n"
    tmp_resultat_txt+= f"Gjennomsnittlig skatteinntekt pr. innbygger:{round(gjennomsnitt/1000,0):.0f}' kr\n\n"
    return tmp_resultat_txt

def sok_kommune_data():
    soketerm = entry_soketerm.get()
    resultat_txt =f"Søkeresultat for: {soketerm}\n\n"
    if len(soketerm) > 0:
        if soketerm[0]==soketerm[-1]=="*":
            soketerm=soketerm[1:-1]
            for kommune, verdi in dict_Viken_kommuner_skatt.items():
                antall, skatt, gjennomsnitt = verdi
                if soketerm in kommune:
                    resultat_txt += resulat_utskrift(kommune, antall, skatt, gjennomsnitt)

        if soketerm[-1]=="*":
            #    Nes*
            soketerm=soketerm[0:-1]
            for kommune, verdi in dict_Viken_kommuner_skatt.items():
                antall, skatt, gjennomsnitt = verdi
                if len(soketerm)<= len(kommune):
                    if kommune[0:len(soketerm)]== soketerm:
                        resultat_txt += resulat_utskrift(kommune, antall, skatt, gjennomsnitt)

        elif soketerm[0]=="*":
            #    *er
            soketerm = soketerm[1:]
            for kommune, verdi in dict_Viken_kommuner_skatt.items():
                antall, skatt, gjennomsnitt = verdi
                if len(soketerm)<= len(kommune):
                    if kommune[-(len(soketerm)):]== soketerm:
                        resultat_txt += resulat_utskrift(kommune, antall, skatt, gjennomsnitt)
     
        else:
            for kommune, verdi in dict_Viken_kommuner_skatt.items():
                antall, skatt, gjennomsnitt = verdi
                if kommune== soketerm:
                    resultat_txt += resulat_utskrift(kommune, antall, skatt, gjennomsnitt)


    lbl_resultat.config(text=f"{resultat_txt}")
print(dict_Viken_kommuner_skatt)
root = Tk()
root.title("Søk etter kommune")
root.geometry("400x800")
# Opprett en label for å vise valgt verdi

# Opprett rullegardinlisten
lbl_sokefelt = Label(root, text="Søk: ")
lbl_sokefelt.pack(pady=10)
entry_soketerm = Entry(root)
entry_soketerm.pack(pady=10)
btn_sok = Button(root, text="Søk!", command=sok_kommune_data)
btn_sok.pack(pady=10)
lbl_resultat = Label(root)
lbl_resultat.pack(pady=10)

# Kjør Tkinter-løkken
root.mainloop()

