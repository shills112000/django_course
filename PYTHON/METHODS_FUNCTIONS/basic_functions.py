#!/usr/local/bin/python3.7

def say_hello(name='default'):    # = this puts a default value
    print (f"hello {name}")

say_hello('Simon')
say_hello()  # prints hello default


def add_num (num1,num2):
    return num1+num2

result = add_num(10,20)
print (result)

def print_result(a,b):
    print (a+b)

def return_result(a,b):
    return a+b

print_result(10,20)

result=return_result(300,300)
print (result)

def sum_nums (num1,num2):
    print (num1+num2)
    return num1+num2

# don't need to set datatypes, can cause issues

sum_nums(10,20)
sum_nums('10','20')


