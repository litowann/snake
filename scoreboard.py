from turtle import Turtle
from constants import ALIGNMENT, FONT


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write_message(f"Score {self.score}", 0, 270)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.write_message("GAME OVER")
        self.write_message(f"YOUR FINAL SCORE: {self.score}", 0, -30)

    def write_message(self, message, x=0, y=0):
        self.goto(x, y)
        self.write(message, align=ALIGNMENT, font=FONT)