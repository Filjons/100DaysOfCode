from random import randint
from turtle import Turtle, Screen


screen = Screen()
screen.setup(height=500,width=400)
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
player_bet = screen.textinput(title="Turtle race", prompt="Who will win?")

def make_turtles():
    turtles = []
    
    for color in colors:
        turtle = Turtle()
        turtle.up()
        turtle.shape("turtle")
        turtle.color(color)
        turtles.append(turtle)
    return turtles

turtle_list = make_turtles()

y = -150
x = -150
for t in turtle_list:
    y += 50
    t.goto(x,y)

run = True
while run:
    for t in turtle_list:
        x = t.pos()[0]
        y = t.pos()[1]
        x += randint(0, 10)
        t.goto(x, y)
        if t.pos()[0] > 100:
            run = False
            winner = str(t.color()[0])
            print(f"The {winner} turtle wins!")
            if winner == player_bet:
                print('You win!')
            else:
                print('Your turtle lost!')
            break
    
screen.exitonclick()
