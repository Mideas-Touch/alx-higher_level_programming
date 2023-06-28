#!/usr/bin/python3
"""Square class based on 1-square.py

"""

class Square:
    """Square class with a private atr -size

    """
    
    def __init__(self, size=0):
        """Initialize class with a private attr,size

        """

        if type(size) != int:
            raise TypeError("size must be an integer")

        """Perform size validation

        """

        if size < 0:
            raise ValueError("size must be >= 0")

        """Declare size variable as a private attribute

        """
        self.__size = size
