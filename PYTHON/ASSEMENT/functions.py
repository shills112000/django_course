#!/usr/bin/python3.6
import collections


# Workout the volme of a sphere
def vol(rad):
    volume=4/3 * 3.14 * rad ** 3
    return volume

x=vol(3)
print (x)



# Check if a number is in a given range

def ran_check(num,low,high):
    if num >= low and num <= high:
        return True
    else:
        return False
   #     print (f"{num} is in the range between {low} and {high}")

# check
x=ran_check(1,2,7)
print (x)


# Accesps string and claulates the number of uppercase and lowercase charectors

def up_low(s):
    lower=0
    upper=0

    for letter in s:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1

    return upper,lower


s="Simon Simon"
upper,lower=up_low(s)
print (f"No of upper case charectors : {upper}")
print (f"No of lower case charectors : {lower}")



