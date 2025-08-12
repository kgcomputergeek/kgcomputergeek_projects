from turtle import Screen, Turtle
import time

# Step 1: Setup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)  # Turn off automatic screen updates

# Step 2: Create the initial snake segments
initial_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in initial_positions:
    segment = Turtle(shape="square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    segments.append(segment)

# Step 3: Move the snake
def move():
    # Start from the last segment and move it to the position of the segment in front of it
    for i in range(len(segments) - 1, 0, -1):
        new_x = segments[i - 1].xcor()
        new_y = segments[i - 1].ycor()
        segments[i].goto(new_x, new_y)
    # Move the first segment forward
    segments[0].forward(20)

# Add controls to move the snake
def go_up():
    if segments[0].heading() != 270:  # Prevent the snake from reversing
        segments[0].setheading(90)

def go_down():
    if segments[0].heading() != 90:
        segments[0].setheading(270)

def go_left():
    if segments[0].heading() != 0:
        segments[0].setheading(180)

def go_right():
    if segments[0].heading() != 180:
        segments[0].setheading(0)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()  # Update the screen once per loop iteration
    move()
    time.sleep(0.1)  # Add a delay to control the speed of the snake

screen.mainloop()
