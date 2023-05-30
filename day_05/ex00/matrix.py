from copy import deepcopy


class Matrix:
    @staticmethod
    def isListOfLists(data):
        return isinstance(data, list) and \
            len(data[0]) > 0 and isinstance(data[0], list)
    
    @staticmethod
    def MMmutipy(first, other):
        newList = []
        m = first.shape[0]
        n = first.shape[1]
        p = other.shape[1]
        for i in range(m):
            innerList = []
            for j in range(p):
                newEl = 0
                for k in range(n):
                    newEl += first.data[i][k] * other.data[k][j]
                innerList.append(newEl)
            newList.append(innerList)
        return Matrix(newList)

    def __init__(self, data):
        if Matrix.isListOfLists(data):
            self.data = deepcopy(data)
            self.shape = (len(data), len(data[0]))
        elif isinstance(data, tuple) and len(data) == 2 and data[0] > 0 and data[1] >= 0:
            self.data = [[0] * data[1] for i in range(data[0])]
            self.shape = data
        else:
            raise ValueError

    def T(self):
        newList = []
        for i in range(self.shape[1]):
            innerList = []
            for j in range(self.shape[0]):
                innerList.append(self.data[j][i])
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
        """Warning: can raise DivisionByZeroException"""
        if not isinstance(num, (int, float)):
            raise TypeError("wrong types")
        newList = []
        for line in self.data:
            innerList = []
            for i in range(len(line)):
                innerList.append(num / line[i])
            newList.append(innerList)
        return Matrix(newList)

    # mul : scalars, vectors and matrices , can have errors with vectors and matrices,
    # returns a Vector if we perform Matrix * Vector mutliplication.

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            newList = []
            for line in self.data:
                innerList = []
                for i in range(len(line)):
                    innerList.append(line[i] * other)
                newList.append(innerList)
            return Matrix(newList)
        elif isinstance(other, Matrix):
            if self.shape[1] == other.shape[0]:
                return Matrix.MMmutipy(self, other)


    def __rmul__(self, num):
        return self.__mul__(num)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        line = '[' + ',\n '.join(self.data[k].__str__() for k in range(self.shape[0])) + ']'
        return line


if __name__ == "__main__":
    m = Matrix([[1.0, 2.0], [3.0, 4.0]])
    print(m)
    print(m.T())
    m1 = Matrix([[0.0, 1.0, 2.0, 3.0],
                [0.0, 2.0, 4.0, 6.0]])
    m2 = Matrix([[0.0, 1.0],
                [2.0, 3.0],
                [4.0, 5.0],
                [6.0, 7.0]])
    print(m1 * m2)

    m = Matrix([[1.0, 2.0, 3.0, 4.0]])
    print(m)
    print(m.T())