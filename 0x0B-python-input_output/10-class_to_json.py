#!/usr/bin/python3
'''
funtion return a class format JSON
'''


def class_to_json(obj):
    ''''
    object in JSON format
    '''
    return obj.__dict__
