from copy import deepcopy

def _zero_guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return(func(*args, **kwargs))
        except ZeroDivisionError:
            print("ZeroDivisionError") 
            return None
    return wrapper


class Matrix:
    @staticmethod
    def isListOfLists(data):
        return isinstance(data, list) and \
            len(data[0]) > 0 and isinstance(data[0], list) and \
            not isinstance(data[0][0], list)

    @staticmethod
    def MMmultipy(first, second):
        newList = []
        for i in range(first.shape[0]):
            innerList = []
            for j in range(second.shape[1]):
                newEl = 0
                for k in range(first.shape[1]):
                    newEl += first.data[i][k] * second.data[k][j]
                innerList.append(newEl)
            newList.append(innerList)
        return newList

    @staticmethod
    def MSmultipy(first, second):
        newList = []
        for line in first.data:
            innerList = []
            for i in range(len(line)):
                innerList.append(line[i] * second)
            newList.append(innerList)
        return newList

    @staticmethod
    @_zero_guard_
    def MSdiv(matrix, num):
        newList = []
        for line in matrix.data:
            innerList = []
            for i in range(len(line)):
                innerList.append(line[i] / num)
            newList.append(innerList)
        return newList

    @staticmethod
    @_zero_guard_
    def SMdiv(matrix, num):
        newList = []
        for line in matrix.data:
            innerList = []
            for i in range(len(line)):
                innerList.append(num / line[i])
            newList.append(innerList)
        return newList

    @staticmethod
    def summ(first, second):
        newList = []
        for i in range(len(first.data)):
            innerList = []
            for j in range(len(first.data[i])):
                innerList.append(first.data[i][j] + second.data[i][j])
            newList.append(innerList)
        return newList

    @staticmethod
    def sub(first, second):
        newList = []
        for i in range(len(first.data)):
            innerList = []
            for j in range(len(first.data[i])):
                innerList.append(first.data[i][j] - second.data[i][j])
            newList.append(innerList)
        return newList

    @staticmethod
    def Tlist(matrix):
        newList = []
        for i in range(matrix.shape[1]):
            innerList = []
            for j in range(matrix.shape[0]):
                innerList.append(matrix.data[j][i])
            newList.append(innerList)
        return newList

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
        return Matrix(Matrix.Tlist(self))

    # add & radd : only Matrixs of same shape.
    def __add__(self, other):
        if isinstance(other, Matrix) and self.shape == other.shape:
            return Matrix(Matrix.summ(self, other))
        else:
            raise TypeError("wrong types")

    def __radd__(self, other):
        return self.__add__(other)

    # sub & rsub : only Matrixs of same shape.
    def __sub__(self, other):
        if isinstance(other, Matrix) and self.shape == other.shape:
            return Matrix(Matrix.sub(self, other))
        else:
            raise TypeError("wrong types")

    def __rsub__(self, other):
        return other.__sub__(self)

    # truediv : only with scalars (to perform division of Matrix by a scalar).
    def __truediv__(self, num):
        if not isinstance(num, (int, float)):
            raise TypeError("wrong types")
        if num == 0:
            raise ZeroDivisionError
        newList = Matrix.MSdiv(self, num)
        return Matrix(newList) if newList else None

    def __rtruediv__(self, num):
        """Warning: can raise DivisionByZeroException"""
        if not isinstance(num, (int, float)):
            raise TypeError("wrong types")
        newList = Matrix.SMdiv(self, num)
        return Matrix(newList) if newList else None

    # mul : scalars, vectors and matrices , can have errors with vectors and matrices,
    # returns a Vector if we perform Matrix * Vector mutliplication.

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix(Matrix.MSmultipy(self, other))
        elif isinstance(other, (Matrix, Vector)):
            if self.shape[1] == other.shape[0]:
                return Matrix(Matrix.MMmultipy(self, other))

    def __rmul__(self, other):
        return other.__mul__(self)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        line = 'Matrix([' + ', '.join(self.data[k].__str__()
                                      for k in range(self.shape[0])) + '])'
        return line


class Vector(Matrix):
    @staticmethod
    def isRowOrColumn(data):
        return isinstance(data, list) and \
            len(data[0]) > 0 and isinstance(data[0], list) and \
            (len(data) == 1 or len(data[0]) == 1)

    def __init__(self, data):
        if isinstance(data, Matrix):
            if data.shape[0] == 1 or data.shape[1] == 1:
                self.data = deepcopy(data.data)
                self.shape = data.shape
            else:
                raise ValueError
        elif Vector.isRowOrColumn(data):
            self.data = deepcopy(data)
            self.shape = (len(data), len(data[0]))
        else:
            raise ValueError

    def __str__(self):
        line = 'Vector([' + ', '.join(self.data[k].__str__()
                                      for k in range(self.shape[0])) + '])'
        return line

    # add & radd : only Vectors of same shape.
    def __add__(self, other):
        if isinstance(other, Vector) and self.shape == other.shape:
            return Vector(Matrix.summ(self, other))
        else:
            raise TypeError("wrong types")

    def __radd__(self, other):
        return self.__add__(other)

    # sub & rsub : only Vectors of same shape.
    def __sub__(self, other):
        if isinstance(other, Vector) and self.shape == other.shape:
            return Vector(Matrix.sub(self, other))
        else:
            raise TypeError("wrong types")

    def __rsub__(self, other):
        return other.__sub__(self)

    # truediv : only with scalars (to perform division of Vector by a scalar).
    def __truediv__(self, num):
        if not isinstance(num, (int, float)):
            raise TypeError("wrong types")
        if num == 0:
            raise ZeroDivisionError
        newList = Matrix.MSdiv(self, num)
        return Matrix(newList) if newList else None

    def __rtruediv__(self, num):
        """Warning: can raise DivisionByZeroException"""
        if not isinstance(num, (int, float)):
            raise TypeError("wrong types")
        newList = Matrix.SMdiv(self, num)
        return Matrix(newList) if newList else None

    # mul : scalars, vectors and matrices , can have errors with vectors and matrices,
    # returns a Vector if we perform Matrix * Vector mutliplication.

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(Matrix.MSmultipy(self, other))
        elif isinstance(other, (Matrix, Vector)):
            if self.shape[1] == other.shape[0]:
                return Vector(Matrix.MMmultipy(self, other))

    def __rmul__(self, other):
        return other.__mul__(self)

    def T(self):
        return Vector(Matrix.Tlist(self))

    def dot(self, other):
        if isinstance(other, Vector) and self.shape == other.shape:
            result = 0
            for i in range(len(self.values)):
                for j in range(len(self.values[i])):
                    result += self.values[i][j] * other.values[i][j]
            return result
        else:
            raise TypeError("wrong types")
