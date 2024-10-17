from turtle import Turtle, Screen
import random
import time

from car_manager import CarManager
from player import Player
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()



screen.listen()
screen.onkey(player.up, "Up")

car_manager.create_car()
car_manager.move_cars()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    





screen.exitonclick()