#!/usr/bin/python3
'''
return numbers line of a file
'''


def number_of_lines(filename=""):
    '''
    open and go through and return numbers lines
    '''
    num_line = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            num_line += 1
    return num_line
