from Figure import Figure


class Circle(Figure):
    def __init__(self, r):
        self.name = "Круг"
        self.r = r
        self.area = self.pi * (self.r ** 2)
        self.perimeter = 2 * self.pi * self.r

