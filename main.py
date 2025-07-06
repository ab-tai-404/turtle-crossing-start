import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()

screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.onkey(fun=player.move_player, key="Up")
game_is_on = True
num_car = 0

car = CarManager()

while game_is_on:
    if num_car % (7 - scoreboard.level) == 0   :
        car.create_car()

    car.move_car()

    for x_car in car.all_cars:
        if x_car.xcor() < 30 and player.distance(x_car) < 25:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() >= 280 :
        scoreboard.increment_level()
        player.player_to_home()
        car.increment_speed()

    time.sleep(0.1)
    screen.update()
    num_car  += 1

screen.exitonclick()