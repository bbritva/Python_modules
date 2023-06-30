import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

from polynomial_model import add_polynomial_features
from ridge import MyRidge as MyLR


test_file = "test_set.csv"
train_file = "train_set.csv"
features = ["weight", "prod_distance", "time_delivery"]


def train_model(train_set, test_set, power, lambda_):
    theta = np.zeros(((3 * power + 1), 1))
    model = MyLR(theta, 0.1, 1e4, lambda_)

    x_train_ = add_polynomial_features(train_set[:, :-1], power)
    x_test_ = add_polynomial_features(test_set[:, :-1], power)
    model.fit_(x_train_, train_set[:, -1].reshape((-1, 1)))
    print("Model with power %d, lambda %f trained" %
          (power, lambda_))
    y_hat = model.predict_(x_test_)
    mse = MyLR.mse_(test_set[:, -1].reshape((-1, 1)), y_hat)
    print("MSE =", mse)


def plot_model(X, Y, Y_hat, feature, power, lambda_):
    plt.title(feature + " with power = " +
              str(power) + ", lambda = " + str(lambda_))
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
          (power, lambda_, MyLR.mse_(y_test, y_hat)))


if __name__ == "__main__":
    try:
        with open("model.pickle", 'rb') as my_file:
            models_data = pickle.load(my_file)
    except KeyError:
        exit()
    """ Read data """
    try:
        test_data = np.genfromtxt(
            "day_07/resources/tmp/" + test_file, delimiter=',')
        train_data = np.genfromtxt("day_07/resources/tmp/" + train_file)
    except FileNotFoundError:
        try:
            test_data = np.genfromtxt(
                "../resources/tmp/" + test_file, delimiter=',')
            train_data = np.genfromtxt(
                "../resources/tmp/" + train_file, delimiter=',')
        except FileNotFoundError:
            exit()

    best_power = models_data["best_power"]
    best_lambda = models_data["best_lambda"]
    models = models_data["models"]
    max_x = models_data["max_x"]
    min_x = models_data["min_x"]

    train_model(train_data, test_data, best_power, best_lambda)

    for i in (1, 2, 3, 4):
        for j in range(6):
            poly_multivar_processing(
                i, test_data[:,:-1], test_data[:,-1].reshape((-1,1)), models[i][j / 5], j / 5)
