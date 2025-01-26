```mermaid
classDiagram
    class Oppskrift {
        - navn: str
        - ingredienser: list
        - tid: int
        + vis_oppskrift(): void
        + legg_til_ingredient(ingredient: str): void
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
