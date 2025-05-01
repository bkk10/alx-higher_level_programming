#!/usr/bin/python3
"""
BaseGeometry class with an area method that raises an exception
"""

class BaseGeometry:
    """A base class for geometry."""

    def area(self):
        """Method not implemented yet."""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """method that checks the type"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
