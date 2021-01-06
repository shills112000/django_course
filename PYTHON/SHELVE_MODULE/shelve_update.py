#!/usr/bin/python3.6
import shelve

#s = shelve.open('test_shelf.db')
#try:
#    s['key1'] = { 'int': 10, 'float':9.5, 'string':'Sample data' }
#finally:
#    s.close()

s = shelve.open('test_shelf.db', writeback=True)
try:
    print (s['key1'])
    s['key1']['string'] = 'this was not here before'
    s['key1']['int'] = 2
    print (s['key1'])
finally:
    s.close()
