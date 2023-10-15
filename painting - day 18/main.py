import colorgram
import turtle as t
import random as r

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
#
#
# for color in colors:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         color = (r,g,b)
#         rgb_colors.append(color)
#
#
# print(rgb_colors)

color_list = [(198, 13, 32), (250, 237, 19), (39, 76, 189), (39, 217, 68), (238, 227, 5), (229, 159, 47), (28, 40, 156), (214, 75, 13), (242, 246, 252), (16, 154, 16), (198, 15, 11), (243, 34, 165), (68, 10, 30), (228, 18, 120), (60, 15, 8), (223, 141, 209), (11, 97, 62), (221, 161, 9), (50, 212, 231), (18, 20, 47), (11, 227, 239), (238, 156, 217), (84, 74, 211), (78, 210, 163), (82, 234, 200), (61, 233, 241), (5, 68, 42)]
t.colormode(255)

tim = t.Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
POSX = -300

for i in range(10):
    # currect = tim.pos()
    # posy = currect[1] + 50
    # tim.setpos(POSX, posy)
    for _ in range(10):
        tim.dot(20, r.choice(color_list))
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)



screen = t.Screen()
screen.exitonclick()