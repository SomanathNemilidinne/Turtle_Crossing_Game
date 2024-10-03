import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("A Turtle Crossing game")

turtle = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.up, "Up")
screen.tracer(0)

# target_x = -300
#In future add the delete turtles function that deletes the turtle that's off the screen with the variable mentioned above
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.make_car()
    car.move_cars()
    for honda in car.all_cars:
        if honda.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()
    if turtle.ycor() > 280:
        turtle.starting_position()
        car.increase_speed()
        scoreboard.level_up()


screen.exitonclick()