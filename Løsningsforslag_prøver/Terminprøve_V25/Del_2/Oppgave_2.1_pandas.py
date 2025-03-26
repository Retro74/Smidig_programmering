from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

fileName = 'offentlige_utgifter.csv'
pyFilePath = Path(__file__).resolve().parent
fullFilePath = pyFilePath.joinpath(fileName)
df = pd.read_csv(fullFilePath, delimiter=";")
aarstall = "2003" # int(input("Skriv inn årstall: "))
Totalt = df[df["Formål (mill. kr)"]=="Totalt"][aarstall][0]

#print(df[["Formål (mill. kr)", aarstall]].sort_values(aarstall, ascending=False))

#Henter ut dataframe til bruk i daigram 
diagram_df = df[["Formål (mill. kr)", aarstall]]

#Sorterer diagram_df
diagram_df= diagram_df.sort_values(aarstall, ascending=False)

# Filtrerer ut Totalt - linjen
#print(diagram_df[diagram_df["Formål (mill. kr)"]!="Totalt"])
diagram_df= diagram_df[diagram_df["Formål (mill. kr)"]!="Totalt"]

plt.pie(diagram_df[aarstall], labels=diagram_df["Formål (mill. kr)"], autopct='%1.1f%%', startangle=20)
plt.title(f"Utgifter prosentfordling av {Totalt/1000:.1f} milliarder. kr for {aarstall}")
plt.show()