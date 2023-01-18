from hw_02_oop.src.Figure import Figure


class Square(Figure):
    def __init__(self, a):
        self.name = "Square"
        self.a = a
        self.area = self.a ** 2
        self.perimeter = self.a * 4

