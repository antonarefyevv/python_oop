from shape_task.shape import Shape, Rectangle, Triangle, Square, Circle


def get_shape_with_max_area(items):
    def sort_shape(shape):
        return shape.get_area()

    sorted_list = sorted(items, key=sort_shape, reverse=True)

    return sorted_list[0]


def get_shape_with_next_perimeter_after_max(items):
    def sort_shape(shape):
        return shape.get_perimeter()

    sorted_list = sorted(items, key=sort_shape, reverse=True)

    return sorted_list[1]


rectangle_1 = Rectangle(9, 5)

circle_1 = Circle(10)

triangle_1 = Triangle(1, 4, 5, 2, 6, 7)

square_1 = Square(5)

square_2 = Square(15)

triangle_2 = Triangle(0, 2, 1, 5, 1, 8)

circle_2 = Circle(8)
print(circle_2)

print(circle_2.get_area())

shapes_list = [square_1, square_2, triangle_1, triangle_2, rectangle_1, circle_2]

print(f"Фигура с максимальной площадью из заданного списка фигур = {get_shape_with_max_area(shapes_list)})")
print(
    f"Фигура со вторым по величине периметром из заданного списка фигур = {get_shape_with_next_perimeter_after_max(shapes_list)})")
