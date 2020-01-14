#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to
the URL and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        req = request(sys.argv[1])
        with urllib.request.urlopen(req) as f:
            print(f.response.read().decode())
    except urlib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
