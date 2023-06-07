import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cycler import cycler

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
    def __init__(self, thetas, alpha=0.01, max_iter=10000):
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
def plot_model(data, Y_model, feature="Age"):
    plt.figure(figsize=(10, 6))
    plt.plot(data[feature], Y_model, "--",
             c='lime', label="S$_{predict}$(pills)")
    plt.scatter(data[feature], Y_model, marker='x', c='lime')
    plt.scatter(data[feature], data[target], marker='o',
                c='cyan', label="S$_{true}$(pills)")
    plt.legend(bbox_to_anchor=(0, 1, 1, 0),
               loc="lower left", ncol=2, frameon=False)
    plt.grid()
    plt.show()


@_guard_
def plot_cost(x, y):
    amount = 100
    thetas_1 = np.linspace(-15, -3, amount)
    thetas_0 = np.linspace(80, 100, 6)
    theta_0 = 89.0
    mlr = MyLinearRegression(np.array([[theta_0], [thetas_1[0]]]))
    cost = [0] * amount
    plt.figure(figsize=(10, 10))
    plt.rcParams['axes.prop_cycle'] = cycler(
        color=['#111111', '#333333', '#555555', '#777777', '#999999', '#BBBBBB'])

    for j, theta_0 in enumerate(thetas_0):
        mlr.thetas[0][0] = theta_0
        for i, theta_1 in enumerate(thetas_1):
            mlr.thetas[1][0] = theta_1
            y_hat = mlr.predict_(x)
            cost[i] = mlr.loss_(y, y_hat)
        plt.plot(thetas_1, cost, label=f"J$(\\theta_0=c_{j}, \\theta_1)$")
    plt.xlabel("$\\theta_1$")
    plt.ylabel("cost function J$(\\theta_0, \\theta_1)$")
    plt.legend(loc='lower right')
    plt.ylim([10, 150])
    plt.grid()
    plt.show()



@_guard_
def univar_processing(data, feature):
    Xage = np.array(data[feature]).reshape(-1, 1)
    Yscore = np.array(data[target]).reshape(-1, 1)
    mlr = MyLinearRegression(np.array([[0.0], [0.0]]))
    model_before = mlr.predict_(Xage)
    mlr.fit_(Xage, Yscore)
    model_after = mlr.predict_(Xage)
    plot_model(data, model_before, feature)
    plot_model(data, model_after, feature)

try:
    data = pd.read_csv("day_07/resources/spacecraft_data.csv")
except FileNotFoundError:
    data = pd.read_csv("../resources/spacecraft_data.csv")
except FileNotFoundError:
    exit()
univar_processing(data, "Age")
