import pandas as pd

data = {
    'Verdensdel': ['Europa', 'Asia', 'Europa', 'Nord-Amerika', 'Asia', 'Europa'],
    'Land': ['Norge', 'Japan', 'Tyskland', 'USA', 'Kina', 'Frankrike'],
    'By': ['Oslo', 'Tokyo', 'Berlin', 'New York', 'Beijing', 'Paris'],
    'Innbyggertall': [681067, 37435191, 3644826, 8419600, 21516000, 2140526]
}

df = pd.DataFrame(data)
print(f'a) Filtrer DataFrame slik at kun byer i "Asia" blir vist.')
print(df[df["Verdensdel"]=="Asia"])
#print(df[df["Verdensdel"].isin(["Asia"])])

print(f'b) Hvor mange byer er det i DataFrame totalt?')
print(f'Antall byer: {df["By"].count()}')


print(f"c) Hent ut navnene på alle kolonnene i DataFrame.")
for kolonne in df.columns: # aletrnativ bare ...in df:
    print(kolonne)

print(f'd) Sorter DataFrame etter kolonnen "Land" i stigende rekkefølge.')
print(df.sort_values("Land"))

print(f'e) Hva er det totale antallet innbyggere i Europa?')
print(df[df["Verdensdel"]=="Europa"]["Innbyggertall"].sum())

