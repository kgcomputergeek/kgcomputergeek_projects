"""
INSTRUCTIONS:


Instructions
The objective is to write a program that will collect the names and bids of different people. The program should ask for each bidder's name and their bid individually.

Welcome to the secret auction program. 
What is your name?: Angela
What's your bid?: $123
Are there any other bidders? Type 'yes' or 'no'.
yes
If there are other bidders, the screen should clear, so you can pass your phone to the next person. If there are no more bidders, then the program should display the name of the winner and their winning bid.

The winner is Elon with a bid of $55000000000
Use your knowledge of Python dictionaries and loops to solve this challenge.

My console doesn't clear!
This will happen if you’re using an IDE other than replit (e.g., VSCode, PyCharm etc). Similar to how we used the "random" module previously, in this project we will use the "replit" module. The clear() function is available here via the replit module without any extra configuration.

I’ll cover how to use PyCharm and import modules on Day 15. That said, you can write your own clear() function or configure your IDE like so:

"""




#from replit import clear
#HINT: You can call clear() to clear the output in the console.

"""
Part 2: The Secret Auction Game
Now, let's make the game where people can put in their bids.

Game File (secret_auction.py)
First, we need to tell the game to get the treasure chest drawing from the other file.


Steps in the Game
Show the Drawing: At the beginning, we show the treasure chest drawing.
Ask for Bids: We ask each player for their name and how much money they want to bid.
Check for More Players: After each bid, we ask if there are more players.
Clear the Screen: If there are more players, we clear the screen so they can't see the previous bids.
Find the Winner: When no more players want to bid, we see who bid the most money and they win!


"""


"""
1. Import the logo variable from art.py.
Print the logo at the start of the secret_auction function.
python
"""
import os
from art import logo  # Get the drawing from art.py



"""
Clear Screen Function:

The clear_screen function clears the terminal screen to hide the previous bidder's information. It uses the os.system command to execute the clear command depending on the operating system.
"""
def clear_screen():
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

"""


"""

"""
Find Highest Bidder Function:

The find_highest_bidder function iterates over the bidding record dictionary to find the highest bid and prints the winner.
"""
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


"""
Blind Auction Function:

The blind_auction function manages the bidding process.
It starts by printing a welcome message and initializes an empty dictionary to store bids.
A while loop keeps asking for bidders' names and bids until there are no more bidders.
If there are more bidders, the screen is cleared using the clear_screen function.

the clear_screen functions provides secrecy and protects the integrity of each bid
Once there are no more bidders, it calls the find_highest_bidder function to determine and print the winner.

"""
def blind_auction():
    print(logo)  # Show the treasure chest drawing
    print("Welcome to the secret auction program.")
    bids = {}
    bidding_finished = False

    while not bidding_finished:
        name = input("Please enter your name: ")
        bid = int(input("Please enter your bid?: $"))
        bids[name] = bid

        should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if should_continue == 'no':
            bidding_finished = True
            find_highest_bidder(bids)
        elif should_continue == 'yes':
            clear_screen()

# Run the auction program
blind_auction()
