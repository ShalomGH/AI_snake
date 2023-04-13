class Settings:
    SCREEN_W = 360
    SCREEN_H = 360
    FPS: int = 8

    # необходимые цвета
    SNAKE_COLOR: tuple = (0, 255, 0, 255)
    SURFACE_COLOR: tuple = (156, 159, 163, 255)
    FOOD_COLOR: tuple = (255, 0, 0, 255)
    TEXT_COLOR: tuple = (0, 0, 0)
    GAME_OVER_COLOR: tuple = (255, 0, 0)

    COLLISION: bool = True
    AUTORESTART_GAME: bool = False
