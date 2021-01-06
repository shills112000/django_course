#!/usr/local/bin/python3.7

import requests

payload = {'username' : 'admin' , 'password' : 'password'}
r = requests.post('http://httpbin.org/post', data=payload)

print  (r.url)
print  (r.text)


