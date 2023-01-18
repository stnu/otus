def test_square():
    from src.Square import Square

    s = Square(3)
    assert s.area == 9
    assert s.perimeter == 12