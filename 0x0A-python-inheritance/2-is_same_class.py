#!/usr/bin/python3


"""Function that checks whether an object is an instance"""


def is_same_class(obj, a_class):
    """returns True if it is an instance else False"""

    return type(obj) is a_class
