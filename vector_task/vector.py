class Vector:
    def __init__(self, items, size):
        self.__items = items
        self.__size = size



    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(f'Параметры вектора должны быть числом, а не {type(value).__name__}.')

        self.__size = float(value)

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(f'Параметры вектора должны быть числом, а не {type(value).__name__}.')

        self.__items = float(value)

    def __repr__(self):
        return f"Vector({self.__size!r})"

    def __iadd__(self, other):
        return

    def __len__(self):
        return self.__size

# def __operate(f, u, v):
#     return Vector(*f(u, v))
#
#
# def __str__(self):
#     return "(" + str(self.x) + "," + str(self.y) + ")"
#
#
# def __add__(self, other):
#     return Vector.__operate(lambda u, v: (u.x + v.x, u.y + v.y), self, other)
#
#
# def __sub__(self, other):
#     return Vector.__operate(lambda u, v: (u.x - v.x, u.y - v.y), self, other)
#
#
# def __mul__(self, other):
#     return self.x * other.x + self.y * other.y
#
#
# def __rmul__(self, k):
#     return Vector(k * self.x, k * self.y)
