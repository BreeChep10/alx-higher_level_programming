#!/usr/bin/python3

"""
function tha returns JSON representatation of an objsct.
"""
import json


def to_json_string(my_obj):
    """serializing my_obj"""
    return (json.dumps(my_obj))
