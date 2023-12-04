
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

my_screen = Screen()

for lines in range(10):
    timmy.down()
    timmy.forward(10)
    timmy.up()
    timmy.forward(10)

my_screen.exitonclick()
