from menu import Menu #, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# from menu import Menu
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine

def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    is_on = True

    # Display the menu prices at the beginning
    print("Welcome to the Coffee Machine!")
    print("Here are the available drinks and their prices:")
    for item in menu.menu:
        print(f"{item.name.capitalize()}: ${item.cost}")

    while is_on:
        choice = input(f"What would you like? ({menu.get_items()}): ").lower()
        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if drink and coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        
        # Ask if the user wants another drink
        another_drink = input("Would you like another drink? (yes/no): ").lower()
        if another_drink != "yes":
            is_on = False
            print("Thank you! Have a nice day!")

if __name__ == "__main__":
    main()

# def main():
#     menu = Menu()
#     coffee_maker = CoffeeMaker()
#     money_machine = MoneyMachine()

#     is_on = True

#     # Display the menu prices at the beginning
#     print("Welcome to the Coffee Machine!")
#     print("Here are the available drinks and their prices:")
#     for item in menu.menu:
#         print(f"{item.name.capitalize()}: ${item.cost}")

#     while is_on:
#         choice = input(f"What would you like? ({menu.get_items()}): ").lower()
#         if choice == "off":
#             is_on = False
#         elif choice == "report":
#             coffee_maker.report()
#             money_machine.report()
#         else:
#             drink = menu.find_drink(choice)
#             if drink and coffee_maker.is_resource_sufficient(drink):
#                 if money_machine.make_payment(drink.cost):
#                     coffee_maker.make_coffee(drink)

# if __name__ == "__main__":
#     main()


# class CoffeeMachine:
#     def __init__(self):
#         self.MENU = {
#             "espresso": {
#                 "ingredients": {
#                     "water": 50,
#                     "coffee": 18,
#                 },
#                 "cost": 1.5,
#             },
#             "latte": {
#                 "ingredients": {
#                     "water": 200,
#                     "milk": 150,
#                     "coffee": 24,
#                 },
#                 "cost": 2.5,
#             },
#             "cappuccino": {
#                 "ingredients": {
#                     "water": 250,
#                     "milk": 100,
#                     "coffee": 24,
#                 },
#                 "cost": 3.0,
#             }
#         }

#         self.resources = {
#             "water": 300,
#             "milk": 200,
#             "coffee": 100,
#             "money": 0
#         }
#         self.total_change_given = 0

#     def print_menu(self):
#         """Prints the menu with prices."""
#         print("Welcome to the Coffee Machine!")
#         print("Here are the available drinks and their prices:")
#         for drink, details in self.MENU.items():
#             print(f"{drink.capitalize()}: ${details['cost']}")

#     def print_report(self):
#         """Prints a report of all resources."""
#         print(f"Water: {self.resources['water']}ml")
#         print(f"Milk: {self.resources['milk']}ml")
#         print(f"Coffee: {self.resources['coffee']}g")
#         print(f"Money: ${self.resources['money']}")
#         print(f"Total change given: ${self.total_change_given}")

#     def is_resource_sufficient(self, drink):
#         """Checks if resources are sufficient for making the drink."""
#         for item in self.MENU[drink]["ingredients"]:
#             if self.MENU[drink]["ingredients"][item] > self.resources[item]:
#                 print(f"Sorry, there is not enough {item}.")
#                 return False
#         return True

#     def process_coins(self):
#         """Processes coins inserted by the user."""
#         print("Please insert coins.")
#         total = int(input("How many quarters?: ")) * 0.25
#         total += int(input("How many dimes?: ")) * 0.10
#         total += int(input("How many nickels?: ")) * 0.05
#         total += int(input("How many pennies?: ")) * 0.01
#         return total

#     def is_transaction_successful(self, money_received, drink_cost):
#         """Checks if the transaction is successful."""
#         if money_received >= drink_cost:
#             change = round(money_received - drink_cost, 2)
#             self.resources["money"] += drink_cost
#             self.total_change_given += change
#             print(f"You've given ${money_received}. The drink costs ${drink_cost}. Here is ${change} in change.")
#             return True
#         else:
#             print("Sorry, that's not enough money. Money refunded.")
#             return False

#     def make_coffee(self, drink):
#         """Makes the coffee and deducts resources."""
#         for item in self.MENU[drink]["ingredients"]:
#             self.resources[item] -= self.MENU[drink]["ingredients"][item]
#         print(f"Here is your {drink}. Enjoy! ☕")

#     def start(self):
#         """Starts the coffee machine program."""
#         is_on = True

#         # Print menu with prices at the start
#         self.print_menu()

#         while is_on:
#             choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
#             if choice == "off":
#                 is_on = False
#             elif choice == "report":
#                 self.print_report()
#             elif choice in self.MENU:
#                 if self.is_resource_sufficient(choice):
#                     payment = self.process_coins()
#                     if self.is_transaction_successful(payment, self.MENU[choice]["cost"]):
#                         self.make_coffee(choice)
#             else:
#                 print("Invalid choice. Please choose espresso, latte, or cappuccino.")

# # Create an instance of CoffeeMachine and start the machine
# coffee_machine = CoffeeMachine()
# coffee_machine.start()
