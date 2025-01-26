```mermaid
classDiagram
    class Innlegg {
        - brukernavn: str
        - tekst: str
        - antall_likes: int
        + like_innlegg(): void
        + vis_informasjon(): void
    }
    class BildeInnlegg {
        - bilde_url: str
        + vis_informasjon(): void
    }
    class VideoInnlegg {
        - lengde: int
        + vis_informasjon(): void
    }
    Innlegg <|-- BildeInnlegg
    Innlegg <|-- VideoInnlegg


