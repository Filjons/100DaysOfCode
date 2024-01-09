from turtle import Turtle


class Padel(Turtle):

    def __init__(self, position=(0, 0)):
        super().__init__()
        self.up()
        self.speed('fastest')
        self.shape('square')
        self.color('white')
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        if self.ycor() < 240:
            ycor = self.ycor()

            self.goto(self.xcor(), ycor + 20)

    def go_down(self):
        if self.ycor() > -240:
            ycor = self.ycor()

            self.goto(self.xcor(), ycor - 20)
