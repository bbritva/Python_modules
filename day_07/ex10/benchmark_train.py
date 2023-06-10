import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from polynomial_model import add_polynomial_features
from mylinearregression import MyLinearRegression as MyLR
from data_spliter import data_spliter

# filename = "small.csv"
filename = "space_avocado.csv"


def plot_model(data, Y_model, feature):
    plt.title(feature)
    plt.scatter(data[feature], data["target"], marker='o',
                c='darkblue', label="Sell price")
    plt.scatter(data[feature], Y_model, marker='.',
                c='cornflowerblue', label="Predicted price")
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()


def univar_processing(data, feature, alpha, thetas=np.array([[0.0], [0.0]])):
    X = np.array(data[feature]).reshape(-1, 1)
    Y = np.array(data["target"]).reshape(-1, 1)
    print(np.unique(X))
    mlr = MyLR(thetas, alpha=alpha)
    model_before = mlr.predict_(X)
    mlr.fit_(X, Y)
    model_after = mlr.predict_(X)
    plot_model(data, model_before, feature)
    plot_model(data, model_after, feature)
    print("Thetas:", mlr.thetas)
    print("MSE = ", mlr.mse_(Y, mlr.predict_(X)))


def do_process(thetas, x_train, x_test, y_train, y_test, alpha=2e-7, max_iter=1e5):
    mlr = MyLR(thetas, alpha, max_iter)
    # x_ = add_polynomial_features(x_train, len(thetas) - 1)
    x_ = x
    mlr.fit_(x_, y)
    print(mlr.thetas)
    # continuous_x = np.arange(1, 7.0, 0.1).reshape(-1, 1)
    # continuous_x_ = add_polynomial_features(continuous_x, len(thetas) - 1)
    # y_hat = mlr.predict_(continuous_x_)
    # plt.scatter(x, y)
    # plt.plot(continuous_x, y_hat, color='orange')
    # plt.grid()
    # plt.show()


try:
    data = pd.read_csv("day_07/resources/" + filename)
except FileNotFoundError:
    data = pd.read_csv("../resources/" + filename)
except FileNotFoundError:
    exit()
# x = np.array(data[["weight","prod_distance","time_delivery"]])
# y = np.array(data[["target"]])
# x_train, x_test, y_train, y_test = data_spliter(x, y, 0.8)

univar_processing(data, "weight", 0.0001, thetas=np.array([[500000.], [4000.]]))
# univar_processing(data, "prod_distance", 0.0001,
#                 thetas=np.array([[0.0], [4.0]]))
# univar_processing(data, "time_delivery", 0.0002,
#                 thetas=np.array([[700.0], [-1.0]]))


# theta1 = np.array([[30000.], [4909.], [173.], [6000.]])
# theta2 = np.array([[85.], [-7.], [-0.2]])
# theta3 = np.array([[87.], [-5.], [-1.5], [0.15]])
# theta4 = np.array([[-20], [160], [-80], [14], [-1]])
# theta5 = np.array([[1140], [-1850], [1110], [-305], [40], [-2]])
# theta6 = np.array([[9110], [-18015], [13400], [-4935], [966], [-96.4], [3.86]])
# do_process(theta1, x_train, x_test, y_train, y_test)
# do_process(theta2, data)
# do_process(theta3, data, 1e-6, 1000000)
# do_process(theta4, data, 1e-6, 1000000)
# do_process(theta5, data, 1e-8, 1000000)
# do_process(theta6, data, 1e-9, 1000000)
