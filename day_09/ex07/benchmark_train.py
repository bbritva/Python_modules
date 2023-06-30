import numpy as np
import pandas as pd
import pickle

from polynomial_model import add_polynomial_features
from ridge import MyRidge as MyLR
from data_spliter import data_spliter

filename = "space_avocado.csv"
features = ["weight", "prod_distance", "time_delivery"]
results = {}
models = {1: {}, 2: {}, 3: {}, 4: {}}
# max_iter = 1e6
max_iter = 1e4
alpha = .01

def train_model(train_set, power, lambda_):
    theta = np.zeros(((3 * power + 1), 1))
    model = MyLR(theta, alpha, max_iter, lambda_)
    
    x_train_ = add_polynomial_features(train_set[:, :-1], power)
    model.fit_(x_train_, train_set[:, -1].reshape((-1, 1)))
    models[power][lambda_] = model.theta
    print("Model with power %d, lambda %f trained" %
          (power, lambda_))


def train_models(train_set):
    for i in range(1, 5):  # powers
        for j in range(6):  # lambdas
            train_model(train_set, i, j / 5)


def validate_models(cv_set):
    best_power = 1
    best_lambda = 0
    best_mse = 0
    for i in range(1, 5):  # powers
        x_cv_ = add_polynomial_features(cv_set[:, :-1], i)
        for j in range(6):  # lambdas
            model = MyLR(models[i][j/5], alpha, max_iter, j/5)
            y_hat = model.predict_(x_cv_)
            mse = MyLR.mse_(cv_set[:, -1].reshape((-1, 1)), y_hat)
            if mse < best_mse or best_mse == 0:
                best_mse = mse
                best_power = i
                best_lambda = j / 5
    print(best_power, best_lambda, best_mse)
    return (best_power, best_lambda, best_mse)


def norm_data(x):
    x_max = max(x)
    x_min = min(x)
    return (x - x_min) / (x_max - x_min), x_max, x_min


if __name__ == "__main__":
    """ Read data """
    try:
        data = pd.read_csv("day_07/resources/" + filename)
    except FileNotFoundError:
        try:
            data = pd.read_csv("../resources/" + filename)
        except FileNotFoundError:
            exit()

    """ Split and normalize data"""
    train_set, cv_set, test_set = data_spliter(np.array(
        data[["weight", "prod_distance", "time_delivery", "target"]]))
    print(train_set.shape, cv_set.shape, test_set.shape)
    max_x = [0., 0., 0.]
    min_x = [0., 0., 0.]
    for i in range(len(features)):
        train_set[:, i], max_x[i], min_x[i] = norm_data(train_set[:, i])
        cv_set[:, i] = (cv_set[:, i] - min_x[i]) / (max_x[i] - min_x[i])
        test_set[:, i] = (test_set[:, i] - min_x[i]) / (max_x[i] - min_x[i])

    print(np.max(train_set[:, :3]), np.max(
        cv_set[:, :3]), np.max(test_set[:, :3]))
    print(np.max(train_set[:, 3]), np.max(
        cv_set[:, 3]), np.max(test_set[:, 3]))
    # np.savetxt("../resources/tmp/train_set.csv", train_set, delimiter=",")
    # np.savetxt("../resources/tmp/cv_set.csv", cv_set, delimiter=",")
    # np.savetxt("../resources/tmp/test_set.csv", test_set, delimiter=",")

    train_models(train_set)
    best_power, best_lambda, best_mse = validate_models(cv_set)
    results["models"] = models
    results["max_x"] = max_x
    results["min_x"] = min_x
    results["best_power"] = best_power
    results["best_lambda"] = best_lambda

    print(results)
    with open("model.pickle", 'wb') as my_file:
        pickle.dump(results, my_file)
        print("All results saved =)")
