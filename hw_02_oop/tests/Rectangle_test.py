import

def test_rectangle():
    from src.Rectangle import Rectangle

    r = Rectangle(2, 4)
    assert r.area == 8
    assert r.perimeter == 12