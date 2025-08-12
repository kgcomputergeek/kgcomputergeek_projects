#import math

# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

#Write your code below this line 👇

#bmi formula = kg/m^2



#need an result output = ("Your BMI is" + "%)
#might need rounding for percentage to the nearest 10th math.ceil
"""
#potential upgrades
#dude you should totally upgrade your program to convert weight in kg to lbs and same thing with height (ft/in)
#conditions where bmi falls into a certain percentage, it corresponds with a label

BMI <18.5 underweight
BMI >=18.5 AND <=25 normal
BMI >25 AND <30 overweight
BMI >30 +
"""
"""

****LET THE CODE BELOW THIS COMMENT REPRESENT THE REQUESTED PROGRAM WHICH IS

1) CALCULATE BMI BASED ON HEIGHT INPUT (IN M) AND WEIGHT INPUT (IN KG)

"""
#height in m
#weight in kg
#bmi = kg/m2

import math
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#height converter from metric to imperial

#1 kg = 2.205 lbs
def weight_conversion (height, lbs):
    height * 2.205
def height_conversion (heights, ft,):




    BMI = weight/math.pow(height,2)
print(math.floor(BMI))