

class BankKonto:
    def __init__(self, kontonavn, eier, kontonummer, saldo):
        self.kontonavn =        kontonavn
        self.kontotype =        ""
        self.__eier =           eier
        self.__kontonummer =    kontonummer
        self._saldo =           saldo

    def innskudd(self, belop):
        self._saldo += belop
        print(f"Saldoen på {self.__kontonummer} er {self._saldo:.2f} kr")

    def uttak(self, belop):
        if belop > self._saldo:
            print(f"Ikke nok penger på kontoen, saldoen er på {self._saldo:.2f} kroner")
        else:
            self._saldo -= belop
            print(f"Her er {belop} kr, saldoen er nå {self._saldo:.2f} kroner")

    def __str__(self):
        return ", ".join(f"{key}={value}" for key, value in vars(self).items())


class SpareKonto(BankKonto):
    def __init__(self, kontonavn, eier, kontonummer, saldo):
        super().__init__(kontonavn, eier, kontonummer, saldo)
        self.kontotype = "Sparekonto"
    
    def leggTilRenter(self, rentefot):
        self._saldo *= (1+rentefot/100)
        print(f"Renter er nå lagt til, ny saldo er: {self._saldo:.2f} kroner")


class BruksKonto(BankKonto):
    def __init__(self, kontonavn, eier, kontonummer, saldo, dagliggrense):
        super().__init__(kontonavn, eier, kontonummer, saldo)
        self.kontotype= "Brukskonto med Visa-kort"
        self.dagliggrense = dagliggrense

    def uttak(self, belop):
        if belop > self._saldo:
            print(f"Ikke nok penger på kontoen, saldoen er på {self._saldo:.2f} kroner")
        else:
            if belop > self.dagliggrense:
                print(f"Uttaket overstiger maks dagsbeløp, maks uttak i dag er {self.dagliggrense:.2f} kroner")
            else:
                self._saldo -= belop
                self.dagliggrense-= belop
                print(f"Her er {belop} kr, saldoen er nå {self._saldo:.2f} kroner")

LassesBrukskonto= BruksKonto("Visakort-konto", "Lasse Olsen", 23456787, 5000,3000)
LassesBrukskonto.innskudd(15000)
LassesBrukskonto.uttak(1000)
LassesBrukskonto.uttak(1000)
LassesBrukskonto.uttak(1500)
print(LassesBrukskonto)


#MartinsSparekonto = SpareKonto("Tante Martas arvepenger", "Martin", 12345678, 20_000)
#print(MartinsSparekonto)
#MartinsSparekonto.innskudd(5000)
#print(MartinsSparekonto)
#MartinsSparekonto.leggTilRenter(5)
#print(MartinsSparekonto)
#MartinsSparekonto.uttak(12000)
#print(MartinsSparekonto)
#MartinsSparekonto.uttak(12000)
#print(MartinsSparekonto)
#MartinsSparekonto.uttak(12000)
#print(MartinsSparekonto)

