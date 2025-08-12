"""
You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x
Example Input

78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

Example Output

The highest score in the class is: 91



"""



# Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
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
student_scores = input("Please enter in the student scores separated by commmas: ").split(",")
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# sum the total scores
total_score = 0
for score in student_scores:
  total_score += score
print(f"Total of scores: {total_score}")

#find the highest score in the class


# find number of scores
num_of_stu = 0
for student in student_scores:
  num_of_stu += 1
print(f"Number of students: {num_of_stu}")

# find average scores:
avg_score = round((total_score / num_of_stu))
print(f"Average score: {avg_score} ")

#find the highest score in the class
high_score = max((student_scores))
print(f"Highest score: {high_score} ")