from turtle import Turtle


class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
            
        self.color("white")
        self.penup()
        self.shapesize(5,1)
        self.goto(position)
        self.shape("square")
            # self.segment.append(paddle)
            

    def go_up(self):
        new_y = self.ycor()+30
        self.goto(self.xcor(),new_y)
        
    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(),new_y)