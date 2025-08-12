"""
src: https://www.linkedin.com/pulse/how-calculate-bmi-using-python-sameer-ahmed-shah/


"""

weight = float(input("Enter your Weight in KG: "))
height = float (input("Enter your height in Meter: "))
BMI = weight / (height)**2
print ("your BMI is", BMI)

if BMI <= 18.5:
    print ("Underweight.")
elif BMI <= 24.9:
    print ("Healthy.")
elif BMI <= 29.9:
    print ("Overweight.")
else:
    print ("Obese.")