# #Step 1 




 
import random

# List of words
word_list = ["aardvark", "baboon", "camel"] # List of words

# Randomly choose a word from the list
random_word = random.choice(word_list)

# Create a list to store the guessed letters
guessed_letters = []

# Counter to keep track of the number of tries
tries = 0

# Initialize a variable to store the revealed word
revealed_word = ['_'] * len(random_word)

# Function to reveal guessed letters in the word
def reveal_letters(word, guessed):
    revealed = ''
    for letter in word:
        if letter in guessed:
            revealed += letter
        else:
            revealed += '_'
    return revealed

# Main loop for guessing
while '_' in revealed_word and tries < len(random_word):
    # Ask the user to guess a letter
    guess = input("Guess a letter: ").lower()
    
    # Add the guessed letter to the list of guessed letters
    guessed_letters.append(guess)
    
    # Check if the guessed letter is correct
    if guess in random_word:
        print(f"Correct! '{guess}' is one of the letters in the word.")
        # Update the revealed word with the guessed letters
        revealed_word = list(reveal_letters(random_word, guessed_letters))
    else:
        print(f"Incorrect! '{guess}' is not one of the letters in the word.")

    # Increment the number of tries
    tries += 1

# Check if the user has guessed the word correctly
if '_' not in revealed_word:
    print("Congratulations! You have guessed the word:", random_word)
else:
    print("Sorry, you have run out of tries. The word was:", random_word)

# Print the list of guessed letters
print("Guessed letters:", guessed_letters)
