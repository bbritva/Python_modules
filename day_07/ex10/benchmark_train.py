import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from polynomial_model import add_polynomial_features
from mylinearregression import MyLinearRegression as MyLR
from data_spliter import data_spliter

# filename = "small.csv"
filename = "space_avocado.csv"


def plot_model(X, Y, Y_model, feature):
    plt.title(feature)
    plt.scatter(X, Y, marker='o',
                c='darkblue', label="Sell price", alpha=0.01)
    plt.scatter(X, Y_model, marker='.',
                c='cornflowerblue', label="Predicted price", alpha=0.01)
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()


def univar_processing(data, Y, feature, alpha, thetas=np.array([[0.0], [0.0]]), max_iter=1e5):
    X = np.array(data[feature]).reshape(-1, 1)
    mlr = MyLR(thetas, alpha=alpha, max_iter=max_iter)
    max_X = max(X)
    X = X / max_X
    model_before = mlr.predict_(X)
    mlr.fit_(X, Y)
    model_after = mlr.predict_(X)
    plot_model(X, Y, model_before, feature)
    plot_model(X, Y, model_after, feature)
    print("Thetas:", mlr.thetas)
    print("MSE = ", mlr.mse_(Y, mlr.predict_(X)))


try:
    data = pd.read_csv("day_07/resources/" + filename)
except FileNotFoundError:
    data = pd.read_csv("../resources/" + filename)
except FileNotFoundError:
    exit()
# x = np.array(data[["weight","prod_distance","time_delivery"]])
y = np.array(data[["target"]]).reshape((-1, 1))
# x_train, x_test, y_train, y_test = data_spliter(x, y, 0.8)
# print(min(data['weight']), max(data['weight']))
# univar_processing(data,y, "weight", 0.0001, thetas=np.array([[400000.], [3000.]]))
univar_processing(data, y, "prod_distance", 1e-4,
                thetas=np.array([[4e5], [2e-5]]), max_iter=1e5)
# univar_processing(data, "time_delivery", 0.01,
#                 thetas=np.array([[6e+05], [-100.0]]), max_iter=1e5)


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
