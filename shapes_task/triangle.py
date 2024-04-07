from shapes_task.shape import Shape
import math


class Triangle(Shape):
    def __init__(self, x_1, y_1, x_2, y_2, x_3, y_3):

        self.__x_1 = None
        self.__y_1 = None
        self.__x_2 = None
        self.__y_2 = None
        self.__x_3 = None
        self.__y_3 = None

        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2
        self.x_3 = x_3
        self.y_3 = y_3

    @property
    def x_1(self):
        return self.__x_1

    @x_1.setter
    def x_1(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(f'Координаты треугольника должны быть числом, a не {type(value).__name__}')

        self.__x_1 = float(value)

    @property
    def y_1(self):
        return self.__y_1

    @y_1.setter
    def y_1(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(f'Координаты треугольника должны быть числом, a не {type(value).__name__}')

        self.__y_1 = float(value)

    @property
    def x_2(self):
        return self.__x_2

    @x_2.setter
    def x_2(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(f'Координаты треугольника должны быть числом, a не {type(value).__name__}')

        self.__x_2 = float(value)

    @property
    def y_2(self):
        return self.__y_2

    @y_2.setter
    def y_2(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(f'Координаты треугольника должны быть числом, a не {type(value).__name__}/.')

        self.__y_2 = float(value)

    @property
    def x_3(self):
        return self.__x_3

    @x_3.setter
    def x_3(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(f'Координаты треугольника должны быть числом, a не {type(value).__name__}.')

        self.__x_3 = float(value)

    @property
    def y_3(self):
        return self.__y_3

    @y_3.setter
    def y_3(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(f'Координаты треугольника должны быть числом, a не {type(value).__name__}.')

        self.__y_3 = float(value)

    @classmethod
    def get_length(cls, *coordinates):
        return max(coordinates) - min(coordinates)

    @classmethod
    def get_side_length(cls, x_1, x_2, y_1, y_2):
        return math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))

    def __repr__(self):
        return f"Triangle({self.__x_1, self.__y_1}, {self.__x_2, self.__y_2}, {self.__x_3, self.__y_3})"

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__x_1 == other.__x_1 and self.__y_1 == other.__y_1 \
            and self.__x_2 == other.__x_2 and self.__y_2 == other.__y_2 \
            and self.__x_3 == other.__x_3 and self.__y_3 == other.__y_3

    def __hash__(self):
        return hash((self.__x_1, self.__y_1, self.__x_2, self.__y_2, self.__x_3, self.__y_3))

    def get_height(self):
        return self.get_length(self.__y_1, self.__y_2, self.__y_3)

    def get_width(self):
        return self.get_length(self.__x_1, self.__x_2, self.__x_3)

    def get_perimeter(self):
        ab_side_length = self.get_side_length(self.__x_1, self.__x_2, self.__y_1, self.__y_2)
        bc_side_length = self.get_side_length(self.__x_2, self.__x_3, self.__y_2, self.__y_3)
        ac_side_length = self.get_side_length(self.__x_1, self.__x_3, self.__y_1, self.__y_3)

        return ab_side_length + bc_side_length + ac_side_length

    def get_area(self):
        epsilon = 1.0e-10

        if abs((self.__x_3 - self.__x_1) * (self.__y_2 - self.__y_1) - (self.__y_3 - self.__y_1) * (
                self.__x_2 - self.__x_1)) <= epsilon:
            return 0

        return self.get_height() * self.get_width() * 0.5
