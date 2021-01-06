#!/usr/local/bin/python3.7

# % 2 == 0 then it's an even number

# function to show only even numbers

#def check_even(num):
#    result=num % 2 == 0
#    return result


def check_even(num):
    return num % 2 == 0

print(check_even(29))
print(check_even(20))

# RETURN TRUE IF ANY NUM EVEN IN LIST

def list_even_check(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
    return False # if all numbers are even return false

print(list_even_check([1,3,5]))
print(list_even_check([1,3,2]))

# RETURN ALL EVEN NUMBERS IN A LIST

def even_number_list(num_list):
    # placeholder variables for what I will return
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers

result=even_number_list([1,3,5])
print (result)
result=even_number_list([2,2,5])
print (result)
