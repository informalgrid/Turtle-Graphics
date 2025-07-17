import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")

# if player.ycor() >= 280 and player.xcor() == 0:
#     player.restarting()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()
    if player.ycor() >= 280:
        scoreboard.increase_level()
        player.restarting()
        car.level_up()
       

    for cars in car.cars_list:
        if cars.distance(player)< 20:
            scoreboard.game_over()
            game_is_on = False   

screen.exitonclick()