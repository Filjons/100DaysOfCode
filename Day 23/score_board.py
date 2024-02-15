from turtle import Turtle

class Scoreboard(Turtle):
    score = 0

    def __init__(self, position=(0, 0)):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.goto(position)
        self.old_score = -1

    '''def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False,
                   align="center", font=("Arial", 24, "normal"))
'''

    def write_score(self, score):
        
        if score > self.old_score:

            self.clear()
            self.write(str(score), move=False,
                   align="center", font=("Arial", 20, "normal"))
        
