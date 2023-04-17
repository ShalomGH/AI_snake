import pygame
import time
import sys
from settings import Settings


class Game:
    def __init__(self, fps: int):
        self.play_surface = None
        self.fps = fps
        self.fps_controller = pygame.time.Clock()
        self.score = 0

    def set_surface_and_title(self):
        """Задаем surface(поверхность поверх которой будет все рисоваться)
        и устанавливаем заголовок окна"""
        self.play_surface = pygame.display.set_mode((
            Settings.SCREEN_W, Settings.SCREEN_H))
        pygame.display.set_caption('Snake Game')

    def refresh_screen(self):
        """Обновляем экран и задаем фпс"""
        pygame.display.flip()
        self.fps_controller.tick(self.fps)

    def show_score(self, choice: int = 1):
        """Отображение результата"""
        s_font = pygame.font.SysFont('monaco', 24)
        s_surf = s_font.render(
            'Score: {0}'.format(self.score), True, Settings.TEXT_COLOR)
        s_rect = s_surf.get_rect()
        if choice:
            s_rect.midleft = (int(Settings.SCREEN_W/16), int(Settings.SCREEN_H/16))
        else:
            s_rect.midtop = (int(Settings.SCREEN_W/2), int(Settings.SCREEN_H/4))
        self.play_surface.blit(s_surf, s_rect)

    def game_over(self, snake):
        """Функция для вывода надписи Game Over и результатов
        в случае завершения игры и выход из игры"""

        if Settings.GAME_AUTORESTART:
            self.score = 0
            snake.snake_head_pos = [100, 50]
            snake.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50], [60, 50], [50, 50]]
            snake.direction = "False"
            snake.change_to = snake.direction
            return
        else:
            go_font = pygame.font.SysFont('monaco', 72)
            go_surf = go_font.render('Game over', True, Settings.GAME_OVER_COLOR)
            go_rect = go_surf.get_rect()
            go_rect.midtop = (int(Settings.SCREEN_W / 2), int(Settings.SCREEN_H / 16))
            self.play_surface.blit(go_surf, go_rect)
            self.show_score(0)
            pygame.display.flip()
            time.sleep(3)
            pygame.quit()
            sys.exit()
