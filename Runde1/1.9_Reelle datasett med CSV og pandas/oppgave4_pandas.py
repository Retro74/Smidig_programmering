#Sorter listen etter brukervalgte kritterier
import pandas
innbyggere_byer_df = pandas.read_csv("Runde1/Innbyggertall_Byer.csv")
print(f"Hva vil du sortere listen etter?")
for kolonne in innbyggere_byer_df.columns:
    print(f"* {kolonne}")
brukervalg = input("Skriv en eller flere kolonner, med komma mellom: ").split(",")
brukervalg = [valg.strip() for valg in brukervalg]

ascending_list =[]
for kolonne in brukervalg:
    ascending_list.append(True if input(f"Stigende (a) eller synkende (d) for {kolonne}: ").strip().lower() =="a" else False)

print (brukervalg)
print (ascending_list)
print(innbyggere_byer_df.sort_values(by=brukervalg, ascending=ascending_list))
