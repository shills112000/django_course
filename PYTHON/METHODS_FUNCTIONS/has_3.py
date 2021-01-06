#!/usr/bin/python3.6

def has_33(nums):
    print (nums)
    count = 0
    nums_len=len(nums)
    while count < nums_len - 1:
        print (f"   entrycount is {nums[count]}")
        if nums[count] == 3 and nums[count+1] == 3:
            return True
        count += 1
    return False


# Check
x=has_33([1, 3, 3])
print (x)
# Check
x=has_33([1, 3, 1, 3])
print (x)
# Check
x=has_33([3, 1, 3])
print (x)
# Check
x=has_33([3, 1, 3, 1 , 3, 4 , 3 , 3 , 4])
print (x)
# Check
x=has_33([3, 1, 3, 1 , 3, 4 , 3 , 2 , 4])
print (x)
