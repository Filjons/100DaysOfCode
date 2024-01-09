
from turtle import Turtle


class Divider(Turtle):

    def __init__(self):
        super().__init__()
        self.dividers = []
        self.new_divider()

    def new_divider(self):
        y = 290
        for n in range(0, 16):
            div = Turtle()
            div.up()
            div.speed('fastest')
            div.shape('square')
            div.color('white')
            div.goto(0, y)
            div.resizemode("user")
            div.shapesize(1, 0.1, 0.5)
            y -= 40
            self.dividers.append(div)
