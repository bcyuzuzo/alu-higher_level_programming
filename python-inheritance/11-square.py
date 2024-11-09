#!/usr/bin/python3
"""Import Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle."""

    def __init__(self, size):
        """Initialize square with size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return string of square."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
