import numpy as np
from my_linear_regression import MyLinearRegression as MyLR
import math


def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


class MyRidge(MyLR):
    """
    Description:
    My personnal ridge regression class to fit like a boss.
    """
    @_guard_
    def __init__(self, theta, alpha=0.001, max_iter=1000, lambda_=0.5):
        super().__init__(theta, alpha, max_iter)
        self.lambda_ = lambda_

    @_guard_
    def set_params_(self, theta, alpha=0.001, max_iter=1000, lambda_=0.5):
        self.alpha = alpha
        self.max_iter = max_iter
        self.theta = theta
        self.lambda_ = lambda_

    @_guard_
    def get_params_(self):
        return self.alpha, self.max_iter, self.theta, self.lambda_

    @_guard_
    def gradient(self, x, y):
        self.theta_[1:] = self.theta[1:]
        res = self.x_.T.dot(self.x_.dot(self.theta) - y) + self.lambda_ * self.theta_
        return res / x.shape[0]

    @_guard_
    def fit_(self, x, y):
        self.theta_ = np.zeros(self.theta.shape)
        super().fit_(x, y)
