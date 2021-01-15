from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def move_cclockwise():
    turtle.left(10)


def move_clockwise():
    turtle.right(10)


screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_cclockwise)
screen.onkey(key="d", fun=move_clockwise)

screen.exitonclick()
