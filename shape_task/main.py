from shape_task.rectangle import Rectangle
from shape_task.triangle import Triangle
from shape_task.square import Square
from shape_task.circle import Circle


def get_shape_with_max_area(shapes):
    if len(shapes) == 0:
        return None
    sorted_list = sorted(shapes, key=lambda sort_shape: sort_shape.get_area(), reverse=True)
    return sorted_list[0]


def get_shape_with_next_perimeter_after_max(shapes):
    if len(shapes) == 0:
        return None
    sorted_list = sorted(shapes, key=lambda sort_shape: sort_shape.get_area(), reverse=True)

    return sorted_list[1]


shapes_list = [Square(4), Square(15), Triangle(0, 2, 1, 5, 1, 8), Triangle(0, 2, 1, 5, 1, 8), Rectangle(9, 5),
               Circle(8)]

shapes_list_2 = []

print(f"Фигура с максимальной площадью из заданного списка фигур = {get_shape_with_max_area(shapes_list)}")
print(
    f"Фигура со вторым по величине периметром из заданного списка фигур = {get_shape_with_next_perimeter_after_max(shapes_list)}")

print(f"Фигура с максимальной площадью из заданного списка фигур = {get_shape_with_max_area(shapes_list_2)}")
print(
    f"Фигура со вторым по величине периметром из заданного списка фигур = {get_shape_with_next_perimeter_after_max(shapes_list_2)}")
