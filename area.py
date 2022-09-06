#!/usr/bin/python3
# This module will calculate the area of a rectangle using the concept of OOP


class Area:
    """A class that will calculate area of a rectangle"""

    def __init__(self):

        """class method to calculate area"""
        self.length = float(input("Enter length: "))
        self.breadth = float(input("Enter breadth: "))
        if self.length < 0 or self.breadth < 0:
            raise ValueError("Please Enter a Number greater than zero")
        if type(self.length) not in (int, float):
            raise TypeError("Please Enter a Number of type integer of float")
        if type(self.breadth) not in (int, float):
            raise TypeError("Please Enter a Number of type integer of float")
        self.area = self.length * self.breadth


value = Area()
print(f"Area of the rectangle is {value.area}")
