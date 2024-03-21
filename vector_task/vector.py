# class Vector:
#     def __init__(self, size=None, components=None):
#         self.__size = [0] * size
#         self.__components = [components]
#
#     def __repr__(self):
#         return f"Vector({self.__size!r})"
#
#     def __iadd__(self, other):
#             return


class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @staticmethod
    def __operate(f, u, v):
        return Vector(*f(u, v))

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __add__(self, other):
        return Vector.__operate(lambda u, v: (u.x + v.x, u.y + v.y), self, other)

    def __sub__(self, other):
        return Vector.__operate(lambda u, v: (u.x - v.x, u.y - v.y), self, other)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __rmul__(self, k):
        return Vector(k * self.x, k * self.y)



