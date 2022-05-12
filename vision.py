import numpy as np


class Vision:
    def __init__(self):
        self.size = 11
        self.neighbors = np.zeros([self.size, self.size])

    def snake_vision(self, play_surface, snake_head_pos, screen_width, screen_height):
        for x in range(- int(self.size / 2), int(self.size / 2)):
            for y in range(- int(self.size / 2), int(self.size / 2)):
                temp_x = snake_head_pos[0] + x * 10 + 5
                temp_y = snake_head_pos[1] + y * 10 + 5
                pixel_color = str(play_surface.get_at(
                    (min(max(temp_x, 0), screen_width - 1), min(max(temp_y, 0), screen_height - 1))))
                match pixel_color:
                    case "(255, 255, 255, 255)":
                        temp_color = 0
                    case "(0, 255, 0, 255)":
                        temp_color = 2
                    case "(255, 0, 0, 255)":
                        temp_color = 1
                    case "(0, 0, 0, 255)":
                        temp_color = 9
                    case _:
                        temp_color = 8
                self.neighbors[y + 5][x + 5] = temp_color
        print(self.neighbors)
        print()
