
from turtle import Screen, Turtle
from Paddle import Paddle
from ball import Ball
from  scoreboard import  Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
balls = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(balls.ball_speed)
    screen.update()
    balls.move()

    #detect ball with y wall
    if balls.ycor() > 280 or balls.ycor() < -280:
        balls.bounce_y()

    #detect collison with paddl
    if (balls.distance(r_paddle) < 50 and balls.xcor() > 320) or (balls.distance(l_paddle) < 50 and balls.xcor() < -320):
        balls.bounce_x()

    # detect ball miss
    if balls.xcor() > 380:
        print("lose")
        balls.reset_position()
        scoreboard.increase_l_score()

    if balls.xcor() < -380:
        balls.reset_position()
        scoreboard.increase_r_score()

screen.exitonclick()