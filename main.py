import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
car_mgr = CarManager()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
screen.listen()
screen.onkey(tim.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_mgr.create_car()
    car_mgr.car_crossing()

    # # Detect collison with car
    for car in car_mgr.all_cars:
        if car.distance(tim) < 20:
            scoreboard.game_over()
            game_is_on = False

    #  Detect turtle reached finish line
    if tim.ycor() > 280:
        scoreboard.update_score()
        screen.update()
        tim.go_to_start()
        car_mgr.increase_speed()













screen.exitonclick()
