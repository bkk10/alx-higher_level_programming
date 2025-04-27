#!/usr/bin/python3
class Rectangle:
    """Defines a Rectangle."""

    number_of_instances = 0  # Public class attribute
    print_symbol = "#"       # Public class attribute

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment instance counter

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width, with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height, with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns the string representation of the rectangle with print_symbol."""
        if self.width == 0 or self.height == 0:
            return ""
        rect = ""
        symbol = str(self.print_symbol)  # Convert print_symbol to string
        for _ in range(self.height):
            rect += symbol * self.width + "\n"
        return rect.rstrip()  # Remove the last newline

    def __repr__(self):
        """Returns a string that recreates the rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when an instance is deleted and decrement the instance counter."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect1, rect2):
        if not isinstance(rect1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect1.area() == rect2.area()):
            return rect1
        else:
            return rect2
