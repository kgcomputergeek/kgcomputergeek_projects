print("Thank you for choosing Python Pizza Deliveries!")
size = input("Please select S, M or L for the pizza size: ") # What size pizza do you want? S, M, or L
add_pepperoni = input("Would you like to add pepperoni?: ") # Do you want pepperoni? Y or N
extra_cheese = input("Would you like to add extra cheese?: ")

bill = 0

if size == "S":
    #print("You have selected a small pizza. It costs $15!")
    bill = 15
    if add_pepperoni == "Y":
       # print(f"The pizza now costs {bill}")
        bill +=2
    if extra_cheese == "Y":
        bill +=1
elif size == "M":
   # print("You have selected a medium pizza. It costs $20!")
    bill = 20
    if add_pepperoni == "Y":
        bill +=3
    if extra_cheese == "Y":
        bill +=1
elif size == "L":
  #  print("You have selected a medium pizza. It costs $25!")
    bill = 25
    if add_pepperoni == "Y":
        bill +=3
    if extra_cheese == "Y":
        bill +=1

print(f"Your final bill is ${bill}")


#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#
#     print(f"Your final bill is ${bill}")
#
# else:
#     print("Sorry, you have to grow taller before you can ride.")
