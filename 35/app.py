from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Turtle Pong")
screen.tracer(0)

paddle_one = Paddle((350, 0))
paddle_two = Paddle((-350, 0))


screen.listen()
screen.onkey(paddlemove_up, "Up")
screen.onkey(move_down, "Down")

game_on = True

while game_on:
    screen.update()

screen.exitonclick()
