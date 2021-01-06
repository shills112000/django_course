#!/usr/local/bin/python3.7

# WEB BROWSER MODULE

# use pip to install brautiful soup
# pip install bs4

import requests, webbrowser, sys, bs4  # bs4 beautiful soup


# OOPEN WEBBROSWER
webbrowser.open('https://www.google.co.uk')

#sys.argv  , takes argument from command line
Address = ' '.join(sys.argv[1:])

webbrowser.open('https://www.google.com/maps/place' + Address)
print (sys.argv[1:])
print (Address)

# BEAUTIFUL SOUP

r = requests.get('http://www.google.co.uk')
r = requests.get('http://www.bbc.co.uk')
res = r.raise_for_status() # ERROR checking
print (res)
print (r.status_code)

site_soup = bs4.BeautifulSoup(r.text)
print (site_soup)
print (type(site_soup))

elements =  site_soup.select('div')
print (len(elements))
print (elements)

print ("\n" * 4)
for word in elements:
    print (word.getText())  # print out all the text



