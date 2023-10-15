from turtle import Turtle, Screen
import random

screen = Screen()
screen.listen()
screen.setup(width=500, height=400)
on_race = False
user_bet = screen.textinput(title="Choose you bet", prompt="warna apa jagoanmu")


y_pos = [-70, -40, -10, 20, 50, 80]
colors = ['red', 'green', 'blue', 'purple', 'orange', 'pink']
turtle_list = []

for index in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[index])
    tim.goto(-200, y_pos[index])
    turtle_list.append(tim)

if user_bet:
    on_race = True

while on_race:
    for turtle in turtle_list:
        if turtle.xcor() >= 230:
            on_race = False
            winning = turtle.pencolor()
            if winning == user_bet:
                print(f"kamu menang, {winning} juara 1")
            else:
                print(f"kamu kalah, {winning} juara 1, sedangkan pilihanmu {user_bet}")
        turtle.forward(random.randrange(0,11))


screen.exitonclick()
