from turtle import Turtle
import time
import math


class Face(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")

        self.circle_face()
        self.home()
        ## self.eye_border()

        self.eyes()
        self.home()

        self.up_design()
        self.home()

        self.mouth()
        self.home()

        self.mouth_top()
        self.ring()


    def circle_face(self):
        radius = 115
        self.dot(260)
        self.pensize(2)
        self.setheading(90)
        self.forward(radius)
        self.setheading(0)
        self.pencolor("yellow")
        self.pendown()
        for i in range(1, 361):
            self.forward(2 * math.pi * radius / 360)
            self.right(1)
        self.penup()


    def eye_border(self):
        self.pencolor("red")
        self.begin_fill()
        self.forward(100)
        self.right(90)
        self.forward(100)
        self.end_fill()


    def eye(self):
        self.pencolor("white")
        self.dot(50)
        self.pencolor("black")
        self.dot(20)


    def eyes(self):
        self.setheading(90)
        self.forward(20)
        self.setheading(180)
        self.forward(50)
        self.eye()
        self.setheading(0)
        self.forward(100)
        self.eye()

    
    def draw_ellipse(self, radius_x, radius_y):
        self.penup()
        self.goto(0, -radius_y)
        self.pendown()
        for i in range(2):
            self.circle(radius_y, 90)
            self.circle(radius_x, 90)
        
    
    def up_design(self):
        self.color("yellow")
        self.setheading(90)
        self.forward(115)
        self.setheading(0)
        self.backward(10)
        self.setheading(270)
        self.pensize(4)
        self.pendown()
        while self.xcor() < 0:
            self.forward(2.5)
            self.left(0.25)

        self.pensize(1)
        self.begin_fill()
        self.setheading(260)
        self.forward(20)
        self.setheading(280)
        self.forward(20)
        self.setheading(80)
        self.forward(20)
        self.setheading(100)
        self.forward(20)
        self.end_fill()
        self.pensize(4)

        self.setheading(80)
        while self.ycor() < 115:
            self.forward(2.5)
            self.left(0.25)
        self.penup()
            
        
    def mouth(self):
        self.penup()
        self.goto(-68, -50)
        self.pensize(1)
        self.pendown()
        self.color("white")
        self.begin_fill()
        self.forward(5)
        for _ in range(90):
            self.forward(0.2)
            self.right(1)

        for _ in range(90):
            self.forward(0.3)
            self.left(1)

        start_x, start_y = -34.402837467672484, -78.69716253232751
        end_x, end_y = 34.402837467672484, -78.69716253232751

        steps = 100  # Number of steps to make the curve smoother
        for i in range(steps + 1):
            # Calculate the x coordinate
            x = start_x + (end_x - start_x) * i / steps
            # Calculate the y coordinate using the sine function
            y = start_y - 8 * math.sin(math.pi * i / steps)  # 20 is the amplitude of the sine wave
            self.goto(x, y)

        for _ in range(90):
            self.forward(0.3)
            self.left(1)
        for _ in range(90):
            self.forward(0.2)
            self.right(1)
        self.forward(5)

        self.setheading(180)
        self.forward(10)

        for _ in range(90):
            self.forward(0.2)
            self.left(1)
        for _ in range(26):
            self.forward(0.3)
            self.right(1)
            
        # print(self.heading())

        start_x, start_y = 44.867332616143116, -69.00889960091588
        end_x, end_y = -44.867332616143116, -69.00889960091588

        steps = 100  # Number of steps to make the curve smoother
        for i in range(steps + 1):
            # Calculate the x coordinate
            x = start_x + (end_x - start_x) * i / steps
            # Calculate the y coordinate using the sine function
            y = start_y - 8 * math.sin(math.pi * i / steps)  # 20 is the amplitude of the sine wave
            self.goto(x, y)

        self.setheading(116)

        for _ in range(26):
            self.forward(0.3)
            self.right(1)
        for _ in range(90):
            self.forward(0.2)
            self.left(1)

        self.goto(-68, -50)
        self.end_fill()
        self.penup()
        

    def mouth_top(self):
        self.penup()
        self.goto(-38, -50)
        self.pensize(1)
        self.pendown()
        self.color("red")
        self.begin_fill()
        self.setheading(270)
        self.forward(10)
        
        for _ in range(90):
            self.forward(0.1)
            self.left(1)
        

        start_x, start_y = -32.320567493534526, -65.77943250646544
        end_x, end_y = 32.320567493534526, -65.77943250646544

        steps = 100
        for i in range(steps + 1):
            x = start_x + (end_x - start_x) * i / steps
            y = start_y - 6 * math.sin(math.pi * i / steps)
            self.goto(x, y)

        self.setheading(0)
        for _ in range(90):
            self.forward(0.1)
            self.left(1)

        self.forward(10)
        self.setheading(260)

        self.forward(5)
        for _ in range(90):
            self.forward(0.09)
            self.right(1)

        start_x, start_y = 31.29469573266919, -59.25890491696411
        end_x, end_y = -31.29469573266919, -59.25890491696411

        steps = 100
        for i in range(steps + 1):
            x = start_x + (end_x - start_x) * i / steps
            y = start_y - 6 * math.sin(math.pi * i / steps)
            self.goto(x, y)

        for _ in range(90):
            self.forward(0.09)
            self.right(1)

        self.goto(-38, -50)
        self.end_fill()
        self.penup()

    
    def ring(self):
        self.penup()
        self.goto(-27.0, -30.0)
        self.pencolor("yellow")
        self.dot(20)
        self.pencolor("orange")
        self.dot(15)
        self.pencolor("red")
        self.dot(5)