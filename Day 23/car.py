from random import randint
from turtle import Turtle, xcor, ycor


class Car(Turtle):

    def __init__(self, x_start, x_stop, car_speed = 1):
        super().__init__()

        self.start_position = (randint(x_start,x_start + 100), randint(-260, 260))
        self.stop_pos = x_stop
        self.speedv = car_speed
        self.up()
        self.shape('square')
        self.color(self.car_color())
        self.shapesize(1.0, 1.0)
        self.setheading(180)
        self.goto(self.start_position)

    def car_move(self):
        new_pos = (self.xcor() - self.speedv, self.ycor())
        print(new_pos)
        self.goto(new_pos)

    def car_color(self):
        r = randint(10,255)
        g = randint(10,255)
        b = randint(10, 255)

        color = (r, g, b)
        return color
    
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
