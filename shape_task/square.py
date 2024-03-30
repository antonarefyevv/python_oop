from shape_task.shape import Shape


class Square(Shape):
    def __init__(self, side_length):
        if not isinstance(side_length, (float, int)):
            raise TypeError(f'Длина стороны квадрата должна быть числом, а не {type(side_length).__name__}')
        if side_length <= 0:
            raise ValueError('Длина стороны квадрата должна быть больше нуля')

        self.__side_length = side_length

    @property
    def side_length(self):
        return self.__side_length

    @side_length.setter
    def side_length(self, side_length):
        if not isinstance(side_length, (float, int)):
            raise TypeError(f'Длина стороны квадрата должна быть числом, а не {type(side_length).__name__}')

        if self.__side_length <= 0:
            raise ValueError(f"Длина стороны квадрата {self.__side_length} должна быть больше нуля")

        self.__side_length = float(side_length)

    def __repr__(self):
        return f"Square({self.__side_length})"

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__side_length == other.__side_length

    def __hash__(self):
        return hash(self.__side_length)

    def get_height(self):
        return self.__side_length

    def get_width(self):
        return self.__side_length

    def get_area(self):
        return self.__side_length * self.__side_length

    def get_perimeter(self):
        return self.__side_length * 4
