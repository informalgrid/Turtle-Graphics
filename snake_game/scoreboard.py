from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,290)
        self.write(f"score: {self.score} High Score : {self.high_score}", align= "center", font=("arial", 24, "normal"))
        self.hideturtle()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} High score : {self.high_score}", align= "center", font=("arial", 24, "normal"))


    def increase_score(self):
        self.score +=1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode = "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

