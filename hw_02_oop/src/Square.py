from Figure import Figure


class Square(Figure):
    def __init__(self, a):
        self.name = "Квадрат"
        self.a = a
        self.area = self.a ** 2
        self.perimeter = self.a * 4

    def print_name(self):
        print(self.name)


sq = Square(10)
