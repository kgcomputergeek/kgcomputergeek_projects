# from turtle import Turtle, Screen
# import random

# # Create a screen object
# screen = Screen()
# screen.setup(width=500, height=400)  # Set up the screen size

# # Define colors and y positions for the turtles
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# y_positions = [-70, -40, -10, 20, 50, 80]

# # Display available colors in the menu
# color_menu = "Choose a color to bet on:\n"
# for color in colors:
#     color_menu += f"- {color.capitalize()}\n"
# user_bet = screen.textinput(title="MAKE YOUR BET", prompt=color_menu)

# turtles = []

# # Create 6 turtles and set their starting positions
# for index in range(6):
#     new_turtle = Turtle(shape="turtle")
#     new_turtle.color(colors[index])
#     new_turtle.penup()
#     new_turtle.goto(x=-230, y=y_positions[index])
#     turtles.append(new_turtle)

# # Start the race
# def start_race():
#     race_on = True

#     while race_on:
#         for turtle in turtles:
#             if turtle.xcor() > 230:  # Check if a turtle has crossed the finish line
#                 race_on = False
#                 winning_color = turtle.pencolor()
#                 print(f"The {winning_color} turtle won the race!")

#                 if winning_color.lower() == user_bet.lower():  # Check if user's bet matches the winning turtle's color
#                     print(f"Congratulations! Your {winning_color} turtle won the race!")
#                 else:
#                     print(f"Sorry! Your {user_bet} turtle lost. The {winning_color} turtle won the race.")
#                 break
#             random_distance = random.randint(0, 10)  # Move the turtles forward by a random distance
#             turtle.forward(random_distance)

#     # Ask the user if they want to play again
#     play_again = screen.textinput(title="Play Again?", prompt="Do you want to play again? Type 'yes' or 'no': ")
#     if play_again.lower() == 'yes':
#         reset_race()
#     else:
#         print("Thank you for playing!")
#         screen.bye()  # Close the turtle graphics window

# def reset_race():
#     # Reset turtle positions
#     for turtle in turtles:
#         turtle.goto(x=-230, y=y_positions[turtles.index(turtle)])

#     # Prompt the user to make a new bet
#     global user_bet
#     user_bet = screen.textinput(title="MAKE YOUR BET", prompt=color_menu)

#     start_race()

# # Initiate the first race
# start_race()

# # Keep the window open and responsive to all events
# screen.mainloop()

"""
"""

from turtle import Turtle, Screen
import random

# Create a screen object
screen = Screen()
screen.setup(width=500, height=400)  # Set up the screen size

# Define colors and y positions for the turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

# Display available colors in the menu
color_menu = "Choose a color to bet on:\n"
for color in colors:
    color_menu += f"- {color.capitalize()}\n"
user_bet = screen.textinput(title="MAKE YOUR BET", prompt=color_menu)

turtles = []

# Create 6 turtles and set their starting positions
for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])
    turtles.append(new_turtle)

# Initialize text turtles for displaying results
result_turtle = Turtle()
result_turtle.hideturtle()
result_turtle.penup()
result_turtle.goto(0, 0)

# Start the race
def start_race():
    race_on = True

    while race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:  # Check if a turtle has crossed the finish line
                race_on = False
                winning_color = turtle.pencolor()
                print(f"The {winning_color} turtle won the race!")

                if winning_color.lower() == user_bet.lower():  # Check if user's bet matches the winning turtle's color
                    result_turtle.color("green")
                    result_turtle.write(f"Congratulations! Your {winning_color} turtle won the race!", align="center", font=("Arial", 16, "normal"))
                else:
                    result_turtle.color("red")
                    result_turtle.write(f"Sorry! Your {user_bet} turtle lost. The {winning_color} turtle won the race.", align="center", font=("Arial", 16, "normal"))
                break
            random_distance = random.randint(0, 10)  # Move the turtles forward by a random distance
            turtle.forward(random_distance)

    # Ask the user if they want to play again
    play_again = screen.textinput(title="Play Again?", prompt="Do you want to play again? Type 'yes' or 'no': ")
    if play_again.lower() == 'yes':
        reset_race()
    else:
        print("Thank you for playing!")
        screen.bye()  # Close the turtle graphics window

def reset_race():
    result_turtle.clear()  # Clear previous result text
    # Reset turtle positions
    for turtle in turtles:
        turtle.goto(x=-230, y=y_positions[turtles.index(turtle)])

    # Prompt the user to make a new bet
    global user_bet
    user_bet = screen.textinput(title="MAKE YOUR BET", prompt=color_menu)

    start_race()

# Initiate the first race
start_race()

# Keep the window open and responsive to all events
screen.mainloop()
