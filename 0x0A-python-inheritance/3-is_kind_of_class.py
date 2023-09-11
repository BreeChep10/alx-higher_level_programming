#!/usr/bin/python3

"""Defining a function that checks for an instance"""


def is_kind_of_class(obj, a_class):
    """returns true if the object is an instance else false"""
    return (isinstance(obj, a_class))
