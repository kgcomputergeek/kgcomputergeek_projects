
# from turtle import Turtle, Screen, colormode
# import random

# colormode(255) #this is a function used to return the color mode or set it to 1.0 or 255 (r,g,b) values of color must be in rang 0 to c mode and requires only one argument as "cmode" one of the values 1.0 or 255
# screen = Screen()
# screen.setup(350,350) #setting up the screen width & ht to 350 pixels 
# timiteo = Turtle
# timiteo.speed("fastest") #animation speed is set to fastest
# #path to the image.
# timiteo.penup()# As the turtle moves, it draws a line along its trail
# timiteo.hideturtle()
# timiteo.setposition(-130,-130)
# timiteo.setheading(0)

# rows = 10
# cols = 10

 
# image_path = "/Users/kgreen/PycharmProjects/PYLEARNING/day18-start/hirst-painting-start/image.jpg"

# #number of colors to extract from the image-
# num_of_colors = 30

# #color extraction that will extract colors from the image(s)
# #it is a method that has two arguments passed to it which is the image path, and number of colors
# colors = colorgram.extract(image_path,num_of_colors)

# RGB_Colors = [] #a list that contains the colors from one of Damien Hirst's spot paintings and matches the required format we are to follow for python's turtle module
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     RGB_Colors.append((r,g,b))


from turtle import Turtle, Screen, colormode
import random
import colorgram

# Set color mode to 255 (RGB)
colormode(255)

# Set up the screen width & height to 350 pixels
screen = Screen()
screen.setup(350, 350)

# Create a turtle object
timiteo = Turtle()
timiteo.speed("fastest")  # Set animation speed to fastest
timiteo.penup()  # Lift the pen to not draw lines as it moves
timiteo.hideturtle()  # Hide the turtle cursor
timiteo.setposition(-130, -130)  # Set the starting position
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
for _ in range(rows):
    for _ in range(cols):
        timiteo.dot(20, random.choice(RGB_Colors))  # Draw a dot with a random color from the extracted list
        timiteo.forward(50)  # Move forward for the next dot
    timiteo.backward(50 * cols)  # Move back to the start of the row
    timiteo.right(90)  # Turn right
    timiteo.forward(50)  # Move down for the next row
    timiteo.left(90)  # Turn left back to the original direction

# Keep the screen open
screen.mainloop()
