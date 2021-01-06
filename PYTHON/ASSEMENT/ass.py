#!/usr/local/bin/python3.7

word = 'hello'

print (word[1]) # print e

print (word[::-1]) #reverse the string
print (word)
print (word[4])
print (word[4:51:1])


list=[0,0]
list.append(0)

print (list)

list=[0,0,0,0]

list.remove(0)
print (list)

list3= [1,2,[3,4,'hello']]
list3[2][2] ='goodbye'
print (list3)

list4=[5,4,3,2,1]
list4.sort()
print (list4)


d = {'simple_key' : 'hello'}

print (d['simple_key'])
d = {'k1' :{ 'k2': 'hello'}}

print (d['k1']['k2'])


d = {'k1' :[{'nest_key': ['this is deep' , ['hello']]}]}

print (d['k1'][0]['nest_key'][1][0])


d= {'k1':[1,2,{'k2' : ['this is tricky', {'tough' :[1,2,['hello']]}]}]}

print (d['k1'][2]['k2'][1]['tough'][2][0])

list=[1,2,2,33,4,4,11,22,3,3,2]

new_list=set(list)
print (new_list)

