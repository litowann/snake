from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake")

first_snake_body = Turtle("square")
second_snake_body = Turtle("square")
third_snake_body = Turtle("square")

first_snake_body.color("white")

second_snake_body.color("white")
second_snake_body.forward(20)

third_snake_body.color("white")
third_snake_body.forward(40)

screen.exitonclick()