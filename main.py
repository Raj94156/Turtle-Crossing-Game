import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
scoreboard.increment()
screen.listen()
screen.onkey(player.move,"Up")
# if player.ycor() >= 280:
#     player.goto(0,-280)

car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.Game_Over()
            game_is_on = False
    if player.ycor() > 280:
        player.goto(0,-280)
        car_manager.car_level_up()
        scoreboard.increment()
screen.exitonclick()






