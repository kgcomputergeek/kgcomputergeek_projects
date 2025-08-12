########### Challenge 4 - Random Walk ########

# import turtle as t
# import random

# tim = t.Turtle()


####MY CODE###

import turtle as t
import random

# Create a turtle named timmy_the_turtle and set its appearance
timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")

# Function to change the color of the turtle randomly
def random_color():
    R = random.random()
    G = random.random()
    B = random.random()
    timmy_the_turtle.color(R, G, B)

# Draw a random walk
for _ in range(100):  # Move 100 steps
    random_color()  # Change color for each step
    timmy_the_turtle.forward(20)  # Move forward by 20 units
    timmy_the_turtle.setheading(random.randint(0, 360))  # Turn to a random direction

# Keep the window open until it is closed manually
t.done()



"""
teacher's code

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))


"""