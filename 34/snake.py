from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCES = 20


class Snake:

    def __init__(self):

        self.snake_segments = []
        self.create_snake()

    def create_snake(self):

        for position in STARTING_POSITIONS:

            snake_body = Turtle(shape="square")
            snake_body.color("white")
            snake_body.penup()
            snake_body.goto(position)

            self.snake_segments.append(snake_body)

    def move_snake(self, direction):
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment - 1].xcor()
            new_y = self.snake_segments[segment - 1].ycor()

          return self.snake_segments[segment].goto(new_x, new_y)

        # self.snake_segments[0].forward(
        #     MOVE_DISTANCES), self.snake_segments[0].left(90)

    def up(self):
        self.move_snake()

    def down(self):
        pass

    def left(self):
        pass

    def right(self):
        pass
