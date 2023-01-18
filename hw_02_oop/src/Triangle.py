from hw_02_oop.src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            self.name = "Triangle"
            self.a = a
            self.b = b
            self.c = c
            self.perimeter = self.a + self.b + self.c
            half_perimeter = self.perimeter / 2
            self.area = (half_perimeter * (half_perimeter - self.a) * (half_perimeter - self.b) * (
                        half_perimeter - self.c)) ** 0.5
        else:
            raise ValueError
