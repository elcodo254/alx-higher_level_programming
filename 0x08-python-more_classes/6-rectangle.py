#!/usr/bin/python3
""" Defines Rectangle class"""


class Rectangle:
    """Represents a rectangle

    Attributes:
        number_of_instances (int): The number of Rectangle instances
        """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialize new rectangle

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return area of Rectagle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns printable representation of Rectangle
        rectangle printed with character #
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """return a string representation of the rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """ Prints message on deletion of an instance of Rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
