from turtle import Turtle, Screen
timiteo = Turtle()
screen = Screen()

def charges_forward():
    timiteo.forward(10)


screen.listen()
screen.onkey(key="space",fun=charges_forward)
screen.mainloop() #screen.mainloop()is better AS IT keeps the window open and responsive to all events, making it suitable for more interactive programs.

# screen.exitonclick() screen aka gui Keeps the window open and closes it when the user clicks anywhere inside the window. It's simpler and often used in basic turtle graphics scripts where you want to close the window with a mouse click.
