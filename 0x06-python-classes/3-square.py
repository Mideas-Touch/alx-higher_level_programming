#!/usr/bin/python3
""""A class Square defining a square base on 1-square.py

"""

class Square:
    """Square class with a private attr -size

    """
    def __init__(self,size=0):
        """Initializes the size variable as a private instance attr

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self)
    """Returns the square area

    """
        return (self.__size * self.__size)
