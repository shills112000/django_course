#!/usr/bin/python3.6

#The filter() method constructs an iterator from elements of an iterable for which a function returns true.

# In simple words, filter() method filters the given iterable with the help of a function that tests each element in the iterable to be true or not.

def check_even (num):
    return num%2 == 0

mynums=[1,2,3,4,5,6]

new_list=list(filter(check_even,mynums))
print (new_list)

for n in filter(check_even,mynums):
    print (n)
