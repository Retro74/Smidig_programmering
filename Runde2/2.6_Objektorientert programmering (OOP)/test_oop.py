# Definerer en baseklasse
class Dyr:
    def __init__(self, navn):
        self.navn = navn
    def get_navn(self):
        return (self.navn)
    def snakk(self):
        print(f"{self.navn} lager en lyd")

# Definerer en subklasse som arver fra Dyr
class Hund(Dyr):
    def snakk(self):
        print(f"{self.navn} sier voff!")

# Lager et objekt av subklassen Hund
hund = Hund("Rex")
print(hund.get_navn())
hund.snakk()  # Kaller snakk() fra Hund-klassen

# Lager et objekt av baseklassen Dyr
dyr = Dyr("Generisk dyr")
dyr.snakk()  # Kaller snakk() fra Dyr-klassen
