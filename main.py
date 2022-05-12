from snake import Snake
from game import Game
from food import Food
from func import init_and_check_for_errors, event_loop

game = Game()
snake = Snake(game.green)
food = Food(game.brown, game.screen_width, game.screen_height)
pushed = False
init_and_check_for_errors()
game.set_surface_and_title()

while True:
    snake.change_to = event_loop(snake.change_to)

    snake.validate_direction_and_change()
    snake.change_head_position()
    game.score, food.food_pos = snake.snake_body_mechanism(game.score, food.food_pos, game.screen_width, game.screen_height)
    snake.draw_snake(game.play_surface, game.white)

    food.draw_food(game.play_surface)
    if pushed:
        snake.check_for_boundaries(game.game_over, game.screen_width, game.screen_height)

    game.show_score()
    game.refresh_screen()