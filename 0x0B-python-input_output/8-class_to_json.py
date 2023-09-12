#!/usr/bin/python3

"""
function that returns the dictionary description.
"""


def class_to_json(obj):
    """
    initialize an empty dictionary to store the json rep.
    """
    json_dict = {}

    for name in dir(obj):
        if not name.startswith('-'):
            value = getattr(obj, name)

            """
            check if the attribute is a serializable data type.
            """
            if isinstance(value, (list, dict, str, int, bool)):
                json_dict[name] = value
    """
    returning the json dictionary
    """
    return json_dict
