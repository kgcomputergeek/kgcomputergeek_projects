#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


import random

# ASCII art logo
logo = """
  __  __            _    _ _   ____  _ _      
 |  \/  |          | |  | (_) |  _ \| (_)     
 | \  / | ___  __ _| | _| |_| | |_) | |_  ___ 
 | |\/| |/ _ \/ _` | |/ / | | |  _ <| | |/ _ \\
 | |  | |  __/ (_| |   <| | | | |_) | | |  __/
 |_|  |_|\___|\__,_|_|\_\_|_| |____/|_|_|\___|
"""

# Function to set the difficulty level
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return 10
    else:
        return 5

# Function to check the player's guess
def check_guess(guess, answer, turns):
    """Checks the player's guess against the answer and returns remaining turns."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

# Function to play the game
def play_game():
    print(logo)  # Display the logo
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    answer = random.randint(1, 100)  # Generate a random number between 1 and 100
    turns = set_difficulty()  # Set the difficulty level
    
    guess = 0  # Initialize the guess variable
    while guess != answer and turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        
        # Let the player make a guess
        guess = int(input("Make a guess: "))
        
        # Check the guess
        turns = check_guess(guess, answer, turns)
        
        # If no turns are left, the player loses
        if turns == 0:
            print("You've run out of guesses, you lose.")
            print(f"The correct answer was {answer}.")
        elif guess != answer:
            print("Guess again.")

# Main loop to play the game
while input("Do you want to play the Number Guessing Game? Type 'yes' or 'no': ").lower() == "yes":
    play_game()
