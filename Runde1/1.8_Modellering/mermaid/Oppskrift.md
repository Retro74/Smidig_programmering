```mermaid
classDiagram
    class Oppskrift {
        - navn: str
        - ingredienser: list
        - tid: int
        - fremgangsmaate: str
        + vis_oppskrift(): void
        + legg_til_ingrediens(ingrediens:str, mengde:float, enhet:str): void
        + slett_ingrediens(ingrediens:str)
    }
    class VegetarOppskrift {
        - veganvennlig: bool
        + vis_oppskrift(): void
    }
    class DessertOppskrift {
        - kalorier: int
        + vis_oppskrift(): void
    }
    Oppskrift <|-- VegetarOppskrift
    Oppskrift <|-- DessertOppskrift
