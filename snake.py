from turtle import Turtle
from constants import *
import time


class Snake():
    def __init__(self):
        self.segments = []
        self.set_position()
        self.head = self.segments[0]

    def set_position(self):
        for position in STARTING_POSITIONS:
            snake_segment = Turtle("square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(position)
            self.segments.append(snake_segment)

    def move(self):
        for segment_index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[segment_index - 1].xcor()
            y = self.segments[segment_index - 1].ycor()
            self.segments[segment_index].goto(x, y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN_DIRECTION:
            self.head.setheading(UP_DIRECTION)

    def down(self):
        if self.head.heading() != UP_DIRECTION:
            self.head.setheading(DOWN_DIRECTION)

    def left(self):
        if self.head.heading() != RIGHT_DIRECTION:
            self.head.setheading(LEFT_DIRECTION)

    def right(self):
        if self.head.heading() != LEFT_DIRECTION:
            self.head.setheading(RIGHT_DIRECTION)
