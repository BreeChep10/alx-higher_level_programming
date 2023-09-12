#!/usr/bin/python3

import json

"""
function tha returns JSON representatation of an objsct.
"""


def to_json_string(my_obj):
    """serializing my_obj"""
    return (json.dumps(my_obj))
