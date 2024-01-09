from turtle import Turtle, xcor, ycor

X_LIMIT = 250
Y_LIMIT = 250


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.up()
        self.shape('square')
        self.color('white')
        self.move_x = 10
        self.move_y = 10

    def move(self):
        new_x = xcor() + self.move_x
        new_y = ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_y(self):
       
        self.move_y = -1 * self.move_y

    def collision(self):
       
        if self.ycor() > Y_LIMIT or self.ycor() < -Y_LIMIT:
            self.bounce_y()
        
