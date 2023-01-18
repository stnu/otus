from Triangle import Triangle
from Rectangle import Rectangle

rectangle = Rectangle(10, 2)
print(rectangle.area)

triangle = Triangle(13, 14, 15)
print(triangle.area)

print(rectangle.add_area(triangle))
