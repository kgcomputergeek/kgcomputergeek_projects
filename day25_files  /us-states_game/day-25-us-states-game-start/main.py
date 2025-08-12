"""
U.S States Game
Objective: 

1. Converting user input to title case
2. Loading the state data from CSV
3.Checking if the guessed state is correct
Keeping track of correct guesses
Displaying the state name on the map at the correct coordinates
Showing the user's progress (e.g., "2/50 states correct")
Game loop and exit condition
"""

import turtle as tl
import pandas as pa

screen = tl.Screen()
screen.title("U.S. States Game")

map_image = "/Users/kgreen/PycharmProjects/PYLEARNING/day25_files  /us-states_game/day-25-us-states-game-start/blank_states_img.gif"

screen.addshape(map_image)
tl.shape(map_image) #changes shape to the map image


#create turtle for writing state names on the map
write_state_name = tl.Turtle()
write_state_name.penup()
write_state_name.hideturtle()#hides turtle cursor from screen

# Create a turtle for displaying the score
display_score = tl.Turtle()
display_score.penup()
display_score.hideturtle()
display_score.goto(0, 250)  # Position at the top of the screen

# Load the state data from CSV
# CSV should have columns: state,x,y (state name and coordinates)
states_data = pa.read_csv("/Users/kgreen/PycharmProjects/PYLEARNING/day25_files  /us-states_game/day-25-us-states-game-start/50_states.csv")
all_states = states_data.state.tolist()

# Initialize variables to track game progress
states_guessed = []
total_states = len(all_states)


# Function to convert guess to title case
def guess_convert_to_title_case(state_guess):
    return state_guess.title() if state_guess else"" # purpose of the if state_guess else "" part is not about whether formatting is needed, but about handling the case where the input might be None or an empty string, which would cause an error if you tried to call .title() on it.


# Function to update the score display
def update_score():
    """Update the score display showing correct guesses."""
    display_score.clear()
    display_score.write(f"{len(states_guessed)}/{total_states} States Correct", 
                       align="center", font=("Arial", 16, "normal"))

# Initial score display
update_score()

#main game loop
game_is_on = True
while game_is_on:

    users_guess = screen.textinput(title=f"Guess the state", prompt="What's another state's name? (Type 'Exit' to quit)") #what the user is answering in response to the prompt
 
#check if user would like to quit
    if not users_guess or users_guess.lower() == 'exit':
        # Generate a CSV of states the user didn't guess
        missing_states = [state for state in all_states if state not in states_guessed]
        pa.DataFrame(missing_states, columns=["state"]).to_csv("states_to_learn.csv")
        # Print confirmation message
        print(f"GAME OVER! Created states_to_learn.csv with {len(missing_states)} states to learn.")
        break

# Convert guess to title case
    formatted_guess = guess_convert_to_title_case(users_guess)
    
    # Check if the guess is correct and not already guessed
    if formatted_guess in all_states and formatted_guess not in states_guessed:
        # Add to guessed states list
        states_guessed.append(formatted_guess)
        
        # Get coordinates for the state
        state_data = states_data[states_data.state == formatted_guess]
        x_coord = int(state_data.x.iloc[0])
        y_coord = int(state_data.y.iloc[0])
        
        # Write the state name on the map
        write_state_name.goto(x_coord, y_coord)
        write_state_name.write(formatted_guess, align="center", font=("Arial", 8, "normal"))
        
        # Update the score
        update_score()
        
        # Check if all states have been guessed
        if len(states_guessed) == total_states:
            display_score.clear()
            display_score.write("Congratulations! You've guessed all states!", 
                              align="center", font=("Arial", 16, "bold"))
            game_is_on = False

# Note: No exitonclick() to allow the program to end cleanly when exiting


# def convert_to_title_case(state_guess):
#     """
#     Convert user input to title case formatting.
#     Example: 'new york' -> 'New York', 'TEXAS' -> 'Texas'
#     """
#     return state_guess.title()



"""
don't actually need bc we already have the csv values containing the coordinates


# def get_mouse_click_coord(x,y):
#     print(x,y)
# tl.onscreenclick(get_mouse_click_coord) #event listener that listens for when the mouse clicks to give the location of the click

#tl.mainloop()

"""


