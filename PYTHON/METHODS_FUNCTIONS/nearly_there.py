#!/usr/bin/python3.6


def almost_there(n):
    if n > 90 and n < 110:
        return True
    elif n > 190 and n < 210:
        return True
    else:
        return False
# Check
x=almost_there(104)
print (x)
# Check
x=almost_there(150)
print (x)
# Check
x=almost_there(209)
print (x)
