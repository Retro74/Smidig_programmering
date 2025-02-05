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
        + bruk_spesial(): int
    }

    class VannPokemon {
        - spesialangrep: str
        + VannPokemon(navn: str, spesialangrep: str = "Vannkanon")
      + bruk_spesial(): int
    }

    Pokemon <|-- IldPokemon
    Pokemon <|-- VannPokemon


