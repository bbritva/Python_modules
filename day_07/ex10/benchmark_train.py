import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import pickle 

from polynomial_model import add_polynomial_features
from mylinearregression import MyLinearRegression as MyLR
from data_spliter import data_spliter

filename = "space_avocado.csv"
features = ["weight", "prod_distance", "time_delivery"]
plot = False


def plot_model(X, Y, Y_hat, feature):
    plt.title(feature)
    plt.scatter(X, Y, marker='o',
                c='darkblue', label="Sell price", alpha=0.05)
    plt.scatter(X, Y_hat, marker='.',
                c='blue', label="Prediction")
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()


def lin_univar_processing(data, feature, alpha, thetas=np.array([[0.0], [0.0]]), max_iter=1e5):
    mlr = MyLR(thetas, alpha=alpha, max_iter=max_iter)
    model_before = mlr.predict_(data['x_test'])
    mlr.fit_(data['x_train'], data['y_train'])
    model_after = mlr.predict_(data['x_test'])
    plot_model(data['x_test'], data['y_test'],
               model_after, model_before, feature)
    print("Thetas:", mlr.thetas)
    return mlr.mse_(data['y_test'], model_after)


def sqr_univar_processing(data, feature, alpha, thetas=np.array([[0.0], [0.0], [0.0]]), max_iter=1e5):
    mlr = MyLR(thetas, alpha=alpha, max_iter=max_iter)
    x_train_ = add_polynomial_features(data['x_train'], 2)
    x_test_ = add_polynomial_features(data['x_test'], 2)
    model_before = mlr.predict_(x_test_)
    mlr.fit_(x_train_, data['y_train'])
    model_after = mlr.predict_(x_test_)
    plot_model(data['x_test'], data['y_test'],
               model_after, model_before, feature)
    print("Thetas:", mlr.thetas)
    return mlr.mse_(data['y_test'], model_after)


def poly_univar_processing(data, feature, power, alpha, thetas, max_iter=1e5):
    mlr = MyLR(thetas, alpha=alpha, max_iter=max_iter)
    x_train_ = add_polynomial_features(data['x_train'], power)
    x_test_ = add_polynomial_features(data['x_test'], power)
    model_before = mlr.predict_(x_test_)
    mlr.fit_(x_train_, data['y_train'])
    model_after = mlr.predict_(x_test_)
    plot_model(data['x_test'], data['y_test'],
               model_after, model_before, feature)
    print("Thetas:", mlr.thetas)
    return mlr.mse_(data['y_test'], model_after)

def poly_multivar_processing(power, x_train, x_test, y_train, y_test):
    thetas = np.zeros(((3 * power + 1), 1))
    alpha = .1
    max_iter = 1e4
    my_lreg = MyLR(thetas, alpha, max_iter)
    x_train_ = add_polynomial_features(x_train, power)
    x_test_ = add_polynomial_features(x_test, power)
    my_lreg.fit_(x_train_, y_train)
    y_hat = my_lreg.predict_(x_test_)
    poly_mse[power] = {
        "mse" : my_lreg.mse_(y_test, y_hat),
        "thetas" : my_lreg.thetas
    }
    if plot:
        for i in range(len(features)):
            plot_model(x_test[:, i], y_test, y_hat, features[i])


def norm_data(x):
    x_max = max(x)
    return x / x_max, x_max

if __name__=="__main__":
    """ Read data """
    plot = len(sys.argv) > 1 and sys.argv[1] == "-P"
    try:
        data = pd.read_csv("day_07/resources/" + filename)
    except FileNotFoundError:
        data = pd.read_csv("../resources/" + filename)
    except FileNotFoundError:
        exit()

    """ Split and normalize data"""
    x_train, x_test, y_train, y_test = data_spliter(
        data[["weight", "prod_distance", "time_delivery"]], data[["target"]], 0.8)
    max_x = [0., 0., 0.]
    lin_mse = []
    for i in range(len(features)):
        x_train[:, i], max_x[i] = norm_data(x_train[:, i])
        x_test[:, i] /= max_x[i]
    # max_y = max(y_train)
    # y_test /= max_y
    # y_train /= max_y

    poly_mse = {}
    poly_mse["max_x"] = max_x
    
    for i in range(1, 5):
        poly_multivar_processing(i, x_train, x_test, y_train, y_test)


    # for i in poly_mse.keys():
    #     print("Mse for power {:d} = {:e}".format(i, poly_mse[i]["mse"]))
    print(poly_mse)

    with open("model.pickle", 'wb') as my_file:
        pickle.dump(poly_mse, my_file)