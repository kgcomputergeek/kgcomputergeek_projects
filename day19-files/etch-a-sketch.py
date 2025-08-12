# from turtle import Turtle, Screen

# # Create a turtle object
# timiteo = Turtle()
# timiteo.shape("turtle")
# timiteo.color("Indian Red")

# # Create a screen object
# screen = Screen()

# # Function to move forward
# def charges_forward():
#     timiteo.forward(10)

# # Function to move backward
# def charges_backwards():
#     timiteo.backward(10)

# # Function to turn left
# def gira_a_la_izquierda():
#     timiteo.left(25)

# # Function to turn right
# def gira_a_la_derecha():
#     timiteo.right(25)

# # Function to clear the screen
# def clear_screen():
#     timiteo.clear()
#     timiteo.penup()
#     timiteo.home()
#     timiteo.pendown()

# # Listen for key presses
# screen.listen()
# screen.onkey(charges_forward, "w")
# screen.onkey(charges_backwards, "s")
# screen.onkey(gira_a_la_izquierda, "a")
# screen.onkey(gira_a_la_derecha, "d")
# screen.onkey(clear_screen, "c")

# # Keep the window open and responsive to all events
# screen.mainloop()

from turtle import Turtle, Screen

# Create a turtle object for drawing
timiteo = Turtle()
timiteo.shape("turtle")
timiteo.color("Indian Red")

# Create a turtle object for writing instructions
writer = Turtle()
writer.hideturtle()
writer.penup()
writer.goto(-200, 200)
writer.pendown()

# Create a screen object
screen = Screen()

# Function to display instructions so that users can know how to play
def display_instructions():
    writer.clear()
    writer.penup()
    writer.goto(-200, 200)
    writer.pendown()
    writer.write("Controls:\nW/Up Arrow: Move Forward\nS/Down Arrow: Move Backward\nA/Left Arrow: Turn Left\nD/Right Arrow: Turn Right\nC: Clear Screen", align="left", font=("Arial", 12, "normal"))

# Function to move forward
def move_forward():
    timiteo.forward(10)

# Function to move backward
def move_backward():
    timiteo.backward(10)

# Function to turn left
def turn_left():
    timiteo.left(25)

# Function to turn right
def turn_right():
    timiteo.right(25)

# Function to clear the screen
def clear_screen():
    timiteo.clear()
    timiteo.penup()
    timiteo.home()
    timiteo.pendown()
    # Redraw the instructions after clearing the screen
    display_instructions()

# Prompt the user to choose the controls they want to use which is wither WASD or Arrow keys
control_scheme = screen.textinput("Control Scheme", "Choose your control scheme: (WASD/Arrows)").strip().lower()

# Set up key bindings based on user choice
screen.listen()
if control_scheme == "wasd":
    screen.onkey(move_forward, "w")  # "w" to move forward
    screen.onkey(move_backward, "s")  # "s" to move backward
    screen.onkey(turn_left, "a")  # "a" to turn left
    screen.onkey(turn_right, "d")  # "d" to turn right
elif control_scheme == "arrows":
    screen.onkey(move_forward, "Up")  # Up arrow to move forward
    screen.onkey(move_backward, "Down")  # Down arrow to move backward
    screen.onkey(turn_left, "Left")  # Left arrow to turn left
    screen.onkey(turn_right, "Right")  # Right arrow to turn right
else:
    writer.write("Invalid control scheme. Please restart and choose either 'WASD' or 'Arrows'.", align="left", font=("Arial", 12, "normal"))

# Clear the screen with "c"
screen.onkey(clear_screen, "c")  # "c" to clear the screen

# Display initial instructions
display_instructions()

# Keep the window open and responsive to all events
screen.mainloop()
