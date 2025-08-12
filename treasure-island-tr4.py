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

level_1 = ''
while level_1 != 'left':
 level_1 = input(input("You are in Cuarto Uno. Please make a selection. 'left' or 'right'?:  \n"))
 level_1.lower()
 if level_1 == 'right':
    print("You fell into a hole. Game over =( \n")
 else:
     pass

level_2 = input("You've made it to Cuarto Dos. Please make a selection. 'swim' or 'wait'?: \n ")
level_2.lower()
if level_2 == 'swim' :
    print("You've been attacked by the nasty, trickster trout. GAME OVER =(\n")
if level_2 == 'wait' :
    level_3 = input("It seems you've made it to Cuarto Tres. In this room, there are three doors and two of them are trampas or traps. Choose 'red' , 'blue', or 'yellow' ").lower()
if level_3 == 'red' :
    print("You've ALWAYS liked to play with fire, and now you've been burned.  Game over =(\n")
elif level_3 == 'blue' :
    print("You've just offered yourself as dinner for the beasts. Game over =(\n")
elif level_3 == 'yellow' :
    print("¡Felicidades!, you've found the treasure XD!!!!\n")
else :
    print("GAME OVER.")