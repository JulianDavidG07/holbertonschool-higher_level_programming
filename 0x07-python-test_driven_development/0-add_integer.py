#!/usr/bin/python3
"""Module add two integers
"""


def add_integer(a, b=98):
    """Function to add two integer.

    Args:
        a: is a number
        b: is number to add b

    Returns:
        int : The value to add a and b. if number is not
        iny return error.

    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
