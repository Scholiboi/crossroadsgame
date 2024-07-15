from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=300)
        self.round = 0
        self.updatescore()

    def increasescore(self):
        self.round += 1

    def updatescore(self):
        self.clear()
        self.write(f"Round: {self.round}", align='center', font=("Arial", 24, "normal"))

    def end_game(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 30, "normal"))
