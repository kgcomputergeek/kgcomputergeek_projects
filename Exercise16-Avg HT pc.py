"""

You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in student_heights

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops


"""
"""
#help from the internet

src: 
https://deepnote.com/app/tiffany-der/100-days-of-python-3a275842-3f68-40d8-8dbf-85c8385ad3b0

"""
# 🚨 Don't change the code below 👇
student_heights = input("Please enter in the student heights separated by commmas: ").split(",")
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# sum the total height
total_ht = 0
for height in student_heights:
  total_ht += height
print(f"Height total: {total_ht}")

# find number of students
num_of_stu = 0
for student in student_heights:
  num_of_stu += 1
print(f"Number of students: {num_of_stu}")

# find average heights:
avg_ht = round((total_ht / num_of_stu))
print(f"Average height: {avg_ht} cm")
