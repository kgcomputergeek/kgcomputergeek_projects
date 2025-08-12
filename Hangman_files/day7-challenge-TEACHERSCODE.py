"""
Teacher's code has a logic error in which does not give the user multiple 
opportunities to guess the word (the length of the randomly chosen word)



"""



# #Step 1 

# word_list = ["aardvark", "baboon", "camel"]

# #TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# import random
# chosen_word = random.choice(word_list)

# #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input("Guess a letter: ").lower()

# #TODO-3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")



import random

# Step 1
word_list = ["aardvark", "baboon", "camel"]

# TODO-1: Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

# Initialize a variable to store the user's remaining guesses
remaining_guesses = len(chosen_word)

# Create an empty list to store correctly guessed letters
correct_guesses = []

# Main loop for guessing
while remaining_guesses > 0:
    # Ask the user to guess a letter and make the guess lowercase
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter is one of the letters in the chosen_word
    if guess in chosen_word:
        print("Right")
        # Add the correct guess to the list of correct guesses
        correct_guesses.append(guess)
    else:
        print("Wrong")

    # Decrease the remaining guesses
    remaining_guesses -= 1

    # Check if the user has guessed all the letters
    if set(chosen_word) == set(correct_guesses):
        print("Congratulations! You guessed the word:", chosen_word)
        break
    elif remaining_guesses == 0:
        print("Sorry, you've run out of guesses. The word was:", chosen_word)
