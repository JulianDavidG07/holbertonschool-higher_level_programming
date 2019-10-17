#!/usr/bin/python3
import json

'''
funcion return JSON format
'''


def from_json_string(my_str):
    '''
    object represented in JSON format
    '''
    return json.loads(my_str)
