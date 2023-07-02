import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

from my_logistic_regression import MyLogisticRegression as MyLR


test_file = "ssc_test_set.csv"
train_file = "ssc_train_set.csv"
features = ["weight", "height", "bone_density"]
max_iter = 5e5
alpha = .001


def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except ZeroDivisionError:
            return 0
        except Exception as e:
            print(func.__name__ + ': ' + str(e))
            return None
    return wrapper


@_guard_
def train_model(x_train, y_train, lambda_):
    theta = np.zeros((10, 1))
    my_lreg = MyLR(theta, alpha=alpha, max_iter=max_iter,
                   penalty='l2', lambda_=lambda_)
    my_lreg.fit_(x_train, y_train)
    return my_lreg.theta


def calc_params(y, y_hat, pos_label):
    tp = len(y[(y == pos_label) & (y_hat == pos_label)])
    fp = len(y[(y != pos_label) & (y_hat == pos_label)])
    tn = len(y[(y != pos_label) & (y_hat != pos_label)])
    fn = len(y[(y == pos_label) & (y_hat != pos_label)])
    return tp, fp, tn, fn


@_guard_
def precision_score_(y, y_hat, pos_label=1):
    tp, fp, tn, fn = calc_params(y, y_hat, pos_label)
    return tp / (tp + fp)


@_guard_
def recall_score_(y, y_hat, pos_label=1):
    tp, fp, tn, fn = calc_params(y, y_hat, pos_label)
    return tp / (tp + fn)


@_guard_
def f1_score_macro_(y, y_hat):
    """ Compute the f1 score """
    mac_avg_prec = sum(precision_score_(y, y_hat, i) for i in range(4)) / 4
    mac_avg_recall = sum(recall_score_(y, y_hat, i) for i in range(4)) / 4
    mac_avg_f1 = 2 * (mac_avg_prec * mac_avg_recall) / \
        (mac_avg_prec + mac_avg_recall)
    return mac_avg_f1


@_guard_
def get_predictions(thetas, data):
    y_hat = []
    for theta in thetas:
        mdl = MyLR(theta)
        y_hat.append(mdl.predict_(data[:, :-5]))
    y_hat = np.c_[y_hat[0], y_hat[1], y_hat[2], y_hat[3]]
    y_hat = np.argmax(y_hat, axis=1).reshape((-1, 1))
    return y_hat


@_guard_
def get_scores(thetas, data):
    f1_scores = []
    for j in range(6):
        theta = thetas[j/5]
        y_hat = get_predictions(theta, data)
        # res = y_hat == data[:, -1].reshape((-1, 1))
        # print("Correct predictions =", res.sum())
        # print("Wrong predictions =", res.shape[0] - res.sum())
        f1_scores.append(f1_score_macro_(data[:, -1].reshape(-1, 1), y_hat))
    return f1_scores


@_guard_
def train_models(train_data, test_data, lambda_):
    thetas = []
    X = train_data[:, :-5]
    Y = train_data[:, -5:-1]
    for i in range(4):
        thetas.append(train_model(X, Y[:, i].reshape((-1, 1)), lambda_))
    print("Models with lambda %f trained" % (lambda_))
    return thetas


@_guard_
def main():
    try:
        # with open("day_09/ex09/model.pickle", 'rb') as my_file:
        with open("model.pickle", 'rb') as my_file:
            models_data = pickle.load(my_file)
    except KeyError:
        print("Data loading error")
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
            print("Data loading error")
            exit()

    best_lambda = models_data["best_lambda"]
    thetas = models_data["models"]
    max_x = models_data["max_x"]
    min_x = models_data["min_x"]
    print("Data loaded")
    best_thetas = train_models(train_data, test_data, best_lambda)
    thetas[best_lambda] = best_thetas
    """ Visualize the performance of the different models with a
    bar plot showing the score of the models given their λ value. """

    lambdas = np.arange(0., 1.2, step=.2)
    f1_scores = get_scores(thetas, test_data)
    for i, score in enumerate(f1_scores):
        print("Lambda = %.2f, f1-score = %.5f" % (lambdas[i], score))
    plt.xlabel("lambda")
    plt.ylabel("f1_score")
    plt.plot(lambdas, f1_scores)
    plt.grid()
    plt.show()

    y_hat = get_predictions(best_thetas, test_data)
    x_test = test_data[:, :-5]
    y_test = test_data[:, -5:]
    color = ["red", "green", "blue", "black"]

    plt.xlabel(features[0])
    plt.ylabel(features[1])
    for i in range(4):
        predicted = x_test[np.where(y_hat == i)[0]]
        actual = x_test[np.where(y_test[:, 4].reshape((-1, 1)) == i)[0]]
        plt.scatter(predicted[:, 0], predicted[:, 1],
                    marker='o', label="Origin", alpha=0.2, c=color[i])
        plt.scatter(actual[:, 0], actual[:, 1],
                    marker='.', label="Origin", c=color[i])
    plt.grid()
    plt.show()

    plt.xlabel(features[1])
    plt.ylabel(features[2])
    for i in range(4):
        predicted = x_test[np.where(y_hat == i)[0]]
        actual = x_test[np.where(y_test[:, 4].reshape((-1, 1)) == i)[0]]
        plt.scatter(predicted[:, 1], predicted[:, 2],
                    marker='o', label="Origin", alpha=0.5, c=color[i])
        plt.scatter(actual[:, 1], actual[:, 2],
                    marker='.', label="Origin", c=color[i])
    plt.grid()
    plt.show()

    plt.xlabel(features[0])
    plt.ylabel(features[2])
    for i in range(4):
        predicted = x_test[np.where(y_hat == i)[0]]
        actual = x_test[np.where(y_test[:, 4].reshape((-1, 1)) == i)[0]]
        plt.scatter(predicted[:, 0], predicted[:, 2],
                    marker='o', label="Origin", alpha=0.5, c=color[i])
        plt.scatter(actual[:, 0], actual[:, 2],
                    marker='.', label="Origin", c=color[i])
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
