import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

from polynomial_model import add_polynomial_features
from ridge import MyRidge as MyLR
from data_spliter import data_spliter

filename = "space_avocado.csv"
features = ["weight", "prod_distance", "time_delivery"]
results = {}
models = {1: {}, 2: {}, 3: {}, 4: {}}
max_iter = 1e6
# max_iter = 1e2
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
def train_model(train_set, power, lambda_):
    theta = np.zeros(((3 * power + 1), 1))
    model = MyLR(theta, alpha, max_iter, lambda_)

    x_train_ = add_polynomial_features(train_set[:, :-1], power)
    model.fit_(x_train_, train_set[:, -1].reshape((-1, 1)))
    models[power][lambda_] = model.theta
    print("Model with power %d, lambda %f trained" %
          (power, lambda_))


@_guard_
def train_models(train_set):
    for i in range(1, 5):  # powers
        for j in range(6):  # lambdas
            train_model(train_set, i, j / 5)


@_guard_
def plot_mse(power, data):
    data = data[np.where(data[:, 0] == power)]
    plt.title("Mse with power = " + str(power))
    plt.plot(data[:, 1], data[:, 2], marker='o')
    plt.grid()
    plt.show()


@_guard_
def validate_models(cv_set):
    best_power = 1
    best_lambda = 0
    best_mse = 0
    results = []
    for i in range(1, 5):  # powers
        x_cv_ = add_polynomial_features(cv_set[:, :-1], i)
        for j in range(6):  # lambdas
            model = MyLR(models[i][j/5], alpha, max_iter, j/5)
            y_hat = model.predict_(x_cv_)
            mse = MyLR.mse_(cv_set[:, -1].reshape((-1, 1)), y_hat)
            results.append([i, j / 5, mse])
            if mse < best_mse or best_mse == 0:
                best_mse = mse
                best_power = i
                best_lambda = j / 5
    print(best_power, best_lambda, best_mse)
    results = np.array(results)
    for i in range(1, 5):
        plot_mse(i, results)
    return (best_power, best_lambda, best_mse)


@_guard_
def norm_data(x):
    x_max = max(x)
    x_min = min(x)
    return (x - x_min) / (x_max - x_min), x_max, x_min


@_guard_
def main():
    """ Read data """
    try:
        data = pd.read_csv("day_07/resources/" + filename)
    except FileNotFoundError:
        try:
            data = pd.read_csv("../resources/" + filename)
        except FileNotFoundError:
            exit()

    """ Normalize data"""
    data = np.array(
        data[["weight", "prod_distance", "time_delivery", "target"]])
    max_x = np.zeros((data.shape[1]))
    min_x = np.zeros((data.shape[1]))
    for i in range(data.shape[1]):
        data[:, i], max_x[i], min_x[i] = norm_data(data[:, i])

    train_set, cv_set, test_set = data_spliter(data)
    print(train_set.shape, cv_set.shape, test_set.shape)

    print(np.max(train_set[:, :3]), np.max(
        cv_set[:, :3]), np.max(test_set[:, :3]))
    print(np.max(train_set[:, 3]), np.max(
        cv_set[:, 3]), np.max(test_set[:, 3]))
    np.savetxt("../resources/tmp/train_set.csv", train_set, delimiter=",")
    np.savetxt("../resources/tmp/cv_set.csv", cv_set, delimiter=",")
    np.savetxt("../resources/tmp/test_set.csv", test_set, delimiter=",")

    train_models(train_set)
    best_power, best_lambda, best_mse = validate_models(cv_set)
    results["models"] = models
    results["max_x"] = max_x
    results["min_x"] = min_x
    results["best_power"] = best_power
    results["best_lambda"] = best_lambda

    with open("model.pickle", 'wb') as my_file:
        pickle.dump(results, my_file)
        print("All results saved =)")

if __name__=="__main__":
    main()