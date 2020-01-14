#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":

    with requests.get("https://intranet.hbtn.io/status") as f:

        url = f.text
        print('Body response:\n\t- type: {}\n\t'
              '- content: {}'.format(type(url),
                                     url))
