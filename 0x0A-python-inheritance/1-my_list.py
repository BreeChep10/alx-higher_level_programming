#!/usr/bin/python3


"""Defining a class"""


class MyList(list):
    """functions that sorts in ascending order"""

    def print_sorted(self):
        sorts = sorted(self)

        """printing the sorted list"""
        print(sorts)
