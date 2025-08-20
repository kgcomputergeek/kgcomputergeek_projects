"""
BMI calculator

- Formula: BMI = weight_kg / (height_m**2)
- Categories: <18.5 underweight, 18.5–24.9 normal, 25–29.9 overweight, >=30 obese
"""

import math

# Inputs
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# Compute BMI
bmi = weight / height**2



if bmi < 18.5:
	print("You are underweight.")
elif bmi < 25:
	print("You have a normal weight.")
elif bmi < 30:
	print("You are overweight.")
else:
	print("You are obese.")

# Display rounded BMI (nearest whole number) and category
print(f"Your BMI is {round(bmi)}")