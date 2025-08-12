"""
Instructions:

Step 1 - Check out how the game play works
1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.

2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.

3. When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. On the next level, the car speed increases.

4. When the turtle collides with a car, it's game over and everything stops.

Step 2 - Break down the Problem
If you haven't already, download the starting project here and open it inside PyCharm.

The first step of creating any large project is to breakdown the problem into smaller, bite-sized chunks. Add the following comments to the starting code and try to tackle them one-by-one.

Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north. If you get stuck, check the video walkthrough in Step 3.

Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs. If you get stuck, check the video walkthrough in Step 4.


Detect when the turtle player collides with a car and stop the game if this happens. If you get stuck, check the video walkthrough in Step 5.

Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle to the starting position and increase the speed of the cars. Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed. If you get stuck, check the video walkthrough in Step 6.

Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre. If you get stuck, check the video walkthrough in Step 7.


"""






import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
# screen.tracer(0) #tracer is turned off because of 0 value
screen.tracer(0) #tracer is turned off because of 0 value



player = Player()

car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.go_up,"Up")




game_is_on = True
while game_is_on:
    time.sleep(0.1) #within the while loop, the code is going to run every 0.1 seconds
    screen.update()


    car_manager.create_cars()
    car_manager.move_cars()
    
    #detect collision with car

    for car in car_manager.all_cars:
       if car.distance(player) < 20:
           game_is_on = False
           scoreboard.game_over()
          # print("game over. loser :*(")


    #detect successful movement

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()
