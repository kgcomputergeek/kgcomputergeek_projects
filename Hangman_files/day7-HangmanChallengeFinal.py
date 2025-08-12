"""
######-DAY7 CHALLENGE 5-######


objectives as outlined by the teacher

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
Delete this line: word_list = ["ardvark", "baboon", "camel"]
#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])


"""

#
import random

# Step 1
#word_list = ["aardvark", "baboon", "camel"]
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo
    #print(stages[lives])
# Main loop for the game


while True:
    # Initialize a variable to store the randomly chosen word
    chosen_word = random.choice(word_list)

    # Initialize a variable to store the user's remaining guesses
    lives = 6

    # Create an empty list to store correctly guessed letters
    correct_guesses = []

    # Create an empty list to store the display of the word
    display = ['_' for _ in chosen_word]

    # Main loop for guessing
    print(logo) #placed here because this is where the game begins
    while '_' in display and lives > 0:
        # Ask the user to guess a letter and make the guess lowercase
        guess = input("Guess a letter: ").lower()

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
            # Decrease the remaining lives and print the corresponding hangman stage
            lives -= 1
            print(f"Lives remaining: {lives}")
            print(stages[len(stages) - lives - 1])
            
        # Check if lives go down to 0
        if lives == 0:
            print("You lose.")
            break

    # Check if the user has guessed all the letters
    if set(chosen_word) == set(correct_guesses):
        print("Congratulations! You guessed the word:", chosen_word)
        print(f"Lives remaining: {lives}")
    else:
        print("Sorry, you've run out of lives. The word was:", chosen_word)

    # Ask the user if they want to keep playing
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        #print("You said no. Goodbye!") #don't need this it's just unnecessary
        break

    # Remove the chosen word from the word list if all words have been played
    word_list.remove(chosen_word)
    if not word_list:
        print("You've played all the words. Goodbye!")
        break

print("Goodbye!")



