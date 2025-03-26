:::mermaid
classDiagram
    class MemoryGame {
        # surface: pygame.display
        # cards: list~Card~
        # flipNumber: int = 0
        # previousCard: ~Card~ = None
        + attempts:int = 0
        + __init__(surface: pygame.display)
        + handle_click(pos: tuple) None
        + draw() None
    }

    class Card {
        # front_image: str
        # back_image: str
        # row: int
        # col: int
        + is_flipped: bool = False
        + is_matched: bool = False
        + __init__(front_image: str, back_image: str, row: int, col: int)
        + get_front_image() str
        + draw() None
    }

    MemoryGame "1" *-- "20" Card : har
