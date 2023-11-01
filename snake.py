from turtle import Turtle
import time


class Snake:
    __starting_positions__ = [(0, 0), (-20, 0), (-40, 0)]
    __segments__ = []

    __is_game_on__ = True

    def set_position(self):
        for position in self.__starting_positions__:
            snake_segment = Turtle("square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(position)
            self.__segments__.append(snake_segment)

    def move(self, screen):
        while self.__is_game_on__:
            for segment in self.__segments__:
                segment.forward(20)
                screen.update()
                time.sleep(1)
