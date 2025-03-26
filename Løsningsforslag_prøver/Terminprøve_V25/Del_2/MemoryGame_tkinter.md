:::mermaid
classDiagram
    class Card {
        # front_image: str 
        # back_image: str
        # row: int
        # col: int
        # is_flipped: bool
        # is_matched: bool 
        + __init__(root: tk.Tk, front_image: str, back_image: str, row: int, col: int)
        + flip()
        + update_image()
    }

    class MemoryGame {
        # root: tk.Tk
        # cards: list ~Card~
        + previous_card: ~Card~
        + click_sequence: int = 0
        + __init__(root, pyFilePath)
        + load_cards(pyFilePath)
    }

    MemoryGame "1" *-- "*" Card : inneholder
