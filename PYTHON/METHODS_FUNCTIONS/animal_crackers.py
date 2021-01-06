#!/usr/bin/python3.6

def animal_crackers(text):
    words=text.split(' ')
    if words[0][0].upper() == words[1][0].upper():
        print ("they are the same")
    else:
        print ("different")


# Check
animal_crackers('Levelheaded llama')


# Check
animal_crackers('Crazy Cangaroo')
