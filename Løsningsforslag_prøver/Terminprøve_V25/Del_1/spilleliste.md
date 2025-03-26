```mermaid
classDiagram
    class Spilleliste {
        + spilleListeNavn: string 
        - sanger: list~Sang~
        - aktivSangIndex: int
        - gjenta: bool 
        
        + leggTilSang(sang: Sang)
        + fjernSang(sangtittel: str)
        + spillSang()
        + spillNesteSang()
        + stoppSang()
    }

    class Sang {
        - sangTittel: string 
        - artist: string
        - spilletid: int  // i sekunder
        - album: string 
        - filSti: string 
        
        + getDetaljer() string
        + spill() None
    }

    Spilleliste "0" o-- "*" Sang : inneholder