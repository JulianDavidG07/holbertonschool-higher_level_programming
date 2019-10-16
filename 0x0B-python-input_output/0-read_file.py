#!/usr/bin/python3
'''
funtion to print the content of a file
'''


def read_file(filename=""):
    '''
    open and go through a file
    '''
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end="")
