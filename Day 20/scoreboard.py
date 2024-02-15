from turtle import Turtle


class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.set_board()
        self.refresh_score()

    def set_board(self):
        self.goto(0, 280)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False,
                   align="center", font=("Arial", 24, "normal"))

    def new_score(self):
        self.score += 1
        self.clear()
        self.refresh_score()

    def refresh_score(self):
        self.write("Score: " + str(self.score), move=False,
                   align="center", font=("Arial", 14, "normal"))
