#!/usr/local/bin/python3.7

stock_prices = [('APPL',200), ('GOOG',400), ('MSFT',100)]

for item in stock_prices:
    print (item)

for ticker,price in stock_prices:
    print (ticker)
    print (price+(0.1*price))


# NOW USE FUNCTIONS

def employee_check(work_hours):
    # placeholder varibles
    current_max = 0
    employee_of_month = ''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    # Return
    return (employee_of_month, current_max)

work_hours = [('Abby',100), ('Billy', 400) , ('Dick' , 500)]
print(employee_check(work_hours))


work_hours = [('Abby',700), ('Billy', 400) , ('Dick' , 500)]
print(employee_check(work_hours))

name,hours = employee_check(work_hours)
print (f" name : {name}, hours : {hours}")
