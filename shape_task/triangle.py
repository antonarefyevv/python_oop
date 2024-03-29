from shape_task.shape import Shape
import math


class Triangle(Shape):

    def __init__(self, x_1, y_1, x_2, y_2, x_3, y_3):
        arg_list = [x_1, y_1, x_2, y_2, x_3, y_3]
        for arg in range(len(arg_list)):
            if not isinstance(arg_list[arg], (float, int)):
                raise TypeError(f'Координаты треугольника должны быть числом, a не {type(arg_list[arg]).__name__}')
            if arg_list[arg] < 0:
                raise ValueError ('Координаты треугольника должны быть быть больше нуля')

        self.__x_1 = x_1
        self.__y_1 = y_1
        self.__x_2 = x_2
        self.__y_2 = y_2
        self.__x_3 = x_3
        self.__y_3 = y_3

    def __repr__(self):
        return f"Triangle({self.__x_1, self.__y_1}, {self.__x_2, self.__y_2}, {self.__x_3, self.__y_3})"

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__x_1 == other.__x_1 and self.__y_1 == other.__y_1 and self.__x_2 == other.__x_2 and self.__y_2 == \
            other.__y_2 and self.__x_3 == other.__x_3 and self.__y_3 == other.__y_3

    def __hash__(self):
        return hash((self.__x_1, self.__y_1,self.__x_2, self.__y_2, self.__x_3, self.__y_3))

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
