#!/usr/local/bin/python3.7

## def name_of_function():

# def - definition

# Snake or Casing all lowercase with underscores
#object orinated use camel casing

# () are where we pass paremters
# : here comes the indented block
# then ""     # optional
#      Docstring explains function
#      ""

def name_of_function(name):
    """
    Docstring just print hello
    """
    print (f"hello {name}")

name_of_function("Simon")


# return sends back result of function

def add_function(num1,num2):
    return num1+num2

result=add_function(1,2)
print (result)


