#!/usr/bin/python3

"""
A module that adds two numbers
"""

def add_integer(a, b=98):
    """
    this fuction adds two numbers

    @a: the first number
    @b: the second number

    raises an exception if:
    a or b is not int or float

    Return:
    an addition of the two numbers
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
