import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print("Error:", func.__name__, e)
            return None
    return wrapper


@_guard_
def add_polynomial_features(x, power):
    """Add polynomial features to vector x by raising its values up to the power given in argument.
    Args:
    x: has to be an numpy.array, a vector of dimension m * 1.
    power: has to be an int, the power up to which the components of vector x are going to be raised.
    Return:
    The matrix of polynomial features as a numpy.array, of dimension m * n,
    containing the polynomial feature values for all training examples.
    None if x is an empty numpy.array.
    None if x or power is not of expected type.
    Raises:
    This function should not raise any Exception.
    """
    res = x.copy()
    for i in range(1, power):
        res = np.c_[res, x ** (i + 1)]
    return res

x = np.arange(1,6).reshape(-1, 1)
# Example 0:
print(add_polynomial_features(x, 3))
# Output:
# array([[ 1, 1, 1],
# [ 2, 4, 8],
# [ 3, 9, 27],
# [ 4, 16, 64],
# [ 5, 25, 125]])
# Example 1:
print(add_polynomial_features(x, 6))
# Output:
# array([[ 1, 1, 1, 1, 1, 1],
# [ 2, 4, 8, 16, 32, 64],
# [ 3, 9, 27, 81, 243, 729],
# [ 4, 16, 64, 256, 1024, 4096],
# [ 5, 25, 125, 625, 3125, 15625]])