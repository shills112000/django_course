#!/usr/local/bin/python3.7

#https://docs.python.org/3/tutorial/controlflow.html#defining-functions


#Function Basics
#We can create functions in Python using the following:

#    The def keyword
#    The function name - lowercase starting with a letter or underscore (_)
#    Left parenthesis (()
#    0 or more argument names
#    Right parenthesis ())
#    A colon :
#    An indented function body





# CREATE code one and reuse it

def hello_world():
    print ("Hello World")


hello_world() # Call the function

def print_name(name):
    print (f"name is {name}")

print_name("Simon")
print_name("Peter")


def add_two(num):
    return num + 2

result = add_two(2)
print_name(result)
result = add_two(1000)
print_name(result)


def add (num1,num2):
    return num1+ num2

result= add(1,5)
print_name(result)



def contact_card(name, age, car_model):
    return f"{name} is {age} drives a {car_model}"

contact_card("keith", 29, "civic")
contact_card(age=28, car_model ="civic", name="keith")



def can_drive(age, driving_age=16):
    return age >= driving_age

x=can_drive(15)
print (f" {x}")

x=can_drive(15,12) # the second argument 14 over rides the arg set in the function (16)
print (f" {x}")
