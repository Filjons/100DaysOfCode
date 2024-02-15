from turtle import Turtle, Screen

tur = Turtle()
myscreen = Screen()
def move_foreward():
    tur.forward(10)

myscreen.listen()
myscreen.onkey(key="space", fun=move_foreward)
myscreen.exitonclick()