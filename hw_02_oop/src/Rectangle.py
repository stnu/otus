from hw_02_oop.src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        self.name = "Rectangle"
        self.a = a
        self.b = b
        self.area = self.a * self.b
        self.perimeter = (self.a + self.b) * 2
