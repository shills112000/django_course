#!/usr/local/bin/python3.7

import requests # make sure requests installed

r = requests.get ('https://google.co.uk')

## PRINT PAGE HTML CONTENT
print ("\n R.CONTENT \n")
print (r.content)

# PRINT TEXT
print ("\n R.TEXT \n")

print (r.text)

#print (r.status_code)
print ("\n R.STATUS_CODE \n")
print (r.status_code)


# httpbin.org , testing site


r = requests.get ('http://httpbin.org/get')

print ("\n R.HEADERS \n")
print (r.headers)

# YOU can print specific headers
#{'Date': 'Mon, 24 Aug 2020 12:40:49 GMT', 'Content-Type': 'application/json', 'Content-Length': '305', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}

# Print out each individual header
print (r.headers['Server' ])
print (r.headers['Date' ])


# JSON PARSER

r = requests.get ('http://httpbin.org/get')
#{'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.24.0', 'X-Amzn-Trace-Id': 'Root=1-5f43b8ab-0a376a00310dfbf097177100'}, 'origin': '34.241.3.183', 'url': 'http://httpbin.org/get'}

response = r.json()  # put the list in veriable response
print (type(response))
print (response)
print (response['url'])  # print out the url from the list
print (response['args'])  # print out the url from the list
print (response['headers'])  # print out the url from the list
print (f"Headers Accept from r.json output : {response['headers']['Accept']}")  # print out the url from the list
print (f"Headers Accept-Encoding from r.json output : {response['headers']['Accept-Encoding']}")  # print out the url from the list
print (f"Headers Host from r.json output : {response['headers']['Host']}")  # print out the url from the list
print (f"Headers User-Agent from r.json output : {response['headers']['User-Agent']}")  # print out the url from the list


# DELIVER PAYLOAD

payload = {'username': 'admin' , 'password' : 'password'}

r = requests.get('http://httpbin.org/get', params=payload)
print (r.text)

