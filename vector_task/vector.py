class Vector:
    def __init__(self, size = None, components=None):
        if components is None:
            components = []
        components.append(size)

        self.__size = [components] * size
        self.__components = [components]

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
