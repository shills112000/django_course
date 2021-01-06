#!/usr/local/bin/python3.7

#https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming

#while True:
#  print ("Looping")

count = 1
while count <=4:
    print (f"counting : {count}")
    count += 1


count =0
while count < 10:
    if count % 2 == 0:# miss even numbers
        count +=1
        continue
    print (f"were counting odd numbers: {count}")
    count += 1
    count += 1


count = 1
while count < 10:
    if count % 2 == 0:
        break
    print (f"We are counting odd numbers {count}")
    count += 1


x = 0
while x < 5 :
    print (f"the current value of x is {x}")
    #x = x+1
    x+= 1 # same as above
else:
    print (f"x is {x} not less than 5")


# break continue pass

#break : breaks out of the current closest enclosing loop
#continue: goes to the top of the closted enclosing loop
#pass; does nothing at all

# PASS
x = [1,2,3]

for item in x:
    pass   # this is a filler and allows the for loop without having any code and processes no errorspass


#CONTINUE

mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        continue # go to the top of the for loop
    print (letter)

#BREAK

for letter in mystring:
    if letter == 'a':
        break # breaks out of loop when a is hit
    print (letter)

x = 0
while x < 5:
    if x == 2: # break out of loop if x equals to 2
        break
    print (x)
    x+=1
