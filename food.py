import numpy as np
import pygame
import random
from settings import Settings


class Food:
    def __init__(self, food_color: tuple):
        """Инициализации еды"""
        self.food_color = food_color
        self.food_size_x = 10
        self.food_size_y = 10
        self.food_pos = np.array([random.randrange(1, Settings.SCREEN_W / 10) * 10,
                                  random.randrange(1, Settings.SCREEN_H / 10) * 10])

    def draw_food(self, play_surface):
        """Отображение еды"""
        pygame.draw.rect(
            play_surface, self.food_color, pygame.Rect(
                self.food_pos[0], self.food_pos[1],
                self.food_size_x, self.food_size_y))
