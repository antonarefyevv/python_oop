from shape_task.shape import Shape
import math


def get_side(*args):
    return max(args) - min(args)


class Triangle(Shape):
    def __init__(self, x_1, y_1, x_2, y_2, x_3, y_3):
        args_list = [x_1, y_1, x_2, y_2, x_3, y_3]
        for arg in range(len(args_list)):
            if not isinstance(args_list[arg], (float, int)):
                raise TypeError(f'Координаты треугольника должны быть числом, a не {type(args_list[arg]).__name__}')
            if args_list[arg] < 0:
                raise ValueError('Координаты треугольника должны быть быть больше либо равны нулю')

        self.__x_1 = x_1
        self.__y_1 = y_1
        self.__x_2 = x_2
        self.__y_2 = y_2
        self.__x_3 = x_3
        self.__y_3 = y_3

    @property
    def x_1(self):
        return self.__x_1

    @x_1.setter
    def x_1(self, x_1):
        if not isinstance(x_1, (float, int)):
            raise TypeError(f'Координаты треугольника {self.__x_1} должны быть числом, a не {type(x_1).__name__}')
        if self.__x_1 <= 0:
            raise ValueError(f"Координаты треугольника {self.__x_1} должны быть быть больше либо равны нулю")

        self.__x_1 = float(x_1)

    @property
    def y_1(self):
        return self.__y_1

    @y_1.setter
    def y_1(self, y_1):
        if not isinstance(y_1, (float, int)):
            raise TypeError(f'Координаты треугольника {self.__y_1} должны быть числом, a не {type(y_1).__name__}')
        if self.__y_1 <= 0:
            raise ValueError(f"Координаты треугольника {self.__y_1} должны быть быть больше либо равны нулю")

        self.__y_1 = float(y_1)

    @property
    def x_2(self):
        return self.__x_2

    @x_2.setter
    def x_2(self, x_2):
        if not isinstance(x_2, (float, int)):
            raise TypeError(f'Координаты треугольника {self.__x_2} должны быть числом, a не {type(x_2).__name__}')
        if self.__x_2 <= 0:
            raise ValueError(f"Координаты треугольника {self.__x_2} должны быть быть больше либо равны нулю")

        self.__x_2 = float(x_2)

    @property
    def y_2(self):
        return self.__y_2

    @y_2.setter
    def y_2(self, y_2):
        if not isinstance(y_2, (float, int)):
            raise TypeError(f'Координаты треугольника {self.__y_2} должны быть числом, a не {type(y_2).__name__}')
        if self.__y_2 <= 0:
            raise ValueError(f"Координаты треугольника {self.__y_2} должны быть быть больше либо равны нулю")

        self.__y_2 = float(y_2)

    @property
    def x_3(self):
        return self.__x_3

    @x_3.setter
    def x_3(self, x_3):
        if not isinstance(x_3, (float, int)):
            raise TypeError(f'Координаты треугольника {self.__x_3} должны быть числом, a не {type(x_3).__name__}')
        if self.__x_3 <= 0:
            raise ValueError(f"Координаты треугольника {self.__x_3} должны быть быть больше либо равны нулю")

        self.__x_3 = float(x_3)

    @property
    def y_3(self):
        return self.__y_3

    @y_3.setter
    def y_3(self, y_3):
        if not isinstance(y_3, (float, int)):
            raise TypeError(f'Координаты треугольника {self.__y_3} должны быть числом, a не {type(y_3).__name__}')
        if self.__y_3 <= 0:
            raise ValueError(f"Координаты треугольника {self.__y_3} должны быть быть больше либо равны нулю")

        self.__y_3 = float(y_3)

    def __repr__(self):
        return f"Triangle({self.__x_1, self.__y_1}, {self.__x_2, self.__y_2}, {self.__x_3, self.__y_3})"

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__x_1 == other.__x_1 and self.__y_1 == other.__y_1 and self.__x_2 == other.__x_2 \
            and self.__y_2 == other.__y_2 and self.__x_3 == other.__x_3 and self.__y_3 == other.__y_3

    def __hash__(self):
        return hash((self.__x_1, self.__y_1, self.__x_2, self.__y_2, self.__x_3, self.__y_3))

    def get_width(self):
        return get_side(self.__x_1, self.__x_2, self.__x_3)

    def get_height(self):
        return get_side(self.__y_1, self.__y_2, self.__y_3)

    def get_perimeter(self):
        ab_side_length = math.sqrt(math.pow(self.__x_2 - self.__x_1, 2) + math.pow(self.__y_2 - self.__y_1, 2))
        bc_side_length = math.sqrt(math.pow(self.__x_3 - self.__x_2, 2) + math.pow(self.__y_3 - self.__y_2, 2))
        ac_side_length = math.sqrt(math.pow(self.__x_3 - self.__x_1, 2) + math.pow(self.__y_3 - self.__y_1, 2))

        return ab_side_length + bc_side_length + ac_side_length

    def get_area(self):
        epsilon = 1.0e-10
        if abs((self.__x_3 - self.__x_1) * (self.__y_2 - self.__y_1) - (self.__y_3 - self.__y_1) * (
                self.__x_2 - self.__x_1)) <= epsilon:
            return 0

        return self.get_width() * (self.get_height() / 2)
