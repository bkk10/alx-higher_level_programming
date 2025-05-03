class Rectangle:
    """Defines a Rectangle."""

    # Public class attribute
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle with width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment when instance is created

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width, with type and value checks."""
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
        """Setter for height, with type and value checks."""
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
        """Return the string representation of the rectangle with '#' characters."""
        if self.width == 0 or self.height == 0:
            return ""
        rect = ""
        for _ in range(self.height):
            rect += "#" * self.width + "\n"
        return rect.rstrip()  # Remove the last newline

    def __repr__(self):
        """Return a string that can recreate a new Rectangle instance."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when an instance is deleted and decrement the instance counter."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
