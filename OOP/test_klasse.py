
class Person:
    
    def __init__(self, fornavn, etternavn, alder, kjonn, mobilnummer):
        self.fornavn = fornavn 
        self.etternavn = etternavn 
        self.alder = alder 
        self.kjonn = kjonn
        self.mobilnummer = list(mobilnummer)
    def visInfo(self):
        for attr, value in vars(self).items():
            print(f"{attr}: {value}")
            print(f"{type(attr)}: {type(value)}")

ole = Person("ole", "olsen", 23, "mann", [190,9022,11])
ole.visInfo()


