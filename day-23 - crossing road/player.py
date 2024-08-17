from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.shape("turtle")
        self.seth(90)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0, -270)

    def move_up(self):

        self.forward(MOVE_DISTANCE)

    def reset_point(self):
        self.teleport(0, -270)