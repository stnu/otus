
def test_circle():
    from src.circle import Circle
    import math

    c = Circle(2)
    assert c.area == math.pi * 4
    assert c.perimeter == math.pi * 4