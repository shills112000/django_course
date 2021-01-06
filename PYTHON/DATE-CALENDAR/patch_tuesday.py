#!/usr/bin/python3.6

import calendar
import datetime

#https://www.w3schools.com/python/python_datetime.asp


# Function to take the current date, add a month on and workout patch tuesday + specified number of days
# if no specified number of dates given , then default will be 0 patch_day_plus=0
def path_day_calc(day,month,year,patch_day_plus=0):    # = this puts a default value
    day = day + patch_day_plus

    # Set the year ahead if in december and month to january
    if ( month == 12) :
        year +=1
        month = 1
    else:     #  Check patch tuesday for the month + 1
        month = month+1


    cal = calendar.monthcalendar(year, month)
    first_week  = cal[0]
    second_week = cal[1]
    third_week  = cal[2]

    # If a Tuesday presents in the first week, the second Tuesday
    # is in the second week.  Otherwise, the second Tuesday must
    # be in the third week.

    if first_week[calendar.TUESDAY]:
        patch_tuesday = second_week[calendar.TUESDAY]
        patch_tuesday_plus_date = patch_day_plus + patch_tuesday
    else:
        patch_tuesday = third_week[calendar.TUESDAY]
        patch_tuesday_plus_date = patch_day_plus + patch_tuesday
    print(f"patch_tuesday = {patch_tuesday}")
    print(f"patch_tuesday_plus_date = {patch_tuesday_plus_date}")
    print(f"checking month = {month} ")
    print(f"checking year = {year}")

today_date = datetime.datetime.now()
#path_day_calc(today_date.day,12,2020,2)
path_day_calc(today_date.day,11,2021,2)
#path_day_calc(today_date.day,today_date.month,today_date.year,7)
