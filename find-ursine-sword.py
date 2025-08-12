print("Welcome to the dungeon.")
print("Your mission is to find the ursine sword.")

level_1 = ''
while level_1 != 'left':
 level_1 = input("there is two doors infront of you type 'right' for the right door and 'left' for the left door.\n")
 level_1.lower()
 if level_1 == 'right':
    print("this door is closed your level is too low to open it.\n")
 else:
     pass

level_2 = input("you found a two ladder one leads to upstairs type 'upstairs' and another leads to the basement type 'basement'.\n ")
level_2.lower()
if level_2 == "basement" :
    print("hisssssss ,  you got bitten by snake game over")
if level_2 == "upstairs" :
    level_3 = int(input("it seems like the final room thre is three swords infront of you two of them must be traps chose '1','2' or '3' "))
#level_3.lower()
level_3_as_int = int(level_3)
if level_3_as_int == 1 :
    print("you released a powerful ghost you'r dead")
elif level_3_as_int == 3 :
    print("you opened a portal to a cater you're dead")
elif level_3_as_int == 2 :
    print("congratulations you found the ursine sword")
else :
    print("game over.")