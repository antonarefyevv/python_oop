import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_width(self):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Square(Shape, ABC):
    def __init__(self, side_length):
        if isinstance(side_length, str):
            raise TypeError(f'Длина стороны квадрата должна быть числом, а не {type(side_length).__name__}')
        if side_length <= 0:
            raise ValueError(f'Длина стороны квадрата должна быть больше нуля')

        self.__side_length = side_length

    def __repr__(self):
        return f"Square({self.__side_length})"

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__side_length == other.__side_length

    def __hash__(self):
        return self.__side_length

    def get_height(self):
        return self.__side_length

    def get_width(self):
        return self.__side_length

    def get_area(self):
        return self.__side_length * self.__side_length

    def get_perimeter(self):
        return self.__side_length * 4


class Triangle(Shape, ABC):

    def __init__(self, x_1, y_1, x_2, y_2, x_3, y_3):
        self.__x_1 = x_1
        self.__y_1 = y_1
        self.__x_2 = x_2
        self.__y_2 = y_2
        self.__x_3 = x_3
        self.__y_3 = y_3

    def __repr__(self):
        return f"Triangle({self.__x_1}, {self.__y_1}, {self.__x_2}, {self.__y_2}, {self.__x_3}, {self.__y_3})"

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__x_1 == other.__x_1 and self.__y_1 == other.__y_1 and self.__x_2 == other.__x_2 and self.__y_2 == \
            other.__y_2 and self.__x_3 == other.__x_3 and self.__y_3 == other.__y_3

    def __hash__(self):
        return [self.__x_1, self.__y_1, self.__x_2, self.__y_2, self.__x_3, self.__y_3]

    def get_width(self):
        return max(self.__x_1, self.__x_2, self.__x_3) - min(self.__x_1, self.__x_2, self.__x_3)

    def get_height(self):
        return max(self.__y_1, self.__y_2, self.__y_3) - min(self.__y_1, self.__y_2, self.__y_3)

    def get_perimeter(self):
        ab_side_length = math.sqrt(math.pow(self.__x_2 - self.__x_1, 2) + math.pow(self.__y_2 - self.__y_1, 2))
        bc_side_length = math.sqrt(math.pow(self.__x_3 - self.__x_2, 2) + math.pow(self.__y_3 - self.__y_2, 2))
        ac_side_length = math.sqrt(math.pow(self.__x_3 - self.__x_1, 2) + math.pow(self.__y_3 - self.__y_1, 2))
        return ab_side_length + bc_side_length + ac_side_length

    def get_area(self):
        EPSILON = 1.0e-10
        if abs((self.__x_3 - self.__x_1) * (self.__y_2 - self.__y_1) - (self.__y_3 - self.__y_1) * (
                self.__x_2 - self.__x_1)) <= EPSILON:
            return None

        return (self.get_width() * self.get_height()) / 2


class Rectangle(Shape, ABC):
    def __init__(self, side_length, side_width):
        if isinstance(side_length, str):
            raise TypeError(f'Длина стороны прямоугольника должна быть числом, а не {type(side_length).__name__}')
        if isinstance(side_width, str):
            raise TypeError(f'Ширина стороны прямоугольника должна быть числом, а не {type(side_length).__name__}')
        if side_length <= 0:
            raise ValueError(f'Длина стороны квадрата должна быть больше нуля')
        if side_width <= 0:
            raise ValueError(f'Ширина стороны квадрата должна быть больше нуля')

        self.__side_length = side_length
        self.__side_width = side_width

    def __repr__(self):
        return f"Rectangle({self.__side_width}, {self.__side_length})"

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__side_length == other.__side_length and self.__side_width == other.__side_width

    def __hash__(self):
        return [self.__side_length, self.__side_width]

    def get_width(self):
        return self.__side_width

    def get_height(self):
        return self.__side_length

    def get_area(self):
        return self.__side_length * self.__side_width

    def get_perimeter(self):
        return 2 * self.__side_length + 2 * self.__side_width


class Circle(Shape, ABC):
    def __init__(self, radius):
        if isinstance(radius, str):
            raise TypeError(f'Радиус круга должен быть числом, а не {type(side_length).__name__}')
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
