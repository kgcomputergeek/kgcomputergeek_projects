# Write a program that adds the digits in
# a 2 digit number. e.g. if the input was 35,
# then the output should be 3 + 5 = 8


# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
#you'll need to divide the entered number by decimal place
#for example, 39. split into 3 and 9 then add and get a total
# 1)take an input
# 2). split input into digit_1 and digit_2
# 3). the_answer is digit_1 + digit_2

digit_1 = two_digit_number[0] #we start at 0 when counting numbers or regarding index position of a string so let 0 represent the first digit

digit_2 = two_digit_number [1] #let 1 represent the position of digit 2

the_answer = int(digit_1) + int(digit_2) #the_answer will be the position of the first digit [0] which is based on user input,  plus the position of second digit [1] also based on user input.
#for instance, if the user entered 60 for input as the two digit number then first digit is 6 and second digit is 0. Add first digit, plus second digit, and the_answer = 6.

print(the_answer)
# the_answer = (int(two_digit_number) + int(two_digit_number))



