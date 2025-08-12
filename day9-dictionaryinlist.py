"""
Instructions
You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries. Your job is to create a function that can add new countries to this list.

Write a function that will work with the following line of code on line 21 to add the entry for Brazil to the travel_log.

add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])
DO NOT modify the travel_log directly. The goal is to create a function that modifies it.

Example Input
Brazil
5
["Sao Paulo", "Rio de Janeiro"]

Example Output
I've been to Brazil 5 times.
My favourite city was Sao Paulo.
Hint
Look at the function call above to see what the name of the function should be.

The inputs for the function are positional arguments. The order is very important.

Feel free to choose your own parameter names.



"""

"""
User Inputs:

The user is prompted to input the country name, number of visits, and list of cities.
"""
country = input("Enter the country name: ") # Add country name
visits = int(input("Enter the number of visits: ")) # Number of visits
list_of_cities = eval(input("Enter the list of cities (e.g., ['City1', 'City2']): ")) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
"""
Function Definition:

The add_new_country function is defined to take country, visits, and cities as parameters.
Inside the function, a new dictionary new_country is created with the given values.
This dictionary is then appended to the travel_log list.

"""

"""
Function Call:

The add_new_country function is called with the user inputs.

"""
def add_new_country(country, visits, cities):
    new_country = {
        "country": country,
        "visits": visits,
        "cities": cities
    }
    travel_log.append(new_country)

# Call the function with user inputs
add_new_country(country, visits, list_of_cities)


"""
Verification:

The final print statements check if the new country has been added correctly by accessing the newly added dictionary in the travel_log list.

By running this program, you can add a new country to the travel_log based on user inputs, and the program will display information about the newly added country.

"""
# Check the updated travel_log
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
