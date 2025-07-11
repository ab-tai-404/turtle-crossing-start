from  turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y =   280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)


    def move_player(self):
        self.fd(MOVE_DISTANCE)

    def player_to_home(self):
        self.goto(STARTING_POSITION)