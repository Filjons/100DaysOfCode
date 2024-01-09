from turtle import Turtle, xcor, ycor

X_LIMIT = 270




class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.up()
        self.shape('square')
        self.color('white')
        self.shapesize(1.0, 1.0)
        self.move_x = 10
        self.move_y = 10

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_x(self):
       
        self.move_x *= -1

    def bounce_y(self):
       
        self.move_y *= -1

    def wall_collision(self, y_limit):
       
        if self.ycor() > y_limit or self.ycor() < -y_limit:
            self.bounce_y()
    
    def padel_collision(self, x_limit, padel_distance):
        print(padel_distance)
        if x_limit > 0 and self.xcor() > x_limit :
            print(self.xcor())
            if padel_distance < 10:
                print("padel hit")
                self.bounce_x()
        elif x_limit < 0 and self.xcor() < x_limit:
            print(self.xcor())
            if padel_distance < 10:
                self.bounce_x()
