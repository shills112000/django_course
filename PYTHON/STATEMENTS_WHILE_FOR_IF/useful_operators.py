#!/usr/local/bin/python3.7

mylist = [1,2,3]

#range (start,stop[,step[])

# This will pring all number up to 10 starting at 0

for num in range(10):
    print (num)

for num in range(3,10): # start are 3 go up to 10
    print (num)

for num in range(0,10,2): # start at 0 going to up to 10 steping two at a time , even numbers
    print (num)


mylist= list(range(0,11,2)) # cast the range to a list start at 0 up to 11 stepping 2
for num in mylist:
    print (num)


index_count = 0
for letter in 'abcde':
    print (f"At index {index_count} the letter is {letter}")
    index_count +=1

# to do the above use the enumerate counter

index_count = 0
word = 'abcde'
for item in enumerate(word):
    print (item) # show in tuple

for count,letter in enumerate(word):
    print (f"number is {count}")
    print (f"letter is {letter}")


# zip function , zip togher two list

mylist1 =[1,2,3,4]
mylist2 =['a','b','c']
for item in zip(mylist1,mylist2):
    print (item)


# can use 3 lists or more with zip

mylist3 = [100,200,300]
for item in zip(mylist1,mylist2,mylist3):
    print (item)

print ("put in to new_list a zip")
new_list=list(zip(mylist1,mylist2,mylist3))

for entry in new_list:
    print (entry)

# in keyword searches for the entry in the list
if 1 in [1,2,3]:
    print (" 1 is in the list")

if 'a' in 'is it an animal':
    print (" a is in the word")


if 'mykey' in {'mykey':3}:
    print ("mykey is in the dictionary")

d={'mykey':345}

if 345 in d.values():
    print ("345 is in dictionary value")

if 'mykey' in d.keys():
    print ("mykey is in the dict")


#min : show the minimum value

mylist = [10,20,30,40]
print (min(mylist))

# max : show max value
mylist = [10,20,30,40]
print (max(mylist))


# IMPOT
