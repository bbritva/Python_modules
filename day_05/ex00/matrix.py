class Matrix:
    def __init__(self, data, shape) -> None:
        self.data = data
        self.shape = data.shape()
        
def isListOfLists(data):
    return isinstance(data, list) and \
        len(data[0]) > 0 and isinstance(data[0], list)


def checkShape(shape):
    return (shape[0] == 1 and shape[1] > 0) or (shape[0] > 0 and shape[1] == 1)


class Matrix:
    def __init__(self, data):
        if isListOfLists(data):
            self.data = data
            self.shape = (len(data), len(data[0]))
        elif isinstance(data, tuple) and len(data) == 2 and data[0] > 0 and data[1] >= 0:
            self.data = []
            for i in range(data[0]):
                innerList = []
                for j in range(data[1]):
                    innerList.append(0)
                self.data.append(innerList)
        else:
            raise ValueError

    def dot(self, other):
        if isinstance(other, Matrix) and self.shape == other.shape:
            result = 0
            for i in range(len(self.data)):
                for j in range(len(self.data[i])):
                    result += self.data[i][j] * other.data[i][j]
            return result
        else:
            raise TypeError("wrong types")

    def T(self):
        newList = []
        if self.shape[0] == 1:
            for i in range(len(self.data[0])):
                newList.append([self.data[0][i],])
        else:
            innerList = []
            for line in self.data:
                innerList.append(line[0])
            newList.append(innerList)
        return Matrix(newList)

    # add & radd : only Matrixs of same shape.
    def __add__(self, other):
        if isinstance(other, Matrix) and self.shape == other.shape:
            newList = []
            for i in range(len(self.data)):
                innerList = []
                for j in range(len(self.data[i])):
                    innerList.append(self.data[i][j] + other.data[i][j])
                newList.append(innerList)
            return Matrix(newList)
        else:
            raise TypeError("wrong types")

    def __radd__(self, other):
        return self.__add__(other)

    # sub & rsub : only Matrixs of same shape.
    def __sub__(self, other):
        if isinstance(other, Matrix) and self.shape == other.shape:
            newList = []
            for i in range(len(self.data)):
                innerList = []
                for j in range(len(self.data[i])):
                    innerList.append(self.data[i][j] - other.data[i][j])
                newList.append(innerList)
            return Matrix(newList)
        else:
            raise TypeError("wrong types")

    def __rsub__(self, other):
        return self.__sub__(other)

    # truediv : only with scalars (to perform division of Matrix by a scalar).
    def __truediv__(self, num):
        if not isinstance(num, (int, float)):
            raise TypeError("wrong types")
        if num == 0:
            raise ZeroDivisionError
        newList = []
        for line in self.data:
            innerList = []
            for i in range(len(line)):
                innerList.append(line[i] / num)
            newList.append(innerList)
        return Matrix(newList)

    def __rtruediv__(self, num):
        raise NotImplementedError(
            "Division of a scalar by a Matrix is not defined here.")

    # mul & rmul: only scalars (to perform multiplication of Matrix by a scalar).

    def __mul__(self, num):
        if not isinstance(num, (int, float)):
            raise TypeError("wrong types")
        newList = []
        for line in self.data:
            innerList = []
            for i in range(len(line)):
                innerList.append(line[i] * num)
            newList.append(innerList)
        return Matrix(newList)

    def __rmul__(self, num):
        return self.__mul__(num)

    def __repr__(self):
        return self.data.__str__()

    def __str__(self):
        return self.data.__str__()
