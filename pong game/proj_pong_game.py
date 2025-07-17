from turtle import Turtle , Screen
from paddle_making import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.screensize(800,600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)


# for item in positions:
#     paddle = Turtle()
#     paddle.color("white")
#     paddle.penup()
#     paddle.shapesize(3,0.4)
#     paddle.goto(item)
#     paddle.shape("square")

# paddle = Paddle()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-360,0))
score = Score()
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")



game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # ball.collisions()

    if ball.ycor() > 280 or ball.ycor()< -280:
        ball.bounce_y()

    if ball.distance(r_paddle)< 30 and ball.xcor()> 320 or ball.distance(l_paddle)< 30 and ball.xcor() < -330:
        ball.bounce_x()
    

    if ball.xcor()> 380:
        score.left_score()
        ball.reset()

    if ball.xcor() < -380:
        score.right_score()
        ball.reset()

screen.exitonclick()