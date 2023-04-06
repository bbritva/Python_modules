class Vector:
    def __init__(self, values):
        if isinstance(values, list):
            self.values = values
        elif isinstance(values, int):
            self.values = []
            innerList = []
            for i in range(values):
                innerList.append(float(i))
            self.values.append(innerList)
        elif isinstance(values, tuple):
            self.values = []
            innerList = []
            for i in range(values[0], values[1]):
                innerList.append(float(i))
            self.values.append(innerList)
        self.shape = (len(self.values), len(self.values[0]))

    def __str__(self):
        return self.values.__str__()

