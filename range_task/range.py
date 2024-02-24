class Range:
    def __init__(self, start, end):
        if not isinstance(start, int):
            raise TypeError(f"Начало диапазона должно быть целым числом, а не {type(start).__name__}")

        if not isinstance(start, int):
            raise TypeError(f"Конец диапазона должен быть целым числом, а не {type(end).__name__}")

        self.__start = start
        self.__end = end

    def __repr__(self):
        return f"({self.__start};{self.__end})"

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start):
        self.__start = start

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end):
        self.__end = end

    def get_length(self):
        return self.__end - self.__start

    def is_inside(self, number):
        return self.__start <= number <= self.__end

    def get_intersection(self, numbers_range):
        items = []

        if self.__end <= numbers_range.__start:
            return None
        else:
            if self.__start > numbers_range.__start:
                items.append(self.__start)
            else:
                items.append(numbers_range.__start)

            if self.__end < numbers_range.__end:
                items.append(self.__end)
            else:
                items.append(numbers_range.__end)

        return items

    def get_union(self, numbers_range):
        items = []

        if self.__end < numbers_range.__start:
            items.append(self)
            items.append(numbers_range)
        else:
            if self.__start <= numbers_range.__start:
                items.append(self.__start)
            else:
                items.append(numbers_range.__start)

            if self.__end >= numbers_range.__end:
                items.append(self.__end)
            else:
                items.append(numbers_range.__end)

        return items

    def get_difference(self, numbers_range):
        items = []

        if self.__start != numbers_range.__start and self.__start != numbers_range.__end:
            items.append(self.__start)
        if self.__end != numbers_range.__end and self.__end != numbers_range.__start:
            items.append(self.__end)

        return items
