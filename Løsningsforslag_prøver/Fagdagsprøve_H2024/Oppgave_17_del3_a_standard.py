from pathlib import Path
import matplotlib.pyplot as plt
from tkinter import *

#a)
#print(f"\na) Leser inn data\n")

fileName_2023 = 'BeregnedeSkatterOgAvgifterPrKommuneFollo2023.csv'

pyFilePath = Path(__file__).resolve().parent
fullFilePath_2023 = pyFilePath.joinpath(fileName_2023)
Follo_kommuner_skatt_2023 = {}

with open(fullFilePath_2023, encoding="utf8") as fil:
    overskrift = fil.readline().strip().split(";")
    for linje in fil:
        temp_kommune = linje.strip().split(";")
        temp_kommune[1] = int(temp_kommune[1].replace(" ", "")) 
        temp_kommune[2] = int(temp_kommune[2].replace(" ", "")) 
        Follo_kommuner_skatt_2023[temp_kommune[0]]=temp_kommune[1:]

#print(f"\ne) Legger til felt i data for gjennomsnitt\n")

def vis_diagram_pie():
    kommuner_x =[]
    skatter_y = []
    for kommune, verdier in Follo_kommuner_skatt_2023.items():
        kommuner_x.append(kommune)
        skatter_y.append(verdier[1])
    plt.pie(skatter_y, labels=kommuner_x, autopct='%1.0f%%')
    plt.title("Skatte og avgiftsintekter for kommunene i Follo")
    plt.xlabel(f"Totalt {sum(skatter_y)/1000000:.1f} i mill. kroner kr")
    plt.show()

def vis_diagram_bar():
    kommuner_x =[]
    skatter_y = []
    for kommune, verdier in Follo_kommuner_skatt_2023.items():
        kommuner_x.append(kommune)
        skatter_y.append(verdier[1]/1000000)
    plt.bar(kommuner_x, skatter_y)
    plt.title("Inntekt pr kommune")
    plt.ylabel("i mill kr kr")
    plt.xlabel("Kommuner i Follo")
    plt.show()

def vis_diagram_barh():
    kommuner_x =[]
    skatter_y = []
    for kommune, verdier in Follo_kommuner_skatt_2023.items():
        kommuner_x.append(kommune)
        skatter_y.append(verdier[1]/1000000)
    plt.barh(kommuner_x, skatter_y)
    plt.title("Inntekt pr kommune")
    plt.xlabel("i mill kr kr")
    plt.ylabel("Kommuner i Follo")
    plt.show()

root = Tk()
root.title("Diagram for kommune")
root.geometry("400x400")

btn_pie = Button(root, text="vis kake diagram 2023", command=vis_diagram_pie)
btn_pie.pack(pady=10)
btn_bar = Button(root, text="vis vertikalt stolpediagram 2023", command=vis_diagram_bar)
btn_bar.pack(pady=10)
btn_barh = Button(root, text="vis horisontalt stolpediagram 2023", command=vis_diagram_barh)
btn_barh.pack(pady=10)

# Kjør Tkinter-løkken
root.mainloop()