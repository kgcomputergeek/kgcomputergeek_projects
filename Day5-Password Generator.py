

#Password Generator Project
import random
import string
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

def generate_password(length=12, nr_numbers=True, nr_letters=True, nr_symbols=True):
    # Define characters based on user input
    characters = ''
    if nr_letters:
        characters += string.ascii_letters
    if nr_numbers:
        characters += string.digits
    if nr_symbols:
        characters += string.punctuation
    if not characters:
        print("Error: At least one character type (numbers, letters, or symbols) must be selected.")
        return None

# Generate a password by randomly choosing characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))

    # Shuffle the password to randomize the order of characters
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

length = int(input("Enter the length of the password: ")) #length will be how many characters in your password (aka symbols, numbers, and letters altogether)

nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = generate_password(length, nr_numbers, nr_letters, nr_symbols)
if password:
    print(f"Here is your generated password:{password}")
#randomness function