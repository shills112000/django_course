#!/usr/local/bin/python3.7

st = 'Print only the words that sta4rt with s in this sentence'

x=st.split()

for items in x:
    if (items[0:1] == 's'):
        print (f"{items}")
