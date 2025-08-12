import turtle as t
import random

# Create the turtle object
timmy_the_turtle = t.Turtle()

def random_color():
    # Generate random values for Red, Green, and Blue
    rgb = (random.random(), random.random(), random.random())
    # Set the turtle's color to the random RGB values using a tuple
    timmy_the_turtle.color(rgb)

# Set the turtle's speed to the fastest
timmy_the_turtle.speed('fastest')

# Perform a random walk with the turtle
for _ in range(100):
    random_color()  # Change the turtle's color to a random color
    timmy_the_turtle.forward(30)  # Move the turtle forward by 30 units
    timmy_the_turtle.setheading(random.choice([0, 90, 180, 270]))  # Change the turtle's direction randomly

# Keep the window open until it is clicked
t.Screen().exitonclick()
