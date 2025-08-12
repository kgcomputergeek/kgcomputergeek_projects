
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    position = alphabet.index(char)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)






"""



# # main.py
# from art import logo

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# # Print the logo at the start of the program
# print(logo)

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     if cipher_direction == "decode":
#         shift_amount *= -1
#     for letter in start_text:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             new_position = (position + shift_amount) % 26
#             end_text += alphabet[new_position]
#         else:
#             end_text += letter
#     print(f"The {cipher_direction}d text is: {end_text}")

# # Call the caesar function
# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

"""
Step-by-step explanation:
Import the logo:

from art import logo imports the ASCII art logo from art.py.
Print the logo:

print(logo) displays the ASCII art when the program starts.
Define the caesar function:

This function handles both encoding and decoding.
It adjusts the shift amount with shift_amount = shift_amount % 26 to ensure it stays within the range of the alphabet.
Handle the shift amount:

Using shift_amount % 26, we wrap around shifts greater than the alphabet length. For example, a shift of 27 is effectively the same as a shift of 1 (27 % 26 = 1).
Create a while loop to keep the program running:

The run_caesar_cipher function contains the while loop.
It repeatedly asks the user for direction, text, and shift amount, then calls caesar with those inputs.
After each round, it asks the user if they want to go again. If they type 'no', the loop breaks and the program ends.
Now the program will keep running, asking for new inputs and encoding/decoding as many times as the user wants. The shift amount will always work correctly even if it's greater than 26.

"""

# main.py
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] * 2

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    # Ensure the shift_amount is within the range of 0-25
    shift_amount = shift_amount % 26
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is: {end_text}")

def run_caesar_cipher():
    print(logo)
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

        restart = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
        if restart != 'yes':
            print("Goodbye!")
            break

# Start the program
run_caesar_cipher()
