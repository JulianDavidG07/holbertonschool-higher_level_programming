#!/usr/bin/python3
import json

'''
funtion return a class format JSON
'''


def class_to_json(obj):
    ''''
    object in JSON format
    '''
    return json.dumps(obj.__dict__)
