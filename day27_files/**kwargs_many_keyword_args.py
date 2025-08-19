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
