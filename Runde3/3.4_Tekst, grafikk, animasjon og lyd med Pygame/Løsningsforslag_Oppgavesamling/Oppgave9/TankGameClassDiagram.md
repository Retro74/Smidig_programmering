```mermaid

classDiagram
    class Tank {
        - tank_image:pygame.image
        - turret_image:pygame.image
        - TURRET_OFFSET:tuple='25,25'
        - rect:pygame.rect
        - speed
        - angle
        - turret_angle
        - size
        + __init__(x, y, size=1)
        + move(keys)
        + rotate_turret(keys)
        + draw(screen)
    }
