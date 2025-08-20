"""

using tkinter to create a mi to km converter
kwargs and args if needed
"""

from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=500, height=500)

# #label
# my_label = Label(text="Miles to Kilometers Converter", font=("Arial", 14, "bold"))
# my_label.grid(column=0, row=0)

#label for the result
num = Label(text="0")
num.grid(column=1, row=1)

mi_label = Label(text="Miles")
mi_label.grid(column=2, row=0)

#is equal to label
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

km_label = Label(text="Kilometers")
km_label.grid(column=2, row=1)



#user input
miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)



#conversion function
def m_to_k_conversion():
    conversion_factor = int(miles_entry.get()) * 1.6
    num.config(text=conversion_factor)


my_button = Button(text="Calculate", command=m_to_k_conversion)
my_button.grid(column=1,row=2)

window.mainloop()

# #BUTTON FOR CALCULATION
# def button_clicked():
#     my_label.config(text=m_to_k_conversion())

# my_button = tkr.Button(text="Calculate", command=button_clicked)
# my_button.grid(column=1, row=1)

# #BUTTON FOR CLEAR
# def clear_button():
#     input.delete(0, tkr.END)
#     my_label.config(text="MI TO KM CONVERTER")
# clear_button = tkr.Button(text="Clear", command=clear_button)
# clear_button.grid(column=2, row=1)



