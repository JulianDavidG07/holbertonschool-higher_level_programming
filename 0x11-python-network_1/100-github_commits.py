#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
"""
import requests
import sys

if __name__ == "__main__":

    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'
    response = requests.get(url)

for i in range(10):
    commit = (response.json()[i].get('sha'))
    author = (response.json()[i].get('commit').get('author').get('name'))
    print(f'{commit}: {author}')
