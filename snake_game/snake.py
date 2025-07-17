from turtle import Turtle
from scoreboard import Score

UP = 90
DOWN= 270
LEFT = 180
RIGHT = 0
POSITIONS = [(0,0),(-20,0),(-40,0)]

class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]



    def create_snake(self):
        for value in POSITIONS:
            self.add_segment(value)



    def add_segment(self,value):
            new_turtles = Turtle("square")
            new_turtles.color("white")
            new_turtles.penup()
            new_turtles.goto(value)
            self.segment.append(new_turtles)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]


    def extent(self):
        self.add_segment(self.segment[-1].position())


    def move(self):
        for turtle_seg in range(len(self.segment)-1,0,-1):
            new_x = self.segment[turtle_seg-1].xcor()
            new_y = self.segment[turtle_seg-1].ycor()
            self.segment[turtle_seg].goto(new_x,new_y)
            if self.segment[turtle_seg].xcor()== 290 or self.segment[turtle_seg].ycor()== 290:                print("you lost")
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segment[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segment[0].setheading(RIGHT)
