#!/usr/bin/python3.6


# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

def square(num):
    return num**2

my_nums=[1,2,3,4]

# Tis iterates through the function using the list
for item in map(square,my_nums):
    print (item)

new_list=list(map(square,my_nums)) # creates a list of function
print (new_list)


def splicer(mystring):
    if len(mystring) %2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']

new_list=list(map(splicer,names))
print (new_list)
