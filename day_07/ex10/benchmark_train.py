import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from polynomial_model import add_polynomial_features
from mylinearregression import MyLinearRegression as MyLR
from data_spliter import data_spliter

# filename = "small.csv"
filename = "space_avocado.csv"


def plot_model(X, Y, Y_hat, Y_had_base, feature):
    plt.title(feature)
    plt.scatter(X, Y, marker='o',
                c='darkblue', label="Sell price", alpha=0.01)
    plt.scatter(X, Y_had_base, marker='.',
                c='blue', label="Prediction base")
    plt.scatter(X, Y_hat, marker='.',
                c='red', label="Prediction learned")
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()


def univar_processing(data, feature, alpha, thetas=np.array([[0.0], [0.0]]), max_iter=1e5):
    mlr = MyLR(thetas, alpha=alpha, max_iter=max_iter)
    model_before = mlr.predict_(data['x_test'])
    mlr.fit_(data['x_train'], data['y_train'])
    model_after = mlr.predict_(data['x_test'])
    plot_model(data['x_test'], data['y_test'],
               model_after, model_before, feature)
    print("Thetas:", mlr.thetas)
    print("MSE = ", mlr.mse_(data['y_test'], model_after))


def norm_data(x):
    x_max = max(x)
    return x / x_max, x_max


try:
    data = pd.read_csv("day_07/resources/" + filename)
except FileNotFoundError:
    data = pd.read_csv("../resources/" + filename)
except FileNotFoundError:
    exit()
x_train, x_test, y_train, y_test = data_spliter(
    data[["weight", "prod_distance", "time_delivery"]], data[["target"]], 0.8)
x_w, max_weight = norm_data(x_train[:, 0])
w_data = {"x_train": x_w, "x_test": x_test[:,0] / max_weight,
          "y_train": y_train, "y_test": y_test, "x_max": max_weight}

x_d, max_dist = norm_data(x_train[:,1])
d_data = {"x_train": x_d, "x_test": x_test[:,1] / max_dist,
          "y_train": y_train, "y_test": y_test, "x_max": max_dist}

x_t, max_time = norm_data(x_train[:,2])
t_data = {"x_train": x_t, "x_test": x_test[:,2] / max_time,
          "y_train": y_train, "y_test": y_test, "x_max": max_time}
          
univar_processing(w_data, "weight", 1e-1,
                  thetas=np.array([[6e5], [2e5]]))
univar_processing(d_data, "prod_distance", 1e-1,
                  thetas=np.array([[6e5], [2e4]]))
univar_processing(t_data, "time_delivery", 1e-1,
                  thetas=np.array([[6e5], [-2e3]]))
exit()
X_mult = np.c_[x_w, x_d, x_t]
my_lreg = MyLR(thetas=np.array(
    [[5e5], [3e5], [-2.8e4], [-2e3]]), alpha=1e-1, max_iter=1e5)
y_hat_base = my_lreg.predict_(X_mult)
my_lreg.fit_(X_mult, y)
y_hat = my_lreg.predict_(X_mult)
print(my_lreg.thetas)
print("MSE =", my_lreg.mse_(y, y_hat))

plot_model(x_w, y, y_hat, y_hat_base, "weight")
plot_model(x_d, y, y_hat, y_hat_base, "prod_distance")
plot_model(x_t, y, y_hat, y_hat_base, "time_delivery")


# # theta1 = np.array([[30000.], [4909.], [173.], [6000.]])
# # theta2 = np.array([[85.], [-7.], [-0.2]])
# # theta3 = np.array([[87.], [-5.], [-1.5], [0.15]])
# # theta4 = np.array([[-20], [160], [-80], [14], [-1]])
# # theta5 = np.array([[1140], [-1850], [1110], [-305], [40], [-2]])
# # theta6 = np.array([[9110], [-18015], [13400], [-4935], [966], [-96.4], [3.86]])
# # do_process(theta1, x_train, x_test, y_train, y_test)
# # do_process(theta2, data)
# # do_process(theta3, data, 1e-6, 1000000)
# # do_process(theta4, data, 1e-6, 1000000)
# # do_process(theta5, data, 1e-8, 1000000)
# # do_process(theta6, data, 1e-9, 1000000)
