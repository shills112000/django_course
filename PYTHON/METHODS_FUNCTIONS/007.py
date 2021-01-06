#!/usr/bin/python3.6

def spy_game(nums):
    print (nums)
    count = 0
    nums_len=len(nums)
    while count < nums_len - 1:
        if nums[count] == 0 and nums[count+1] == 0 and nums[count+2] == 7:
            return True
        count += 1
    return False
# Check
x=spy_game([1,2,4,0,0,7,5])
print (x)
x=spy_game([1,0,2,4,0,5,7])
print (x)
x=spy_game([1,0,2,4,0,5,7,0,0,0,0,0,0,0,0,7])
print (x)
x=spy_game([1,0,2,4,0,5,7,0,0,0,0,0,0,0,0,17])
print (x)
