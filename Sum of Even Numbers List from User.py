# This function gets a list of numbers from the user.
def get_numbers_from_user():
  numbers = []
  while True:
    number = input("Enter a number (or 'q' to quit): ")
    if number == 'q':
      break
    numbers.append(int(number))
  return numbers

# This function sums the even numbers in a list.
def sum_even_numbers(numbers):
  sum = 0
  for number in numbers:
    if number % 2 == 0:
      sum += number
  return sum

# Get a list of numbers from the user.
numbers = get_numbers_from_user()

# Print the sum of the even numbers in the list.
print("The sum of the even numbers is", sum_even_numbers(numbers))