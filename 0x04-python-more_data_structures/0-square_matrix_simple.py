#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square_matrix = []
    for row in matrix:
        row_squared = []
        for i in row:
            row_squared.append(i ** 2)
        square_matrix.append(row_squared)
    return (square_matrix)
