import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

target = "Sell_price"


def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print("Error:", func.__name__, e)
            return None
    return wrapper


class MyLinearRegression():
    """
    Description:
    My personnal linear regression class to fit like a boss.
    """
    @_guard_
    def __init__(self, thetas, alpha=0.01, max_iter=100000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.thetas = thetas

    @_guard_
    def predict_(self, x):
        return np.c_[np.ones(x.shape[0]), x].dot(self.thetas)

    @_guard_
    def gradient(self, x, y):
        x_ = np.c_[np.ones(x.shape[0]), x]
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
        return float((y_hat - y).T.dot((y_hat - y))) / (y.shape[0])


@_guard_
def plot_model(data, Y_model, feature):
    plt.title(feature)
    plt.scatter(data[feature], Y_model, marker='.',
                c='cornflowerblue', label="Predicted price")
    plt.scatter(data[feature], data[target], marker='o',
                c='darkblue', label="Sell price")
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()


@_guard_
def univar_processing(data, feature, alpha, thetas=np.array([[0.0], [0.0]])):
    X = np.array(data[feature]).reshape(-1, 1)
    Y = np.array(data[target]).reshape(-1, 1)
    mlr = MyLinearRegression(thetas, alpha=alpha)
    model_before = mlr.predict_(X)
    mlr.fit_(X, Y)
    model_after = mlr.predict_(X)
    plot_model(data, model_before, feature)
    plot_model(data, model_after, feature)
    print("Thetas:", mlr.thetas)
    print("MSE = ", mlr.mse_(Y, mlr.predict_(X)))


try:
    data = pd.read_csv("day_07/resources/spacecraft_data.csv")
except FileNotFoundError:
    data = pd.read_csv("../resources/spacecraft_data.csv")
except FileNotFoundError:
    exit()
# univar_processing(data, "Age", 0.01, thetas=np.array([[500.], [0.]]))
# univar_processing(data, "Thrust_power", 0.0001,
#                   thetas=np.array([[0.0], [4.0]]))
# univar_processing(data, "Terameters", 0.0002,
#                   thetas=np.array([[700.0], [-1.0]]))

# X = np.array(data[['Age']])
# Y = np.array(data[['Sell_price']])
# myLR_age = MyLinearRegression(thetas = [[1000.0], [-1.0]], alpha = 2.5e-5, max_iter = 100000)
# myLR_age.fit_(X[:,0].reshape(-1,1), Y)
# y_pred = myLR_age.predict_(X[:,0].reshape(-1,1))
# print(myLR_age.mse_(y_pred,Y))
np.seterr(all='raise')
X = np.array(data[['Age','Thrust_power','Terameters']])
Y = np.array(data[['Sell_price']])
my_lreg = MyLinearRegression(thetas = np.array([[1.0], [1.0], [1.0], [1.0]]), alpha = 5e-5, max_iter = 600000)
# Example 0:
# print(X)
y_hat = my_lreg.predict_(X)
print(my_lreg.mse_(Y, y_hat))
# Output:
# 144044.877...
# Example 1:
my_lreg.fit_(X,Y)
print(my_lreg.thetas)
# Output:
# array([[334.994...],[-22.535...],[5.857...],[-2.586...]])
# Example 2:
print(my_lreg.mse_(Y, my_lreg.predict_(X)))
# Output:
# 586.896999...