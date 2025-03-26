
:::mermaid
classDiagram
    class Person {
        + fornavn: string
        + etternavn: string
        # alder: int
        - personnummer: int
        + init(fornavn, etternavn, alder, personnummer)
        + hilsen() string
        + oek_alder(antall_aar:int) void
    }

    class Ansatt {
        + ansattNummer:int
        + tittel: string
        
    }

    Person "1" <|-- "1" Ansatt : er