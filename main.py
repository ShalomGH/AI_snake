import pygame
import sys
from snake import Snake
from game import Game
from food import Food
from vision import Vision
from settings import Settings
from func import init_and_check_for_errors


init_and_check_for_errors()

game: Game = Game(Settings.FPS)
snake: Snake = Snake(Settings.SNAKE_COLOR)
food = Food(Settings.FOOD_COLOR)
vision = Vision()

game.set_surface_and_title()
pushed: bool = False


def event_loop(change_to) -> str:
    """Функция для отслеживания нажатий клавиш игроком"""
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            global pushed
            pushed = True
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = "RIGHT"
            elif event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = "LEFT"
            elif event.key == pygame.K_UP or event.key == ord('w'):
                change_to = "UP"
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = "DOWN"
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    return change_to


while True:
    snake.change_to = event_loop(snake.change_to)

    snake.change_direction()
    snake.change_head_position()
    game.score, food.food_pos = snake.snake_body_mechanism(game.score, food.food_pos)

    snake.draw_snake(game.play_surface, Settings.SURFACE_COLOR)
    food.draw_food(game.play_surface)
    vision.snake_vision(game.play_surface, snake.snake_head_pos)

    if pushed and Settings.COLLISION:
        snake.check_for_boundaries(game.game_over)

    game.show_score()
    game.refresh_screen()
