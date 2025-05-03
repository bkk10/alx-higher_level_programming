#!/usr/bin/python3
#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size  # Use the setter to validate

    @property
    def size(self):  # Getter
        return self.__size

    @size.setter
    def size(self, value):  # Setter
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
