#!/usr/bin/python3

"""
defining a class Student.
"""


class Student:
    """
    instantiation.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """
    public method that retrieves a dictionary rep.
    """
    def to_json(self, attrs=None):
        if attrs is None:
            """
            retrieve all attributes.
            """
            return self.__dict__
        else:
            """
            create a dictionary with only the specified attributes.
            """
            filtered_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_dict[attr] = getattr(self, attr)
            return filtered_dict
