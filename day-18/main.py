import turtle
from turtle import Turtle, Screen, colormode
import  random

colormode(255)
tim = Turtle()
tim.shape('circle')
tim.color('coral')

def set_color():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    return r, g, b


degree = [90, 180, 270, 360]

tim.speed('fastest')
# tim.pensize(5)
# def draw_shape(angle):
#     rad = 360/angle
#
#     for i in range(angle):
#         tim.forward(50)
#         tim.rt(rad)
#
#
# for angle in range(3, 10):
#     rand_color = random.choice(colors)
#     tim.color(rand_color)
#     draw_shape(angle)


# def make_path():
#
#     tim.color(set_color())
#     deg = random.choice(degree)
#     tim.setheading(deg)
#     tim.forward(50)
#
#
# for _ in range(100):
#     make_path()


# make circle
def make_spirograph(size):
    for i in range(36):
        tim.color(set_color())
        tim.setheading(10*i)
        tim.circle(size)



screen = Screen()
screen.exitonclick()