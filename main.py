from turtle import Screen
from snake import Snake

# Default game screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake")
screen.tracer(0)

# Snake implementation
snake = Snake()
snake.set_position()
snake.move(screen)

screen.exitonclick()