#!/usr/bin/python3.6

def myfuc(a,b):
    # RETURNS 5 % of the sum of a and b
    return sum((a,b)) * 0.05

print(myfuc(40,60))


def myfunc(*args):   # turple of parameters for args
    for item in args:
        print (item)
    return sum(args) * 0.05

print(myfunc(40,60))  # YOU CAN ADD AS MANY ARGS as you want now in a tuple
print(myfunc(40,60,100,100,100,100,100,100))  # YOU CAN ADD AS MANY ARGS as you want now in a tuple


def test_args(*args):
    print (args)

test_args('test',30,400,979)

def newfunc(**kwargs):   # KARGS , key,word arguements from a dictionary
    print (kwargs)
    if 'fruit' in kwargs:
        print (f"My fruit of choice is {kwargs['fruit']}")
    else:
        print ('I did not find fruit')

newfunc(fruit='apple',Veggie='tomato')

def both_args_kwargs(*args,**kwargs):
    print (f"I would like {args[0]} {kwargs['food']}")

print(both_args_kwargs(10,20,30,fruit='orange',food='eggs',animal='dog'))


# return sum of a list
def myfunc(*args):
    print (args)
    return sum(args)


x=myfunc(1,2,3,4,5)
print (x)

# Check a tuple to return only even numbers in a list
def new_evens(*args):
    list_evens=[]
    for arg in args:
        if arg % 2 == 0:
            print (arg)
            list_evens.append(arg)
    return list_evens


x=new_evens(1,2,3,4,5,6,7)
print (x)

