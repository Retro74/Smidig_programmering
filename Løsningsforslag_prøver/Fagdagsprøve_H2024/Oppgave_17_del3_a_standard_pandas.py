from pathlib import Path
import matplotlib.pyplot as plt
from tkinter import *
import pandas as pd

#a) ## Denne delen av løsningsfoslaget leser filen inn i dataframe med pandas
#print(f"\na) Leser inn data\n")

fileName_Follokommuner_2023 = 'BeregnedeSkatterOgAvgifterPrKommuneFollo2023.csv'

pyFilePath = Path(__file__).resolve().parent
fullFilePath_Follokommuner_2023 = pyFilePath.joinpath(fileName_Follokommuner_2023)
df = pd.read_csv(fullFilePath_Follokommuner_2023, delimiter=";", encoding="utf8")

#Fjerner mellomrom på starten og slutten i overskriftene
df.columns = df.columns.str.strip()
#Fjerner mellomrom i tallverier og gjør dem til tall
df["Skattepliktige"] = df["Skattepliktige"].str.replace(" ", "").astype(int)
df["Beregnede skatter og avgifter"] = df["Beregnede skatter og avgifter"].str.replace(" ", "").astype(int)


def vis_diagram_pie():
    plt.pie(df["Beregnede skatter og avgifter"], labels=df["Kommune"], autopct='%1.0f%%')
    plt.title("Skatte og avgiftsintekter for kommunene i Follo")
    plt.xlabel(f"Totalt {df["Beregnede skatter og avgifter"].sum()/1000000:.1f} i mill. kroner kr")
    plt.show()

def vis_diagram_bar():
    plt.bar(df["Kommune"], df["Beregnede skatter og avgifter"])
    plt.title("Skatte og avgiftsintekter for kommunene i Follo")
    plt.ylabel("i mill kr kr")
    plt.xlabel("Kommuner i Follo")
    plt.show()

def vis_diagram_barh():
    plt.barh(df["Kommune"], df["Beregnede skatter og avgifter"])
    plt.title("Skatte og avgiftsintekter for kommunene i Follo")
    plt.xlabel("i mill kr kr")
    plt.ylabel("Kommuner i Follo")
    plt.show()

#GUI
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