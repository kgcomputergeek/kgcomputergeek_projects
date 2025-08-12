####MY SNAKE GAME####


"""
--Instructions--
We will be working with this program from days 20-23 and here are the different steps that will be addressed

1. Create a snake body
2. Move the snake
3. Detect collision with food
4. Create scoreboard
5. Detect collision with wall
6. Detect collision with tail


"""
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")

# Create the initial snake body
segments = []

# Starting positions for the initial snake body segments
# starting_positions = [(0, 0), (-20, 0), (-40, 0)]
initial_segments = 3 #alt way of starting positions
# Create the initial snake body segments
for i in range (initial_segments):
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    #segment.goto(position) #Uses a predefined tuple position to determine the coordinates & can move the segment to any arbitrary coordinates provided by position
    segment.goto(-i * 20, 0) #alt way of Positions each segment at specific coordinates, ensuring they are placed 20 units apart horizontally. Specifically spaces out segments horizontally in a line with fixed spacing (20 units apart) and the same y-coordinate.
    segments.append(segment)

# Keep the screen open and responsive
screen.mainloop()