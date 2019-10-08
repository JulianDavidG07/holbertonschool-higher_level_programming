#!/usr/bin/python3
"""Creating an empty Class"""


class Rectangle:
    """Print rectangle"""
    def __init__(self, width=0, height=0):
        """Begining the object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """convert width in private"""
        return self.__width

    @width.setter
    def width(self, value):
        """handle errors of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """convert height in private"""
        return self.__height

    @height.setter
    def height(self, value):
        """handle error of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """return area rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return perimeter rectangle"""
        if self.__width is 0 or self.__height is 0:
            self.perimeter = 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """return rectangule with characters"""
        if self.__width is 0 or self.__height is 0:
            return""
        else:
            for h in range(self.__height):
                for w in range(self.height - 1):
                    print('#' * self.__width)
                return '#' * self.width

    def __repr__(self):
        """recreate new instance"""
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """delete instance"""
        print("{}".format('Bye rectangle...'))
