from shapes_task.shape import Shape


class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = None
        self.__width = None

        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(f'Длина прямоугольника должна быть числом, а не {type(value).__name__}.')

        if value <= 0:
            raise ValueError(f"Длина прямоугольника должна быть больше нуля.")

        self.__height = float(value)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(f'Ширина прямоугольника должна быть числом, а не {type(value).__name__}.')

        if value <= 0:
            raise ValueError(f"Ширина прямоугольника должна быть больше нуля.")

        self.__width = float(value)

    def __repr__(self):
        return f"Rectangle({self.__height}, {self.__width})"

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__height == other.__height and self.__width == other.__width

    def __hash__(self):
        return hash((self.__height, self.__width))

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_area(self):
        return self.__height * self.__width

    def get_perimeter(self):
        return 2 * (self.__height * self.__width)
