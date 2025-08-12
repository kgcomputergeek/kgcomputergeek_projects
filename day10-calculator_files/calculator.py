
"""




"""





# calculator.py
from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

operations = { #make a list that tells the calculator which math function to use for each symbol
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
####-MAIN JOB OF PROGRAM####



"""
Show the Picture: First, it shows the big text picture.
Ask for First Number: It asks the user for the first number.
Loop for More Calculations: It keeps asking for more calculations until the user wants to stop.
Show Symbols: It shows the user all the symbols they can use (+, -, *, /).
Ask for Operation: It asks which operation the user wants.
Ask for Second Number: It asks for the second number.
Calculate and Show Result: It does the calculation and shows the result.
Ask to Continue: It asks if the user wants to keep going with the current result or start over.

"""
def calculator():
    print(logo)
    should_continue = True
    num1 = float(input("What's the first number?: "))
    
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator() #CALCULATOR STARTS
