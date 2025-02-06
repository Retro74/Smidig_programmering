from random import randint

class Pokemon:
    def __init__(self, navn: str):
        self.navn = navn
        self._helse = 100

    def motta_skade(self, skade: int):
        self._helse = max(0, self._helse - skade) 
        print(f"{self.navn} mistet {skade} HP! Helse nå: {self._helse}")

    def er_vaaken(self):
        return self._helse > 0

class IldPokemon(Pokemon):
    def __init__(self, navn: str, spesialangrep: str = "Flammehav"):
        super().__init__(navn)
        self.__spesialangrep = spesialangrep

    def bruk_spesial(self):
        skade = randint(5, 20)
        print(f"{self.navn} bruker {self.__spesialangrep}! Det gjør {skade} skade!")
        return skade


class VannPokemon(Pokemon):
    def __init__(self, navn: str, spesialangrep: str = "Vannkanon"):
        super().__init__(navn)
        self.__spesialangrep = spesialangrep

    def bruk_spesial(self):
        skade = randint(10, 15)
        print(f"{self.navn} bruker {self.__spesialangrep}! Det gjør {skade} HP skade!")
        return skade


# Opprett Pokémon
pokemon1  = IldPokemon("Charizard")
pokemon2   = VannPokemon("Blastoise")

# Kamp!
while pokemon1.er_vaaken() and pokemon2.er_vaaken():
    pokemon2.motta_skade(pokemon1.bruk_spesial())
    pokemon1.motta_skade(pokemon2.bruk_spesial())

if not pokemon1.er_vaaken() and not pokemon2.er_vaaken():
    print("Begge har besvimt! Ingen vinner")
elif pokemon1.er_vaaken(): 
    print(f"{pokemon2.navn} har besvimt! {pokemon1.navn} vinner")
else:
    print(f"{pokemon1.navn} har besvimt! {pokemon2.navn} vinner")