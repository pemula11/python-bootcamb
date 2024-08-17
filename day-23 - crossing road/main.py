import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()
screen.listen()
screen.onkey(player.move_up, "Up")

car_manager = CarManager()

for i in range(15):
    car_manager.generate_car()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in car_manager.cars:
        car.move_car()
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= 260:
        player.reset_point()
        scoreboard.increase_score()
        car_manager.level_up()

screen.exitonclick()