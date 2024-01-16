from turtle import Turtle, xcor, ycor


class Little_turtle(Turtle):

    def __init__(self, x_limit, y_limit, start_position, finish_position):
        super().__init__()
        
        self.x_limit = x_limit
        self.y_limit = y_limit
        self.score = 0
        self.goal = finish_position
        self.start = start_position

        self.up()
        self.shape('turtle')
        self.color('green')
        self.shapesize(1.0, 1.0)
        self.setheading(90)
        self.goto(self.start)


    def go_forward(self):
        pos = (self.xcor(), self.ycor() + 10)
        self.goto(pos)

    def go_right(self):
        pos = (self.xcor() + 10, self.ycor())
        self.goto(pos)
    
    def go_left(self):
        pos = (self.xcor() - 10, self.ycor())
        self.goto(pos)

    def turtle_reset(self):
       
        self.goto(self.start)

    def turtle_win(self):

        if self.ycor() >= self.goal:
            self.score += 1
            self.turtle_reset()

    def car_collision(self, padel_distance):

        if self.right_padel_limit > 0 and self.xcor() > self.right_padel_limit:
            
            if padel_distance < 200:
                
                self.bounce_x()
        elif self.left_padel_limit < 0 and self.xcor() < self.left_padel_limit:
            
            if padel_distance < 200:
                self.bounce_x()
