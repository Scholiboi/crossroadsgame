from turtle import Turtle


class Pawn(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def move(self):
        self.forward(10)
