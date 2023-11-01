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

# Snake controller
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.listen()

snake.move(screen)

# Exit from the screen
screen.exitonclick()