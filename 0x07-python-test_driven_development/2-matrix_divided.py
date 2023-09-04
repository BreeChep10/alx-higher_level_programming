#!/usr/bin/python3

"""
a module to divide a matrix

"""
def matrix_divided(matrix, div):
    """
    Divides a matrix(list of list) by the given input divisor

    @matrix: the list of list input
    @div: the divisor

    Execptions are raised if:
    div is zero
    any of the elements is not a number
    any of the matrix data elements is not a list

    """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    message = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(message)

    length = 0

    for j in matrix:
        if not isinstance(j, list) or not j:
            raise TypeError(message)

        for k in j:
            if not isinstance(k, (float, int)):
                raise TypeError(message)
        if (length != 0) and len(j) != length:
            raise TypeError("Each row of the matrix must have the same size")
        length = len(j)

    doll = list(map(lambda a : list(map(lambda b : round(b / div, 2), a)), matrix))
    return (doll)
