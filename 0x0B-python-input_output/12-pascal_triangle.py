#!/usr/bin/python3

"""
function that returns a list of lists of integers representing
the Pascal’s triangle
"""


def pascal_triangle(n):
    """
    Return and empty list if n is less or equal to 0
    """
    if n <= 0:
        return []

    result = []
    for i in range(n):
        current_row = [1]
        """
        calculate the elements in the current row
        """
        if i > 0:
            previous_row = result[i - 1]
            for j in range(1, i):
                current_row.append(previous_row[j - 1] + previous_row[j])
            current_row.append(1)

        """
        add the current row to the result
        """
        result.append(current_row)
    return result
