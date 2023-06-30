import numpy as np
import time


def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper

class MyLinearRegression():
    """
    Description:
    My personnal linear regression class to fit like a boss.
    """
    @_guard_
    def __init__(self, theta, alpha=0.001, max_iter=1000):
        self.alpha = alpha
        self.max_iter = int(max_iter)
        self.theta = theta.astype(np.float64)

    @_guard_
    def predict_(self, x):
        return np.c_[np.ones(x.shape[0]), x].dot(self.theta)

    @_guard_
    def gradient(self, x, y):
        self.theta_[1:] = self.theta[1:]
        return self.x_.T.dot(self.x_.dot(self.theta) - y) / y.shape[0]

    @_guard_
    def fit_(self, x, y):
        start = time.time()
        cycles = int(self.max_iter / 20)
        self.x_ = (np.c_[np.ones(x.shape[0]), x])
        print("\r%3d%%, time =%5.2fs" % (0, 0), end="")
        for j in range(20):
            for i in range(cycles):
                self.theta -= self.alpha * self.gradient(x, y)
            now = time.time() - start
            print("\r%3d%%, time =%6.2fs" % ((j + 1) * 5, now), end="")
            # print(self.theta)
        print("")
        return self.theta

    @_guard_
    def loss_(self, y, y_hat):
        return float((y_hat - y).T.dot((y_hat - y))) / (2 * y.shape[0])

    @_guard_
    def loss_elem_(self, y, y_hat):
        return (y - y_hat) ** 2

    @staticmethod
    @_guard_
    def mse_(y, y_hat):
        return float((y_hat - y).T.dot((y_hat - y))) / (y.shape[0])