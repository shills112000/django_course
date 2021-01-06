#!/usr/bin/python3.6


def makes_twenty(n1,n2):
    print (f"n1 {n1} n2 {n2}")
    if n1 == 20 or n2 == 20:
        print (f" == 20 n1 {n1} n2 {n2}")
        return True
    elif sum((n1,n2)) == 20:
        print (n1)
        return True
    else:
        return False
# Check
x=makes_twenty(20,10)
print (x)
# Check
x=makes_twenty(200,20)
print (x)
