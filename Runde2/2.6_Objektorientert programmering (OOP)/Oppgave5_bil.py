import datetime as dt 
class Bil:
    def __init__(self, merke:str, modell:str, aarsmodell:int, nypris:float, prisreduksjoner:list=[-0.21, -0.17, -0.15, -0.10]):
        """Klasse for en bil 

        Args:
            merke (str): Bilmerket
            modell (str): modellen
            aarsmodell (int): Bilens årsmodell
            nypris (float): Bilens nypris
            prisreduksjoner (list, optional): Prisutviklingsliste, siste tall gjentas som verdi til slutt. 
                                                Defaults to [-0.21, -0.17, -0.15, -0.10].
        """
        self.merke              = merke
        self.modell             = modell
        self.aarsmodell         = aarsmodell
        self.nypris             = nypris
        self.prisreduksjoner    = prisreduksjoner

    def naapris(self, km_stand:int, stand:int):
        """Beregner bilens nåpris-verdi bassert på alder, prisutvikling, km-stand og generell stand

        Args:
            km_stand (int): bilens km-stand
            stand (int): Bilens generelle stand (Karakter fra 1-20 hvor 20 er best)

        Returns:
            _type_: _description_
        """
        beregnetPris = self.nypris
        aarstall = dagensDato = dt.datetime.now().year

        #Reduserer pris pga av alder
        for i in range(aarstall-self.aarsmodell):
            if i >= len(self.prisreduksjoner):
                beregnetPris *= (1 + self.prisreduksjoner[-1])
            else:
                beregnetPris *= (1 + self.prisreduksjoner[i])

        #Redusrer prisen pga av km_stand
        for i in range(km_stand//50_000):
            beregnetPris *= 0.9
        
        #Reduser prisen pga stand
        vekstfaktor = 1 - (22.22 - 2.222*stand)/100 # modellen for denne beregningen 
                                                    # er funnet ved hjelp av 
                                                    # bruk av lineær regresjon i Geogebra
        beregnetPris *= vekstfaktor

        ##Avrunder prisen til nærmeste 1000-lapp
        beregnetPris = round(beregnetPris/1000)*1000
        ## 5000 er vrakpant for bilder i Norge så kan ikke bli under dette
        return max(5000, beregnetPris) 


magdisToyota = Bil("Toyota", "Corolla", 1990, 370000)
print(magdisToyota.naapris(250000,2))

minFordExplorer = Bil("Ford", "Explorter", 2023, 670_000)
print(minFordExplorer.naapris(15000,8))