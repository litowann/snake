from turtle import Screen
from snake import Snake
from food import Food
import time

is_game_on = True

# Default game screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake")
screen.tracer(0)

# Snake and Food implementation
snake = Snake()
food = Food()

# Snake controller
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.listen()

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()


# Exit from the screen
screen.exitonclick()