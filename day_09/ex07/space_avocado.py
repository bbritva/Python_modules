import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

from polynomial_model import add_polynomial_features
from ridge import MyRidge as MyLR
from data_spliter import data_spliter


filename = "space_avocado.csv"
features = ["weight", "prod_distance", "time_delivery"]


def plot_model(X, Y, Y_hat, feature, power, lambda_):
    plt.title(feature + " with power = " + str(power) + ", lambda = " + str(lambda_))
    plt.scatter(X, Y, marker='o',
                label="Sell price", alpha=0.05)
    plt.scatter(X, Y_hat, marker='.',
                label="Prediction")
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()


def poly_multivar_processing(power, x_test, y_test, theta, lambda_):
    my_lreg = MyLR(theta, lambda_)
    x_test_ = add_polynomial_features(x_test, power)
    y_hat = my_lreg.predict_(x_test_)
    for i in range(len(features)):
        plot_model(x_test[:, i], y_test, y_hat, features[i], power, lambda_)

    print("MSE for power %d lambda %f = %e" %
            (power, lambda_, models_data[str(i) + ', ' + str(j / 5)]["mse"]))


if __name__ == "__main__":
    try:
        with open("model.pickle", 'rb') as my_file:
            models_data = pickle.load(my_file)
        max_x = models_data["max_x"]
    except KeyError:
        exit()
    """ Read data """
    try:
        data = pd.read_csv("day_07/resources/" + filename)
    except FileNotFoundError:
        try:
            data = pd.read_csv("../resources/" + filename)
        except FileNotFoundError:
            exit()

    """ Split and normalize data"""
    x_train, x_test, y_train, y_test = data_spliter(
        data[["weight", "prod_distance", "time_delivery"]], data[["target"]], 0.8)
    for i in range(3):
        x_test[:, i] /= max_x[i]

    for i in (1, 2, 3, 4):
        for j in range(6):
            poly_multivar_processing(
                i, x_test, y_test, models_data[str(i) + ', ' + str(j / 5)]["theta"], j / 5)