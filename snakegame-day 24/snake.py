from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0), (-60,0 )]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake():
    def __init__(self):
        self.length = 3
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for i in STARTING_POSITION:
            self.create_segment(i)


    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)


        self.head.forward(MOVE_DISTANCE)

    def create_segment(self, pos):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segment.append(new_segment)

    def extend(self):
        self.create_segment((self.segment[-1].position()))

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].seth(UP)

    def down(self):

        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)