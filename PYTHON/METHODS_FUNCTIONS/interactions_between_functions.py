#!/usr/local/bin/python3.7

from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess =''  # 1 of 3 index positions

    while guess not in ['0','1','2']:
        guess = input ("Pick a number either 0 , 1 , 2 :")
    return int(guess)  # return as interger

def check_guess(mylist,guess):
    if my_list[guess] == 'O':
        print ("Correct!")
        print (mylist)
    else:
        print ("wrong guess!")
        print (mylist)


# INITAL LIST
my_list= [' ' , 'O', ' ']

# SHUFFLE LIST
mixedup_list = shuffle_list(my_list)

# USER GUESS
myindex = player_guess()

#CHECK GUESS
check_guess(mixedup_list,myindex)
