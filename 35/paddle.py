from turtle import Turtle


class Paddle(Turtle):

    def _init__(self, position):
        super().__init__()

        self.shape("square")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
