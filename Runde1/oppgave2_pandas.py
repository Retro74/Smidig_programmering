import pandas
innbyggere_byer_df = pandas.read_csv("Runde1/Innbyggertall_Byer.csv")


#ny_rad = {'Verdensdel': 'Europe', 'Land': 'Norway', 'By': 'Harstad', 'Innbyggertall': 25077}
#innbyggere_byer_df = pandas.concat([innbyggere_byer_df, pandas.DataFrame([ny_rad])], ignore_index=True)

#nye_rader = [{'Verdensdel': 'Europe', 'Land':"Norway", 'By': 'Bodø', 'Innbyggertall': 53066}, 
#             {'Verdensdel': 'Europe', 'Land':"Norway",'By': 'Kristiansand', 'Innbyggertall': 66576}]

#innbyggere_byer_df = pandas.concat([innbyggere_byer_df, pandas.DataFrame(nye_rader)], ignore_index=True)

print(innbyggere_byer_df)
while True:
    valg = input("Velg\n1. Legg til ny by\n2. Endre innbyggertall\nValg:")
    if valg not in ["1", "2"]:
        break
    if valg == "1":
        raddata = {} #Oppretter en tom ordbok til å kunne putte inn 
        for kolonne in innbyggere_byer_df.columns:
            kolonneverdi = input(f"Skriv inn {kolonne}: ") 
            if kolonne == "Innbyggertall":
                raddata[kolonne]=int(kolonneverdi)
            else:
                raddata[kolonne]=kolonneverdi
        if raddata["By"] not in innbyggere_byer_df["By"]:
            innbyggere_byer_df = pandas.concat([innbyggere_byer_df, pandas.DataFrame([raddata])], ignore_index=True)
    else:
        by = input("Hvilken by vil du registrere innbyggertall på?")
        innbyggertall = int(input(f"Innbyggertall til {by}: "))
        innbyggere_byer_df.loc[innbyggere_byer_df['By'] == by, 'Innbyggertall'] = innbyggertall


print(innbyggere_byer_df)
