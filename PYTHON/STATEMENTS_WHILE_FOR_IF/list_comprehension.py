#!/usr/local/bin/python3.7

mystring = 'hello'

mylist =[]
for letter in mystring:
    mylist.append(letter)

print (mylist)

# MORE effiecnet to do the above

mylist = [letter for letter in mystring]
print (mylist)


mylist = [num for num in range(0,100)]
print (mylist)

mylist= [num**2 for num in range(0,11)]
print (mylist)

mylist = [num+5 for num in range(0,100)] # make a list of 0 to 100 and add 5
print (mylist)

mylist = [num for num in range(0,11) if num%2==0] # just get even numbers
print (mylist)


celcius = [0,10,20,34.5]

farenheight = [( (9/5)* temp +32) for temp in celcius]
print (farenheight)

