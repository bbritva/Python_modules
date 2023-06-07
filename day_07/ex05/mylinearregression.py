import numpy as np

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
    def __init__(self, thetas, alpha=0.001, max_iter=1000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.thetas = thetas

    @_guard_
    def predict_(self, x):
        return np.c_[np.ones(x.shape[0]), x].dot(self.thetas)

    @_guard_
    def gradient(self, x, y):
        x_ = (np.c_[np.ones(x.shape[0]), x])
        return x_.T.dot(x_.dot(self.thetas) - y) / y.shape[0]

    @_guard_
    def fit_(self, x, y):
        for i in range(self.max_iter):
            self.thetas = self.thetas - self.alpha * self.gradient(x, y)
        return self.thetas

    @_guard_
    def loss_(self, y, y_hat):
        return float((y_hat - y).T.dot((y_hat - y))) / (2 * y.shape[0])

    @_guard_
    def loss_elem_(self, y, y_hat):
        return (y - y_hat) ** 2

X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [34., 55., 89., 144.]])
Y = np.array([[23.], [48.], [218.]])
mylr = MyLinearRegression([[1.], [1.], [1.], [1.], [1]])
# Example 0:
y_hat = mylr.predict_(X)
print(y_hat)
# Output:
# array([[8.], [48.], [323.]])
# Example 1:
print(mylr.loss_elem_(Y, y_hat))
# Output:
# array([[225.], [0.], [11025.]])
# Example 2:
print(mylr.loss_(Y, y_hat))
# Output:
# 1875.0
# Example 3:
mylr.alpha = 1.6e-4
mylr.max_iter = 200000
mylr.fit_(X, Y)
print(mylr.thetas)
# Output:
# array([[18.188..], [2.767..], [-0.374..], [1.392..], [0.017..]])
# Example 4:
y_hat = mylr.predict_(X)
print(y_hat)
# Output:
# array([[23.417..], [47.489..], [218.065...]])
# Example 5:
print(mylr.loss_elem_(Y, y_hat))
# Output:
# array([[0.174..], [0.260..], [0.004..]])
# Example 6:
print(mylr.loss_(Y, y_hat))
# Output:
# 0.0732..