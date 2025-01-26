from math import pi
class Planet:
    bb = 11

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
            float: volum
        """
        return (4/3) * pi * self.radius**3

mars = Planet("Mars", 227.9, 3389.5 )
jupiter = Planet("Jupiter", 778.5, 69911, 4)
#jupiter.bb = "b"
print(jupiter.bb)
print("TypeMars sitt volum er: ", mars.volum(), "km^3")

