#!/usr/bin/python3

"""
defining a class student.
"""


class Student:
    """
    instantiation
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """
    public method that retrieves a dictionary rep of a Student instance.
    """
    def to_json(self, attrs=None):
        if attrs is None:
            """
            if attrs is not provided, retrive all attributes.
            """
            return self.__dict__
        else:
            """
            create a dictionary with only the specified attributes.
            """
            filtered_dict = []
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_dict[attr] = getattr(self, attr)
            return filtered_dict

    """
    public method that replaces attributes of the student instance.
    """
    def reload_from_json(self, json):
        """
        Update attributes based on the provided JSON dictionary
        """
        for key, value in json.items():
            setattr(self, key, value)
