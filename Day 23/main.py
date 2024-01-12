
# Crossing game
from time import sleep
from turtle import Screen
from little_turtle import Little_turtle

Y_LIMIT = 270
X_LIMIT = 270
START_POSITION = (0, -280)
# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

# The player turtle
timmy_turtle = Little_turtle(X_LIMIT, Y_LIMIT, START_POSITION)

# The score
#score = Scoreboard((30, 260))

# Game mechanics
screen.listen()
screen.onkeypress(timmy_turtle.go_forward, "w")
screen.onkeypress(timmy_turtle.go_right, "d")
screen.onkeypress(timmy_turtle.go_left, "a")


game_on = True
while game_on:
    sleep(0.1)
    screen.update()
    
    #bal.padel_collision(padel_distance=ball.distance(padel_l))
    

