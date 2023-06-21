import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from polynomial_model import add_polynomial_features
from mylinearregression import MyLinearRegression as MyLR


def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


@_guard_
def do_process(thetas, data, alpha=1e-4, max_iter=1e5):
    mlr = MyLR(thetas, alpha, max_iter)
    x = np.array(data["Micrograms"]).reshape(-1, 1)
    x_ = add_polynomial_features(x, len(thetas) - 1)
    y = np.array(data["Score"]).reshape(-1, 1)
    mlr.fit_(x_, y)
    print(mlr.thetas)
    continuous_x = np.arange(1, 7.0, 0.1).reshape(-1, 1)
    continuous_x_ = add_polynomial_features(continuous_x, len(thetas) - 1)
    y_hat = mlr.predict_(continuous_x_)
    plt.scatter(x, y)
    plt.plot(continuous_x, y_hat, color='orange')
    plt.grid()
    plt.title("Power = " + str(len(thetas) - 1))
    plt.show()


try:
    data = pd.read_csv("day_07/resources/are_blue_pills_magics.csv")
except FileNotFoundError:
    data = pd.read_csv("../resources/are_blue_pills_magics.csv")
except FileNotFoundError:
    exit()

theta1 = np.array([[80.], [-7.]])
theta2 = np.array([[85.], [-7.], [-0.2]])
theta3 = np.array([[87.], [-5.], [-1.5], [0.15]])
theta4 = np.array([[-20.], [160.], [-80.], [14.], [-1.]])
theta5 = np.array([[1140.], [-1850.], [1110.], [-305.], [40.], [-2.]])
theta6 = np.array([[9110.], [-18015.], [13400.], [-4935.], [966.], [-96.4], [3.86]])
do_process(theta1, data)
do_process(theta2, data)
do_process(theta3, data, 1e-6, 1000000)
do_process(theta4, data, 1e-6, 1000000)
do_process(theta5, data, 1e-8, 1000000)
do_process(theta6, data, 1e-9, 1000000)
