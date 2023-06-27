import numpy as np


def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e)
            return None
    return wrapper


@_guard_
def reg_linear_grad(y, x, theta, lambda_):
    """Computes the regularized linear gradient of three non-empty numpy.ndarray,
    with two for-loop. The three arrays must have compatible shapes.
    Args:
    y: has to be a numpy.ndarray, a vector of shape m * 1.
    x: has to be a numpy.ndarray, a matrix of dimesion m * n.
    theta: has to be a numpy.ndarray, a vector of shape (n + 1) * 1.
    lambda_: has to be a float.
    Return:
    A numpy.ndarray, a vector of shape (n + 1) * 1, containing the results of the formula for all j.
    None if y, x, or theta are empty numpy.ndarray.
    None if y, x or theta does not share compatibles shapes.
    None if y, x or theta or lambda_ is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """
    res = np.zeros(theta.shape)
    y_hat = np.c_[np.ones(x.shape[0]), x].dot(theta)
    for i in range(x.shape[0]):
        diff = y_hat[i][0] - y[i][0]
        res[0][0] += diff
        for j in range(x.shape[1]):
            res[j + 1][0] += (diff * x[i][j]) + (lambda_ * theta[j + 1][0]) / x.shape[0]
    return res / x.shape[0]

@_guard_
def vec_reg_linear_grad(y, x, theta, lambda_):
    """Computes the regularized linear gradient of three non-empty numpy.ndarray,
    without any for-loop. The three arrays must have compatible shapes.
    Args:
    y: has to be a numpy.ndarray, a vector of shape m * 1.
    x: has to be a numpy.ndarray, a matrix of dimesion m * n.
    theta: has to be a numpy.ndarray, a vector of shape (n + 1) * 1.
    lambda_: has to be a float.
    Return:
    A numpy.ndarray, a vector of shape (n + 1) * 1, containing the results of the formula for all j.
    None if y, x, or theta are empty numpy.ndarray.
    None if y, x or theta does not share compatibles shapes.
    None if y, x or theta or lambda_ is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """
    theta_ = np.zeros(theta.shape)
    theta_[1:] = theta[1:]
    x_ = np.c_[np.ones(x.shape[0]), x]
    res = x_.T.dot(x_.dot(theta) - y) + lambda_ * theta_
    return res / x.shape[0]


if __name__ == "__main__":
    x = np.array([
    [ -6, -7, -9],
    [ 13, -2, 14],
    [ -7, 14, -1],
    [ -8, -4, 6],
    [ -5, -9, 6],
    [ 1, -5, 11],
    [ 9, -11, 8]])
    y = np.array([[2], [14], [-13], [5], [12], [4], [-19]])
    theta = np.array([[7.01], [3], [10.5], [-6]])
    # Example 1.1:
    print(reg_linear_grad(y, x, theta, 1))
    # Output:
    # array([[ -60.99 ],
    # [-195.64714286],
    # [ 863.46571429],
    # [-644.52142857]])
    # Example 1.2:
    print(vec_reg_linear_grad(y, x, theta, 1))
    # Output:
    # array([[ -60.99 ],
    # [-195.64714286],
    # [ 863.46571429],
    # [-644.52142857]])
    # Example 2.1:
    print(reg_linear_grad(y, x, theta, 0.5))
    # # Output:
    # # array([[ -60.99 ],
    # # [-195.86142857],
    # # [ 862.71571429],
    # # [-644.09285714]])
    # # Example 2.2:
    print(vec_reg_linear_grad(y, x, theta, 0.5))
    # # Output:
    # # array([[ -60.99 ],
    # # [-195.86142857],
    # # [ 862.71571429],
    # # [-644.09285714]])
    # # Example 3.1:
    print(reg_linear_grad(y, x, theta, 0.0))
    # # Output:
    # # array([[ -60.99 ],
    # # [-196.07571429],
    # # [ 861.96571429],
    # # [-643.66428571]])
    # # Example 3.2:
    print(vec_reg_linear_grad(y, x, theta, 0.0))
    # # Output:
    # # array([[ -60.99 ],
    # # [-196.07571429],
    # # [ 861.96571429],
    # # [-643.66428571]])