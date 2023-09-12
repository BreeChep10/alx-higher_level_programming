#!/usr/bin/python3

"""
defining a class Student.
"""


class Student:
    """
    instantination.
    """
    def __init__(self, first_name, last_name, age):
        """
        initializing the students.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Create and return a dictionary representation of the Student instance
        """
        return self.__dict__
