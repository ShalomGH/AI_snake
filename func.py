import pygame
import sys


def init_and_check_for_errors():
    """Начальная функция для инициализации и
       проверки как запустится pygame"""
    check_errors = pygame.init()
    if check_errors[1] > 0:
        sys.exit()
