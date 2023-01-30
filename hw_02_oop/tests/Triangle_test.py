def test_ids_triangle():
    from src.Triangle import Triangle
    try:
        t = Triangle(1, 1, 1)
    except Exception as e:
        assert e == ValueError


def test_triangle():
    from src.triangle import Triangle
    t = Triangle(13, 14, 15)
    assert t.perimeter == 42
    assert t.area == 84