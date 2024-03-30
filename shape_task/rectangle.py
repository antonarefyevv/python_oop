from shape_task.shape import Shape


class Rectangle(Shape):
    def __init__(self, side_length, side_width):
        if not isinstance(side_length, (float, int)):
            raise TypeError(f'Длина стороны прямоугольника должна быть числом, а не {type(side_length).__name__}')
        if not isinstance(side_width, (float, int)):
            raise TypeError(f'Ширина стороны прямоугольника должна быть числом, а не {type(side_length).__name__}')
        if side_length <= 0:
            raise ValueError('Длина стороны прямоугольника должна быть больше нуля')
        if side_width <= 0:
            raise ValueError('Ширина стороны прямоугольника должна быть больше нуля')

        self.__side_length = side_length
        self.__side_width = side_width

    @property
    def side_length(self):
        return self.__side_length

    @side_length.setter
    def side_length(self, side_length):
        if not isinstance(side_length, (float, int)):
            raise TypeError(f'Длина стороны прямоугольника должна быть числом, а не {type(side_length).__name__}')
        if self.__side_length <= 0:
            raise ValueError(f"Длина стороны прямоугольника {self.__side_length} должна быть больше нуля")

        self.__side_length = float(side_length)

    @property
    def side_width(self):
        return self.__side_width

    @side_width.setter
    def side_width(self, side_width):
        if not isinstance(side_width, (float, int)):
            raise TypeError(f'Ширина стороны прямоугольника должна быть числом, а не {type(side_width).__name__}')
        if self.__side_width <= 0:
            raise ValueError(f"Ширина стороны прямоугольника {self.__side_width} должна быть больше нуля")

        self.__side_width = float(side_width)

    def __repr__(self):
        return f"Rectangle({self.__side_width}, {self.__side_length})"

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__side_length == other.__side_length and self.__side_width == other.__side_width

    def __hash__(self):
        return hash((self.__side_length, self.__side_width))

    def get_width(self):
        return self.__side_width

    def get_height(self):
        return self.__side_length

    def get_area(self):
        return self.__side_length * self.__side_width

    def get_perimeter(self):
        return 2 * self.__side_length + 2 * self.__side_width
