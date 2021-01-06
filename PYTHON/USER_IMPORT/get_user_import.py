#!/usr/local/bin/python3.7

result = input ('what is your name:')
print (f"hello {result}")

result = input ('type in a number:') # NOTE it always comes back a string, need to change type
result=float(result)# set to floating point
print (type(result))
print (result)
result=int(result)# set to integer
print (type(result))
print (result)


# OR do this
result = int(input ('type in a number:')) # NOTE it always comes back a string, need to change type

print (result)
