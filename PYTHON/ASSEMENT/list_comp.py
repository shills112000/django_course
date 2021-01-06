#!/usr/local/bin/python3.7

st = "Create a list of the first letters of every word"

x=st.split()
newlist=[]
for item in x:
    print (f"{item}")
    print (f"{item[0:1]}")
    newlist.append(item[0:1])

print (f"{newlist}")

