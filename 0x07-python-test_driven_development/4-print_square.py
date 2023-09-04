#!/usr/bin/python3

"""
a module to print a square

"""

def print_square(size):


    """
    a function to print a square give imput as the dimension

    @size: the dimension of the square

    Return: nothing
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if (size // 1) != size and size < 0:
        raise TypeError("size must be an integer")

    for j in range(0, size):
        for i in range(0, size):
            print("#", end="")
        print()
