from turtle import Turtle


class Ball(Turtle):

    def __init__(self, x_limit, y_limit, padel_limit):
        super().__init__()
        self.up()
        self.shape('square')
        self.color('white')
        self.shapesize(1.0, 1.0)
        self.move_x = 10
        self.move_y = 10
        self.x_limit = x_limit
        self.y_limit = y_limit
        self.right_padel_limit = padel_limit
        self.left_padel_limit = -padel_limit

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)
        print(self.xcor(), new_x)
        if new_x > 0 and new_x > self.x_limit:
            self.ball_reset()
            return 1
        elif new_x < 0 and new_x < -self.x_limit:
            self.ball_reset()
            return 2
        return 0

    def bounce_x(self):

        self.move_x *= -1

    def bounce_y(self):

        self.move_y *= -1

    def ball_reset(self):
        self.bounce_x()
        self.goto(0, 0)

    def wall_collision(self):

        if self.ycor() > self.y_limit:
            self.bounce_y()

    def padel_collision(self, padel_distance):

        if self.right_padel_limit > 0 and self.xcor() > self.right_padel_limit:
            
            if padel_distance < 200:
                print("padel hit")
                self.bounce_x()
        elif self.left_padel_limit < 0 and self.xcor() < self.left_padel_limit:
            
            if padel_distance < 200:
                self.bounce_x()
