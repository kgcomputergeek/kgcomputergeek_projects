"""
show "BUTTON GOT CLICKED" on my_label when the button getsclicked
"""

import tkinter as tkr

window = tkr.Tk()
window.title("LET'S GO BABY!")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200) #adds padding to the window

#label
my_label = tkr.Label(text="I AM A LABEL", font=("Arial", 24, "bold"))
#my_label.pack()
my_label.config(padx=50, pady=50) #adds padding to the label


#my_label.place(x=100, y=200) #downside is you must be specific about the x and y coordinates
my_label.grid(column=0, row=0) #grid is a better way to place the label

#entry
input = tkr.Entry(width=10)
input.grid(column=2, row=2) #cannot have pack() anywhere in the code if using grid()


#button
def button_clicked():
    my_label.config(text=input.get()) #get the text from the entry and configures the label based on the text

my_button = tkr.Button(text="Click Me", command=button_clicked)
my_button.grid(column=1, row=1)


#new button
new_button = tkr.Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0) #remember to use grid() for new buttons and that rows and columns start at 0


window.mainloop()