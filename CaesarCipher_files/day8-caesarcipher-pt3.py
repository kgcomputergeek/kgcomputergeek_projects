# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# #TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")

# if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#   decrypt(cipher_text=text, shift_amount=shift)

# #TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.




"""
---Explanation of Day8 Caesar Cipher Code Part 3---

Our Alphabet List:
Think of the alphabet like a long train with carriages labeled with letters:
['a', 'b', 'c', 'd', 'e', ... 'x', 'y', 'z', 'a', 'b', 'c', ... 'x', 'y', 'z']
Notice that we have the alphabet twice in this list. This helps us wrap around when we shift letters.

Choosing to Encode or Decode:
We ask you if you want to make a secret message (encode) or figure out a secret message (decode). You tell us by typing "encode" or "decode".

Getting the Message:
You type a message you want to hide or reveal. Let's say your message is "hello".

Shifting Letters:
You tell us how many steps to move each letter in the alphabet. This number is called the "shift". For example, if you say 3, 'a' would become 'd', 'b' would become 'e', and so on.

The Caesar Function:

We have a special function called caesar that does all the work. It takes your message, the shift number, and whether you're encoding or decoding.
Inside the function, we look at each letter in your message:
If it's a letter, we find where it is in our alphabet list and move it forward or backward by the shift number.
If it's not a letter (like a space or punctuation), we leave it as is.
Encoding and Decoding:

When you want to encode, we move letters forward in the alphabet by the shift number.
When you want to decode, we move letters backward by the shift number. We do this by using a negative shift.
Printing the Result:

After shifting all the letters, we put them together to make the new secret message.
We then show you the secret message if you're encoding, or the original message if you're decoding.


So, when you run this game:

It asks if you want to hide a message or figure out a hidden message.
It asks for the message and the shift number.
It moves the letters around to create a secret message or reveal one, and then shows you the result.
It's like playing with a secret code machine that shifts letters to make new words!

"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

"""
#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
"""
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is: {end_text}")

"""
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

"""
# Call the caesar function
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
