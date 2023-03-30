from turtle import Turtle

STARTINGPOST = [(0, 0), (-20, 0), (-30, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for index in STARTINGPOST:
            self.add_segemnt(index)

    def add_segemnt(self, index):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(index)
        self.segments.append(turtle)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 100)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segemnt(self.segments[-1].position())

    def move(self):
        for turtle in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[turtle - 1].xcor()
            new_y = self.segments[turtle - 1].ycor()
            self.segments[turtle].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
