from turtle import Turtle
from random import randint


class Obstacle:
    def __init__(self):
        self.obstacles = []
        self.add_obstacle()
        for obstacle in self.obstacles:
            obstacle.move_speed = 0
        self.add_speed()

    def add_obstacle(self):
        y_pos = -260
        for n in range(30):
            x_pos = randint(-250, 250)
            if not y_pos > 280:
                t = Turtle()
                t.shape("square")
                t.color("blue")
                t.shapesize(stretch_wid=1, stretch_len=2)
                t.setheading(180)
                t.penup()
                t.goto(x=x_pos, y=y_pos)
                t.color(randint(0, 255), randint(0, 255), randint(0, 255))
                t.distance = randint(5, 15)
                y_pos = y_pos + 30
                self.obstacles.append(t)
            else:
                break

    def add_speed(self):
        y = 0
        for obstacle in self.obstacles:
            random_speed = randint(y + 5, y + 15)
            obstacle.move_speed = random_speed
        y += 1

    def move_obstacles(self):
        for obstacle in self.obstacles:
            if obstacle.xcor() <= 320:
                obstacle.forward(obstacle.move_speed)

    def new_x(self):
        for obstacle in self.obstacles:
            x = randint(-250, 250)
            obstacle.goto(x, obstacle.ycor())
