"""
You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.

Example Input 1
10
Example Output 1
30
Example Input 2
52
Example Output 2
702
Hint
There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.


"""

target = int(input("Please enter a number between 0 and 1000: ")) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
even_sum = 0
for number in range(2, target + 1, 2):
    """
#let 2 in the parameters represent our first even number, let target represent the number collected from user input, and the "target + 1" with the 1 added is there to include the target number in the summation, and finally 2, is how much we want to add to the starting number each time
    """
    even_sum += number
print(f"The total of the even numbers (0-1000) is: {even_sum}")


#alternative solution
