import numpy as np
import matplotlib.pyplot as plt
import pickle

from polynomial_model import add_polynomial_features
from ridge import MyRidge as MyLR


test_file = "test_set.csv"
train_file = "train_set.csv"
features = ["weight", "prod_distance", "time_delivery"]



def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


@_guard_
def train_model(train_set, test_set, power, lambda_):
    theta = np.zeros(((3 * power + 1), 1))
    model = MyLR(theta, 0.1, 5e3, lambda_)

    x_train_ = add_polynomial_features(train_set[:, :-1], power)
    x_test_ = add_polynomial_features(test_set[:, :-1], power)
    model.fit_(x_train_, train_set[:, -1].reshape((-1, 1)))
    print("Model with power %d, lambda %f trained" %
          (power, lambda_))
    y_hat = model.predict_(x_test_)
    mse = MyLR.mse_(test_set[:, -1].reshape((-1, 1)), y_hat)
    print("MSE =", mse)


@_guard_
def plot_model(X, Y, Y_hat, feature, power, lambda_):
    plt.title(feature + " with power = " +
              str(power) + ", lambda = " + str(lambda_))
    plt.scatter(X, Y, marker='o',
                label="Sell price", alpha=0.05)
    plt.scatter(X, Y_hat, marker='.',
                label="Prediction")
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()


@_guard_
def poly_multivar_processing(power, x_test, y_test, theta, lambda_):
    my_lreg = MyLR(theta, lambda_)
    x_test_ = add_polynomial_features(x_test, power)
    y_hat = my_lreg.predict_(x_test_)
    for i in range(len(features)):
        plot_model(x_test[:, i], y_test, y_hat, features[i], power, lambda_)

    print("MSE for power %d lambda %f = %e" %
          (power, lambda_, MyLR.mse_(y_test, y_hat)))


@_guard_
def plot_lambdas(test_data, power, thetas):
    x_test = test_data[:, :-1]
    y_test = test_data[:, -1].reshape((-1, 1))
    x_test_ = add_polynomial_features(x_test, power)
    y_hats = []

    """ Predict """
    for j in range(6):
        my_lreg = MyLR(thetas[j/5], j/5)
        y_hats.append(my_lreg.predict_(x_test_))

    for i in range(len(features)):
        plt.title(features[i])

        """ Real values """
        plt.scatter(x_test[:,i], y_test, marker='x',
                    label="Sell price")

        """ Predicted values """
        for j, y_hat in enumerate(y_hats):
            plt.scatter(x_test[:,i], y_hat, marker='.',
                        label="lambda = " + str(j/5), alpha=0.5)

        plt.legend(loc='lower right')
        plt.grid()
        plt.show()

@_guard_
def main():
    try:
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
    except Exception:
        try:
            test_data = np.genfromtxt(
                "../resources/tmp/" + test_file, delimiter=',')
            train_data = np.genfromtxt(
                "../resources/tmp/" + train_file, delimiter=',')
        except Exception:
            exit()

    best_power = models_data["best_power"]
    best_lambda = models_data["best_lambda"]
    models = models_data["models"]
    max_x = models_data["max_x"]
    min_x = models_data["min_x"]

    train_model(train_data, test_data, best_power, best_lambda)
    plot_lambdas(test_data, best_power, models[best_power])

if __name__ == "__main__":
    main()