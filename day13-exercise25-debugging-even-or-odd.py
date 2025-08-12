"""

Instructions
Read this the code in main.py
Spot the problems 🐞.
Modify the code to fix the program.
Fix the code so that it works and passes the tests when you submit.

Hint
Review the previous lesson and go through the 10 steps to tackle these debugging problems.


####ORIGINAL CODE####
number = int(input()) # Which number do you want to check?

if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  
"""
#######FIXED CODE#######

number = int(input("Which number do you want to check?:  ")) # Which number do you want to check?

if number % 2 == 0: #if the number is divisible b two and the remainder is 0, then this is an even number
  print("This is an even number.")
else:
  print("This is an odd number.")
  