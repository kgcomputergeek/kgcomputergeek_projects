
########### Challenge 5 - Spirograph ########

# import turtle as t
# import random

# tim = t.Turtle()
# t.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color

####MY CODE####
import turtle as t
import random

# Set up the screen
screen = t.Screen()
screen.bgcolor("white")

# Set up the turtle
tim = t.Turtle()
tim.speed("fastest")

# Define a function to create a spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random.random(), random.random(), random.random())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

# Call the function with a gap size
draw_spirograph(10)

# Finish the drawing
screen.exitonclick()

"""
teacher's code
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)
"""