import numpy as np


def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except:
            return None
    return wrapper


@_guard_
def predict(x, theta):
    width = x.shape[0]
    return np.c_[np.ones(width), x].dot(theta)


@_guard_
def simple_gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.array, with a for-loop.
    The three arrays must have compatible shapes.
    Args:
    x: has to be an numpy.array, a vector of shape m * 1.
    y: has to be an numpy.array, a vector of shape m * 1.
    theta: has to be an numpy.array, a 2 * 1 vector.
    Return:
    The gradient as a numpy.array, a vector of shape 2 * 1.
    None if x, y, or theta are empty numpy.array.
    None if x, y and theta do not have compatible shapes.
    None if x, y or theta is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """
    x_ = (np.c_[np.ones(x.shape[0]), x])
    return x_.T.dot(x_.dot(theta) - y) / y.shape[0]


@_guard_
def fit_(x, y, theta, alpha, max_iter):
    """
    Description:
    Fits the model to the training dataset contained in x and y.
    Args:
    x: has to be a numpy.ndarray, a vector of dimension m * 1: (number of training examples, 1).
    y: has to be a numpy.ndarray, a vector of dimension m * 1: (number of training examples, 1).
    theta: has to be a numpy.ndarray, a vector of dimension 2 * 1.
    alpha: has to be a float, the learning rate
    max_iter: has to be an int, the number of iterations done during the gradient descent
    Returns:
    new_theta: numpy.ndarray, a vector of dimension 2 * 1.
    None if there is a matching dimension problem.
    Raises:
    This function should not raise any Exception.
    """
    for i in range(max_iter):
        theta = theta - alpha * simple_gradient(x, y, theta)
    return theta


x = np.array([[12.4956442], [21.5007972], [
             31.5527382], [48.9145838], [57.5088733]])
y = np.array([[37.4013816], [36.1473236], [
             45.7655287], [46.6793434], [59.5585554]])
theta = np.array([1, 1]).reshape((-1, 1))
# Example 0:
theta1 = fit_(x, y, theta, alpha=5e-8, max_iter=1500000)
print(theta1)
# Output:
# array([[1.40709365],
# [1.1150909 ]])
# Example 1:
print(predict(x, theta1))
# # Output:
# array([[15.3408728 ],
# [25.38243697],
# [36.59126492],
# [55.95130097],
# [65.53471499]])
