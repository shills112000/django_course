#!/usr/bin/python3.6


# A lambda function is a small anonymous function.
#'A lambda function can take any number of arguments, but can only have one expression.

def square(num):
    result =  num**2
    return result

result=square(9)
print (result)


# convert the above into lambda
square1 = lambda num: num ** 2

result=square1(9)
print (result)


#Example
#Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))


#Why Use Lambda Functions?
#The power of lambda is better shown when you use them as an anonymous function inside another function.

#Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:


def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
print (mydoubler)
print(mydoubler(11))
exit()


mynums=[1,2,3,4,5,6]

new_list=list(map(lambda num:num ** 2, mynums))
print (new_list)


new_list=list(filter(lambda num:num%2 ==0,mynums))
print (new_list)
