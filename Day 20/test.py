from time import sleep
from turtle import Turtle, Screen


def go_right():
    t.setheading(0)
def go_up():
    t.setheading(90)
def go_left():
    t.setheading(180)
def go_down():
    t.setheading(270)


t = Turtle()

sc = Screen()
sc.listen()
sc.onkey(go_right, "Right")
sc.onkey(go_left, "Left")
sc.onkey(go_up, "Up")
sc.onkey(go_down, "Down")


while True:

    t.forward(10)
    sleep(0.1)
    




sc.exitonclick()
