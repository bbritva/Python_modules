import numpy as np

def add_intercept(x):
    """Adds a column of 1's to the non-empty numpy.array x.
    Args:
    x: has to be a numpy.array of dimension m * n.
    Returns:
    X, a numpy.array of dimension m * (n + 1).
    None if x is not a numpy.array.
    None if x is an empty numpy.array.
    Raises:
    This function should not raise any Exception.
    """
    width = x.shape[0]
    return np.c_[np.ones(width), x ]

x = np.arange(1,6)
print(repr(add_intercept(x)))
# Output:
# array([[1., 1.],
# [1., 2.],
# [1., 3.],
# [1., 4.],
# [1., 5.]])
# Example 2:
y = np.arange(1,10).reshape((3,3))
print(repr(add_intercept(y)))
# Output:
# array([[1., 1., 2., 3.],
# [1., 4., 5., 6.],
# [1., 7., 8., 9.]])