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
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value is 0 or value < 0:
            raise ValueError('{} must be greater than 0'.format(name))

'''
rectangle inheritance
'''


class Rectangle(BaseGeometry):
    '''
    method__init__
    '''
    def __init__(self, width, height):
        '''
        width and height must be private. No getter or setter
        '''
        self.__width = width
        self.__height = height
        super().integer_validator(width, height)

    def area(self):
        '''
        return area rectangle
        '''
        return self.__width * self.__height

    def __str__(self):
        '''
        informal representation of a Rectangle
        '''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
