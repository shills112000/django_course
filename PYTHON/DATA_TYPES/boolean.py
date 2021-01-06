#!/usr/local/bin/python3.7

# https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not

#True
#False

 # NOT

 #not ""   # boolean of empty string is false  , so not of a false will be true.

if not 1 > 2:
     print ("not will give the inverse, hence be true and run this ")


# OR
#a or b

if 1 > 2 or 2 > 1:
    print (" 2 is greater than 2")

    if 1 > 2 or 2 > 1:
        print (" 2 is greater than 1")

 # AND

first = "Simon"
last = "Hills"

if first and last:
        print (f"name has first and last {first} {last}")

print (type(False))
