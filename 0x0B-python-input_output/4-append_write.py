#!/usr/bin/python3
'''
funtion that write a string to a text file
'''


def append_write(filename="", text=""):
    '''
    return the number of characters written
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
