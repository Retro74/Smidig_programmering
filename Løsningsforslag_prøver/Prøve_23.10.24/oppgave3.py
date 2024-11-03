import pandas

bil_salg_df = pandas.read_csv("Rogers Øvingsoppgaver/Prøve2/bil_salg.csv")

#a) 
print(bil_salg_df.head(5))  

#b)
brukervalg = "ny" if input("Vil du se en liste over nye (n) eller brukte (b) biler? ")=="n" else "brukt"
print(f'\nHer er en liste over {brukervalg} biler:')
print(bil_salg_df[bil_salg_df["Tilstand"]==brukervalg])

#c) 
print(f"Gjennomsnittsprisen på de brukte bilene er: {bil_salg_df[bil_salg_df["Tilstand"]=="brukt"]["Pris"].mean()} kroner")

#d) 
print(bil_salg_df.groupby("Bilmerke")["Bilmerke"].count())

#e)
bukerPris= int(input("Din makspris: "))
bukerÅrsmodell= int(input("Din maks-årsmodell: "))
print(bil_salg_df[((bil_salg_df["Pris"]<= bukerPris) & (bil_salg_df["Årsmodell"]>=bukerÅrsmodell))])

#f)
gjennomsnittskm_bruktbiler = bil_salg_df[bil_salg_df["Tilstand"]=="brukt"]["Kilometerstand"].mean()
print(gjennomsnittskm_bruktbiler)
print(bil_salg_df[(bil_salg_df["Kilometerstand"]< gjennomsnittskm_bruktbiler) & (bil_salg_df["Tilstand"]=="brukt")])

#g)
#print(bil_salg_df[bil_salg_df["Tilstand"]=="ny"]["Tilstand"].count())
bil_salg_df.loc[(bil_salg_df["Kilometerstand"]<20000)&(bil_salg_df["Årsmodell"]> 2021), "Tilstand"]="ny"
#print(bil_salg_df)
#print(bil_salg_df[bil_salg_df["Tilstand"]=="NY"]["Tilstand"].count())
bil_salg_df.to_csv('oppdatert_bil_salg.csv', index=False)

