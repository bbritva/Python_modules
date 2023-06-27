import numpy as np
import math


def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e)
            return None
    return wrapper


@_guard_
def reg_logistic_grad(y, x, theta, lambda_):
    """Computes the regularized logistic gradient of three non-empty numpy.ndarray, with two for-loops. The three arrayArgs:
    y: has to be a numpy.ndarray, a vector of shape m * 1.
    x: has to be a numpy.ndarray, a matrix of dimesion m * n.
    theta: has to be a numpy.ndarray, a vector of shape n * 1.
    lambda_: has to be a float.
    Returns:
    A numpy.ndarray, a vector of shape n * 1, containing the results of the formula for all j.
    None if y, x, or theta are empty numpy.ndarray.
    None if y, x or theta does not share compatibles shapes.
    Raises:
    This function should not raise any Exception.
    """
    dj = np.zeros(theta.shape)
    x_ = np.c_[np.ones((x.shape[0])), x]
    y_hat = 1 / (1 + math.e ** -(x_.dot(theta)))
    for i in range(x.shape[0]):
        diff = y_hat[i] - y[i]
        dj[0][0] += diff
        for j in range(x.shape[1]):
            dj[j + 1][0] += diff * x[i][j] + lambda_ * theta[j + 1][0] / x.shape[0]
    return dj / x.shape[0]


@_guard_
def vec_reg_logistic_grad(y, x, theta, lambda_):
    """Computes the regularized logistic gradient of three non-empty numpy.ndarray, without any for-loop. The three arrArgs:
    y: has to be a numpy.ndarray, a vector of shape m * 1.
    x: has to be a numpy.ndarray, a matrix of shape m * n.
    theta: has to be a numpy.ndarray, a vector of shape n * 1.
    lambda_: has to be a float.
    Returns:
    A numpy.ndarray, a vector of shape n * 1, containing the results of the formula for all j.
    None if y, x, or theta are empty numpy.ndarray.
    None if y, x or theta does not share compatibles shapes.
    Raises:
    This function should not raise any Exception.
    """
    theta_ = np.zeros(theta.shape)
    theta_[1:] = theta[1:]
    x_ = np.c_[np.ones(x.shape[0]), x]
    y_hat = 1 / (1 + math.e ** -(x_.dot(theta)))
    return (x_.T.dot(y_hat - y) + + lambda_ * theta_)/ y.shape[0]



if __name__ == "__main__":
    x = np.array([[0, 2, 3, 4],
    [2, 4, 5, 5],
    [1, 3, 2, 7]])
    y = np.array([[0], [1], [1]])
    theta = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])
    print("Example 1.1:")
    print(reg_logistic_grad(y, x, theta, 1))
    # Output:
    # array([[-0.55711039],
    # [-1.40334809],
    # [-1.91756886],
    # [-2.56737958],
    # [-3.03924017]])
    print("Example 1.2:")
    print(vec_reg_logistic_grad(y, x, theta, 1))
    # Output:
    # array([[-0.55711039],
    # [-1.40334809],
    # [-1.91756886],
    # [-2.56737958],
    # [-3.03924017]])
    print("Example 2.1:")
    print(reg_logistic_grad(y, x, theta, 0.5))
    # Output:
    # array([[-0.55711039],
    # [-1.15334809],
    # [-1.96756886],
    # [-2.33404624],
    # [-3.15590684]])
    print("Example 2.2:")
    print(vec_reg_logistic_grad(y, x, theta, 0.5))
    # Output:
    # array([[-0.55711039],
    # [-1.15334809],
    # [-1.96756886],
    # [-2.33404624],
    # [-3.15590684]])
    print("Example 3.1:")
    print(reg_logistic_grad(y, x, theta, 0.0))
    # Output:
    # array([[-0.55711039],
    # [-0.90334809],
    # [-2.01756886],
    # [-2.10071291],
    # [-3.27257351]])
    print("Example 3.2:")
    print(vec_reg_logistic_grad(y, x, theta, 0.0))
    # Output:
    # array([[-0.55711039],
    # [-0.90334809],
    # [-2.01756886],
    # [-2.10071291],
    # [-3.27257351]])
