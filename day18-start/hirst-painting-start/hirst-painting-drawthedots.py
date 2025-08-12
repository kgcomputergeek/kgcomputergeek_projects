# from turtle import Turtle, Screen, colormode
# import random
# import colorgram

# # Set color mode to 255 (RGB)
# colormode(255)

# # Set up the screen width & height to 350 pixels
# screen = Screen()
# screen.setup(350, 350)

# # Create a turtle object
# timiteo = Turtle()
# timiteo.speed("fastest")  # Set animation speed to fastest
# timiteo.penup()  # Lift the pen to not draw lines as it moves
# timiteo.hideturtle()  # Hide the turtle cursor
# timiteo.setposition(-130, -130)  # Set the starting position
# timiteo.setheading(0)  # Set the direction to the right

# # Define the number of rows and columns for the dots
# rows = 10
# cols = 10

# # Path to the image
# image_path = "/Users/kgreen/PycharmProjects/PYLEARNING/day18-start/hirst-painting-start/image.jpg"

# # Number of colors to extract from the image
# num_of_colors = 30

# # Extract colors from the image
# colors = colorgram.extract(image_path, num_of_colors)

# # Create a list to store the RGB values
# RGB_Colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     RGB_Colors.append((r, g, b))

# # Print the RGB values to verify
# print(RGB_Colors)

# # Use the RGB values to draw dots with the turtle
# for _ in range(rows):
#     for _ in range(cols):
#         timiteo.dot(20, random.choice(RGB_Colors))  # Draw a dot with a random color from the extracted list
#         timiteo.forward(50)  # Move forward for the next dot
#     timiteo.backward(50 * cols)  # Move back to the start of the row
#     timiteo.right(90)  # Turn right
#     timiteo.forward(50)  # Move down for the next row
#     timiteo.left(90)  # Turn left back to the original direction

# # Keep the screen open
# screen.mainloop()

####TEACHER'S CODE####

# import turtle as turtle_module
# import random

# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100

# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)

#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)









# screen = turtle_module.Screen()
# screen.exitonclick()

from turtle import Turtle, Screen, colormode
import random
import colorgram

# Set color mode to 255 (RGB)
colormode(255)

# Set up the screen width & height to 350 pixels
screen = Screen()
screen.setup(500, 500)

# Create a turtle object
timiteo = Turtle()
timiteo.speed("fastest")  # Set animation speed to fastest
timiteo.penup()  # Lift the pen to not draw lines as it moves
timiteo.hideturtle()  # Hide the turtle cursor
timiteo.setposition(-200, -200)  # Set the starting position
timiteo.setheading(0)  # Set the direction to the right

# Define the number of rows and columns for the dots
rows = 10
cols = 10

# Path to the image
image_path = "/Users/kgreen/PycharmProjects/PYLEARNING/day18-start/hirst-painting-start/image.jpg"

# Number of colors to extract from the image
num_of_colors = 30

# Extract colors from the image
colors = colorgram.extract(image_path, num_of_colors)

# Create a list to store the RGB values
RGB_Colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    RGB_Colors.append((r, g, b))

# Print the RGB values to verify
print(RGB_Colors)

# Use the RGB values to draw dots with the turtle
dot_distance = 50
for row in range(rows):
    for col in range(cols):
        timiteo.dot(20, random.choice(RGB_Colors))  # Draw a dot with a random color from the extracted list
        timiteo.forward(dot_distance)  # Move forward for the next dot
    timiteo.backward(dot_distance * cols)  # Move back to the start of the row
    timiteo.right(90)  # Turn right
    timiteo.forward(dot_distance)  # Move down for the next row
    timiteo.left(90)  # Turn left back to the original direction

# Draw horizontal lines
timiteo.penup()
timiteo.setposition(-200, -200)
timiteo.pendown()
for row in range(rows + 1):
    timiteo.forward(dot_distance * cols)
    timiteo.penup()
    timiteo.backward(dot_distance * cols)
    timiteo.right(90)
    timiteo.forward(dot_distance)
    timiteo.left(90)
    timiteo.pendown()

# Draw vertical lines
timiteo.penup()
timiteo.setposition(-200, -200)
timiteo.pendown()
for col in range(cols + 1):
    timiteo.setheading(90)
    timiteo.forward(dot_distance * rows)
    timiteo.penup()
    timiteo.backward(dot_distance * rows)
    timiteo.right(90)
    timiteo.forward(dot_distance)
    timiteo.left(90)
    timiteo.pendown()

# Keep the screen open
screen.mainloop()
