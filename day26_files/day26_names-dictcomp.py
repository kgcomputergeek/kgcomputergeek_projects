"""
Objectives: using dictionary comprehension to create a dictionary of random scores for each name

"""


import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

student_scores = {name: random.randint(1, 100) for name in names}
print(student_scores)





