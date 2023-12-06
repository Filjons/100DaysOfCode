from random import choice
import colorgram
from turtle import Turtle, Screen


def get_colors():

    colors = colorgram.extract(
        "C:\\Users\\filjon\\OneDrive - Mildef\\Dokument\\Code\\100DaysOfCode\\Day 18\\painting\\my_image.jpg", 30)

    rgb_colors = []
    for color in colors:
        rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

    return rgb_colors


def new_dot(color_list):
    color = choice(color_list)
    my_turtle.dot(20, color)


def move(x, y):
    
    my_turtle.goto(x, y)


my_colors = get_colors()
my_turtle = Turtle()
my_turtle.up()
my_turtle.hideturtle()
my_turtle.speed(0)
my_screen = Screen()
my_screen.colormode(255)


for y in range(-300, 300, 60):

    for x in range(-300, 300, 60):
        move(x, y)
        new_dot(my_colors)

my_screen.exitonclick()