#!/usr/bin/python3
"""Module matrix divided
"""


def matrix_divided(matrix, div):
    """Funtion to divided a matrix.

    Args:
        matrix: matrix to divided
        div: the number to divide matrix


    Returns:
        matrix divided for div

    """
    c = [[round(elem / div, 2) for elem in list]for list in matrix]
    new_matrix = c.copy()
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix " +
                        "(list of lists) of integers/float")
    elif type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div is 0:
        raise ZeroDivisionError("division by zero")
    elif len(matrix[0]) is not len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")

    return new_matrix
