"""

Objectives: using list comprehension cut down the code by 3-4 lines regarding the states to learn


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
        pa.DataFrame([state for state in all_states if state not in states_guessed], columns=["state"]).to_csv("states_to_learn.csv")
        # Print confirmation message
        print(f"GAME OVER! Created states_to_learn.csv with {len(all_states) - len(states_guessed)} states to learn.")
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