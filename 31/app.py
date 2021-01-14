# import colorgram


# rgb_colours = []
# colours = colorgram.extract('art.jpg', 16)


# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     rgb_tuple = (r, g, b)
#     rgb_colours.append(rgb_tuple)

# print(rgb_colours)

import turtle as turtle
import random

drawing_turtle = turtle.Turtle()
drawing_turtle.speed("fastest")
drawing_turtle.penup()

colour_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227),
               (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47)]

drawing_turtle.setheading(225)
drawing_turtle.forward(300)
drawing_turtle.setheading(0)
number_dots = 100

for dot in range(1, number_dots + 1):

    turtle.colormode(255)
    drawing_turtle.dot(30, random.choice(colour_list))
    drawing_turtle.forward(50)

    if dot % 10 == 0:

        drawing_turtle.setheading(90)
        drawing_turtle.forward(50)
        drawing_turtle.setheading(180)
        drawing_turtle.forward(500)
        drawing_turtle.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
