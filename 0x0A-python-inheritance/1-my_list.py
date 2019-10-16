#!/usr/bin/python3
'''
class to inherit from list class
'''


class MyList(list):
    '''
    Class inhiritance
    '''
    def print_sorted(self):
        '''
        print list sorted
        '''
        print(sorted(self))
