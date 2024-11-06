import pandas
innbyggere_byer_df = pandas.read_csv("Runde1/Innbyggertall_Byer.csv")
print("a) Alle byene")
print(innbyggere_byer_df[["By"]])

print("\n\nb) Alle byene med innbyggertall")
print(innbyggere_byer_df[["By","Innbyggertall"]])

print("\n\nc) Sortert liste etter antall innbyggere")
print(innbyggere_byer_df.sort_values("Innbyggertall"))

print("\n\nd) Alle byer i Europa")
print(innbyggere_byer_df[innbyggere_byer_df["Verdensdel"]=="Europa"])

print("\n\ne) Alle byer i Europa og Asia")
print(innbyggere_byer_df[innbyggere_byer_df["Verdensdel"].isin(["Europa", "Asia"])])

print("\n\nf) Alle byer som ikke er i Europa ")
print(innbyggere_byer_df[~innbyggere_byer_df["Verdensdel"].isin(["Europa"])])

print(f"\n\nMax() = {innbyggere_byer_df["Innbyggertall"].max()}")

print("\n\ng) Største byen")
print(innbyggere_byer_df[innbyggere_byer_df["Innbyggertall"]==innbyggere_byer_df["Innbyggertall"].max()])

print("\n\nh) Antall innbyggere for byene i Asia")
print(innbyggere_byer_df[innbyggere_byer_df["Verdensdel"]=="Asia"]["Innbyggertall"].sum())

print("\n\ni) Alle byer med mer enn  10 mill innbygere")
print(innbyggere_byer_df[innbyggere_byer_df["Innbyggertall"]>=10000000])

print("\n\nj) Europeiske byer med mer enn 3 mill innbyggere")
print(innbyggere_byer_df[(innbyggere_byer_df["Innbyggertall"]>=3000000) & (innbyggere_byer_df["Verdensdel"]=="Europa")])

print("\n\nk) Nord og Sør-Amerikanske byer med mer enn 8 mill innbyggere")
print(innbyggere_byer_df[((innbyggere_byer_df["Innbyggertall"]>=8000000) & ((innbyggere_byer_df["Verdensdel"]=="Nord-Amerika")|(innbyggere_byer_df["Verdensdel"]=="Sør-Amerika")))])

print("\n\nl) Verdensdelene som er registert:")
print(innbyggere_byer_df["Verdensdel"].unique())

print("\n\nm) Gruppert og summert for byene i hver verdensdel:")
print(innbyggere_byer_df.groupby('Verdensdel')['Innbyggertall'].sum())