#!/usr/bin/python3
import json

'''
funcion object JSON representation
'''


def save_to_json_file(my_obj, filename):
    '''
    Write a object to a text file
    '''
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
