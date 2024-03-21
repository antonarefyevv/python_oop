class Range:
    def __init__(self, start: float, end: float):
        if not isinstance(start, (float, int)):
            raise TypeError(f'Начало диапазона должно быть числом, а не {type(start).__name__}')

        if not isinstance(end, (float, int)):
            raise TypeError(f'Конец диапазона должен быть числом, а не {type(end).__name__}')

        if start >= end:
            raise ValueError(f"Начало диапазона ({start}) должно быть меньше конца ({end})")

        self.__start = float(start)
        self.__end = float(end)

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start):
        if not isinstance(start, (float, int)):
            raise TypeError(f'Начало диапазона должно быть числом, а не {type(start).__name__}')

        if start >= self.__end:
            raise ValueError(f"Начало диапазона {self.__start} должно быть меньше конца {self.__end}")

        self.__start = float(start)

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end):
        if not isinstance(end, (float, int)):
            raise TypeError(f'Конец диапазона должен быть числом, а не {type(end).__name__}')

        if self.__start >= end:
            raise ValueError(f"Начало диапазона {self.__start} должно быть меньше конца {self.__end}")

        self.__end = float(end)

    def __repr__(self):
        return f"({self.__start!r}; {self.__end!r})"

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.__start == other.__end and self.__end == other.__end

    def get_length(self):
        return self.__end - self.__start

    def is_inside(self, number):
        return self.__start <= number <= self.__end

    def get_intersection(self, other):
        if self.__end <= other.__start or self.__start >= other.__end:
            return None

        result_start = max(self.__start, other.__start)
        result_end = min(self.__end, other.__end)
        return Range(result_start, result_end)

    def get_union(self, other):
        if self.__end < other.__start or other.__end < self.__start:
            return [Range(self.__start, self.__end), Range(other.__start, other.__end)]

        result_start = min(self.__start, other.__start)
        result_end = max(self.__end, other.__end)
        return Range(result_start, result_end)

    def get_difference(self, other):
        if (self.__start >= other.__start and self.__end <= other.__end) or self.__end < other.__start:
            return []
        elif self.__end >= other.__end:
            return [Range(self.__start, other.__start), Range(other.__start, other.__end)]

        result_start = min(self.__start, other.__start)
        return Range(result_start, other.__start)
