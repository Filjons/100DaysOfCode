from turtle import Turtle


class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.refresh_score()
        self.goto(100,300)

    def new_score(self):
        self.score += 1
        self.refresh_score()

    def refresh_score(self):
        self.write("Score: " + str(self.score), move=False, align="center", font=("Arial", 8, "normal"))