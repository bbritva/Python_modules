import numpy as np
import pandas as pd
import pickle 

from polynomial_model import add_polynomial_features
from ridge import MyRidge as MyLR
from data_spliter import data_spliter

filename = "space_avocado.csv"
features = ["weight", "prod_distance", "time_delivery"]
poly_mse = {}
# max_iter = 5e6
max_iter = 1e4
alpha = .1

def poly_multivar_processing(power, x_train, x_test, y_train, y_test, lambda_):
    theta = np.zeros(((3 * power + 1), 1))
    my_lreg = MyLR(theta, alpha, max_iter, lambda_)
    x_train_ = add_polynomial_features(x_train, power)
    x_test_ = add_polynomial_features(x_test, power)
    my_lreg.fit_(x_train_, y_train)
    y_hat = my_lreg.predict_(x_test_)
    poly_mse[power][lambda_] = {
        "mse" : my_lreg.mse_(y_test, y_hat),
        "theta" : my_lreg.theta
    }
    print("MSE for power %d = %e" % (power, poly_mse[power]["mse"]))


def norm_data(x):
    x_max = max(x)
    return x / x_max, x_max

if __name__=="__main__":
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
    max_x = [0., 0., 0.]
    for i in range(len(features)):
        x_train[:, i], max_x[i] = norm_data(x_train[:, i])
        x_test[:, i] /= max_x[i]


    poly_mse["max_x"] = max_x
    
    for i in range(1, 5):
        for j in range(5):
            poly_multivar_processing(i, x_train, x_test, y_train, y_test, j / 5)

    # print(poly_mse)
    with open("model.pickle", 'wb') as my_file:
        pickle.dump(poly_mse, my_file)
        print("All models data saved =)")
            