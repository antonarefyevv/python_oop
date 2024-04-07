from shapes_task.rectangle import Rectangle
from shapes_task.triangle import Triangle
from shapes_task.square import Square
from shapes_task.circle import Circle


def get_shape_with_max_area(shapes):
    if len(shapes) <= 1:
        return None

    sorted_list = sorted(shapes, key=lambda sort_shape: sort_shape.get_area(), reverse=True)
    return sorted_list[0]


def get_shape_with_next_perimeter_after_max(shapes):
    if len(shapes) <= 1:
        return None

    sorted_list = sorted(shapes, key=lambda sort_shape: sort_shape.get_perimeter(), reverse=True)
    return sorted_list[1]


shapes_list = [Square(5),
               Square(2),
               Triangle(0, 2, -1, 5, 1, 8),
               Triangle(0, 2, 1, 5, 1, -8),
               Rectangle(9, 5),
               Circle(8)]

print(f"Фигура с максимальной площадью из заданного списка фигур "
      f"= {get_shape_with_max_area(shapes_list)}")
print(
    f"Фигура со вторым по величине периметром из заданного списка фигур "
    f"= {get_shape_with_next_perimeter_after_max(shapes_list)}")
