# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import random
import turtle as t

color_list = [(54, 108, 149), (225, 201, 108), (134, 85, 58), (224, 141, 62), (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122), (69, 101, 86), (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202), (58, 47, 41), (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95), (118, 125, 145), (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52)]

tom = t.Turtle()
t.colormode(255)
tom.penup()
tom.hideturtle()
tom.goto(-250, -250)
tom.pendown()
t.speed(10)


def row():
    for i in range(10):
        tom.pendown()
        random_color = random.choice(color_list)
        tom.dot(20, random_color)
        tom.penup()
        tom.forward(50)


def draw():
    y_coord = -250
    while y_coord < 250:
        row()
        tom.goto(-250, y_coord+50)
        y_coord = y_coord + 50

draw()
print(t.screensize())

screen = t.Screen()
screen.exitonclick()
