import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)
player =   Player()
screen.onkey(fun=player.move, key="Up")
game_is_on = True
cars = []
i = 0
while game_is_on:
    if i % 6 == 0   :
        car = CarManager()
        cars.append(car)
    for c in cars :
        c.move()
        if c.xcor() < 30 and player.distance(c) < 30 :
            game_is_on = False
            scoreboard =Scoreboard()
    time.sleep(0.1)
    screen.update()



    i  += 1

screen.exitonclick()