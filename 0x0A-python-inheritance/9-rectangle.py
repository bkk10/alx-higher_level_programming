#!/usr/bin/python3
"""
Module 8-rectangle
Defines a Rectangle class that inherits from BaseGeometry
"""

class BaseGeometry:
    """A base class for geometry."""

    def area(self):
        """Raises an exception since area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a value is an integer greater than 0."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height after validation."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    def area(self):
        """returns the area"""
        return self.__width * self.__height
    def __str__(self):
        """returns a string representation"""
        return f"[Rectangle] {self.__width}/{self.__height}"
