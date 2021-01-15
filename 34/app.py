from turtle import Turtle, Screen
import turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Snake Turtle")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]

snake_segments = []

for position in starting_position:

    snake_body = Turtle(shape="square")
    snake_body.color("white")
    snake_body.penup()
    snake_body.goto(position)

    snake_segments.append(snake_body)

screen.update()


game_on = True

while game_on:
    for segment in snake_segments:
        segment.forward(20)

screen.exitonclick()
