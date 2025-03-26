:::mermaid
classDiagram
    class Elbil {
        -modell: str
        -rekkevidde: float
        +start(): None
        +stopp(): None
    }

    class Motor {
        -effekt: int
        -type: str
        +startMotor(): None
        +stoppMotor(): None
    }

    class Batteri {
        -kapasitet: float
        -spenning: float
        +ladOpp(mengde: float): None
        +brukEnergi(mengde: float): None
    }

    Elbil --* Motor : har
    Elbil --* Batteri : har
