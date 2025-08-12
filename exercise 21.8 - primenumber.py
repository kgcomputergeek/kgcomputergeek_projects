
"""
Prime numbers are numbers that can only be cleanly divided by themselves and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

"""

print("Welcome to the Prime Numbers Calculator")
def prime_checker(number):
    if number <= 1:
        return False
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True

# Function to check prime numbers
def check_primes():
    all_numbers = []  # List to store all the numbers checked
    
    while True:
        # Get user input for the number to check
        user_input = input("Enter a number to check if it's prime (enter 'exit' to exit): ")
        
        if user_input.lower() == 'exit':
            break
        
        n = int(user_input)
        
        # Call the prime_checker function and print the result
        if prime_checker(n):
            print(f"{n} is a prime number.")
        else:
            print(f"{n} is not a prime number.")
        
        # Add the number to the list of all numbers checked
        all_numbers.append(n)

    return all_numbers

# Function to run the program
def run_program():
    all_results = []
    
    while True:
        # Call the check_primes function and get all the numbers checked
        numbers_checked = check_primes()
        
        # Add the numbers checked to the overall list
        all_results.extend(numbers_checked)

        # Ask the user if they want to run the program again
        again = input("Do you want to run the program again? (yes/no): ").lower()
        if again == 'no':
            break
    
    return all_results

# Run the program
all_numbers_checked = run_program()

# Print all the numbers checked
print("All numbers checked:", all_numbers_checked)
