from shapes_task.shape import Shape


class Square(Shape):
    def __init__(self, length):
        self.__length = None
        self.length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(f'Длина квадрата должна быть числом, а не {type(value).__name__}.')

        if value <= 0:
            raise ValueError(f"Длина квадрата должна быть больше нуля.")

        self.__length = float(value)

    def __repr__(self):
        return f"Square({self.__length})"

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__length == other.__length

    def __hash__(self):
        return hash(self.__length)

    def get_height(self):
        return self.__length

    def get_width(self):
        return self.__length

    def get_area(self):
        return self.__length * self.__length

    def get_perimeter(self):
        return self.length * 4
