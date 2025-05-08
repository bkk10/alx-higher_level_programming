#!/usr/bin/python3
"""Rectangle class that inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """get area"""
        return self.width * self.height

    def display(self):
        """display in #"""
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """return strings"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def display(self):
        """display in x and y"""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """ List of attribute names in the expected order"""
        attributes = ['id', 'width', 'height', 'x', 'y']
        """ If positional arguments are given (args), use them"""
        if args and len(args) > 0:
            for index in range(min(len(args), len(attributes))):
                setattr(self, attributes[index], args[index])
        else:
            """ Otherwise, use named arguments (kwargs)"""
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
