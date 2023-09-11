#!/usr/bin/python3


"""defining a class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height."""
        super().__init__()  # Call the constructor of the parent class
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
