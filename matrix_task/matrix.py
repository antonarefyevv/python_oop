from vector_task.vector import Vector


class Matrix:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, vector):
        if vector is None:
            vector = []
        for component in range(len(vector)):
            if not isinstance(vector[component], (float, int)):
                raise TypeError(
                    f'Параметры вектора должны быть числом, а не {type(vector[component]).__name__}.')

        self.__x = vector

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, vector):
        if vector is None:
            vector = []
        for component in range(len(vector)):
            if not isinstance(vector[component], (float, int)):
                raise TypeError(
                    f'Параметры вектора должны быть числом, а не {type(vector[component]).__name__}.')

        self.__y = vector

