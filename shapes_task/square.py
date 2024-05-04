from shapes_task.shape import Shape


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    @property
    def side_length(self):
        return self.__side_length

    @side_length.setter
    def side_length(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(f'Длина стороны квадрата должна быть числом, а не {type(value).__name__}.')

        if value <= 0:
            raise ValueError(f"Длина стороны квадрата {value} должна быть больше нуля.")

        self.__side_length = float(value)

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
        return self.length * 4
