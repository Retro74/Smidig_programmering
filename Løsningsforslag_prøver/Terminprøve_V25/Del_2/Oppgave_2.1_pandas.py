from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

##Henter data fra filen inn i en dataframe
fileName = 'offentlige_utgifter.csv'
pyFilePath = Path(__file__).resolve().parent
fullFilePath = pyFilePath.joinpath(fileName)
df = pd.read_csv(fullFilePath, delimiter=";")

##Henter et gyldig årstall fra brukeren
while True:
    try:
        aarstall = int(input(f"Skriv inn ett år mellom {df.columns[1]}-{df.columns[-1]}: "))
        if int(df.columns[1]) <= aarstall <= int(df.columns[-1]):
            print(f"Henter ut informasjonen fra {aarstall}")
            break
        else:
            print("Ugyldig år")
    except:
        print("Skriv året på nytt")

#Må stringe 
aarstall = str(aarstall)

# b) og c) 
# print(df[["Formål (mill. kr)", aarstall]].sort_values(aarstall, ascending=False))

Totalt = df[df["Formål (mill. kr)"]=="Totalt"][aarstall][0]
df["prosent"] = df[aarstall]/Totalt*100
print(df[["Formål (mill. kr)", aarstall, "prosent"]])
#Henter ut dataframe til bruk i diagram 
diagram_df = df[["Formål (mill. kr)", aarstall]]

#Sorterer diagram_df
diagram_df= diagram_df.sort_values(aarstall, ascending=False)

# Filtrerer bort "Totalt" - linjen
diagram_df= diagram_df[diagram_df["Formål (mill. kr)"]!="Totalt"]

##Lager diagram
plt.pie(diagram_df[aarstall], labels=diagram_df["Formål (mill. kr)"], autopct='%1.1f%%', startangle=20)
plt.title(f"Utgifter prosentfordling av {Totalt/1000:.1f} milliarder. kr for {aarstall}")
plt.show()