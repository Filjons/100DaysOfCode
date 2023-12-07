from turtle import Turtle, Screen

tur = Turtle()
myscreen = Screen()


def w():
    tur.forward(10)


def s():
    tur.back(10)


def d():
    tur.right(10)


def a():
    tur.left(10)

def clear():
    tur.reset()


myscreen.onkey(key="w", fun=w)
myscreen.onkey(key="s", fun=s)
myscreen.onkey(key="d", fun=d)
myscreen.onkey(key="a", fun=a)
myscreen.onkey(key="c", fun=clear)

myscreen.listen()
myscreen.exitonclick()
