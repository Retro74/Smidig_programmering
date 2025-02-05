```mermaid

classDiagram
    class Vapen {
        navn: str
        skade: int
        ammunisjon: int
        Vapen(navn: str, skade: int = 10, ammunisjon: int = 5)
        skyt(): str
        lad_opp(): void
    }
