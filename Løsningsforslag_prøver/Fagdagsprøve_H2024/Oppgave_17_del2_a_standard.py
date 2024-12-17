from pathlib import Path
from tkinter import *  
# alternativt: import tkinter as tk, 
# eller: from tkinter import Tk, Label  
from tkinter import ttk

#a) Denne delen av løsningsforslaget leser inn filen som en ordbok der 
# hvert kommunenavn er en nøkkelog tallene er en liste av verdier
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
#print(dict_Viken_kommuner_skatt)

#print(f"\ne) Legger til felt i data for gjennomsnitt\n")
for kommune, verdier in dict_Viken_kommuner_skatt.items():
    dict_Viken_kommuner_skatt[kommune].append(dict_Viken_kommuner_skatt[kommune][1]/dict_Viken_kommuner_skatt[kommune][0])

def vis_kommune_data(event):
    kommune = cmb_kommune_valg.get()
    resultat_txt =f"Data for: {kommune}\n"
    resultat_txt+= f"Antall Skattepliktige: {round(dict_Viken_kommuner_skatt[kommune][0]/1000,1)}k\n"
    resultat_txt+= f"Skatte- og avgiftinntekter: {round(dict_Viken_kommuner_skatt[kommune][1]/1000000,1)} mill.kr \n"
    resultat_txt+= f"Gjennomsnittlig skatteinntekt pr. innbygger:{round(dict_Viken_kommuner_skatt[kommune][2]/1000,1)}' kr \n"
    lbl_resultat.config(text=f"{resultat_txt}")

root = Tk()
root.title("Kommunenes skatte og avgifts-inntekter")

# Opprett en label for å vise valgt verdi
label = ttk.Label(root, text="Velg kommune:")
label.pack(pady=10)


# Opprett rullegardinlisten
kommunenavn = list(dict_Viken_kommuner_skatt.keys())
cmb_kommune_valg = ttk.Combobox(root, values=kommunenavn)
cmb_kommune_valg.set("Velg et alternativ")  # Sett standard tekst
cmb_kommune_valg.pack(pady=10)
cmb_kommune_valg.bind("<<ComboboxSelected>>", vis_kommune_data)
lbl_resultat = Label(root)
lbl_resultat.pack()

# Kjør Tkinter-løkken
root.mainloop()