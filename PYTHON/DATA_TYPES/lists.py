#!/usr/bin/python3.6

# List is a ordered squence of items

my_list = [1, 2, 3, 4, 5]

print (my_list[0]) # print first entry in list

x =len(my_list)  # get the length of the list
print (f"The number of elements in the list is {x}")

my_list.append(6)
print (my_list)


# Slicing

#my_list[start:end:step]
x= my_list[0:4] # give 1,2,3,4
print (f"sliced elements is {x}")

# reverse a list using slicing
x = my_list[::-1]
print (f"sliced elements is {x}")

# Change list

my_list[0] = "a"

print (f"{my_list}")


# Remove from list

my_list [0:2] = []  # remove first 2 elements in list
print (f"{my_list}")

# methods
# pop : The pop() method removes the element at the specified position.
# remove  : The remove() method removes the first occurrence of the element with the specified value.
# append

my_list = ["a", "a", "c", 4, 5]
print (f"{my_list}")
my_list.remove("a")
print (f"{my_list}")

my_list.pop(1) # remove elememt position 1 in list
print (f"{my_list}")

# POP

my_list = ["a", "a", "c", 4, 5]
print (f"{my_list}")

my_list.pop(0) #remove at element 0
print (f"{my_list}")

