import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):

        self.current_speed = 20
        self.max_total_car = 10
        self.cars = []

    def generate_car(self):
        rand_y = random.randint(-200, 300)
        rand_x = random.randint(0, 900)
        car = Car((rand_x, rand_y))
        self.cars.append(car)

    def level_up(self):
        for i in self.cars:
            i.add_speed()

    def move_car(self):
        for i in self.cars:
            i.move_car()

class Car(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.create_car(pos)
        self.speed_car = 1

    def create_car(self, pos):
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=1.5)
        self.penup()
        self.goto(pos)

    def move_car(self):
        self.goto(self.xcor() - MOVE_INCREMENT*self.speed_car, self.ycor())
        if self.xcor() < -300:
            rand_y = random.randint(-200, 300)
            self.teleport(350, rand_y)

    def add_speed(self):
        self.speed_car += 0.2
