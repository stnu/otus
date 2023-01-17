#import pytest
#from src.Figure import Figure
from Triangle import Triangle
from Rectangle import Rectangle
from Square import Square
from Circle import Circle


rectangle = Rectangle(10, 2)
triangle = Triangle(13, 14, 15)
square = Square(10)
circle = Circle(5)


def test_1():
    assert square.area == 100
