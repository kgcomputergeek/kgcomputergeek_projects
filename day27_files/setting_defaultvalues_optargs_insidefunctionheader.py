




"""

using advanced python function arguments in order to specify a wider range of inputs.


according to the zen of python, "explicit is better than implicit".
https://peps.python.org/pep-0020/ 

explicit vs implicit



    def calculate_area(length, width): #explicit
        return length * width
    def calculate_area(length, width=10): #implicit
        return length * width


    global_config = {"precision": 2} #precision is a global variable that is used to set the precision of the data and implicitly uses it in the function

    def process_data(data):
        # Implicitly uses global_config
        return round(data, global_config["precision"])

"""
#setting default values and optional arguments inside function header





import tkinter as tkr

window = tkr.Tk()
window.title("Baby's First GUI Program") #window title gui pronunced as [goo-ee]
window.minsize(width=500, height=300) #window size 500 pixels wide and 300 pixels tall

# Label
my_label = tkr.Label(text="I am a label! Look at me!", font=("Courier New", 24, "bold"))
my_label.pack(side="left") #pack() is a method that adds the label to the window. it's a packer that shows where the label appears on the window.

import turtle as tort

timmy = tort.Turtle()
timmy.write("Some text", font=("Arial", 80, "bold"))


window.mainloop() #keeps the window open and without it, the window will close immediately

# def my_function(a=1, b=2, c=3): #uses explicit parameters (a, b, c) because they are named in the function header. just becausecthey have default values, doesn't mean they are implicit parameters
#     print(a, b, c)
# my_function()
# my_function(10)
# my_function(10, 20)
# my_function(10, 20, 30)


#optional arguments