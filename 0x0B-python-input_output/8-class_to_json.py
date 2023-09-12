#!/usr/bin/python3

"""
function that returns the dictionary description.
"""


def class_to_json(obj):
    """
    returns a python dictionary with a simple data structure.
    """
    return obj.__dict__
