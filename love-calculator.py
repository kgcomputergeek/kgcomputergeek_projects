"""
 This is a difficult challenge! 💪
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is *z*."
e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

These functions will help you:
lower() count()

Example Input 1
Kanye West
Kim Kardashian
Example Output 1
The Love Calculator is calculating your score...
Your score is 42, you are alright together.
Example Input 2
Brad Pitt
Jennifer Aniston
Example Output 2
The Love Calculator is calculating your score...
Your score is 73.
Hint
You can check your values against mine using this table:

Name 1	Name 2	Score
Brad Pitt	Jennifer Aniston	73
Prince William	Kate Middleton	67
Ashton Kutcher	Mila Kunis	63
Angela Yu	Jack Bauer	53
David Beckham	Victoria Beckham	45
Mario	Princess Peach	43
Kanye West	Kim Kardashian


"""
#print("The Love Calculator is calculating your score...")
name_1 = input("Please input your name?:  \n").lower() # What is your name?
name_2 = input("What is your crush's name?:  \n").lower() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇


letra_t = (name_1.count("t"))+ (name_2.count("t"))
letra_r = (name_1.count("r"))+ (name_2.count("r"))
letra_u = (name_1.count("u"))+ (name_2.count("u"))
letra_e = (name_1.count("e"))+ (name_2.count("e"))


letra_l = (name_1.count("l"))+ (name_2.count("l"))
letra_o = (name_1.count("o"))+ (name_2.count("o"))
letra_v = (name_1.count("v"))+ (name_2.count("v"))
letra_E = (name_1.count("e"))+ (name_2.count("e"))

in_name_TRUE = str(letra_t + letra_r + letra_u + letra_e)

in_name_LOVE = str(letra_l + letra_o + letra_v + letra_E)

Love_in_first_name = str(letra_l + letra_o + letra_v + letra_E)

name_num = in_name_TRUE + Love_in_first_name

name_num_as_int = int(name_num)

if name_num_as_int < 10 or name_num_as_int > 90:
    print(f"Your score is {name_num}, you go together like coke and mentos.")
elif name_num_as_int > 40 and name_num_as_int < 50:
    print(f"Your score is {name_num}, you are alright together.")
else:
    print(f"Your score is {name_num}.")
