import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def data_spliter(x, y, proportion):
    """Shuffles and splits the dataset (given by x and y) into a training and a test set,
    while respecting the given proportion of examples to be kept in the training set.
    Args:
    x: has to be an numpy.array, a matrix of dimension m * n.
    y: has to be an numpy.array, a vector of dimension m * 1.
    proportion: has to be a float, the proportion of the dataset that will be assigned to the
    training set.
    Return:
    (x_train, x_test, y_train, y_test) as a tuple of numpy.array
    None if x or y is an empty numpy.array.
    None if x and y do not share compatible dimensions.
    None if x, y or proportion is not of expected type.
    Raises:
    This function should not raise any Exception.
    """
    try:
        res = np.c_[x, y]
        np.random.shuffle(res)
        limit = int(proportion * x.shape[0])
        return res[:limit,:-1], res[limit:,:-1], res[:limit,-1:], res[limit:,-1:]
    except:
        return None

x1 = np.array([1, 42, 300, 10, 59]).reshape((-1, 1))
y = np.array([0, 1, 0, 1, 0]).reshape((-1, 1))
# Example 1:
print(data_spliter(x1, y, 0.8))
# Output:
# (array([ 1, 59, 42, 300]), array([10]), array([0, 0, 1, 0]), array([1]))
# Example 2:
print(data_spliter(x1, y, 0.5))
# Output:
# (array([59, 10]), array([ 1, 300, 42]), array([0, 1]), array([0, 0, 1]))
x2 = np.array([[ 1, 42],
[300, 10],
[ 59, 1],
[300, 59],
[ 10, 42]])
y = np.array([0, 1, 0, 1, 0]).reshape((-1, 1))
# Example 3:
print(data_spliter(x2, y, 0.8))
# Output:
# (array([[ 10, 42],
# [300, 59],
# [ 59, 1],
# [300, 10]]),
# array([[ 1, 42]]),
# array([0, 1, 0, 1]),
# array([0]))
# Example 4:
print(data_spliter(x2, y, 0.5))
# Output:
# (array([[59, 1],
# [10, 42]]),
# array([[300, 10],
# [300, 59],
# [ 1, 42]]),
# array([0, 0]),
# array([1, 1, 0]))