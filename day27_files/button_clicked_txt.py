"""
show "BUTTON GOT CLICKED" on my_label when the button getsclicked
"""

import tkinter as tkr

window = tkr.Tk()
window.title("LET'S GO BABY!")
window.minsize(width=500, height=300)



my_label = tkr.Label(text="I AM A LABEL", font=("Arial", 24, "bold"))
my_label.pack()

#entry
input = tkr.Entry(width=10)
input.pack()



def button_clicked():
    my_label.config(text=input.get()) #get the text from the entry and configures the label based on the text

my_button = tkr.Button(text="Click Me", command=button_clicked)
my_button.pack()

window.mainloop()