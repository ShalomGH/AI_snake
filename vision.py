import numpy as np


class Vision:
    def __init__(self):
        self.size = 11
        self.neighbors = np.zeros([self.size, self.size])

    def snake_vision(self, play_surface, snake_head_pos, screen_width, screen_height):
        for x in range(- int(self.size / 2), int(self.size / 2) + 1):
            for y in range(- int(self.size / 2), int(self.size / 2) + 1):
                temp_x = snake_head_pos[0] + x * 10 + 5
                temp_y = snake_head_pos[1] + y * 10 + 5
                if temp_x <= 0 or temp_x >= screen_width or temp_y <= 0 or temp_y >= screen_height:
                    self.neighbors[y + 5][x + 5] = -1
                else:
                    pixel_color = str(play_surface.get_at((temp_x, temp_y)))
                    match pixel_color:
                        case "(255, 255, 255, 255)":
                            temp_color = 0
                        case "(0, 255, 0, 255)":
                            temp_color = -1
                        case "(255, 0, 0, 255)":
                            temp_color = 1
                        case _:
                            temp_color = -1
                    self.neighbors[y + 5][x + 5] = temp_color
        print(self.neighbors)
        print()
