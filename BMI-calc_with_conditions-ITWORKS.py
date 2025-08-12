


#need an result output = ("Your BMI is" + "%)
#might need rounding for percentage to the nearest 10th math.ceil
"""
#potential upgrades
#dude you should totally upgrade your program to convert weight in kg to lbs and same thing with height (ft/in)
#conditions where bmi falls into a certain percentage, it corresponds with a label

BMI <18.5 underweight
BMI >=18.5 AND <=25 normal
BMI >25 AND <30 overweight
BMI >30 + but below 35 they are obese
Above 35 they are clinically obese.
"""
#
# import math
# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆
#
# height_as_str = str(height)
# weight_as_str = str(weight)
# BMI = math.floor(weight_as_str/math.pow(height_as_str,2))
# BMI_str = str(BMI)
# #print(str("Your BMI is: " + (BMI_str) +"%"))
#
# if BMI_str < 18.5: #underweight
#     print("You're underweight")
#
# elif BMI_str >= 18.5 & BMI_str < 25:
#     print("You're normal")
#
# elif BMI_str > 25 & BMI_str < 30:
#        print("You're overweight")
#
# elif BMI_str >30 & BMI_str <35:
#     print("You're obese")
#
# elif BMI_str >35:
#     print("You're morbidly obese")
#
# else:
#     print("invalid entry")

import math
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#height_as_str = str(height)
#weight_as_str = str(weight)
BMI = math.floor(weight/height**2)
#BMI_str = str(BMI)
#print(str("Your BMI is: " + (BMI_str) +"%"))

if BMI < 18.5: #underweight
    print(f"Your BMI is {BMI}, and you're underweight")

elif BMI >= 18.5 and BMI < 25:
    print(f"Your BMI is {BMI} and you're normal")

elif BMI > 25 and BMI < 30:
    print(f"Your BMI is {BMI} and you're overweight")

elif BMI >30 and BMI <35:
    print(f"Your BMI is {BMI} and you're obese")

elif BMI >35:
    print(f"Your BMI is {BMI} and you're morbidly obese")

else:
    print("invalid entry")



# print(str("Your BMI is: " + (BMI_str) + "%"))
#
# weight = float(input("Enter your Weight in KG: "))
# Height = float (input("Enter your height in Meter: "))
# BMI = weight / (height)**2
# print ("your BMI is", BMI)
# if BMI <= 18.5:
# print ("Underweight.")
# elif BMI <= 24.9:
# print ("Healthy.")
# elif BMI <= 29.9:
# print ("Overweight.")
# else:
# print ("Obese.")



# BMI <18.5 underweight
# BMI >=18.5 AND <=25 normal
# BMI >25 AND <30 overweight
# BMI >30 +
#print(f"Your BMI is",BMI)