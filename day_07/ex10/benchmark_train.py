import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from polynomial_model import add_polynomial_features
from mylinearregression import MyLinearRegression as MyLR
from data_spliter import data_spliter

filename = "small.csv"
# filename = "space_avocado.csv"

def do_process(thetas, x_train, x_test, y_train, y_test, alpha=1e-4, max_iter=1e5):
    mlr = MyLR(thetas, alpha, max_iter)
    x_ = add_polynomial_features(x_train, len(thetas) - 1)
    y_ = y.reshape((-1,1))
    mlr.fit_(x_, y)
    print(mlr.thetas)
    continuous_x = np.arange(1, 7.0, 0.1).reshape(-1, 1)
    continuous_x_ = add_polynomial_features(continuous_x, len(thetas) - 1)
    y_hat = mlr.predict_(continuous_x_)
    plt.scatter(x, y)
    plt.plot(continuous_x, y_hat, color='orange')
    plt.grid()
    plt.show()


try:
    data = pd.read_csv("day_07/resources/" + filename)
except FileNotFoundError:
    data = pd.read_csv("../resources/" + filename)
except FileNotFoundError:
    exit()
x = np.array(data[["weight","prod_distance","time_delivery"]])
y = np.array(data[["target"]])
x_train, x_test, y_train, y_test = data_spliter(x, y, 0.8)
print(x_train)
print(y_train)
print(x_test)
print(y_test)


theta1 = np.array([[80.], [-7.]])
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
