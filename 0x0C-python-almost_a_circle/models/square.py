#!/usr/bin/python3
"""
square inherited
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """square inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """instantiation"""
        super().__init__(id, x, y, size, size)

    def __str__(self):
        """returning string"""
        return f"[Square] (self.id) self.x/self.y - {self.width}"
