
########### Challenge 2 - Draw a Dashed Line ########




"""
#####INTRO BEGIN#####
import turtle as t

tim = t.Turtle()
#####INTRO END#####
###teacher's code###

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
"""

####MY CODE####

import turtle as t

# Create a turtle named timmy_the_turtle and set its appearance
timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

# Move the turtle to draw a dashed line
for _ in range(10):  # Repeat 10 times to make a dashed line
    timmy_the_turtle.forward(10)  # Move forward 10 units
    timmy_the_turtle.penup()  # Lift the pen up (no drawing)
    timmy_the_turtle.forward(10)  # Move forward another 10 units
    timmy_the_turtle.pendown()  # Put the pen down (start drawing again)

# Keep the window open until it is closed manually
t.done()
