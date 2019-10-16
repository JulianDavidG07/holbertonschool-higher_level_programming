#!/usr/bin/python3
'''
funtion returns to inherits of a superclass
'''


def inherits_from(obj, a_class):
    '''
    return issubclass of funtion
    '''
    return issubclass(type(obj), a_class) and type(obj) != a_class
