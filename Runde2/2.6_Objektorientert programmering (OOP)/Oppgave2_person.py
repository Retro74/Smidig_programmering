import datetime as dt 
class Person:
    def __init__(self, fornavn:str, etternavn:str, fodselsaar:int, fodselsmnd:int, fodselsdato:int, telefonnummer:str=""):
        self.fornavn =      fornavn
        self.etternavn =    etternavn
        self.fodselsaar =   fodselsaar
        self.fodselsmnd =   fodselsmnd
        self.fodselsdato =  fodselsdato
        self.telefonnummer = telefonnummer

    def bergnAlder(self):
        """Beregner den nøyaktige alderen til Personen ut fra dagens dato (NB. Ikke inkl. skuddår) 

        Returns:
            int: personens alder
        """
        # Lager objekter for fødselsdato og datoen i dag
        fodseslsdato = dt.datetime(self.fodselsaar, self.fodselsmnd, self.fodselsdato) # år, måned, dag
        #Henter dagens dato
        dagensDato = dt.datetime.now()
        # Beregner tidsforskjell mellom de to datoene
        tidsforskjell = dagensDato - fodseslsdato
        #Returnerer heltallsdivisjonen av tidforskjell i dager, delt på 365 dager/år
        return tidsforskjell.days // 365

    def visInfo(self):
        """Skriver ut fullt navn og alder til personen
        """
        #print(f"{self.fornavn} {self.etternavn} ({self.bergnAlder()} år)")
        for attr, value in vars(self).items():
            print(f"{attr.title()}: {value}")
        print(f"Alder: {self.bergnAlder()} år")


ola = Person("Ola", "Olsen", 2001, 3, 22, "+4790001001")
morten = Person("Morten", "Vik", 2003, 7, 2, "+4790001123")
per = Person("Per Iver", "Hansen", 2003, 12, 22, "+4790077701")


kompiser = [ola, morten, per]

for kompis in kompiser:
    kompis.visInfo()
    