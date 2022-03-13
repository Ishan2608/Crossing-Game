import random
from turtle import Turtle

COLORS = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red', 'tomato', 'purple', 'deep pink', 'navy',
          'steel blue', 'aquamarine', 'medium aquamarine', 'orange red', 'pink', 'dark gray']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Traffic:
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.traffic_list = []

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-240, 240)
            new_car.goto(300, random_y)
            self.traffic_list.append(new_car)

    def move_cars(self):
        for car in self.traffic_list:
            car.backward(MOVE_INCREMENT)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
