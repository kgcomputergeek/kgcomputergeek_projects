"""
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 

You are going to create a list called result which contains the numbers that are common in both files. 

e.g. if file1.txt contained: 

1 

2 

3

and file2.txt contained: 

2

3

4

result = [2, 3]



IMPORTANT:  The output should be a list of integers and not strings!

Try to use List Comprehension instead of a Loop. 

"""

with open("day26_files/file1.txt") as file1:
    file1_data = [line.strip() for line in file1.readlines()]

with open("day26_files/file2.txt") as file2:
    file2_data = [line.strip() for line in file2.readlines()]

result = [int(num) for num in file1_data if num in file2_data]
print(result)


"""
@day26_data-overlap.py both the with open statements open file1 and file2 so the interpeter knows to be looking into both of them
.readlines is to read all lines in the file which is all of the numbers. without the data type being exactly classified, even though they look like numbers, we must cast them into integers just to be safe and avoid errors. of course num is our variable we've assigned to represent each element in our list assigned to variable result. if element present in file1 is also an element present in file2, we want that in our list. print statement so we can see who made the cut. I do have a question: how is this statement bidirectional? For instance if we constructed our statement to stay for num in file2_data if num in file1_data, would output be the same? also our fiie1_data and file2_data are our files lines read out

line.strip() is to remove any whitespace from the end of the line.

this is a bidirectional statement, so if we did for num in file2_data if num in file1_data, the output would be the same.
"""