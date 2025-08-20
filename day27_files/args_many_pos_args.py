"""

playground for testing out *args


#modify the add function to take an unlimited number of arguments and return the sum of the arguments
#use a loop to sum all the arguments inside the function
#test it out by calling add() to calculate the some of some arguments



"""
def add(*args):
    print(args)       # shows the tuple of arguments
    total = 0
    for n in args:
        total += n
    print(total)

add(1, 2, 3, 4, 5)


"""
my comprehension:



@*args_many_pos_args.py checking comprehension

we dont have to use the variable args but can

*args means unlimited number of arguments in tuple form

print(args) is printing out the args implicitly stated

for n in args: 
is the for loop with n representing all the elements in argument 
sum+=n is to each iteration will add the previous n to the next one (argument) which is a running total,  after getting the answer first


when completed, print out sum which is the the n's added together.
"""