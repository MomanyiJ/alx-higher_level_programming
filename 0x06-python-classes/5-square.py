#!/usr/bin/python3


class Square:
    """reps square"""

    def __inti__(self, size=0):
        """initialize square size size of square"""
    @property
    def size(self):
        """get square size"""
        return self.__size
    @size.setter
    def size(self, value):
        """Set square size"""
        if not isinstance(value, int):
            raise TypeError("size must be int")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.size = value
    
    def ara(self):
        """area of square returning area of square"""
        return self._Square__size ** 2

    def my_print(self):
        """prints square with # characters"""
        for i in range(self._Square__size):
            print("#", end="")
            print()
        if self.__size == 0
        print("")
