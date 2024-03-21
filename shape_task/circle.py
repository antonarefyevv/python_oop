from shape_task.shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        if not isinstance(radius, float) and not isinstance(radius, int):
            raise TypeError(f'Радиус круга должен быть числом, а не {type(radius).__name__}')
        if radius <= 0:
            raise ValueError(f'Радиус круга должен быть больше нуля')

        self.__radius = radius

    def __repr__(self):
        return f"Circle({self.__radius})"

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__radius == other.__radius

    def __hash__(self):
        return self.__radius

    def get_width(self):
        return self.__radius / 2

    def get_height(self):
        return self.__radius / 2

    def get_area(self):
        return float(f"{math.pi * math.pow(self.__radius, 2):.2f}")

    def get_perimeter(self):
        return 0
