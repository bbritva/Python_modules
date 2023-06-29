import numpy as np
import pandas as pd
import pickle

from polynomial_model import add_polynomial_features
from ridge import MyRidge as MyLR
from data_spliter import data_spliter

filename = "space_avocado.csv"
features = ["weight", "prod_distance", "time_delivery"]
models = {1:{},2:{},3:{},4:{} }
poly_mse = {}
# max_iter = 1e6
max_iter = 1e4
alpha = .01


def poly_multivar_processing(power, x_train, x_test, y_train, y_test, lambda_):
    theta = np.zeros(((3 * power + 1), 1))
    my_lreg = MyLR(theta, alpha, max_iter, lambda_)
    x_train_ = add_polynomial_features(x_train, power)
    x_test_ = add_polynomial_features(x_test, power)
    my_lreg.fit_(x_train_, y_train)
    y_hat = my_lreg.predict_(x_test_)
    poly_mse[str(power) + ', ' + str(lambda_)] = {
        "mse": my_lreg.mse_(y_test, y_hat),
        "theta": my_lreg.theta
    }
    print("MSE for power %d, lambda %f = %e" %
          (power, lambda_, poly_mse[str(power) + ', ' + str(lambda_)]["mse"]))



def train_model(train_set, power, lambda_):
    theta = np.zeros(((3 * power + 1), 1))
    models[power][lambda_] = MyLR(theta, alpha, max_iter, lambda_)
    x_train_ = add_polynomial_features(train_set[:,:-1], power)
    models[power][lambda_].fit_(x_train_, train_set[:,-1].reshape((-1,1)))
    
    print("Model with power %d, lambda %f trained" %
          (power, lambda_))

def train_models():
    for i in range(1, 5): # powers
        for j in range(6): # lambdas
            train_model(train_set, i, j / 5)


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

    train_models()
    validate_models()
    poly_mse["max_x"] = max_x
    poly_mse["min_x"] = min_x

    for i in range(1, 5):
        for j in range(6):
            poly_multivar_processing(
                i, x_train, x_test, y_train, y_test, j / 5)

    print(poly_mse)
    with open("model.pickle", 'wb') as my_file:
        pickle.dump(poly_mse, my_file)
        print("All models data saved =)")
