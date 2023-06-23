import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

from my_logistic_regression import MyLogisticRegression as MyLR
from data_spliter import data_spliter


filename = "solar_system_census.csv"
targets = "solar_system_census_planets.csv"
features = ["weight", "height", "bone_density"]


def norm_data(x):
    x_max = max(x)
    x_min = min(x)
    return x - x_min / (x_max - x_min), x_max, x_min


def plot_model(X, Y, Y_hat, feature):
    plt.title(feature)
    plt.scatter(X, Y, marker='o', label="Origin", alpha=0.5)
    plt.scatter(X, Y_hat, marker='.', label="Prediction")
    plt.legend(loc='upper left')
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
    # theta = [[  4.7], [ 44.21395409], [-9.23467909], [-51.59499781]]
    # theta = [[  9.63361262], [ 44.99262607], [-19.61601128], [-51.73793962]]
    # theta = [[  5.25218609], [ 43.00363967], [-12.49077193], [-46.36047297]]
    # theta = [[ 10.40356129], [ 47.89749813], [-21.08483001], [-48.4361374 ]]
    # theta = [[  5.74297911], [ 44.86243869], [-13.02283818], [-46.94864516]]
    # theta = [[  7.74297911], [ 46.36243869], [-15.52283818], [-47.74864516]]

    # after normalization
    theta = [[  4.30163419], [  0.1637979 ], [ -0.03442416], [-17.7718379 ]]
    theta = [[  5.54033263], [  0.17250141], [ -0.0393519 ], [-18.90565736]]

    my_lreg = MyLR(theta, alpha=0.001, max_iter=1e5)
    my_lreg.fit_(x_train, y_train)

    """ Output """
    y_hat = my_lreg.predict_(x_test)
    y_hat_ = np.zeros(y_test.shape, dtype='int8')
    y_hat_[np.where(y_hat > 0.5)] = 1
    for i, feature in enumerate(features):
        plot_model(x_test[:, i], y_test, y_hat_, feature)
    print("loss =", my_lreg.loss_(y_test, y_hat))
    print("theta =", my_lreg.theta)
    res = np.zeros(y_test.shape, dtype='int8')
    res[np.where(y_hat_ != y_test)] = 1
    print("Amount of wrong predictions =",res.sum())
