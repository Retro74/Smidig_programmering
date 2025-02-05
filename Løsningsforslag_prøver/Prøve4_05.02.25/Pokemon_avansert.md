```mermaid

classDiagram
    class Pokemon {
        + navn: str
        # helse: int
        + Pokemon(navn: str)
        + motta_skade(skade: int): void
        + er_vaaken(): bool
    }

    class IldPokemon {
        - spesialangrep: str
        + IldPokemon(navn: str, spesialangrep: str = "Flammehav")
        + bruk_spesial(): str
        + er_sol(vaer): bool
    }

    class VannPokemon {
        - spesialangrep: str
        + VannPokemon(navn: str, spesialangrep: str = "Vannkanon")
        + bruk_spesial(): str
        + er_regn(vaer): bool
    }

    Pokemon <|-- IldPokemon
    Pokemon <|-- VannPokemon


