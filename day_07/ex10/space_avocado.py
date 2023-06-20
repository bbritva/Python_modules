import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle 

from polynomial_model import add_polynomial_features
from mylinearregression import MyLinearRegression as MyLR
from data_spliter import data_spliter


filename = "space_avocado.csv"
features = ["weight", "prod_distance", "time_delivery"]

def plot_model(X, Y, Y_hat, feature, power):
    plt.title(feature + " with power = " + str(power))
    plt.scatter(X, Y, marker='o',
                c='darkblue', label="Sell price", alpha=0.05)
    plt.scatter(X, Y_hat, marker='.',
                c='blue', label="Prediction")
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()


def poly_multivar_processing(power, x_train, x_test, y_train, y_test, thetas):
    my_lreg = MyLR(thetas)
    x_train_ = add_polynomial_features(x_train, power)
    x_test_ = add_polynomial_features(x_test, power)
    y_hat = my_lreg.predict_(x_test_)
    for i in range(len(features)):
        plot_model(x_test[:, i], y_test, y_hat, features[i], power)


if __name__ == "__main__":

    with open("model.pickle", 'rb') as my_file:
        models_data = pickle.load(my_file)
    max_x = models_data["max_x"]

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
    for i in range(3):
        x_train[:, i] /= max_x[i]
        x_test[:, i] /= max_x[i]

    for i in (1, 2, 3, 4):
        poly_multivar_processing(i, x_train, x_test, y_train, y_test, models_data[i]["thetas"])