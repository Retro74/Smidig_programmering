```mermaid
classDiagram
    class Spilleliste {
        - string navn
        - list sanger
        - bool offentlig
        - string beskrivelse
        - int aktivSangIndex
        - bool gjenta
        
        + int antallSanger()
        + int totalSpilletid()
        + leggTilSang(Sang sang)
        + fjernSang(Sang sang)
        + delSpilleliste(string bruker)
        + sorterSanger(string kriterium)
        + spillSang(int indeks)
        + spillNesteSang()
        + stoppSang()
        + oppdaterAvspilling()
    }

    class Sang {
        - string tittel
        - string artist
        - int spilletid // i sekunder
        - string album
        - string filSti
        
        + getDetaljer()
        + spill()
    }

    Spilleliste "1" o-- "*" Sang : inneholder