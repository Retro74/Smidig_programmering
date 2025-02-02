# Liste over gyldige verdensdeler
GYLDIGE_VERDENSDELER = ["Europa", "Asia", "Afrika", "Nord-Amerika", "Sør-Amerika", 
                  "Oseania", "Antarktis"]
UkjentVerdensdel = "Ukjent verdensdel"

class Land:
    def __init__(self, navn:str, befolkning:float, areal:int, verdensdel:str=UkjentVerdensdel):
        """Klasse for land

        Args:
            navn (str): Landes navn
            befolkning (float): befolking i millioner
            areal (int): nat. kvadrat km
            verdensdel (str): Verdensdel default to UkjentVerdensdel
        """
        self.navn = navn
        self.befolkning = befolkning
        self.areal = areal
        if verdensdel not in GYLDIGE_VERDENSDELER:
            self.verdensdel = UkjentVerdensdel
        else:
            self.verdensdel = verdensdel
    
    def befolkningstetthet(self):
        return self.befolkning*1_000_000/self.areal
    
    def iSammeVerdensdel(self, annetLand):
        return self.verdensdel == annetLand.verdensdel
    
    def __str__(self):
        return ", ".join(f"{planetegnskap}={planetegnskap_verdi}" for planetegnskap, planetegnskap_verdi in vars(self).items())


land_data = [
    {"Land": "Norge", "Befolkning (mill.)": 5.4, "Areal (km²)": 385207, "Verdensdel": "Europa"},
    {"Land": "Tyskland", "Befolkning (mill.)": 83.2, "Areal (km²)": 357022, "Verdensdel": "Europa"},
    {"Land": "India", "Befolkning (mill.)": 1428, "Areal (km²)": 3287263, "Verdensdel": "Asia"},
    {"Land": "Japan", "Befolkning (mill.)": 125.7, "Areal (km²)": 377975, "Verdensdel": "Asia"},
    {"Land": "Brasil", "Befolkning (mill.)": 216.4, "Areal (km²)": 8515767, "Verdensdel": "Sør-Amerika"},
    {"Land": "Argentina", "Befolkning (mill.)": 46.2, "Areal (km²)": 2780400, "Verdensdel": "Sør-Amerika"},
    {"Land": "Sør-Afrika", "Befolkning (mill.)": 60.1, "Areal (km²)": 1221037, "Verdensdel": "Afrika"}
]
diverse_land = {}
for ett_land in land_data:
    diverse_land[ett_land["Land"]]=Land(ett_land["Land"], ett_land["Befolkning (mill.)"],ett_land["Areal (km²)"],ett_land["Verdensdel"])

for land_obj in diverse_land.values():
    print(land_obj)

diverse_land["Auroria"]=Land("Auroria", 0.000001, 200,"Utopia")
print(diverse_land["Auroria"])


print("Er Norge i samme verdensdel som Tyskland?")
print(diverse_land["Norge"].iSammeVerdensdel(diverse_land["Tyskland"]))

print("Er Norge i samme verdensdel som Japan?")
print(diverse_land["Norge"].iSammeVerdensdel(diverse_land["Japan"]))