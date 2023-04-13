import numpy as np
from numpy import ndarray

from settings import Settings


class Vision:
    def __init__(self):
        self.size: int = 11
        self.neighbors: ndarray = np.zeros([self.size, self.size])

    def snake_vision(self, play_surface, snake_head_pos: tuple):
        for x in range(- int(self.size / 2), int(self.size / 2) + 1):
            for y in range(- int(self.size / 2), int(self.size / 2) + 1):
                temp_x: int = snake_head_pos[0] + x * 10 + 5
                temp_y: int = snake_head_pos[1] + y * 10 + 5
                if temp_x <= 0 or temp_x >= Settings.SCREEN_W or temp_y <= 0 or temp_y >= Settings.SCREEN_H:
                    self.neighbors[y + int(self.size / 2)][x + int(self.size / 2)] = 1
                else:
                    pixel_color = play_surface.get_at((temp_x, temp_y))
                    match pixel_color:
                        case Settings.SURFACE_COLOR:
                            temp_color = 0.5
                        case Settings.FOOD_COLOR:
                            temp_color = 1
                        case Settings.SNAKE_COLOR:
                            temp_color = 0
                        case _:
                            print(f'wrong color: {pixel_color}')
                            temp_color: int = 0
                    self.neighbors[y + int(self.size / 2)][x + int(self.size / 2)] = temp_color

        print(self.neighbors)
        print()
