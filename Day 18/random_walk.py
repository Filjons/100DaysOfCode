from turtle import Turtle, Screen
from random import choice, randint


def new_color():
    
    for n in range(3):
        
        color = (randint(1, 255), randint(1, 255), randint(1, 255))
    return color


def new_direction():
    direction = choice([0, 90, 180, 270])
    return direction


timmy = Turtle()
timmy.pensize(5)
timmy.speed(10)
my_screen = Screen()
my_screen.colormode(255)
for directions in range(500):
    timmy.down()
    timmy.left(new_direction())
    
    timmy.pencolor(new_color())
    timmy.forward(20)
    timmy.up()

my_screen.exitonclick()
