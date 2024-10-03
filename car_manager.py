COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager():
    def __init__(self) -> None:
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def make_car(self):
        choice = random.randint(1,5)
        if choice == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.goto(290, random.randint(-250, 250))
            self.all_cars.append(new_car)
        
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)
    
    def increase_speed(self):
        self.speed += MOVE_INCREMENT
