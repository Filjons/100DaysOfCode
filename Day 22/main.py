
# Pong game
from time import sleep
from turtle import Screen
from padel import Padel
from divider import Divider
from scoreboard import Scoreboard
from ball import Ball

Y_LIMIT = 270
X_LIMIT = 250


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Padels
padel_r = Padel((270, 0))
padel_l = Padel((-270, 0))

# Ball
ball = Ball()

# Scoreboards
score_one = Scoreboard((30, 260))
score_one.refresh_score()
score_two = Scoreboard((-30, 260))
score_two.refresh_score()

# Divider
net = Divider()

screen.listen()
screen.onkeypress(padel_r.go_up, "o")
screen.onkeypress(padel_r.go_down, "l")
screen.onkeypress(padel_l.go_up, "q")
screen.onkeypress(padel_l.go_down, "a")

game_on = True
while game_on:
    sleep(0.1)
    screen.update()
    ball.move()
    ball.wall_collision(y_limit=Y_LIMIT)
    ball.padel_collision(x_limit=X_LIMIT, padel_distance=ball.distance(padel_r))
    ball.padel_collision(x_limit=-X_LIMIT, padel_distance=ball.distance(padel_l))


