from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.go_up,"Up")
screen.onkey(snake.go_down,"Down")
screen.onkey(snake.go_left,"Left")
screen.onkey(snake.go_right,"Right")

game_on = True
while game_on:
    screen.update()
    snake.move_snake()

    if snake.head.distance(food) < 20:
        food.refresh()      

screen.exitonclick()