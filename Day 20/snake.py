
from time import sleep
from turtle import Turtle
START_POSITION = (0.0,-20.0,-40.0)
SPEED = 0.5
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.sections = []
        self.new_snake()
        self.head = self.sections[0]
    def new_snake(self):

        for i in range(3):
            section = Turtle()
            section.up()
            section.shape("square")
            section.color("white")
            section.setx(START_POSITION[i])
            self.sections.append(section)

    def add_section(self):
        section = Turtle()
        section.up()
        section.shape("square")
        section.color("white")
        # section.shapesize(2,2)
        # Check if this is the first section
        i = len(self.sections)-1

        new_x = self.sections[i-1].xcor()
        new_y = self.sections[i-1].ycor()

        section.setx(new_x)
        section.sety(new_y)

        self.sections.append(section)
        
    # take the positions of all the body segments and store them in a list

    def move_snake(self):
        # update the current position of the segments with the old list

        for i in range(len(self.sections)-1, 0, -1):
            new_x = self.sections[i-1].xcor()
            new_y = self.sections[i-1].ycor()
            self.sections[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        sleep(SPEED)

    def go_right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
    def go_up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)
    def go_left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)
    def go_down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)
