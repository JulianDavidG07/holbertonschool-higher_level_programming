#!/usr/bin/python3
'''
funtion that write a string to a text file
'''


def write_file(filename="", text=""):
    '''
    return the number of characters written
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
