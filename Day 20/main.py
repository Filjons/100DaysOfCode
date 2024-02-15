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
#scoreboard.set_board()
#scoreboard.refresh_score()
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

game_on = True
while game_on:
    screen.update()
    snake.move_snake()

    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.new_score()
        snake.add_section()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()
    
    for segment in snake.sections[1:]:
        
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
