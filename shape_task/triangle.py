from shape_task.shape import Shape
import math


class Triangle(Shape):

    def __init__(self, x_1, y_1, x_2, y_2, x_3, y_3):
        if not isinstance(x_1,x_2: float, float) or not isinstance(x_1, int):
            raise TypeError(f'Длина стороны прямоугольника должна быть числом, а не {type(side_length).__name__}')


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
        return hash(self)

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
