```mermaid

classDiagram
    class Background {
        - pygame.Surface image
        - int image_width
        - float speed
        - int x_pos
        + __init__(image_path: str, image_width: int, speed: float)
        + update(screen: pygame.Surface)
    }

    class Bird {
        - pygame.Surface image
        - int image_width
        - int image_height
        - float x_pos
        - float y_pos
        - float y_speed
        + __init__(image_path: str, image_width: int, image_height: int, x_pos: float, y_pos: float, x_speed: float = 0)
        + update(screen: pygame.Surface)
    }

    class Obstacle {
        - pygame.Surface image
        - int width
        - int height
        - float x_pos
        - float y_pos
        - float speed
        + __init__(image_path: str, width: int, height: int, x_pos: float, y_pos: float, speed: float)
        + update(screen: pygame.Surface)
        + check_collision(bird: Bird) bool
    }

    Bird -- Obstacle : sjekker kollisjon
