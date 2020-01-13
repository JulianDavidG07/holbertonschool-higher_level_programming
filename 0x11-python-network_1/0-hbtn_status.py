#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request

with urllib.request.urlopen("https://intranet.hbtn.io/status") as f:

    url = f.read()
    print('Body response:\n\t- type:{}\n\t'
          '- content: {}\n\t- utf8 content: {}'.format(type(url),
                                                       url,
                                                       url.decode('utf-8')))
