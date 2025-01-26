```mermaid

classDiagram
    class BankKonto {
        + navn: str
        # kontotype: str
        - kontonummer: str
        - saldo: float
        + BankKonto(navn: str, kontonummer: str, start_saldo: float, kontotype: str)
        + innskudd(beløp: float): void
        + uttak(beløp: float): void
        + vis_saldo(): float
        + vis_kontotype(): str
    }

