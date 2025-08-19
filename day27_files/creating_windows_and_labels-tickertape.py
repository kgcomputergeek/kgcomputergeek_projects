import tkinter as tkr

window = tkr.Tk()
window.title("Baby's First GUI Program") #window title gui pronunced as [goo-ee]
window.minsize(width=500, height=300) #window size 500 pixels wide and 300 pixels tall

# Label




my_label = tkr.Label(text="***THIS IS A TEST***", font=("Courier New", 24, "bold"))
def scroll_text():
    current_text = my_label.cget("text")
    # Move first character to the end to create ticker effect
    new_text = current_text[1:] + current_text[0]
    my_label.config(text=new_text)
    window.after(150, scroll_text)  # Adjust speed as needed (milliseconds)

my_label.pack(fill="x")  # Make label stretch across the window
scroll_text()




window.mainloop()