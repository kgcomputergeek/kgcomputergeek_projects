# ######-DAY7 CHALLENGE 3 ######

# """
# objectives as outlined by the teacher

# #TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

# """


# import random

# # Step 1
# word_list = ["aardvark", "baboon", "camel"]

# # TODO-1: Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# chosen_word = random.choice(word_list)

# # Initialize a variable to store the user's remaining guesses
# remaining_guesses = len(chosen_word)

# # Create an empty list to store correctly guessed letters
# correct_guesses = []

# # Create an empty list to store the display of the word
# display = ['_' for _ in chosen_word]

# # Main loop for guessing
# while '_' in display:
#     # Ask the user to guess a letter and make the guess lowercase
#     guess = input("Guess a letter: ").lower()

#     # Check if the guessed letter is one of the letters in the chosen_word
#     if guess in chosen_word:
#         print("Right")
#         # Add the correct guess to the list of correct guesses
#         correct_guesses.append(guess)
        
#         # Update the display with the correctly guessed letters
#         for i in range(len(chosen_word)):
#             if chosen_word[i] == guess:
#                 display[i] = guess
#         print(" ".join(display))  # Print the updated display
#     else:
#         print("Wrong")

#     # Check if the user has guessed all the letters
#     if set(chosen_word) == set(correct_guesses):
#         print("Congratulations! You guessed the word:", chosen_word)
#         break

# # Print the final display
# print(" ".join(display))

 ######-DAY7 CHALLENGE 3-######

"""
objectives as outlined by the teacher

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

"""

"""
Step 1 - import random (see first line of code below)
#This line imports the random module, which we'll use to randomly select a word from the word list.

"""
import random

"""
Step 2 - Choosing a Word from the List


We have a list of words word_list.
We use random.choice(word_list) to randomly select one word from the list and assign it to the variable chosen_word

"""
word_list = ["aardvark", "baboon", "camel"]


"""
step 3 - main loop for game

This is the main loop for the game. It will continue running until explicitly stopped with a break statement.

"""

# Main loop for the game
while True:
    # Initialize a variable to store the randomly chosen word
    
    """
Step 4 - Choosing a Random Word and Initializing Variables

In each iteration of the main loop, we choose a random word from the word_list and initialize variables:

the variable, chosen_word stores the randomly chosen word.

the variable, remaining_guesses stores the number of remaining guesses the user has, initialized to the length of the chosen_word.

the variable, correct_guesses stores the letters the user has correctly guessed, initialized as an empty list.

the variable, display is a list initialized with underscores (_), representing the letters of the chosen_word yet to be guessed.

"""
    chosen_word = random.choice(word_list)

    # Initialize a variable to store the user's remaining guesses
    remaining_guesses = len(chosen_word)

    # Create an empty list to store correctly guessed letters
    correct_guesses = []

    # Create an empty list to store the display of the word
    display = ['_' for _ in chosen_word]

    """
    step 5 - loop for guessing

    This loop continues as long as there are underscores (_) in the display list, indicating that there are still letters to be guessed, and the user has remaining guesses.
    
    """
    
    # Main loop for guessing
    while '_' in display and remaining_guesses > 0:
        
        """
        step 6 - asking the user to guess a letter

        The program prompts the user to guess a letter and converts the input to lowercase for consistency.
        """
        
        # Ask the user to guess a letter and make the guess lowercase
        guess = input("Guess a letter: ").lower()


        """
        step 7 - Checking the Guessed Letter:
        If the guessed letter is in the chosen_word, the program proceeds to update the correct_guesses and display lists accordingly. Otherwise, it informs the user that the guess was incorrect.
        
        """

        # Check if the guessed letter is one of the letters in the chosen_word
        if guess in chosen_word:
            print("Right")

            """
            step 8 - Updating Correct Guesses and Display:

            The program updates the correct_guesses list with the correctly guessed letter.
            It then iterates through each position in the chosen_word to check if the guessed letter matches. If it does, it updates the corresponding position in the display list with the guessed letter.
                        
            """
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

        """
        step 9 - Checking for End Conditions:

        After each guess, the program checks if the user has guessed all the letters correctly or if they have run out of guesses. If the user guesses all the letters correctly, it congratulates the user. If the user runs out of guesses, it reveals the word.
        
        """

    # Check if the user has guessed all the letters
    if set(chosen_word) == set(correct_guesses):
        print("Congratulations! You guessed the word:", chosen_word)
    else:
        print("Sorry, you've run out of guesses. The word was:", chosen_word)


        """
        step 10 - asking the User if They Want to Keep Playing:

        After each game is finished, the program asks the user if they want to play again. If the user declines, the game stops. If the user agrees to play again, a new word is chosen, and the game starts again.
        """

    # Ask the user if they want to keep playing
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("You said no. Goodbye!")
        break


    """
    step 11- Removing Played Words from the Word List:

    The chosen word is removed from the word_list to ensure that it isn't chosen again in subsequent games.
    """
    # Remove the chosen word from the word list if all words have been played
    word_list.remove(chosen_word)


#     """
#     step 12 - Exiting the Game Loop:
    
#     If all words have been played or the user declines to play again, the program exits the main loop, and a farewell message is printed.
        
    
#     """
#     if not word_list:
#         print("You've played all the words. Goodbye!")
#         break

# print("Goodbye!")

