from turtle import Turtle

class Scoreboard(Turtle):
    score = 0

    def __init__(self, position=(0,0)):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(position)
        

    '''def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False,
                   align="center", font=("Arial", 24, "normal"))
'''
    def new_score(self):
        self.score += 1
        self.refresh_score()
    
    def refresh_score(self):
        self.clear()
        self.write(str(self.score), move=False,
                   align="center", font=("Arial", 30, "normal"))
