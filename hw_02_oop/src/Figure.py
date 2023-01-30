class Figure:
    area = 0

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError
        return self.area + figure.area




