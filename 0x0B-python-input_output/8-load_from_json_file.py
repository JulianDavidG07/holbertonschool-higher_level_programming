#!/usr/bin/python3
import json
'''
funcion object JSON representation
'''


def load_from_json_file(filename):
    '''
    Write a object to a text file
    '''

    with open(filename) as f:
        return json.load(f)
