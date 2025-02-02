
class Person:
    def __init__(self, navn, alder, yrke):
        self.navn = navn
        self.alder = alder
        self.yrke = yrke

    def __str__(self):
        return ", ".join( f"{nokkel}: {verdi}" for nokkel,verdi in vars(self).items())

morten = Person("Morten", 44, "Frisør")


print(morten)
