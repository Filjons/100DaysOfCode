from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

my_screen = Screen()
'''timmy.up()
timmy.setposition(-100,0)
for lines in range(4):
    timmy.down()
    timmy.forward(30)
    timmy.up()
    timmy.left(90)

timmy.up()
timmy.setposition(-50,0)
for lines in range(5):
    timmy.down()
    timmy.forward(30)
    timmy.up()
    timmy.left(72)

timmy.up()
timmy.setposition(0,0)
for lines in range(6):
    timmy.down()
    timmy.forward(30)
    timmy.up()
    timmy.left(60)'''
sides = 2

while sides < 10:
    sides += 1
    angle = 360/sides

    for lines in range(sides):
        timmy.down()
        timmy.forward(60)
        timmy.up()
        timmy.left(angle)

my_screen.exitonclick()
