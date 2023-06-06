import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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

    @staticmethod
    @_guard_
    def mse_(y, y_hat):
        return ((y - y_hat) ** 2).sum() / (y.shape[0])

@_guard_
def plot_model(data, Y_model):
    plt.figure(figsize=(10,6))
    plt.plot(data["Micrograms"], Y_model, "--", c='lime', label="S$_{predict}$(pills)")
    plt.scatter(data["Micrograms"], Y_model, marker='x', c='lime')
    plt.scatter(data["Micrograms"], data["Score"], marker='o', c='cyan', label="S$_{true}$(pills)")
    plt.legend(bbox_to_anchor=(0, 1, 1, 0), loc="lower left", ncol=2, frameon=False)
    plt.grid()
    plt.show()


try:
    data = pd.read_csv("are_blue_pills_magic.csv")
    Xpill = np.array(data["Micrograms"]).reshape(-1, 1)
    Yscore = np.array(data["Score"]).reshape(-1, 1)
    linear_model1 = MyLinearRegression(np.array([[89.0], [-8]]))
    linear_model2 = MyLinearRegression(np.array([[89.0], [-6]]))
    Y_model1 = linear_model1.predict_(Xpill)
    Y_model2 = linear_model2.predict_(Xpill)
    print(MyLinearRegression.mse_(Yscore, Y_model1))
    # 57.603042857142825
    print(MyLinearRegression.mse_(Yscore, Y_model2))
    # 232.16344285714285
    plot_model(data, Y_model1)
    plot_model(data, Y_model2)
except Exception as e:
    print("Error:", e)
