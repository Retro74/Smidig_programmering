```mermaid

classDiagram
    class Planet {
        navn: str
        solavstand: float
        radius: float
        antallRinger: int = 0
        __init__(navn: str, solavstand: float, radius: float, antallRinger: int = 0)
        volum(): float
    }
