from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


class MainScene:

    def __init__(self):
        # Default game screen settings
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("snake")
        self.screen.tracer(0)
        self.is_game_on = True

        # Instances implementation
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()

        # Snake controller
        self.snake_controller()
        self.screen.listen()

    def snake_controller(self):
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")

    def start(self):
        while self.is_game_on:
            self.screen.update()
            time.sleep(0.1)
            self.snake.move()

            # Detect collision with food
            if self.snake.head.distance(self.food) < 15:
                self.food.refresh()
                self.snake.extend()
                self.scoreboard.increase_score()

            # Detect collision with wall
            if (
                    self.snake.head.xcor() > 280
                    or self.snake.head.xcor() < - 280
                    or self.snake.head.ycor() > 280
                    or self.snake.head.ycor() < -280
            ):
                self.snake.reset()
                self.scoreboard.reset()

            # Detect collision with tail
            for segment in self.snake.segments[1:]:
                if self.snake.head.distance(segment) < 10:
                    self.snake.reset()
                    self.scoreboard.reset()
