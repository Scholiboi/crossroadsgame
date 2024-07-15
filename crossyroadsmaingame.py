import time
from turtle import Turtle, Screen
from pawn import Pawn
from obstacle import Obstacle
from random import randint
from scoreboard import Scoreboard


def start_game():
    t = Turtle()
    t.penup()
    t.hideturtle()
    t.goto(x=500, y=300)
    t.pendown()
    t.color("white")
    t.pensize(3)
    t.goto(x=-500, y=300)


screen = Screen()
screen.setup(width=600, height=700)
screen.bgcolor("black")
screen.title("CrossyRoads Game")
screen.colormode(255)
screen.tracer(False)

game_is_on = True
pawn = Pawn()
obstacle = Obstacle()
score = Scoreboard()
screen.listen()
screen.onkeypress(fun=pawn.move, key="w")
start_game()

while game_is_on:
    screen.update()
    time.sleep(0.09)
    obstacle.move_obstacles()

    for one in obstacle.obstacles:
        if one.xcor() < -280:
            one.goto(320, one.ycor())

    for one in obstacle.obstacles:
        if pawn.distance(one) < 15:
            game_is_on = False
            score.end_game()

    if pawn.ycor() > 300:
        time.sleep(3)
        pawn.goto(0, -280)
        screen.bgcolor(randint(0, 255), randint(0, 255), randint(0, 255))
        obstacle.add_speed()
        obstacle.new_x()
        score.increasescore()
        score.updatescore()

screen.exitonclick()
