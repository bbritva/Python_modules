import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

from polynomial_model import add_polynomial_features
from my_logistic_regression import MyLogisticRegression as MyLR


test_file = "ssc_test_set.csv"
train_file = "ssc_train_set.csv"
features = ["weight", "height", "bone_density"]
max_iter = 1e4
alpha = .1


def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


@_guard_
def train_model(x_train, y_train, lambda_):
    theta = np.zeros((10, 1))
    my_lreg = MyLR(theta, alpha=alpha, max_iter=max_iter,
                   penalty='l2', lambda_=lambda_)
    my_lreg.fit_(x_train, y_train)
    return my_lreg.theta


@_guard_
def calc_params(y, y_hat):
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for pos_label in range(4):
        tp += len(y[(y == pos_label) & (y_hat == pos_label)])
        fp += len(y[(y != pos_label) & (y_hat == pos_label)])
        tn += len(y[(y != pos_label) & (y_hat != pos_label)])
        fn += len(y[(y == pos_label) & (y_hat != pos_label)])
    return tp, fp, tn, fn


@_guard_
def f1_score_(y, y_hat):
    """ Compute the f1 score """
    tp, fp, tn, fn = calc_params(y, y_hat)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    return (2 * precision * recall) / (precision + recall)


@_guard_
def get_predictions(thetas, data):
    y_hat = []
    for theta in thetas:
        mdl = MyLR(theta)
        y_hat.append(mdl.predict_(data[:, :-5]))
    y_hat = np.c_[y_hat[0], y_hat[1], y_hat[2], y_hat[3]]
    y_hat = np.argmax(y_hat, axis=1).reshape((-1, 1))
    return y_hat


@_guard_
def train_models(train_data, test_data, lambda_):
    thetas = []
    X = train_data[:, :-5]
    Y = train_data[:, -5:-1]
    for i in range(4):
        thetas.append(train_model(X, Y[:, i].reshape((-1, 1)), lambda_))
    print("Models with lambda %f trained" % (lambda_))
    y_hat = get_predictions(thetas, test_data)
    f1_score = f1_score_(test_data[:, -5:-1], y_hat)
    print(lambda_, f1_score)
    return thetas


@_guard_
def main():
    try:
        # with open("day_09/ex09/model.pickle", 'rb') as my_file:
        with open("model.pickle", 'rb') as my_file:
            models_data = pickle.load(my_file)
    except KeyError:
        exit()
    """ Read data """
    try:
        test_data = np.genfromtxt(
            "day_09/resources/tmp/" + test_file, delimiter=',')
        train_data = np.genfromtxt(
            "day_09/resources/tmp/" + train_file, delimiter=',')
    except FileNotFoundError:
        try:
            test_data = np.genfromtxt(
                "../resources/tmp/" + test_file, delimiter=',')
            train_data = np.genfromtxt(
                "../resources/tmp/" + train_file, delimiter=',')
        except FileNotFoundError:
            exit()

    best_lambda = models_data["best_lambda"]
    thetas = models_data["models"]
    max_x = models_data["max_x"]
    min_x = models_data["min_x"]

    best_thetas = train_models(train_data, test_data, best_lambda)

    y_hat = get_predictions(best_thetas, test_data)
    x_test = test_data[:, :-5]
    y_test = test_data[:, -5:]
    color = ["red", "green", "blue", "black"]

    plt.xlabel(features[0])
    plt.ylabel(features[1])
    for i in range(4):
        predicted = x_test[np.where(y_hat == i)[0]]
        actual = x_test[np.where(y_test[:, 4].reshape((-1, 1)) == i)[0]]
        plt.scatter(predicted[:, 0], predicted[:, 1],
                    marker='o', label="Origin", alpha=0.2, c=color[i])
        plt.scatter(actual[:, 0], actual[:, 1],
                    marker='.', label="Origin", c=color[i])
    plt.grid()
    plt.show()

    plt.xlabel(features[1])
    plt.ylabel(features[2])
    for i in range(4):
        predicted = x_test[np.where(y_hat == i)[0]]
        actual = x_test[np.where(y_test[:, 4].reshape((-1, 1)) == i)[0]]
        plt.scatter(predicted[:, 1], predicted[:, 2],
                    marker='o', label="Origin", alpha=0.5, c=color[i])
        plt.scatter(actual[:, 1], actual[:, 2],
                    marker='.', label="Origin", c=color[i])
    plt.grid()
    plt.show()

    plt.xlabel(features[0])
    plt.ylabel(features[2])
    for i in range(4):
        predicted = x_test[np.where(y_hat == i)[0]]
        actual = x_test[np.where(y_test[:, 4].reshape((-1, 1)) == i)[0]]
        plt.scatter(predicted[:, 0], predicted[:, 2],
                    marker='o', label="Origin", alpha=0.5, c=color[i])
        plt.scatter(actual[:, 0], actual[:, 2],
                    marker='.', label="Origin", c=color[i])
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
