from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

my_screen = Screen()

timmy.forward(100)
timmy.left(90)
timmy.forward(100)

my_screen.exitonclick()