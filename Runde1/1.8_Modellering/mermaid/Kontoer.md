```mermaid

classDiagram
    class BankKonto {
        + navn: str
        # kontotype: str
        - kontonummer: str
        # saldo: float
        + BankKonto(navn: str, kontonummer: str, start_saldo: float, kontotype: str)
        + innskudd(beløp: float): void
        + uttak(beløp: float): void
        + vis_saldo(): float
        + vis_kontotype(): str
    }

    class SpareKonto {
        + legg_til_renter(renteprosent: float): void
    }

    class BruksKonto {
        +daglig_grense: float
    }
    
    BankKonto <|-- SpareKonto
    BankKonto <|-- BruksKonto    



