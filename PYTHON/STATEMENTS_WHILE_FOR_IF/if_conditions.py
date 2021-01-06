#!/usr/local/bin/python3.7

# Python comparisons

#https://docs.python.org/3/library/stdtypes.html#comparisons

# IF then else
if 2 < 2:
    print ("1 is less than 2")
elif 1 < 2:
    print ("1 is less than 2")
else:
    print ("I'm here")

name="simonh"
if len(name) > 10:
    print (f" {name} is longer than 10 charectors")
elif len(name) < 2:
    print (f" {name} is less than 2 charectors")
elif len(name) ==5:
    print (f" {name} is 5 charectors")
else:
    print (f" {name} is too short")


hungry = False
if hungry:
    print ("Feed me")
else:
    print ("don't feed me")


# IN keyword

#2 in [1,2,3]
x=[1,2,3]
if 2 in [1,2,3]:
    print ("2 is in the list")

x=[1,2,3]
if 6 in x:
    print ("6 is in the list")
else:
    print (f"6 is not in the list {x} ")

if 4 not in [1,2,3]:
    print ("4 is not in list")

if True:
    print ("True statement")



