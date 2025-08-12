#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇



"""
bill_total is user input for their bill's total

tip_percent is going to be options selected by the user. Let the options be 10, 15, 18, 20 or 25 percent.

Percentages will be float. python should recognize this automatically however, you may need to specify this at a later point to avoid unsupported operand types

people_split is user input for how many people are splitting the bill

"""
import math
# 🚨 Don't change the code below 👇
bill_total = float(input("Please enter your bill total: "))
people_split = float(input("How many people are splitting the bill?: "))
tip = float(input("Please select your tip percentage. 10, 12, 15, 18, 20 or 25:  "))
# weight = float(input("enter your weight in kg: "))
if tip == "10":
    tip = 0.10
elif tip == "12":
    tip = 0.12
elif tip == "15":
    tip = 0.15
elif tip == "18":
    tip = 0.18
elif tip == "20":
    tip = 0.20
elif tip == "25":
    tip = 0.25
# else :
#     print("Invalid selection")


bill_total_AS_INT = int(bill_total)
people_split_AS_INT = int(people_split)
tip_AS_INT = int(tip)

each_person_pays = ((bill_total_AS_INT / people_split_AS_INT))
each_person_tips = ((bill_total_AS_INT / people_split_AS_INT) * tip_AS_INT) / 100
# each_person_tip = each_person_pays * 0.10 || each_person_pays * 0.10 ||
# print(f"The bill total for the whole party is ${math.ceil(bill_total_AS_INT)}, and is split {people_split_AS_INT} ways, each person pays ${math.ceil(each_person_pays)}, and they each tip ${math.ceil(each_person_tips)}, with a {tip_AS_INT} % tip included in the bill split. The total with tip is $ {math.ceil(each_person_pays + each_person_tips)}")
#

# #uses math.ceil for rounding
# print(f"The bill total for the whole party is ${math.ceil(bill_total_AS_INT)}, and is split {people_split_AS_INT} ways. The total per person with a {tip_AS_INT} % tip included was ${math.ceil(each_person_pays + each_person_tips)}. Price breakdown was ${math.ceil(each_person_pays)}, and they each tip ${math.ceil(each_person_tips)}.")


#uses round({variable},2) for rounding 2 decimal places
# print(f"The bill total for the whole party is ${bill_total_AS_INT}, and is split {people_split_AS_INT} ways. The total per person with a {tip_AS_INT} % tip included was ${round(each_person_pays + each_person_tips,2)}. Price breakdown was ${round(each_person_pays,2)}, and they each tip ${round(each_person_tips,2)}.")

#uses  "{:.2f}".format

print(f"The bill total for the whole party is ${bill_total_AS_INT}, and is split {people_split_AS_INT} ways. The total per person with a {tip_AS_INT} % tip included was ${round(each_person_pays + each_person_tips,2)}. Price breakdown is each guest pays ${round(each_person_pays,2)}, and they each tip ${round(each_person_tips,2)}.")