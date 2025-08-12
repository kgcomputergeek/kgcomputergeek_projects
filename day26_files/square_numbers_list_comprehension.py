squared_numbers = []

print("Enter numbers one by one. Type 'done' when finished.")
user_inputs = []
while True:
    user_input = input("Enter a number (or 'done'): ")
    if user_input.lower() == 'done':
        break
    try:
        num = float(user_input)
        user_inputs.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid number or 'done'.")

squared_numbers = [x ** 2 for x in user_inputs]

print("Squared numbers:", squared_numbers) 