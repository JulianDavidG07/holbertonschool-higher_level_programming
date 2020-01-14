#!/usr/bin/python3
"""
sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""
import urllib.request as ur
import sys

if __name__ == "__main__":

    with ur.urlopen(sys.argv[1]) as f:
        print(f.headers['X-Request-Id'])
