

#Write your code below this line 👇
import math
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆


BMI = math.floor(weight/math.pow(height,2))
print(BMI)
#print(str("Your BMI is: " + (BMI_str)))