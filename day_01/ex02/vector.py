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
            for i in range(values):
               self.values.append([float(i),])
        elif isinstance(values, tuple):
            if len(values) != 2 or \
                not isinstance(values[0], int) or \
                not isinstance(values[1], int) or \
                    values[0] >= values[1]:
                raise ValueError
            self.values = []
            for i in range(values[0], values[1]):
                self.values.append([float(i),])
        self.shape = (len(self.values), len(self.values[0]))
        if not checkShape(self.shape):
            raise ValueError

    def dot(self, other):
        if isinstance(other, Vector) and self.shape == other.shape:
            result = 0
            for i in range(len(self.values)):
                for j in range(len(self.values[i])):
                    result += self.values[i][j] * other.values[i][j]
            return result
        else:
            raise TypeError("wrong types")

    def T(self):
        newList = []
        if self.shape[0] == 1:
            for i in range(len(self.values[0])):
                newList.append([self.values[0][i],])
        else:
            innerList = []
            for line in self.values:
                innerList.append(line[0])
            newList.append(innerList)
        return Vector(newList)

    # add & radd : only vectors of same shape.
    def __add__(self, other):
        if isinstance(other, Vector) and self.shape == other.shape:
            newList = []
            for i in range(len(self.values)):
                innerList = []
                for j in range(len(self.values[i])):
                    innerList.append(self.values[i][j] + other.values[i][j])
                newList.append(innerList)
            return Vector(newList)
        else:
            raise TypeError("wrong types")

    def __radd__(self, other):
        return self.__add__(other)

    # sub & rsub : only vectors of same shape.
    def __sub__(self, other):
        if isinstance(other, Vector) and self.shape == other.shape:
            newList = []
            for i in range(len(self.values)):
                innerList = []
                for j in range(len(self.values[i])):
                    innerList.append(self.values[i][j] - other.values[i][j])
                newList.append(innerList)
            return Vector(newList)
        else:
            raise TypeError("wrong types")

    def __rsub__(self, other):
        return self.__sub__(other)

    # truediv : only with scalars (to perform division of Vector by a scalar).
    def __truediv__(self, num):
        if not isinstance(num, (int, float)):
            raise TypeError("wrong types")
        if num == 0:
            raise ZeroDivisionError
        newList = []
        for line in self.values:
            innerList = []
            for i in range(len(line)):
                innerList.append(line[i] / num)
            newList.append(innerList)
        return Vector(newList)

    def __rtruediv__(self, num):
        raise NotImplementedError(
            "Division of a scalar by a Vector is not defined here.")

    # mul & rmul: only scalars (to perform multiplication of Vector by a scalar).

    def __mul__(self, num):
        if not isinstance(num, (int, float)):
            raise TypeError("wrong types")
        newList = []
        for line in self.values:
            innerList = []
            for i in range(len(line)):
                innerList.append(line[i] * num)
            newList.append(innerList)
        return Vector(newList)

    def __rmul__(self, num):
        return self.__mul__(num)

    def __repr__(self):
        return self.values.__str__()

    def __str__(self):
        return self.values.__str__()
