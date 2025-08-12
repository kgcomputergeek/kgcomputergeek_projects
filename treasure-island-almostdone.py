print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************


''')

print("¡Bienvenidos a La Isla de Tesoro!")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
"""
For help with the input function with multiple if statements, use the link below:

https://stackoverflow.com/questions/69443415/how-to-use-input-function-in-multiple-if-statement

https://stackoverflow.com/questions/75077963/can-i-incorporate-if-else-statements-with-input
"""
selection_1 = input("You\'re in El Primero Nivel. Please make a selection. left or right?:  \n").lower()
if selection_1 == "left":
    selection_2 = input("You\'ve made it to El Segundo Nivel. Please make a selection. swim or wait?: \n ").lower()
    if selection_2 == "wait": #wait
        selection_3 = input("It seems you\'ve made it to El Tercero Nivel. In this room, there are three doors and two of them are trampas or traps. Choose red blue, or yellow \n").lower()
        if selection_3 == "red":
            print("You\'ve ALWAYS liked to play with fire, and now you've been burned. Game over =(")
        elif selection_3 == "yellow":
            print("¡Felicidades!, you\'ve found the treasure XD!!!!")

        elif selection_3 == "blue":
            print ("You\'ve just offered yourself as dinner for the beasts. Game over =( ")
        else:
            print("The door you\'ve selected no hay existe. GAME OVER")
    else:
        print("You\'ve been attacked by the nasty, trickster trout. GAME OVER =(")
else:
    print("You fell into a hole. Game over =(")






