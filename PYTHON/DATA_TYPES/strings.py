#!/usr/bin/env python3.7

# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

# strings are sequence of charectors , using either a single or double quotes
# strings are ordered squences , means we can use indexing and slicing to grab subsections of the strings

## indexing

# Indexing notation uses [] , grab single charector of strings
# string  : h e l l 0
# index   : 0 1 2 3 4
# reverse indexing
# string : h e l l o
# index  : 0 1 2 3 4
# reverse: 0 -4 -3 -2 -1      # so last charector will always be -1


## slicing

# uses []    [start:stop:step]

#start is the numerical index for the start of the slice
# stop is the insec you will got up to, but not include
# stop is the size of the jump you take

#\n = newline
#\t = tab
# len = gets the length of a string

# get length
word="Hello World"
length=len(word)  # get the length of a string
print (f"lenth of the word: {word} is this many charectors {length}")

word = "Tinker"
print (f"get ink from word {word} , result is : {word[1:4]}")

word = "abcdefghijk"
# string indexing
print (f"\nthe word is {word}")
print (f"the first charector of the word is {word[0]}") # get first charector of string
print (f"the second last charector of the word is : {word[-2]}") # get second last charector using negative indexing

# string slicing
word="abcdefghijk"
print (f"\n word is {word}")
print (f"grab everything from letter c to the end of word : {word} , here is the result : {word[2:]}") # grab everything from letter c to the end

print (f"get everything upto letter c, remember it does not include 3rd index  : {word} , here is the result : {word[:3]}") #  get everything upto letter c, remember it does not include 3rd index

print (f"same as above but using full index syntax : {word[0:3:1]}") # This is the same as above , but all slice information given eg. everything up to letter class (object):

print (f"get def in word {word} , result {word[3:6]}") # get def in string
print (f"print every other letter of word {word} , result : {word[::2]}") # print every other letter
print (f"reverse the word {word} {word[::-1]}") # reverse the string ###### INTERVIEW QUESTIONS
print (f"print out with word {word} -2 steps {word[::-2]}") # print out with -2 steps

# Print properties and methods

# Immutability - unchangeable
name= "Sam"
# eg you cannot run  name[0] = 'P' as strings are immutable

# if you wanted to change sam to pam
print (f"\nName is {name}")

last_letters= name[1:3:1]  # get am
# or you can just use
last_latters= name[1:] # same as name[1:3:1]
print (f"Print last letters of  {name}, result : {last_letters}")

new_name="P" + last_letters
print (new_name)

letter = "z"
print (letter * 10)  # print 10 z's

# methods
x = "hello world"
x = x.upper()  # this changes the string to uppercase
# x =  x.lower()  # this would set the string to all lowercase
print (x)

x = "Hi this is a sting"
x.split() #  create a list using whitespace  , eg hello and World
x.split('i') #  create a list splitting using 'i'
x=x.split('i')
print (x)

x = "test"
print ("test")
x.find('t') # show where in string test the letter t exists

# STring counting
'string counting'.count("n") # counts how many n's are in the text

#### String formating for printing
# .format() or f-strings

#.format
print ('This is a string {}'.format('INSERTED'))
print ('The {2} {1} {0}'.format ('fox','brown','quick')) # gives the quick brown fox
print ('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))
#float formmat follows "{value:width.precision f}"
result=100/777
print ("the result was {r:1.3f}".format(r=result))

#f-strings , introducted in python 3
name="Jose"
print (f"hello, his name is {name}")
age = 3
print (f"hello, his name is {name}, he is {age} years old")


# every other letter is lowercase
def upper_lower(word):
    count=0
    new_word=''
    for letter in word:
       count += 1
       if count %2 == 0:
           new_word= new_word + letter.lower()
       else:
           new_word= new_word + letter.upper()
    return new_word

x= upper_lower('test')
print (x)

