#!/usr/bin/python3
"""Module to print name ans last name
"""


def say_my_name(first_name, last_name=""):
    """Function to print complete name

    Args:
        firs_name: first name
        last_name: last name

    Returns:
        str: return the first and las name
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
