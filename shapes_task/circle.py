from shapes_task.shape import Shape
import math


class Circle(Shape):
    def __init__(self, radius):

        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(f'Радиус круга должен быть числом, а не {type(value).__name__}.')

        if value <= 0:
            raise ValueError(f'Радиус круга {value} должен быть больше нуля.')

        self.__radius = float(value)

    def __repr__(self):
        return f"Circle({self.__radius})"

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__radius == other.__radius

    def __hash__(self):
        return hash(self.__radius)

    def get_width(self):
        return self.__radius * 2

    def get_height(self):
        return self.__radius * 2

    def get_area(self):
        return math.pi * math.pow(self.__radius, 2)

    def get_perimeter(self):
        return 2 * math.pi * self.__radius
