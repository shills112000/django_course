#!/usr/local/bin/python3.7


# Sets are unordered collections of unique elements

# meansing there can only be one representative of the same oject


myset = set()

print (type(myset))

myset.add(1)

print(myset)

myset.add(2)
print(myset)

myset.add(2) # as 2 has been added already it will not add it again
print(myset)

# cast a list to a set to get rid of duplicates

#mylist = [1,2,3,4,5,5,3,2,6,7,8]
mylist = [1,1,1,1,2,2,2,2,3,3,3,3]
new_set=set(mylist)
print (type(new_set))
print(new_set)

# convert a set to a list

new_list =list(new_set)
print (type(new_list))
print (new_list)





