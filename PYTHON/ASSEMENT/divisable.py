#!/usr/local/bin/python3.7

for num in range(1,50):
    if (num % 3 == 0):
        print (f"{num}")

mylist = [num for num in range(0,50) if num%3==0]
print (mylist)

