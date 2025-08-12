
########### Challenge 3 - Draw Shapes ########

# import turtle as t

# tim = t.Turtle()

####MY CODE####

import turtle

# Create a turtle object
t = turtle.Turtle()

# Function to draw a square
def draw_square(size, color):
  t.color(color)
  t.begin_fill()
  for _ in range(4):
    t.forward(size)
    t.left(90)
  t.end_fill()

# Function to draw a circle
def draw_circle(size, color):
  t.color(color)
  t.begin_fill()
  t.circle(size)
  t.end_fill()

# Function to draw a triangle
def draw_triangle(size, color):
  t.color(color)
  t.begin_fill()
  for _ in range(3):
    t.forward(size)
    t.left(120)
  t.end_fill()

# Draw shapes with different colors
draw_square(100, "IndianRed")
t.penup()
t.goto(150, 0)
t.pendown()
draw_circle(50, "DeepSkyBlue")
t.penup()
t.goto(-150, 0)
t.pendown()
draw_triangle(100, "green")

# Keep the window open until closed manually
turtle.done()

"""
teacher's code
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)


"""