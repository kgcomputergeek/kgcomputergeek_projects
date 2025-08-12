import time
from turtle import Screen, Turtle

# Constants
MOVE_DISTANCE = 20

# Snake class
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction = "right"

    def create_snake(self):
        for i in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(-i * MOVE_DISTANCE, 0)
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        if self.direction == "up":
            self.head.setheading(90)
            self.head.forward(MOVE_DISTANCE)
        elif self.direction == "down":
            self.head.setheading(270)
            self.head.forward(MOVE_DISTANCE)
        elif self.direction == "left":
            self.head.setheading(180)
            self.head.forward(MOVE_DISTANCE)
        elif self.direction == "right":
            self.head.setheading(0)
            self.head.forward(MOVE_DISTANCE)

    def go_up(self):
        if self.direction != "down":
            self.direction = "up"

    def go_down(self):
        if self.direction != "up":
            self.direction = "down"

    def go_left(self):
        if self.direction != "right":
            self.direction = "left"

    def go_right(self):
        if self.direction != "left":
            self.direction = "right"

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off screen updates

snake = Snake()

# Keyboard bindings
def go_up():
    snake.go_up()
    update_controls()

def go_down():
    snake.go_down()
    update_controls()

def go_left():
    snake.go_left()
    update_controls()

def go_right():
    snake.go_right()
    update_controls()

def update_controls():
    screen.title(f"My Snake Game - Direction: {snake.direction.capitalize()}")

# WASD controls
screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")

# Arrow key controls
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()  # Update the screen once per loop iteration
    snake.move()
    time.sleep(0.1)  # Add a delay to control the speed of the snake

screen.mainloop()
