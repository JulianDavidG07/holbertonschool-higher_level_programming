#!/usr/bin/python3
'''class Base 'main''''


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        '''defines the initilization of the class'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
