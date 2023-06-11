import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from polynomial_model import add_polynomial_features
from mylinearregression import MyLinearRegression as MyLR
from data_spliter import data_spliter

# filename = "small.csv"
filename = "space_avocado.csv"
features = ["weight", "prod_distance", "time_delivery"]


def plot_model(X, Y, Y_hat, Y_had_base, feature):
    plt.title(feature)
    plt.scatter(X, Y, marker='o',
                c='darkblue', label="Sell price", alpha=0.01)
    plt.scatter(X, Y_had_base, marker='.',
                c='blue', label="Prediction base")
    plt.scatter(X, Y_hat, marker='.',
                c='red', label="Prediction learned")
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()


def univar_processing(data, feature, alpha, thetas=np.array([[0.0], [0.0]]), max_iter=1e5):
    mlr = MyLR(thetas, alpha=alpha, max_iter=max_iter)
    model_before = mlr.predict_(data['x_test'])
    mlr.fit_(data['x_train'], data['y_train'])
    model_after = mlr.predict_(data['x_test'])
    plot_model(data['x_test'], data['y_test'],
               model_after, model_before, feature)
    print("Thetas:", mlr.thetas)
    return mlr.mse_(data['y_test'], model_after)


def norm_data(x):
    x_max = max(x)
    return x / x_max, x_max

""" Read data """
try:
    data = pd.read_csv("day_07/resources/" + filename)
except FileNotFoundError:
    data = pd.read_csv("../resources/" + filename)
except FileNotFoundError:
    exit()

""" Split and normalize data"""
x_train, x_test, y_train, y_test = data_spliter(
    data[["weight", "prod_distance", "time_delivery"]], data[["target"]], 0.8)
max_x = [0.,0.,0.]
mse_s = []
for i in range(len(features)):
    x_train[:, i], max_x[i] = norm_data(x_train[:, i])
    x_test[:,i] /= max_x[i]

""" Univariate linear regression """
for i in range(len(features)):
    prepared_data = {"x_train": x_train[:, i], "x_test": x_test[:,i],
            "y_train": y_train, "y_test": y_test, "x_max": max_x[i]}
    mse_s.append(univar_processing(prepared_data, features[i], 1e-1,
                  thetas=np.array([[6e5], [2e5]])))

""" Multivariate linear regression """
my_lreg = MyLR(thetas=np.array(
    [[4e5], [3e5], [-3e4], [-2e3]]), alpha=1e-1, max_iter=1e5)
y_hat_base = my_lreg.predict_(x_test)
my_lreg.fit_(x_train, y_train)
y_hat = my_lreg.predict_(x_test)
print(my_lreg.thetas)
mse_s.append(my_lreg.mse_(y_test, y_hat))
for i in range(len(features)):
    plot_model(x_test[:,i], y_test, y_hat, y_hat_base, features[i])

for i in range(len(mse_s)):
    print("{:e}".format(mse_s[i]))



