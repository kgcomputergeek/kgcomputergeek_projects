"""
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height x wall width) ÷ coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 * 4) / 5
               = 1.6
But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

Example Input
3
9
Example Output
You'll need 6 cans of paint.
Hint
Stackoveflow link on how to round up a number: https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python




"""





# Write your code below this line 👇
print("WELCOME TO THE PAINT AREA CALCULATOR")



# # Write your code above this line 👆
# # Define a function called paint_calc() so the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input()) # Height of wall (m)
# test_w = int(input()) # Width of wall (m)

import math

def paint_calc(height, width):
    # Calculate the area of the wall
    area = height * width
    
    # Calculate the number of cans needed (rounding up)
    cans_needed = math.ceil(area / 5)
    
    return cans_needed

def run_program():
    # List to store all the numbers of cans needed
    all_cans_needed = []

    while True:
        # Get user input for wall height and width
        wall_height = float(input("Enter the height of the wall in meters: "))  # Height of wall (m)
        wall_width = float(input("Enter the width of the wall in meters: "))  # width of wall (m)

        # Calculate the number of cans needed
        cans_needed = paint_calc(wall_height, wall_width)
        all_cans_needed.append(cans_needed)

        # Print the result
        print(f"You'll need {cans_needed} can(s) of paint.")

        # Ask the user if they want to run the program again
        again = input("Do you want to calculate again? (yes/no): ").lower()
        if again != 'yes':
            break
    
    return all_cans_needed

# Run the program
all_results = run_program()

# Print all the numbers of cans needed
print("All results:", all_results)
