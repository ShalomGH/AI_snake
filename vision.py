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
                    self.neighbors[y + 5][x + 5] = 1
                else:
                    pixel_color = str(play_surface.get_at((temp_x, temp_y)))
                    match pixel_color:
                        case "(156, 159, 163, 255)":
                            temp_color = 0
                        case "(255, 0, 0, 255)":
                            temp_color = 0.5
                        case "(0, 255, 0, 255)":
                            temp_color = 1
                        case _:
                            print(pixel_color)
                            temp_color: int = 1
                    self.neighbors[y + 5][x + 5] = temp_color

        print(self.neighbors)
        print()
