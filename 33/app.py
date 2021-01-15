from turtle import Turtle, Screen, shape, textinput
import turtle
import random

is_race = False

turtle_colours = ["red", "purple", "orange", "yellow", "green", "blue"]
all_turtles = []

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bets",
                            prompt="Which turtle will take the coverted trophy? Pick the colour and cross your fingers.\n")

y_position = -130

for turtle_indx in range(0, 6):

    turtle = Turtle(shape="turtle")
    turtle.color(turtle_colours[turtle_indx])
    turtle.penup()

    turtle.goto(x=-230, y=y_position)
    y_position += 50

    all_turtles.append(turtle)

if user_bet:
    is_race = True

while is_race:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race = False
            win_turtle = turtle.pencolor()

            if user_bet == win_turtle:
                print("Congradulations You Win!")
            else:
                print("Sorry but your turtle lost")

        speed = random.randint(0, 10)
        turtle.forward(speed)


screen.exitonclick()
