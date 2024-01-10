from turtle import Turtle, xcor, ycor


class Ball(Turtle):

    def __init__(self, x_limit, y_limit):
        super().__init__()
        self.up()
        self.shape('square')
        self.color('white')
        self.shapesize(1.0, 1.0)
        self.move_x = 10
        self.move_y = 10
        self.x_limit = x_limit
        self.y_limit = y_limit

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)
        if new_x > 0 and new_x > self.x_limit:
            self.reset()
        elif new_x < 0 and new_x < -self.x_limit:
            self.reset()    
        

    def bounce_x(self):
       
        self.move_x *= -1

    def bounce_y(self):
       
        self.move_y *= -1
    
    def ball_reset(self):
        self.bounce_x()
        self.goto(0,0)

    def wall_collision(self):
       
        if self.ycor() > self.y_limit:
            self.bounce_y()
    
    def padel_collision(self, padel_limit, padel_distance):
        
        if padel_limit > 0 and self.xcor() > padel_limit :
            print(self.xcor())
            if padel_distance < 200:
                print("padel hit")
                self.bounce_x()
        elif padel_limit < 0 and self.xcor() < padel_limit:
            print(self.xcor())
            if padel_distance < 200:
                self.bounce_x()