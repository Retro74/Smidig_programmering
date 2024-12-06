```mermaid
classDiagram
    class Spilleliste {
        - String navn
        - List<Sang> sanger
        - boolean offentlig
        - String beskrivelse
        - int antallSanger()
        - int totalSpilletid()
        + leggTilSang(Sang sang)
        + fjernSang(Sang sang)
        + delSpilleliste(String bruker)
        + sorterSanger(String kriterium)
    }
    
    class Sang {
        - String tittel
        - String artist
        - int spilletid // i sekunder
        - String album
        - String filSti
        + getDetaljer()
    }

    Spilleliste "1" --> "*" Sang : inneholder

