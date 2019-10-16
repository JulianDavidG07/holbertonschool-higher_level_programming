#!/usr/bin/python3
'''
funtion that reads n lines of a text file
'''


def read_lines(filename="", nb_lines=0):
    '''
    open and go through a file
    '''
    count = 0
    with open(filename, encoding='utf-8') as f:
        for lines in f:
            count += 1
            if nb_lines >= count or nb_lines <= 0:
                print(lines, end="")
