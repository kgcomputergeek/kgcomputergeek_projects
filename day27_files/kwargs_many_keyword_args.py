


def add(*args):
    print(args)       # shows the tuple of arguments
    total = 0
    for n in args:
        total += n
    print(total)

add(1, 2, 3, 4, 5)

def calculate(n, **kwargs): #kwargs is a dictionary of keyword arguments
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Toyota", model="RAV4 Hybrid", color="Blizzard Pearl", seats=5)
print(my_car.make)
print(my_car.model)
print(my_car.color)
print(my_car.seats)
