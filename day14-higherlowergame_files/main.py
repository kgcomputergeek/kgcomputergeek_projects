# main.py

import random
from art import logo, vs
from game_data import data

# Function to format the account data into a printable format
def format_data(account):
    """Format the account data into printable format: name, description and country."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# Function to check if the user's guess is correct
def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess and returns True if they got it right. Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Display the logo
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Main game loop
while game_should_continue:
    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    # Ask the user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    
    # Check if user is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
    # Clear the screen between rounds
    print("\n" * 50)
    print(logo)
    
    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
