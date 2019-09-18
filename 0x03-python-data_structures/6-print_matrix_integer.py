#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return(None)
    for i in range(0, len(matrix)):
        print(*matrix[i])
