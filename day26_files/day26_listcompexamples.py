# name = "Angela"
# new_list = list(name)
# print(new_list)




# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)



"""

checking my comprehension, so please correct where i am wrong. ah yes square brackets is indicative of it being a list and so i in the expression represents each element (aka item) in the list (not index), and it multiples that item by 2, which is doubling it. range works like in math [1,5) square meaning include and parethesis meaning exclude, thus we include 1 in our starting point and exclude 5 in our ending point thus it's really 1 to 4. include our print statement and we're done

The range function is a built-in function in Python that generates a sequence of numbers. It is commonly used in loops to iterate over a specific range of numbers. Thus, your conclusion is correct.


"""
# doubled_numbers = [i * 2 for i in range(1, 5)]
# print(doubled_numbers)  # [2, 4, 6, 8]


#use list comprehension to capitalize all names in the list where there is more than 5 characters
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
capitalized_names = [name.upper() for name in names if len(name) > 5]
print(capitalized_names)

