#!/usr/bin/python3

"""function that returns the list of available attributes and methods"""


def lookup(obj):

    """Return a list of an object's available attributes."""
    _all = dir(obj)

    public = [name for name in _all if not name.startswith('-')]

    """Returning the list"""
    return public
