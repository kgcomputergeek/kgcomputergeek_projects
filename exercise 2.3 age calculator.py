"""
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

"""
"""
max age: 90 years old
current age: any input
need to know how to break down age {years}into days, weeks, months


 x days
 y weeks
 z months left
 
 Steps
 
 1. create 3 variables (x-days, y weeks, z months) for age 90. This will not change as we are comparing the input to this age
 lifetime = 90 years
 365 days/yr
 12 months/yr
 52.143 weeks/yr

 
 
 
"""




# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

lifetime = 90 # years
"""
Declaration of Static Variables 

used proportions to calcuate days, weeks, and months for 90 years
90yrs * 365 days = 32,850 days
90 yrs * 52 wks = 4,680 weeks
90 yrs * 12 mos = 1,080 months

let x_1 represent x which comes from user input # 32,850 days in a calendar year
let y_1 represemt y which comes from user input # 4680 wks in a calendar year
let z_1 represent z which comes from user input # 1080 months in a calendar year
"""

# x_1 = 32850
# y_1 = 4680
# z_1 = 1080
"""
May need to declare these assumptions and complete the calculations for 90 years directly in the code
"""
#x_2 = 365 #days in a yr
#y_2 = 52 # wks in a yr
#z_3 = 12 # mos in a yr



x_1 = 365 #total days in a calendar year
y_1= 52 #total months in a calendar year
z_1 = 12 #total weeks in a calendar year


# x = 365 #total days in a calendar year
# y = 12 #total months in a calendar year
# z = 52 #total weeks in a calendar year

age_fix = int(age) #fix to avoid unsupported operand type() for -: 'int' and 'str'

"""
the calculation - 

"""
# a = lifetime * x_1
# b = lifetime * y_1
# c = lifetime * z_1
# days_left = (lifetime - age) * x_1
# wks_left = (lifetime - age) * y_1
# mos_left = (lifetime - age) * z_1
#age_fix) *z_1

x = (lifetime - age_fix) * x_1
y = (lifetime - age_fix) * y_1
z = (lifetime - age_fix) * z_1


# #Write your code below this line 👇


#f-string

print(f"You have {x} days, {y} weeks, and {z} months left")



