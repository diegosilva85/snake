from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

my_screen.listen()
my_screen.onkey(key="Up", fun=snake.up)
my_screen.onkey(key="Down", fun=snake.down)
my_screen.onkey(key="Left", fun=snake.left)
my_screen.onkey(key="Right", fun=snake.right)

game_on = True
while game_on:

    my_screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecta colisão com a comida.
    if snake.head.distance(food) < 15:
        food.refresh()
        score.new_score()
        snake.extend()

    # Detecta colisão com a parede.
    if snake.head.xcor() < -300 or snake.head.xcor() > 280 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        score.reset_game()
        snake.reset_snake()
        # score.game_over()
        # game_on = False


    # Detecta colisão com o rabo.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_game()
            snake.reset_snake()
            # score.game_over()
            # game_on = False

my_screen.exitonclick()
