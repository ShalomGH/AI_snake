import pygame
import time
import sys
from settings import Settings


class Game:
    def __init__(self, fps):
        self.play_surface = None
        self.fps = fps

        # Frame per second controller
        # будет задавать количество кадров в секунду
        self.fps_controller = pygame.time.Clock()

        # переменная для отображения результата
        # (сколько еды съели)
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

    def show_score(self, choice=1):
        """Отображение результата"""
        s_font = pygame.font.SysFont('monaco', 24)
        s_surf = s_font.render(
            'Score: {0}'.format(self.score), True, Settings.TEXT_COLOR)
        s_rect = s_surf.get_rect()
        # дефолтный случай отображаем результат слева сверху
        if choice == 1:
            s_rect.midtop = (80, 10)
        # при game_over отображаем результат по центру
        # под надписью game over
        else:
            s_rect.midtop = (360, 120)
        # рисуем прямоугольник поверх surface
        self.play_surface.blit(s_surf, s_rect)

    def game_over(self):
        """Функция для вывода надписи Game Over и результатов
        в случае завершения игры и выход из игры"""
        go_font = pygame.font.SysFont('monaco', 72)
        go_surf = go_font.render('Game over', True, Settings.GAME_OVER_COLOR)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (360, 15)
        self.play_surface.blit(go_surf, go_rect)
        self.show_score(0)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()
