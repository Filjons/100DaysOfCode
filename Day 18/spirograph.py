from turtle import Turtle, Screen
from random import choice, randint

'''turtle.home()
turtle.position()
(0.00, 0.00)
turtle.heading()
0.0
turtle.circle(50)
turtle.position()
(-0.00, 0.00)
turtle.heading()
0.0
turtle.circle(120, 180)  # draw a semicircle
turtle.position()
(0.00, 240.00)
turtle.heading()'''


def new_color():

    for n in range(3):

        color = (randint(1, 255), randint(1, 255), randint(1, 255))
    return color


timmy = Turtle()
timmy.pensize(3)
timmy.speed(0)

my_screen = Screen()
my_screen.colormode(255)
for directions in range(36):
    timmy.down()
    timmy.pencolor(new_color())
    timmy.circle(100)
    timmy.up()
    timmy.left(10)

my_screen.exitonclick()
