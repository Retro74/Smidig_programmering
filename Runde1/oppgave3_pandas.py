import pandas
innbyggere_byer_df = pandas.read_csv("Runde1/Innbyggertall_Byer.csv")
brukerValg = "Verdensdel" if input("Hva vil du se byre fra? (v=verdensdel, l=land)")=="v" else "Land"
print(brukerValg)
print(f"Fra hvilken/hvilket {brukerValg} vil du se byer?")
for navn in innbyggere_byer_df[brukerValg].unique():
    print(f"* {navn}")

brukerValgNavn = input(f"Skriv {brukerValg}: ") 

print(innbyggere_byer_df[innbyggere_byer_df[brukerValg]==brukerValgNavn])