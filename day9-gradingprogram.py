"""
Instructions

You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.

The final version of the student_grades dictionary will be checked.

DO NOT modify lines 1-7 to change the existing student_scores dictionary.

DO NOT write any print statements.

This is the scoring criteria:

Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"

Expected Output
'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
Hint
Remember that looping through a Dictionary will only give you the keys and not the values.

If in doubt as to why your code is not doing what you expected, you can always print out the intermediate values.

At the end of your program, the print statement will show the final student_scores dictionary, do not change this.

"""
"""
explaination - breakdown into three components
1. dictionary initialization
2. Looping through student_scores
3. grading criteria


Dictionary Initialization:

student_scores dictionary contains student names as keys and their scores as values.
student_grades dictionary is initialized as an empty dictionary to store the final grades.
Loop through student_scores:

For each student and their corresponding score in student_scores, the program checks the score range using if-elif-else statements and assigns the appropriate grade to student_grades.
Grading Criteria:

-If the score is between 91 and 100 (inclusive), the grade is "Outstanding".
-If the score is between 81 and 90 (inclusive), the grade is "Exceeds Expectations".
-If the score is between 71 and 80 (inclusive), the grade is "Acceptable".
-If the score is 70 or lower, the grade is "Fail".
The result is a student_grades dictionary that contains student names as keys and their corresponding grades as values, based on the provided scoring criteria.

"""

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# # 🚨 Don't change the code above 👆
# # TODO-1: Create an empty dictionary called student_grades.


# # TODO-2: Write your code below to add the grades to student_grades.👇


# # 🚨 Don't change the code below 👇
# print(student_grades)


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student, score in student_scores.items():
    if 91 <= score <= 100:
        student_grades[student] = "Outstanding"
    elif 81 <= score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif 71 <= score <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# No print statements as per instructions

#print statement to test output
print(student_grades)