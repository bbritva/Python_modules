def checkList(values):
    return len(values) > 0 and isinstance(values[0], list) and \
        len(values[0]) > 0 and isinstance(values[0][0], float)


def checkShape(shape):
    return (shape[0] == 1 and shape[1] > 0) or (shape[0] > 0 and shape[1] == 1)


class Vector:
    def __init__(self, values):
        if isinstance(values, list):
            if checkList(values):
                self.values = values
            else:
                raise ValueError
        elif isinstance(values, int):
            if values < 0:
                raise ValueError
            self.values = []
            innerList = []
            for i in range(values):
                innerList.append(float(i))
            self.values.append(innerList)
        elif isinstance(values, tuple):
            if len(values) != 2 or values[0] > values[1]:
                raise ValueError
            self.values = []
            innerList = []
            for i in range(values[0], values[1]):
                innerList.append(float(i))
            self.values.append(innerList)
        self.shape = (len(self.values), len(self.values[0]))
        if not checkShape(self.shape):
            raise ValueError

    def dot(self, num):
        for line in self.values:
            for i in range(len(line)):
                line[i] *= num

    def T(self):
        newList = []
        if self.shape[1] == 1:
            for i in range(len(self.values[0])):
                newList.append([self.values[0][i],])
        else:
            innerList = []
            for i in range(len(self.values)):
                innerList.append([self.values[i][0]])
            newList.append(innerList)
        print(newList)
        return Vector(newList)

    # add & radd : only vectors of same shape.
    def __add__(self, other):
        if isinstance(other, Vector) and self.shape == other.shape:
            for i in range(len(self.values)):
                for j in range(len(self.values[i])):
                    self.values[i][j] += other.values[i][j]
        else:
            raise TypeError("wrong types")

    def __radd__(self, other):
        self.__add__(other)

    # sub & rsub : only vectors of same shape.
    def __sub__(self, other):
        if isinstance(other, Vector) and self.shape == other.shape:
            for i in range(len(self.values)):
                for j in range(len(self.values[i])):
                    self.values[i][j] -= other.values[i][j]
        else:
            raise TypeError("wrong types")

    def __rsub__(self, other):
        self.__sub__(other)

    # truediv : only with scalars (to perform division of Vector by a scalar).
    def __truediv__(self, num):
        if not isinstance(num, (int, float)):
            raise TypeError("wrong types")
        if num == 0:
            raise ZeroDivisionError
        for line in self.values:
            for i in range(len(line)):
                line[i] /= num

    def __rtruediv__(self, num):
        raise NotImplementedError(
            "Division of a scalar by a Vector is not defined here.")

    # mul & rmul: only scalars (to perform multiplication of Vector by a scalar).

    def __mul__(self, num):
        if not isinstance(num, (int, float)):
            raise TypeError("wrong types")
        for line in self.values:
            for i in range(len(line)):
                line[i] *= num

    def __rmul__(self, num):
        self.__mul__(num)

    def __repr__(self):
        return self.values.__str__()

    def __str__(self):
        return self.values.__str__()
