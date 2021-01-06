#!/usr/local/bin/python3.7

st = "Sammy Print only the words that start with an s"
print (st)

for word in st.split():
    #if word[0] == 's' :
    #if word[0].lower()  == 's' : # get uppercase letters by converting to lowercasee
    if word[0] == 's' or word[0] == 'S':
        print (word)

