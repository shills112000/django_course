#!/usr/bin/python3.6

def two_given_number(a,b):
    if  a % 2 == 0 and b % 2 == 0:
        print ("both are even return lower number")
        if a < b :
            return a
        else:
            return b
    else:
        print ("one numbers is odd return larger")
        if a > b :
            return a
        else:
            return b


x=two_given_number(2,301)
print (x)
