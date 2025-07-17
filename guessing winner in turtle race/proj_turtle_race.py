from turtle import Turtle, Screen
import random

screen = Screen()


is_race_on = False

screen.setup(width=500,height=400)
user_bet = screen.textinput("make your bet", "which turtle will win the race ? enter a colour")
colors = ["red","yellow","green","pink","orange","brown"]
y_axis = [-10,-40,-70,20,50,80]
all_turtles = []

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(-240,y_axis[turtle_index])

    all_turtles.append(tim)

if user_bet:
    
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("you won")

            else:
                print("you lost")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()