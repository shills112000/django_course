#!/usr/local/bin/python3.7
# variables cannot start with a numbers
# There cannot be spaces , use _ instead
# canoot use  :"",<>/>?|\()!@#$%^&*~-+
# Names lowercase
# varialbes can be assigned to different data types

my_dogs = 2
print (my_dogs)

my_dogs = my_dogs + 8  # This will be 10
print (my_dogs)

# type  , tells you what data type a variable is

what_type=type(my_dogs)
print (what_type)   # SHOWS INT

my_dogs = "test"

print (my_dogs)
what_type=type(my_dogs)
print (what_type)  # shows str


my_income = 100
tax_rate = 0.1

my_taxes = my_income * tax_rate
print (my_taxes)


# add to veriable

my_name="Simon"

my_name += " Hills"

print (my_name)
