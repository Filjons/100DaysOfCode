
# Crossing game
from time import sleep
from turtle import Screen
from little_turtle import Little_turtle
from score_board import Scoreboard
from car import Car

Y_LIMIT = 270
X_LIMIT = 270
START_POSITION = (0, -280)
FINISH_POSITION = 280
SCOREBOARD_POS = (-290, 270)
# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)
screen.colormode(255)

# The player turtle
timmy_turtle = Little_turtle(X_LIMIT, Y_LIMIT, START_POSITION, FINISH_POSITION)

# The score
scoreboard = Scoreboard(SCOREBOARD_POS)
traffic = []
for i in range(0, 100):
    traffic.append(Car(x_stop=-260, x_start=300))

# Game mechanics
screen.listen()
screen.onkeypress(timmy_turtle.go_forward, "w")
screen.onkeypress(timmy_turtle.go_right, "d")
screen.onkeypress(timmy_turtle.go_left, "a")


game_on = True
while game_on:
    sleep(0.1)
    for c in traffic:
        c.car_move()
        if timmy_turtle.distance(c) < 20:
            game_on = False
            timmy_turtle.turtle_game_over()
    
    timmy_turtle.turtle_win()
    scoreboard.write_score(timmy_turtle.score)

    screen.update()
    
    #bal.padel_collision(padel_distance=ball.distance(padel_l))
    

