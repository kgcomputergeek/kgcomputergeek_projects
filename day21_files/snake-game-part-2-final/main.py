# from turtle import Screen
# from snake import Snake
# from food import Food
# from scoreboard import Scoreboard
# import time

# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)

# snake = Snake()
# food = Food()
# scoreboard = Scoreboard()

# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")


# """
#  # Redraw the instructions after clearing the screen
#     writer.clear()
#     writer.penup()
#     writer.goto(-200, 200)
#     writer.pendown()
#     writer.write("Controls:\nW/Up Arrow: Move Forward\nS/Down Arrow: Move Backward\nA/Left Arrow: Turn Left\nD/Right Arrow: Turn Right\nC: Clear Screen", align="left", font=("Arial", 12, "normal"))



# # Listen for key presses
# screen.listen()
# # WASD controls
# screen.onkey(move_forward, "w")  # "w" to move forward
# screen.onkey(move_backward, "s")  # "s" to move backward
# screen.onkey(turn_left, "a")  # "a" to turn left
# screen.onkey(turn_right, "d")  # "d" to turn right
# # Arrow key controls
# screen.onkey(move_forward, "Up")  # Up arrow to move forward
# screen.onkey(move_backward, "Down")  # Down arrow to move backward
# screen.onkey(turn_left, "Left")  # Left arrow to turn left
# screen.onkey(turn_right, "Right")  # Right arrow to turn right
# # Clear the screen with "c"
# screen.onkey(clear_screen, "c")  # "c" to clear the screen

# # Keep the window open and responsive to all events
# screen.mainloop()


# """

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     snake.move()

#     #Detect collision with food.
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         snake.extend()
#         scoreboard.increase_score()

#     #Detect collision with wall.
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         game_is_on = False
#         scoreboard.game_over()

#     #Detect collision with tail.
#     for segment in snake.segments:
#         if segment == snake.head:
#             pass
#         elif snake.head.distance(segment) < 10:
#             game_is_on = False
#             scoreboard.game_over()





# screen.exitonclick()

"""
####UPDATED CODE####

-PROVIDES DIRECTIONS TO THE USER
-PROVIDES OPTIONS TO CHOOSE WASD OR ARROW KEYS
"""


from turtle import Screen, Turtle
import time
import random

# Step 1: Setup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)

# Step 2: Create the initial snake segments
def create_snake():
    initial_positions = [(0, 0), (-20, 0), (-40, 0)]
    segments = []
    for position in initial_positions:
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        segments.append(segment)
    return segments

# Step 3: Move the snake
def move(segments):
    for i in range(len(segments) - 1, 0, -1):
        new_x = segments[i - 1].xcor()
        new_y = segments[i - 1].ycor()
        segments[i].goto(new_x, new_y)
    segments[0].forward(20)

# Add controls to move the snake
def go_up():
    if segments[0].heading() != 270:
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

# Step 4: Create the Food class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

# Step 5: Create the Scoreboard class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

# Function to set controls based on user's choice
def set_controls(choice):
    screen.listen()
    if choice == "WASD":
        screen.onkey(go_up, "w")
        screen.onkey(go_down, "s")
        screen.onkey(go_left, "a")
        screen.onkey(go_right, "d")
    else:
        screen.onkey(go_up, "Up")
        screen.onkey(go_down, "Down")
        screen.onkey(go_left, "Left")
        screen.onkey(go_right, "Right")

# Function to prompt the user for control choice
def get_control_choice():
    instructions = "Choose your controls:\n- Type 'WASD' for WASD controls\n- Type 'Arrow' for Arrow key controls"
    user_choice = screen.textinput(title="Control Selection", prompt=instructions).strip().upper()
    while user_choice not in ["WASD", "ARROW"]:
        user_choice = screen.textinput(title="Control Selection", prompt="Invalid choice. Please enter 'WASD' or 'Arrow': ").strip().upper()
    return user_choice

# Function to prompt the user if they want to play again
def ask_play_again():
    return screen.textinput(title="Play Again?", prompt="Do you want to play again? Type 'Yes' to play or 'No' to quit: ").strip().upper() == "YES"

# Main game logic
keep_playing = True
while keep_playing:
    # Setup snake, food, and scoreboard
    segments = create_snake()
    food = Food()
    scoreboard = Scoreboard()

    # Get the user's control choice
    control_choice = get_control_choice()
    set_controls(control_choice)

    # Main game loop
    game_is_on = True
    while game_is_on:
        screen.update()
        move(segments)
        time.sleep(0.1)

        # Detect collision with food
        if segments[0].distance(food) < 15:
            food.refresh()
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            segments.append(new_segment)
            scoreboard.increase_score()

        # Detect collision with wall
        if segments[0].xcor() > 290 or segments[0].xcor() < -290 or segments[0].ycor() > 290 or segments[0].ycor() < -290:
            scoreboard.game_over()
            game_is_on = False

        # Detect collision with tail
        for segment in segments[1:]:
            if segments[0].distance(segment) < 10:
                scoreboard.game_over()
                game_is_on = False

    # Ask if the user wants to keep playing
    keep_playing = ask_play_again()

# Close the screen when the user decides to quit
screen.bye()
