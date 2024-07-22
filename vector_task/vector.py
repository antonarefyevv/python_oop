class Vector:
    def __init__(self, *args):
        component = args[0]
        if len(args) == 1:
            if isinstance(component, int):
                self.values = [0] * component
            elif isinstance(component, list):
                self.values = component
            elif isinstance(component, Vector):
                self.values = component.values
            else:
                raise ValueError("Неверный тип аргумента")
        else:
            self.values = args[1]
            list_length = len(args[1])
            if args[0] > list_length:
                difference = component - len(args[1])
                for i in range(difference):
                    self.values.append(0)

    # def __repr__(self):
    #     return f'{self.values}'

    def __repr__(self):
        return f"{{{', '.join(str(x) for x in self.values)}}}"

    def __iadd__(self, other):
        return

    def __len__(self):
        return len(self.values)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.values == other.values and self == other

    def __hash__(self):
        return hash(self.values)


    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Сложение возможно только с другим вектором")

        max_len = max(len(self.values), len(other.values))
        self.values.extend([0] * (max_len - len(self.values)))
        other.values.extend([0] * (max_len - len(other.values)))

        return Vector([x + y for x, y in zip(self.values, other.values)])

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Вычитание возможно только с другим вектором")

        max_len = max(len(self.values), len(other.values))
        self.values.extend([0] * (max_len - len(self.values)))
        other.values.extend([0] * (max_len - len(other.values)))

        return Vector([x - y for x, y in zip(self.values, other.values)])

    def __mul__(self, scalar):
        return Vector([x * scalar for x in self.values])



    def __rmul__(self, k):
        return list(map(lambda x: x * k, self.values))

    def __copy__(self):
        return Vector(*self.values)

    def insert(self, index, value):
        self.values[index] = value

    def reverse(self):
        return list(map(lambda x: x * -1, self.values))

    def vectors_multiply(self, other):
        return Vector(self.values, list(map(lambda x, y: x * y, self.values, other.values)))
