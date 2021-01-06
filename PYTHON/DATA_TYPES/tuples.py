#!/usr/local/bin/python3.7

# TUPLES

#Tuples are a fixed-width, immutable sequence type. We create tuples using parenthesis ((, )) and at least one comma (,):

#tuple is fixed width imutible sequence type

point = (2.0, 3.0)
print (type (point))
print (len (point))

# cannot be modifed once created
# cannot change the length of a tuple

x= point[0]
print (f" x is {x}")
x= point[-1]
print (f" x is {x}")

# The below will not work as you cannot modify a tuple
#point[0] = 1

# can create new tuple from previous

point_3d = point + (4.0,)   # must have the , in the bracket

print (f" point_3d is {point_3d}")

x, y , z = point_3d

print (f"x is {x} y is {y} z is {z}")




# RANGES


#Ranges are an immutable sequence type that defines a start, a stop, and a step value, and then the values within are calculated as it is iteracted with. This allows for ranges to be used in place of sequential lists and while taking less memory and including more items.

x=list(range(1,12,2))  # (start,end,step) convert range into a list

print (f" x is {x}")


t= ('a','a','b')
print (t.count('a')) # count how many a's are in the tuple

print (t.index('a')) # get the index location of the first 'a'
