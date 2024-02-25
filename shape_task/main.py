from shape_task.shape import Rectangle, Triangle, Square, Circle

rectangle = Rectangle(10, 5)

print(rectangle.get_area())

circle = Circle(10)
print(circle.get_area())
print(circle.get_perimeter())

triangle = Triangle(1, 4, 5, 2, 6, 7)
print(triangle.get_area())

square = Square(5)
print(square.get_width())
