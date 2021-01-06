#!/usr/local/bin/python3.7

import requests

r = requests.post('http://www.github.com')

print (r.history) # 301 request code is a redirect
print (r.url)
print (r.status_code)

for resp in r.history:
    print (type(resp))
    print (resp.status_code, resp.url)

r = requests.post('http://www.github.com', allow_redirects=False)
print (r.history) # 301 request code is a redirect
print (r.status_code)
