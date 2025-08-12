
# #splits digits into a list
# number = 243689
# list_of_digits = [int(i) for i in str(number)]
# print(list_of_digits)

two_digit_number = input("Type a two digit number: ")

first_digit = two_digit_number[0] #we start at 0 when counting numbers or regarding index position of a string so let 0 represent the first digit

second_digit = two_digit_number [1] #let 1 represent the position of digit 2

result = int(first_digit) + int(second_digit) #result will be the position of the first digit [0] which is based on user input,  plus the position of second digit [1] also based on user input.
#for instance, if the user entered 60 for input as the two digit number then first digit is 6 and second digit is 0. Add first digit, plus second digit, and result = 6.

print(result)