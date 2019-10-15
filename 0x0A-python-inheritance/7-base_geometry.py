#!/usr/bin/python3
'''
base geometry
'''


class BaseGeometry:
    '''
    metod return to exception
    '''
    def area(self):
        '''
        raise an exception
        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''
        raise exception with validator
        '''
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value is 0 or value < 0:
            raise ValueError('{} must be greater than 0'.format(name))
