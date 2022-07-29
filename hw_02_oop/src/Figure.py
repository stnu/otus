class Figure:
    area = 0

    def add_area(self, figure):
        if (figure.__class__ == "<class 'Square.Square'>" or
                figure.__class__ == "<class 'Triangle.Triangle'>" or
                figure.__class__ == "<class 'Rectangle.Rectangle'>" or
                figure.__class__ == "<class 'Circle.Circle'>"):
            return self.area + figure.area
        raise ValueError
