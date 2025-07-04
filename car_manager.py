import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE   = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.y = random.randint(-260,280)
        self.turtlesize(1,2)
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.goto(320 ,self.y)
        self.setheading(180)
        self.steps = STARTING_MOVE_DISTANCE
    def move(self):
        self.increment_speed()
        self.fd(self.steps)
    def increment_speed(self):
        self.steps = MOVE_INCREMENT

