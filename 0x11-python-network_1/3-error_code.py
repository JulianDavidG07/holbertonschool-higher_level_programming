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
        req = urllib.request.urlopen(sys.argv[1])
        with req as f:
            print(f.read().decode())
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
