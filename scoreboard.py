from turtle import Turtle
FONT = ("Courier", 26  , "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.color("black")
        self.write("GAME OVER" ,align="center",   font= FONT )