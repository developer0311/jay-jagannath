from turtle import Turtle
import time
import math


RADIUS = 140
DIAMETER = RADIUS*2


class Outside(Turtle):
    def __init__(self):
        super().__init__()
        # self.hideturtle()
        self.speed("fastest")
        
        self.penup()

        self.setheading(90)
        self.forward(180)
        self.setheading(0)
        self.circle_loop_1(180 ,40)
        self.home()

        self.setheading(90)
        self.forward(150)
        self.setheading(0)
        self.circle_loop_2(150, 10, "green")
        self.home()

        self.setheading(90)
        self.forward(140)
        self.setheading(0)
        self.circle_loop_2(140, 10, "orange")
        self.home()
    

    def circle_loop_1(self, radius, dot_radius):
        for i in range(1, 361):
            self.forward(2 * math.pi * radius / 360)
            self.right(1)
            if i%15 == 0:
                self.pencolor("red")
                self.dot(dot_radius)
                self.pencolor("yellow")
                self.dot(15)

    def circle_loop_2(self, radius, dot_radius, dot_color):
        for i in range(1, 361):
            self.pencolor(dot_color)
            self.forward(2 * math.pi * radius / 360)
            self.right(1)
            if i%5 == 0:
                self.dot(dot_radius)