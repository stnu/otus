from Figure import Figure
import math


class Circle(Figure):
    def __init__(self, r):
        self.name = "Circle"
        self.r = r
        self.area = math.pi * (self.r ** 2)
        self.perimeter = 2 * math.pi * self.r
