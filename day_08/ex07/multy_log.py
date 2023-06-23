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


def train_model(x_train, y_train):
    theta = np.full((4, 1), 0.0)
    my_lreg = MyLR(theta, alpha=0.001, max_iter=1e6)
    my_lreg.fit_(x_train, y_train)
    return my_lreg


if __name__ == "__main__":
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
    planets = np.array(data_targets["Origin"]).astype(np.int8).reshape((-1, 1))
    Y = np.zeros((planets.shape[0], 4), dtype='int8')
    for i, zipcode in enumerate(planets):
        Y[i][zipcode] = 1
    Y = np.c_[Y, planets]

    X = np.array(data_features[features])
    x_train, x_test, y_train, y_test = data_spliter(X, Y, 0.8)
    max_x = [0., 0., 0.]
    min_x = [0., 0., 0.]
    for i in range(len(features)):
        x_train[:, i], max_x[i], min_x[i] = norm_data(x_train[:, i])
        x_test[:, i] = x_test[:, i] - min_x[i] / (max_x[i] - min_x[i])

    """ Training """
    model = []
    y_hat = []

    for i in range(4):
        model.append(train_model(x_train, y_train[:, i].reshape((-1, 1))))
        y_hat.append(model[i].predict_(x_test))
    y_hat = np.c_[y_hat[0], y_hat[1], y_hat[2], y_hat[3]]
    y_hat = np.argmax(y_hat, axis=1).reshape((-1, 1))

    """ Output """
    res = y_hat == y_test[:, 4].reshape((-1, 1))
    print(res.shape, y_hat.shape, y_test[:, 4].shape)
    print("Amount of wrong predictions =", res.sum() - res.shape[0])

    # y_hat_ = np.zeros(y_test.shape, dtype='int8')
    # y_hat_[np.where(y_hat > 0.5)] = 1
    # for i, feature in enumerate(features):
    #     plot_model(x_test[:, i], y_test, y_hat_, feature)
    # res = np.zeros(y_test.shape, dtype='int8')
    # res[np.where(y_hat_ != y_test)] = 1
    # print("Amount of wrong predictions =",res.sum())
