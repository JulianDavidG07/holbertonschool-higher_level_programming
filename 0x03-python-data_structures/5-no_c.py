#!/usr/bin/python3
def no_c(my_string):
    letters = 'cC'
    delete = ''
    for char in my_string:
        if char not in letters:
            delete = delete + char
            return(delete)
