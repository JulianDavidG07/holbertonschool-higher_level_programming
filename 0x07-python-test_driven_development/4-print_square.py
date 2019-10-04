#!/usr/bin/python3
"""Module print a square
"""


def print_square(size):
    """Function to return a square.


    Args:
        size: is the size of the squre to return


    Returns:
        the size of square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            print("#" * size)
