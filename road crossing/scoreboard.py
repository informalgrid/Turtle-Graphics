from turtle import Turtle

FONT = ("Comic Sans MS", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-270,260)
        self.update_scoreboard()
    
    def update_scoreboard(self):
         self.clear()
         self.write(f"Level :{self.level}",align = "Left", font = FONT )
  
    def increase_level(self):
        self.level+=1
        self.update_scoreboard()


    def game_over(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.write(f" Game Over", align = "center",font = ("Comic Sans MS", 27, "normal"))
