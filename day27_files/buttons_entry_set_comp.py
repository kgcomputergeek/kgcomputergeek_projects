"""

buttons, entry, and setting component options

"""

import tkinter as tkr

window = tkr.Tk()
window.title("LET'S GO BABY!")
window.minsize(width=500, height=300)




#LABEL 

my_label = tkr.Label(text="I AM A LABEL", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"

#my_label.config(text="New Text") #same as my_label["text"] = "New Text"







#button
def button_clicked():
    print("You clicked me!")

my_button = tkr.Button(text="Click Me", command=button_clicked)
my_button.pack()










window.mainloop()