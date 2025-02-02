from math import pi
class Planet:
    def __init__(self, navn:str, solavstand:float, radius:float, antallRinger:int = 0):
        """
        Klasse for å lage planet-objekter
        
        Args:
            navn (str): Planetens navn
            solavstand (float): Avstand fra solen i millioner km
            radius (float): Planetens radius i km
            antallRinger (int, optinal): Antall ringer rundt planeten. Defaults to 0.
        """
        self.navn = navn
        self.solavstand = solavstand
        self.radius = radius
        if radius < 10000:
            self.type = "Terrestrisk planet"
        else:
            self.type = "Gasskjempe"
        self.antallRinger = antallRinger
    def volum(self):
        """
        Returnerer volumet av planeten i kubikk km
        
        Reurns:
            float: planetens volum
        """
        return (4/3) * pi * self.radius**3
    def __str__(self):
        return ", ".join(f"{planetegnskap}={planetegnskap_verdi}" for planetegnskap, planetegnskap_verdi in vars(self).items())

#mars = Planet("Mars", 227.9, 3389.5 )
#jupiter = Planet("Jupiter", 778.5, 69911, 4)
#print("TypeMars sitt volum er: ", mars.volum(), "km^3")

planeter = [
    ["Merkur", 57.9, 2439.7, 0],
    ["Venus", 108.2, 6051.8, 0],
    ["Jorda", 149.6, 6371.0, 0],
    ["Mars", 227.9, 3389.5, 0],
    ["Jupiter", 778.3, 69911.0, 4],
    ["Saturn", 1427.0, 58232.0, 7],
    ["Uranus", 2871.0, 25362.0, 13],
    ["Neptun", 4497.1, 24622.0, 5]
]
solsystemet = {}

for planet in planeter:
    solsystemet[planet[0]]=Planet(planet[0],planet[1], planet[2], planet[3])

#print(solsystemet)
while True:
    finn_planet = input("Hviklen planet vil du se informasjon om? (q=quit) ")
    if finn_planet == "q":
        break
    elif finn_planet in solsystemet:
        print(solsystemet[finn_planet])
