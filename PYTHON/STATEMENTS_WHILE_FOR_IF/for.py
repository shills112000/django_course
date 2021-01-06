#!/usr/local/bin/python3.7

#https://docs.python.org/3/tutorial/controlflo.html#for-statements

colours = ['red', 'blue', 'green']
for colour in colours:
    print (f"{colour}")

# working with dictionarys
ages ={'david': 29, 'alex': 50, 'simon': 60}
print (f"{ages}")
for key in ages:
    print (f"This is the key: {key}")
    print (f"{key} is {ages[key]}")
    x=ages[key]
    print (f"This is the value :{x}")
    if  x >= 50:
        print (f" {key} is over 50 years old")


for colour in colours:
    if colour == 'red':
        print ("Got Red from colours")


for letter in "my_string":
    print (f"{letter}")


list_of_points = [ (1,2) , (2,3) , (3,4)]
for x , y in list_of_points:
    print (f" x: {x} y: {y}")


ages ={'david': 29, 'alex': 50, 'simon': 60}

for name,age in ages.items():
    print (f"Person named : {name}")
    print (f"Age of {age}")

x=ages.items()  # puts into a tuple list
print (f" {x}")


# list

print ("working with lists")

mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
  #  print (num)
  #  print ("jelly")
#  if num % 2 == 0:
  if num % 2 :  # check for even or odd number
      print (f" number {num} is odd")
  else:
      print (f" number {num} is even")

list_sum = 0
for num in mylist:
    list_sum = list_sum + num

print (list_sum)


# list with string

mystring ="Hello World"
for letter in mystring:
    print (letter)

for _ in mystring:  # The _ is not used but you still travel through the whole string
    print ("Cool!")


# list tuple

tup = (1,2,3)
for item in tup:
    print (item)

mylist = [(1,2), (3,4), (5,6), (7,8)]

for item in mylist: # show the tuples in list
    print (item)

#for (a,b) in mylist: # tupler unpacking
for a,b in mylist: # same as the above without brackets
    print (a)
    print (b)

# dictionaty

d = {'k1':1, 'k2':2, 'k3': 3}

for item in d:
    print (item)  # just show keys

for item in d.items():
    print (item) # show the key and valuekey and value
    print (item[0]) # show just the key as it's in a tuple
    print (item[1]) # show just the value as it's in a tuple

for key,value in d.items():
    print (f" key is {key}")
    print (f" value is {value}")

for value in d.values(): # just go through the values
    print (f" value is {value}")
