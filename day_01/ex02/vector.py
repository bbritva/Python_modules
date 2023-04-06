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

    def __str__(self):
        return self.values.__str__()

