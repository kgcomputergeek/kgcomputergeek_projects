"""
instructions
Read this the code in main.py
Spot the problems 🐞.
Modify the code to fix the program.
No shortcuts - don't copy-paste to replace the code entirely with a working solution.
Fix the code so that it works and when you hit submit it should pass all the tests.


####ORIGINAL CODE####


# Which year do you want to check?
year = input()

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
"""


year = int(input("Which year do you want to check?:  ")) #asks user to enter whar year they want to check for leap year

if (year % 4 == 0): #if year is divisible by 4 w/o an leftovers, then it is not a leap year and the program moves onto the second condition. if it's not, the program says it's not a leap year and stops.
  if (year % 100 == 0): #if year is divisible by 100 w/o an leftovers, then the program moves to the third condition. if it's not, the program says it's a leap year and stops.
    if (year % 400 == 0): #this is the third condition (aka the last stop). the code stops here. if year is divisible by 400 w/o an leftovers, then leap year will print. if it's not, the program will print non-leap year.
      print(f"The year {year} is a leap year.")
    else:
      print(f"The year {year} is not a leap year.")
  else:
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")
