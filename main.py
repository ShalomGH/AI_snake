import pygame
import sys
from snake import Snake
from game import Game
from food import Food
from func import init_and_check_for_errors

colission_true = True
game = Game()
snake = Snake(game.green)
food = Food(game.brown, game.screen_width, game.screen_height)
pushed = False
init_and_check_for_errors()
game.set_surface_and_title()


def event_loop(change_to):
    """Функция для отслеживания нажатий клавиш игроком"""
    # запускаем цикл по ивентам
    for event in pygame.event.get():
        # если нажали клавишу
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
            # нажали escape
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    return change_to


while True:
    snake.change_to = event_loop(snake.change_to)

    snake.validate_direction_and_change()
    snake.change_head_position()
    game.score, food.food_pos = snake.snake_body_mechanism(game.score, food.food_pos, game.screen_width, game.screen_height)
    snake.draw_snake(game.play_surface, game.white)

    food.draw_food(game.play_surface)

    if pushed and colission_true:
        snake.check_for_boundaries(game.game_over, game.screen_width, game.screen_height)

    game.show_score()
    game.refresh_screen()