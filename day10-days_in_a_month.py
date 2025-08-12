"""
Instructions
Convert the is_leap() functtion
In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

Create a new function called days_in_month()
You are then going to modify a function called days_in_month() which will take a year and a month as inputs, e.g.

days_in_month(year=2022, month=2)
And it will use this information to work out if the year is a leap year and decide the number of days in the month, then return that as the output, e.g.:

28
The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.

Hint
Look at the function call at the bottom of the code to see the positional arguments. The order is very important.

Feel free to choose your own parameter names.

Remember that month_days is a List and Lists in Python start at position 0. So the number of days in January is month_days[0]

Be careful with indentation.

Here was the starting code:

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year")
      else:
        print("Not leap year")
    else:
      print("Leap year")
  else:
    print("Not leap year")
  
# TODO: Add more code here 👇
def days_in_month():
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

"""

"""

Step-By-Step Explaination


Convert is_leap() function to return a boolean:

Change the function so it returns True if the year is a leap year and False otherwise.
Create days_in_month() function:

This function will take year and month as arguments.
Use the is_leap() function to determine if it's a leap year.
Return the number of days in the given month, accounting for leap years.



How It Works
is_leap(year) Function:

The function checks if the year is divisible by 4.
If it is divisible by 4, it further checks if it is divisible by 100.
If it is divisible by 100, it finally checks if it is divisible by 400.
Based on these conditions, it returns True if it is a leap year, otherwise False.
days_in_month(year, month) Function:

It takes two arguments: year and month.
The list month_days holds the number of days in each month for a non-leap year.
It first checks if the provided month is valid (between 1 and 12).
It then uses the is_leap() function to check if the year is a leap year and if the month is February.
If it's a leap year and February, it returns 29 days. Otherwise, it returns the number of days from the month_days list, adjusting for zero-based indexing (month - 1).
User Input and Function Call:

The user is prompted to enter a year and a month.
These inputs are passed to the days_in_month function.
The result (number of days) is printed.
This should meet your requirements and handle leap years correctly!










"""

def is_leap(year):#Here we're making a tool (function) called is_leap that checks if a year is special (a leap year).
    if year % 4 == 0: #First, see if the year can be divided by 4 without any leftovers. If it can, we go to the next step.
        if year % 100 == 0: #Now, we check if the year can also be divided by 100 without leftovers. If it can, we go to the next step.
            if year % 400 == 0:#Next, we see if the year can be divided by 400 without leftovers. If it can, it means it's a leap year.
                return True #If the year can be divided by 400, we say "Yes, it's a leap year" by returning True.
            else: #If the year can be divided by 100 but not by 400, 
                return False #we say "No, it's not a leap year" by returning False.
        else: #If the year can be divided by 4 but not by 100, 
            return True #we say "Yes, it's a leap year" by returning True.
    else: #If the year can't be divided by 4,
        return False # we say "No, it's not a leap year" by returning False

def days_in_month(year, month):#We're making another tool called days_in_month that tells us how many days are in a month for a given year.
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #We have a list of numbers that tell us how many days each month has in a regular year. January has 31 days, February has 28, and so on.
    
    if month < 1 or month > 12: #checking if the month number is not between 1 and 12. 
        return "Invalid month" #If it's not, we say "Invalid month"
    
    if is_leap(year) and month == 2: #using the is_leap tool to check if the year is a leap year and if the month is February. If both are true,
        return 29 # we say February has 29 days.
    else: #If the year is not a leap year or the month is not February, we look up our list to see how many days the month has. 
        return month_days[month - 1] #We use month - 1 because lists start counting from 0. So January (month 1) is at position 0, February (month 2) is at position 1, and so on.

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: ")) # asking the user to tell us a year. Then, We turn their answer into a number and call it year.

month = int(input("Enter a month: ")) # asking the user to tell us a month. Then, we turn their answer into a number and call it month.
days = days_in_month(year, month) #using our days_in_month tool to find out how many days are in the given month of the given year. We call the result days
print(days) #telling the user how many days are in the month by showing them the number days

