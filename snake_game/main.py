# advancements done in the similar project the advancememt 
# are adding high score to the project ================================================================
# =======================================================================================================



from snake import Snake
from food import Food
from scoreboard import Score
import time
from turtle import Turtle,  Screen
screen = Screen()
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

# positions = [(0,0),(-20,0),(-40,0)]
# segment = []

scoreboard  = Score()

# for value in positions:
#     new_turtles = Turtle("square")
#     new_turtles.color("white")
#     new_turtles.penup()
#     new_turtles.goto(value)
#     segment.append(new_turtles)
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # for turtle_seg in range(len(segment)-1,0,-1):
    #     new_x = segment[turtle_seg-1].xcor()
    #     new_y = segment[turtle_seg-1].ycor()
    #     segment[turtle_seg].goto(new_x,new_y)
    # segment[0].forward(20)

        
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        scoreboard.increase_score()

    if snake.head.xcor()>390 or snake.head.ycor()>320 or snake.head.xcor()< -390 or snake.head.ycor()< -320:
        scoreboard.reset()
        snake.reset()
    


    for segment in snake.segment[1:]:

        if snake.head.distance(segment)<10:
           
            scoreboard.reset()
            snake.reset()




screen.exitonclick()