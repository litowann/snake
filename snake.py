from turtle import Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    __is_game_on__ = True

    def __init__(self):
        self.segments = []
        self.set_position()

    def set_position(self):
        for position in STARTING_POSITIONS:
            snake_segment = Turtle("square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(position)
            self.segments.append(snake_segment)

    def move(self, screen):
        while self.__is_game_on__:
            screen.update()
            time.sleep(0.1)

            for segment_index in range(len(self.segments) - 1, 0, -1):
                x = self.segments[segment_index - 1].xcor()
                y = self.segments[segment_index - 1].ycor()
                self.segments[segment_index].goto(x, y)

            self.segments[0].forward(MOVE_DISTANCE)
