import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
y_distance = [30,60,90,120,-30,-90,-50,-130]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed_car = STARTING_MOVE_DISTANCE
    def create_car(self):
        random_choice = random.randint(1,6)
        if random_choice == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(COLORS[random.randint(0,5)])
            N_ycor = random.randint(-255,255)
            new_car.goto(300,N_ycor)
            self.all_cars.append(new_car)
    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed_car)
    def car_level_up(self):
            self.speed_car+=MOVE_INCREMENT




