import pandas as pd

# Eksempel på en litt større DataFrame
data = {'Bynavn': ['Oslo', 'Bergen', 'Tokyo', 'Paris', 'Berlin', 'London', 'Madrid', 'Roma', 'New York', 'Los Angeles',
                   'Shanghai', 'Mumbai', 'Cairo', 'Johannesburg', 'Sydney', 'Wellington', 'Buenos Aires', 'Sao Paulo',
                   'Mexico City', 'Toronto', 'Seoul', 'Jakarta', 'Bangkok', 'Nairobi', 'Lagos'],
        'Innbyggertall': [681067, 280216, 37435191, 2140526, 3644826, 8982000, 3223334, 2873000, 8419600, 3980400,
                          24150000, 20411000, 20000000, 957441, 5230330, 412500, 2890151, 12325232, 9209944, 2731579,
                          9933000, 10000000, 10000000, 4745000, 14100000],
        'Verdensdel': ['Europa', 'Europa', 'Asia', 'Europa', 'Europa', 'Europa', 'Europa', 'Europa', 'Nord-Amerika', 'Nord-Amerika',
                       'Asia', 'Asia', 'Afrika', 'Afrika', 'Oceania', 'Oceania', 'Sør-Amerika', 'Sør-Amerika', 'Nord-Amerika', 'Nord-Amerika',
                       'Asia', 'Asia', 'Asia', 'Afrika', 'Afrika']}

df = pd.DataFrame(data)

# Endre pandas-innstillinger for å vise alle rader og kolonner
pd.set_option('display.max_rows', None)  # Ingen begrensning på antall rader
pd.set_option('display.max_columns', None)  # Ingen begrensning på antall kolonner

# Skriver ut hele DataFrame-en:
print(df)
