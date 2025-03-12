````mermaid
classDiagram
    class Game {
        - screen: pygame.Surface
        - clock: pygame.time.Clock
        - snake: Snake
        - food: Food
        - running: bool
        + __init__()
        + run()
        + check_collision()
        + restart()
    }

    class Snake {
        - body: list
        - direction: tuple
        - speed: int
        + __init__()
        + move()
        + grow()
        + check_self_collision() bool
        + draw(screen: pygame.Surface)
    }

    class Food {
        - position: tuple
        - color: tuple
        + __init__()
        + randomize_position()
        + draw(screen: pygame.Surface)
    }

    Game "1" *-- "1" Snake : KOMPOSISJON Game eier og styrer Snake
    Game "1" *-- "1" Food : KOMPOSISJON Game eier og genererer Food
    Snake --o Food : AGGREGERING Snake spiser Food, men kan eksistere uavhengig av Snake
