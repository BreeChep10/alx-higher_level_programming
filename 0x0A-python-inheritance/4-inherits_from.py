#!/usr/bin/python3


"""function checks if the object is an instance of a class"""


def inherits_from(obj, a_class):
    """returns True if is else false"""
    return (issubclass(type(obj), a_class))
