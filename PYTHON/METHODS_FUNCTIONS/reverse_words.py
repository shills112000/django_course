#!/usr/bin/python3.6

def master_yoda1(text):
    words=text.split(' ')
    words_in_list=len(words) - 1
    count=0
    while count < words_in_list + 1:
        print (words.pop(words_in_list))
        words_in_list = words_in_list - 1

def master_yoda(text):
    words=text.split(' ')
    words.reverse()
    print (" ".join(words))


master_yoda1('I am home')
# Check
master_yoda('We are ready')
