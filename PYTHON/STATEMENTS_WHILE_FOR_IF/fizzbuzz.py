#!/usr/local/bin/python3.7

x = 1
while x < 101:
    if ( x % 3 == 0 and x % 5 == 0):
        print (f"count is {x} fizzbuzz")
    elif ( x %3 == 0):
        print (f"count is {x} fizz")
    elif ( x %5 == 0):
        print (f"count is {x} buzz")
    x+=1
