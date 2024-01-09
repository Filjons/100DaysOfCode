
# Pong game
from time import sleep
from turtle import Screen
from padel import Padel
from divider import Divider
from scoreboard import Scoreboard
from ball import Ball
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Padels
padel_one = Padel((270, 0))
padel_two = Padel((-270, 0))

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
screen.onkeypress(padel_one.go_up, "o")
screen.onkeypress(padel_one.go_down, "l")
screen.onkeypress(padel_two.go_up, "q")
screen.onkeypress(padel_two.go_down, "a")

game_on = True
while game_on:
    sleep(0.1)
    screen.update()
    ball.move()
    ball.collision()
