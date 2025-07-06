import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE   = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed_car = STARTING_MOVE_DISTANCE
    def create_car(self):
        random_y = random.randint(-260,280)
        new_car = Turtle()
        new_car.turtlesize(1,2)
        new_car.penup()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.goto(320 , random_y)
        new_car.setheading(180)
        self.all_cars.append(new_car)


    def move_car(self):
        for car in self.all_cars:
            car.fd(self.speed_car)

    def increment_speed(self):
        self.speed_car += MOVE_INCREMENT
