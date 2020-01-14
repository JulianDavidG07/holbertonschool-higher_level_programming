#!/usr/bin/python3
"""
Script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import urllib.parse
import urllib.request
from sys import argv


email = {'email': argv[2]}
data = urllib.parse.urlencode(email)
data = data.encode('ascii')
r = urllib.request.Request(argv[1], data)
with urllib.request.urlopen(r) as f:
    print(str(f.read(), 'utf-8'))
