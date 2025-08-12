
#### Day 7 - Challenge 2 ####
"""
objectives outlined by teacher

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.


#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

"""


"""
Step 1 - import random (see first line of code below)

#This line imports the random module, which we'll use to randomly select a word from the word list.

"""
import random 


word_list = ["aardvark", "baboon", "camel"] 
#choosing a word from the word_list We have a list of words word_list.
# We use random.choice(word_list) to randomly select one word from the list and assign it to the variable chosen_word.

# TODO-1: Randomly choose a word from the word_list and assign it to a variable called chosen_word.

"""
Step 2 - Choosing a Word from the List


We have a list of words word_list.
We use random.choice(word_list) to randomly select one word from the list and assign it to the variable chosen_word

"""
chosen_word = random.choice(word_list)

"""
Step 3 - Intializing variables
the variable remaining_guesses stores the number of remaining guesses the user has.
the variable correct_guesses stores the letters the user has correctly guessed.
the variable display is a list initialized with underscores (_), representing the letters of the chosen word yet to be guessed.
"""
# Initialize a variable to store the user's remaining guesses
remaining_guesses = len(chosen_word)

# Create an empty list to store correctly guessed letters
correct_guesses = []

# Create an empty list to store the display of the word
display = ['_' for _ in chosen_word]
"""
step 4 - main loop for guessing
This loop continues as long as there are remaining guesses (remaining_guesses > 0).

"""
# Main loop for guessing
while remaining_guesses > 0:

    """
    step 5 - asking the user to guess a letter

    The program then prompts the user to guess a letter and converts the input to lowercase for consistency.

    """    
    # Ask the user to guess a letter and make the guess lowercase
    guess = input("Guess a letter: ").lower()


    """

    step 6 - checking to see if the guessed letter is in the variable chosen_word

    If the guessed letter is in the chosen_word, the program proceeds to update the correct_guesses and display lists accordingly. Otherwise, it informs the user that the guess was incorrect.

    """


    """
    step 7 - updating the correct_guesses and display


    The program updates the correct_guesses list with the correctly guessed letter.
    
    It then iterates through each position in the chosen_word to check if the guessed letter matches. If it does, it updates the corresponding position in the display list with the guessed letter


    step 9 - The loop continues until either the user guesses all the letters correctly (set(chosen_word) == set(correct_guesses)) or runs out of guesses (remaining_guesses == 0).
    Once the loop ends, the program prints the final display of the word, whether the user guessed it correctly or ran out of guesses.
    """
    # Check if the guessed letter is one of the letters in the chosen_word
    if guess in chosen_word:
        print("Right")
        # Add the correct guess to the list of correct guesses
        correct_guesses.append(guess)
        
        # Update the display with the correctly guessed letters
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print(" ".join(display))  # Print the updated display
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


"""
step 8 - Printing the Updated Display:
After each guess, the program prints the current state of the display list, showing the guessed letter in the correct position and every other letter replaced with "_".

"""
# Print the final display
print(" ".join(display))
