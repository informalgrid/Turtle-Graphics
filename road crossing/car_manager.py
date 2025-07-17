from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    
    def __init__(self):
        self.cars_list=[]
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_numb = random.randint(1,6)
        if random_numb == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1,2)
            new_car.penup()
            random_y = random.randint(-230,230)
            new_car.goto(300,random_y)
            self.cars_list.append(new_car)

    def move_cars(self):
        for i in self.cars_list:
            i.backward(self.car_speed)

    def level_up(self):
        self.car_speed +=MOVE_INCREMENT
