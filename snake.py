import pygame
import random
from settings import Settings


class Snake:
    def __init__(self, snake_color):
        # важные переменные - позиция головы змеи и его тела
        self.snake_head_pos = [100, 50]  # [x, y]
        # начальное тело змеи состоит из трех сегментов
        # голова змеи - первый элемент, хвост - последний
        self.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50], [60, 50], [50, 50]]
        self.snake_color = snake_color
        # направление движения змеи, изначально
        # зададимся вправо

        self.direction = "False"
        # куда будет меняться направление движения змеи
        # при нажатии соответствующих клавиш
        self.change_to = self.direction

    def validate_direction_and_change(self):
        """Изменяем направление движения змеи только в том случае,
        если оно не прямо противоположно текущему"""
        if any((self.change_to == "RIGHT" and not self.direction == "LEFT",
                self.change_to == "LEFT" and not self.direction == "RIGHT",
                self.change_to == "UP" and not self.direction == "DOWN",
                self.change_to == "DOWN" and not self.direction == "UP")):
            self.direction = self.change_to

    def change_head_position(self):
        """Изменяем положение головы змеи"""
        match self.direction:
            case "False":
                self.snake_head_pos[0] += 0
            case "RIGHT":
                self.snake_head_pos[0] += 10
            case "LEFT":
                self.snake_head_pos[0] -= 10
            case "UP":
                self.snake_head_pos[1] -= 10
            case "DOWN":
                self.snake_head_pos[1] += 10

    def snake_body_mechanism(self, score, food_pos):
        # если вставлять просто snake_head_pos,
        # то на всех трех позициях в snake_body
        # окажется один и тот же список с одинаковыми координатами
        # и мы будем управлять змеей из одного квадрата
        self.snake_body.insert(0, list(self.snake_head_pos))
        # если съели еду
        if (self.snake_head_pos[0] == food_pos[0] and
                self.snake_head_pos[1] == food_pos[1]):

            # если съели еду, то задаем новое положение еды случайным
            # образом и увеличивем score на один
            food_pos = [random.randrange(1, Settings.SCREEN_W / 10) * 10,
                        random.randrange(1, Settings.SCREEN_H / 10) * 10]
            while food_pos in self.snake_body:
                food_pos = [random.randrange(1, Settings.SCREEN_W / 10) * 10,
                            random.randrange(1, Settings.SCREEN_H / 10) * 10]
            score += 1
        else:
            # если не нашли еду, то убираем последний сегмент,
            # если этого не сделать, то змея будет постоянно расти
            self.snake_body.pop()
        return score, food_pos

    def draw_snake(self, play_surface, surface_color):
        """Отображаем все сегменты змеи"""
        play_surface.fill(surface_color)
        for pos in self.snake_body:
            pygame.draw.rect(play_surface, self.snake_color, pygame.Rect(pos[0], pos[1], 10, 10))

    def check_for_boundaries(self, game_over):
        """Проверка, что столкнулись с концами экрана или сами с собой"""
        if any((
                self.snake_head_pos[0] > Settings.SCREEN_W - 10
                or self.snake_head_pos[0] < 0,
                self.snake_head_pos[1] > Settings.SCREEN_H - 10
                or self.snake_head_pos[1] < 0
        )):
            game_over()
        for block in self.snake_body[1:]:
            # проверка на то, что первый элемент(голова) врезался в
            # любой другой элемент змеи (закольцевались)
            if (block[0] == self.snake_head_pos[0] and
                    block[1] == self.snake_head_pos[1]):
                game_over()
