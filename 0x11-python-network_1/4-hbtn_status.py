#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":

    req = requests.get("https://intranet.hbtn.io/status")
    url = req.text
    print('Body response:\n\t- type: {}\n\t'
          '- content: {}'.format(type(url), url))
