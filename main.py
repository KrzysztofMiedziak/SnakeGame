from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')

score_board = ScoreBoard()
snake = Snake()
food = Food()
screen.listen()
screen.onkey(key='Up', fun=snake.turn_up)
screen.onkey(key='Down', fun=snake.turn_down)
screen.onkey(key='Left', fun=snake.turn_left)
screen.onkey(key='Right', fun=snake.turn_right)

game_is_on = True
COLLISION_PONT = 300
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        score_board.add_score()
        food.refresh(snake.snake_segments)

    # Detect collision with the wall
    if (snake.head.xcor() > 280 or
            snake.head.xcor() < -290 or
            snake.head.ycor() > COLLISION_PONT or
            snake.head.ycor() < -COLLISION_PONT):
        score_board.reset()
        snake.reset()

    # Detect collision with the tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()

screen.exitonclick()
