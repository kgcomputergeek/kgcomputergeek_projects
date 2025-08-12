######## Challenge 1 - Draw a Square ############



import turtle as t

# Create a turtle named Timmy
timmy_the_turtle = t.Turtle()

# Make Timmy look like a turtle
timmy_the_turtle.shape("turtle")

# Change Timmy's color to red
timmy_the_turtle.color("red")

# Step 1: Move Timmy forward by 100 units
timmy_the_turtle.forward(100)

# Step 2: Turn Timmy 90 degrees to the right (to face downward)
timmy_the_turtle.right(90)

# Step 3: Move Timmy forward by 100 units (downward)
timmy_the_turtle.forward(100)

# Step 4: Turn Timmy 90 degrees to the right (to face left)
timmy_the_turtle.right(90)

# Step 5: Move Timmy forward by 100 units (to the left)
timmy_the_turtle.forward(100)

# Step 6: Turn Timmy 90 degrees to the right (to face upward)
timmy_the_turtle.right(90)

# Step 7: Move Timmy forward by 100 units (upward to complete the square)
timmy_the_turtle.forward(100)

# Keep the window open until it is clicked
t.done()

"""
###teacher's code###
 
# import turtle as t

# timmy_the_turtle = t.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)
#####INTRO END#####
###WORKING SOLUTION####
import turtle as t

timmy_the_turtle = t.Turtle()

for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

"""

####MY CODE####
