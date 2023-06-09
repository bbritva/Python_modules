import numpy as np
import time

def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except:
            return None
    return wrapper


class MyLinearRegression():
    """
    Description:
    My personnal linear regression class to fit like a boss.
    """
    @_guard_
    def __init__(self, thetas, alpha=0.001, max_iter=1000):
        self.alpha = alpha
        self.max_iter = int(max_iter)
        self.thetas = thetas

    @_guard_
    def predict_(self, x):
        return np.c_[np.ones(x.shape[0]), x].dot(self.thetas)

    @_guard_
    def gradient(self, x, y):
        return self.x_.T.dot(self.x_.dot(self.thetas) - y) / y.shape[0]

    @_guard_
    def fit_(self, x, y):
        start = time.time()
        cycles = int(self.max_iter / 20)
        self.x_ = (np.c_[np.ones(x.shape[0]), x])
        print("\r%d%%, time =%5.2fs" % (0, 0), end="")
        for j in range(20):
            for i in range(cycles):
                self.thetas -= self.alpha * self.gradient(x, y)
            now = time.time() - start
            print("\r%d%%, time =%5.2fs" % ((j + 1) * 5, now), end="")
        print("")
        return self.thetas

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
