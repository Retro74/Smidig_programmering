```mermaid

classDiagram
    class Bil {
        merke: str
        modell: str
        årsmodell: int
        nypris: float
        prisreduksjoner: list
        nåpris (km_stand: int, stand: int): float
    }

