"""
You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

Your program should print each number from 1 to 100 in turn and include number 100.

When the number is divisible by 3 then instead of printing the number it should print "Fizz".

When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

e.g. it might start off like this:

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...etc

Hint
Remember your answer should start from 1 and go up to and including 100.

Each number/text should be printed on a separate line.
"""


# print("Welcome to the FizzBuzz Job Interview!")
# #target = int(input("Please enter a number between 0 and 1000: "))
# def fizzbuzz(n):
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)
#
# # Print numbers from 1 to 100 using fizzbuzz
# fizzbuzz(100)


""" PROGRAM BASED ON USER INPUT FOR N"""
print("Welcome to the FizzBuzz Job Interview!")
def fizzbuzz(n): #we have the expressions set to zero to determine divisibility due to integer division with modulus which deals with the remainder
    for i in range(1, n+1):
        if i % 3 == 0 & i % 5 == 0: #divisible by 3 and 5
            print("FizzBuzz")
        elif i % 3 == 0: #divisible by 3
            print("Fizz")
        elif i % 5 == 0: #divisible by 5
            print("Buzz")
        else:
            print(i)

# Ask the user for input
user_input = input("Please enter a number: ") #let user input represent N,

# Convert the input to an integer
try:
    n = int(user_input)
except ValueError:
    print("Please enter a valid integer: ")
    exit()

# Call the fizzbuzz function with user input
fizzbuzz(n)


