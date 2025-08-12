"""
In this list comprehension exercise you will practice using list comprehension to filter out the even numbers from a series of numbers.   



First, use list comprehension to convert the list_of_strings to a list of integers called numbers.   

Then use list comprehension again to create a new list called result.

This new list should only contain the even numbers from the list numbers. 

Again, try to use Python's List Comprehension instead of a Loop. 

"""

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)


"""
my comprehensionint(num) is casting each element which is represented by the variable num, as an integer, and doing this for each element via looping through the list_of_strings. for result =, we needed to do finding even numbers not on the original list (if we did this we'd most likely get an data type error) hence why we needed to cast each element as an integer (converted from string to integer), and to be an even number would need to be divisible by 2 without any remainders hence the statement if number % (modulus which is divison with remainders) by 2  equals 0 which means no remainder
"""