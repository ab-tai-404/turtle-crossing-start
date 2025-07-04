from turtle import Turtle
FONT = ("Courier", 26  , "normal")
FONT_LEVEL =("Courier", 10  , "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.color("black")

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER" ,align="center",   font= FONT )
    def level_(self):
        self.write(f"Level : {self.level}" ,align="center",   font= FONT_LEVEL )

    def increment_level(self):
        self.level += 1
        self.goto(-260,260)
        self.clear()
        self.level_()