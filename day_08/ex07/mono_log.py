import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

from my_logistic_regression import MyLogisticRegression as MyLR
from data_spliter import data_spliter


filename = "solar_system_census.csv"
targets = "solar_system_census_planets.csv"
features = ["weight", "height", "bone_density"]


def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


@_guard_
def norm_data(x):
    x_max = max(x)
    x_min = min(x)
    return x - x_min / (x_max - x_min), x_max, x_min

@_guard_
def plot_model(X, Y, Y_hat, feature):
    plt.title(feature)
    plt.scatter(X, Y, marker='o', label="Origin", alpha=0.5)
    plt.scatter(X, Y_hat, marker='.', label="Prediction")
    plt.legend(loc='center right')
    plt.grid()
    plt.show()


if __name__ == "__main__":
    """Check the arguments"""
    try:
        if len(sys.argv) > 1 and sys.argv[1].startswith("-zipcode=") and int(sys.argv[1][9:]) in range(4):
            zipcode = int(sys.argv[1][9:])
        else:
            raise ValueError
    except ValueError:
        print("Start progamm with zipcode argument: python mono_log.py -zipcode=x, with x being 0, 1, 2 or 3.")
        exit(0)

    """ Read data """
    try:
        data_features = pd.read_csv("day_08/resources/" + filename)
        data_targets = pd.read_csv("day_08/resources/" + targets)
    except FileNotFoundError:
        try:
            data_features = pd.read_csv("../resources/" + filename)
            data_targets = pd.read_csv("../resources/" + targets)
        except FileNotFoundError:
            exit()

    """ Prepare data """
    planets = np.array(data_targets["Origin"]).reshape((-1, 1))
    Y = np.zeros(planets.shape, dtype='int8')
    Y[np.where(planets == zipcode)] = 1
    X = np.array(data_features[features])
    x_train, x_test, y_train, y_test = data_spliter(X, Y, 0.8)
    max_x = [0., 0., 0.]
    min_x = [0., 0., 0.]
    for i in range(len(features)):
        x_train[:, i], max_x[i], min_x[i] = norm_data(x_train[:, i])
        x_test[:, i] = x_test[:, i] - min_x[i] / (max_x[i] - min_x[i])

    """ Training """
    theta = np.full((4, 1), 0.0)

    my_lreg = MyLR(theta, alpha=0.001, max_iter=5e5)
    my_lreg.fit_(x_train, y_train)

    """ Output """
    y_hat = my_lreg.predict_(x_test)
    y_hat_ = np.zeros(y_test.shape, dtype='int8')
    y_hat_[np.where(y_hat > 0.5)] = 1
    for i, feature in enumerate(features):
        plot_model(x_test[:, i], y_test, y_hat_, feature)
    res = np.zeros(y_test.shape, dtype='int8')
    res[np.where(y_hat_ != y_test)] = 1
    print("Correct predictions =", res.shape[0] - res.sum())
    print("Wrong predictions =", res.sum())
