class Range:
    def __init__(self, start: float, end: float):
        if isinstance(start, str):
            raise TypeError(f'Начало диапазона должно быть числом, а не {type(start).__name__}')

        if isinstance(end, str):
            raise TypeError(f'Конец диапазона должен быть числом, а не {type(end).__name__}')

        if start >= end:
            raise ValueError("Начало диапазона должно быть меньше конца")

        self.__start = float(start)
        self.__end = float(end)

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start):
        if isinstance(start, str):
            raise TypeError(f'Начало диапазона должно быть числом, а не {type(start).__name__}')

        if start >= self.__end:
            raise ValueError("Начало диапазона должно быть меньше конца")

        self.__start = float(start)

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end):
        if isinstance(end, str):
            raise TypeError(f'Конец диапазона должен быть числом, а не {type(end).__name__}')

        if self.__start >= end:
            raise ValueError("Начало диапазона должно быть меньше конца")

        self.__end = float(end)
    def __repr__(self):
        return f"Range({self.__start!r}; {self.__end!r})"

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.__start == other.__end and self.__end == other.__end

    def __lt__(self, other):
        return self.__start > other.__start

    def get_length(self):
        return self.__end - self.__start

    def is_inside(self, number):
        return self.__start <= number <= self.__end

    def get_intersection(self, other):
        self_start = self.__start
        self_end = self.__end
        other_start = other.__start
        other_end = other.__end
        new_range_1 = Range(self_start, self_end)
        new_range_2 = Range(other_start, other_end)

        if self_end <= other_start or self_start >= other_end:
            return f'Результат пересечения диапазонов {new_range_1}, {new_range_2}' \
                   f' = {None}'

        result_start = max(self_start, other_start)
        result_end = min(self_end, other_end)
        new_range = Range(result_start, result_end)
        return f'Результат пересечения диапазонов {new_range_1}, {new_range_2}' \
               f' = {new_range}'

    def get_union(self, other):
        self_start = float(self.__start)
        self_end = self.__end
        other_start = other.__start
        other_end = other.__end
        new_range_1 = Range(self_start, self_end)
        new_range_2 = Range(other_start, other_end)

        if self_end < other_start or other_end < self_start:
            return f'Результат объединения диапазонов {new_range_1}, {new_range_2}' \
                   f' = [{new_range_1}, {new_range_2}]'

        result_start = min(self_start, other_start)
        result_end = max(self_end, other_end)
        new_range = Range(result_start, result_end)
        return f'Результат объединения диапазонов {Range(self_start, self_end)}, {Range(other_start, other_end)}' \
               f' = {new_range}'

    def get_difference(self, other):
        self_start = self.__start
        self_end = self.__end
        other_start = other.__start
        other_end = other.__end
        new_range_1 = Range(self_start, self_end)
        new_range_2 = Range(other_start, other_end)

        if self_end > other_start:
            return f'Результат вычитания диапазонов {new_range_1}, {new_range_2} = {[Range(self_start, other_start), Range(self_end, other_end)]}'

        if self_end > other_end:
            return f'Результат вычитания диапазонов {new_range_1}, {new_range_2} = {Range(other_end, self_end)}'

        return f'Результат вычитания диапазонов {new_range_1}, {new_range_2}' \
               f' = {None}'
