def test_add_area_1():
    from src.triangle import Triangle
    t = Triangle(13, 14, 15)

    from src.square import Square
    s = Square(3)

    assert t.add_area(s) == 93


def test_add_area_2():
    from src.triangle import Triangle
    t = Triangle(13, 14, 15)

    from src.rectangle import Rectangle
    r = Rectangle(2, 4)

    from src.figure import Figure
    assert isinstance(r, Figure)

    assert t.add_area(r) == 92


def test_add_area_3():
    from src.triangle import Triangle
    t = Triangle(13, 14, 15)

    from src.circle import Circle
    import math

    c = Circle(2)

    from src.figure import Figure
    assert isinstance(c, Figure)
    assert t.add_area(c) == 84 + math.pi * 4


def test_add_area_4():
    from src.rectangle import Rectangle
    r = Rectangle(2, 4)

    from src.circle import Circle
    import math

    c = Circle(2)

    from src.figure import Figure
    assert isinstance(c, Figure)
    assert r.add_area(c) == 8 + math.pi * 4


def test_add_area_5():
    from src.rectangle import Rectangle
    r = Rectangle(2, 4)

    from src.square import Square
    s = Square(3)

    from src.figure import Figure
    assert isinstance(s, Figure)
    assert r.add_area(s) == 17