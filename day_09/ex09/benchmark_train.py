import numpy as np
import pandas as pd
import pickle

from polynomial_model import add_polynomial_features
from my_logistic_regression import MyLogisticRegression as MyLR
from data_spliter import data_spliter

data_file = "solar_system_census.csv"
target_file = "solar_system_census_planets.csv"
features = ["weight", "height", "bone_density"]
results = {}
models = {0.0: {}, 0.2: {}, 0.4: {}, 0.6: {}, 0.8: {}, 1.0: {}}
max_iter = 5e5
alpha = .001


def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(func.__name__ + ': ' + str(e))
            return None
    return wrapper

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
def train_model(x_train, y_train, lambda_):
    theta = np.zeros((10, 1))
    my_lreg = MyLR(theta, alpha=alpha, max_iter=max_iter,
                   penalty='l2', lambda_=lambda_)
    my_lreg.fit_(x_train, y_train)
    return my_lreg


@_guard_
def train_models(X, Y, lambda_):
    model = []
    for i in range(4):
        model.append(train_model(X, Y[:, i].reshape((-1, 1)), lambda_).theta)
    models[lambda_] = model
    print("Models with lambda %.1f trained" % (lambda_))


@_guard_
def validate_models(X, Y):
    best_lambda = 0
    best_f1 = 0
    for j in range(6):  # lambdas
        thetas = models[j/5]
        y_hat = []
        for theta in thetas:
            mdl = MyLR(theta, alpha=alpha, max_iter=max_iter,
                   penalty='l2', lambda_=j/5)
            y_hat.append(mdl.predict_(X))
        y_hat = np.c_[y_hat[0], y_hat[1], y_hat[2], y_hat[3]]
        y_hat = np.argmax(y_hat, axis=1).reshape((-1, 1))
        f1_score = f1_score_macro_(Y, y_hat)
        if f1_score > best_f1:
            best_f1 = f1_score
            best_lambda = j / 5

        """ Output """
        res = y_hat == Y
        print("Correct predictions =", res.sum())
        print("Wrong predictions =", res.shape[0] - res.sum())
        print(f1_score)
    return (best_lambda, best_f1)


@_guard_
def norm_data(x):
    x_max = max(x)
    x_min = min(x)
    return (x - x_min) / (x_max - x_min), x_max, x_min


@_guard_
def main():
    """ Read data """
    try:
        data_features = pd.read_csv("day_08/resources/" + data_file)
        data_targets = pd.read_csv("day_08/resources/" + target_file)
    except Exception:
        try:
            data_features = pd.read_csv("../resources/" + data_file)
            data_targets = pd.read_csv("../resources/" + target_file)
        except Exception:
            exit()

    planets = np.array(data_targets["Origin"]).reshape((-1, 1)).astype(np.int8)
    Y = np.zeros((planets.shape[0], 4), dtype='int8')
    for i, zipcode in enumerate(planets):
        Y[i][zipcode] = 1
    Y = np.c_[Y, planets]
    X = np.array(data_features[features])

    """ Normalize data"""
    max_x = np.zeros((X.shape[1]))
    min_x = np.zeros((X.shape[1]))
    for i in range(X.shape[1]):
        X[:, i], max_x[i], min_x[i] = norm_data(X[:, i])

    X = add_polynomial_features(X, 3)

    """ Split and save data """
    train_set, cv_set, test_set = data_spliter(np.c_[X, Y])
    np.savetxt("../resources/tmp/ssc_train_set.csv", train_set, delimiter=",")
    np.savetxt("../resources/tmp/ssc_cv_set.csv", cv_set, delimiter=",")
    np.savetxt("../resources/tmp/ssc_test_set.csv", test_set, delimiter=",")

    """ Training """
    for j in range(6):
        train_models(train_set[:, :-5], train_set[:, -5:-1], j / 5)

    best_lambda, best_f1 = validate_models(cv_set[:, :-5], cv_set[:, -1:])
    results["models"] = models
    results["max_x"] = max_x
    results["min_x"] = min_x
    results["best_lambda"] = best_lambda

    with open("model.pickle", 'wb') as my_file:
        pickle.dump(results, my_file)
        print("All results are saved =)")

if __name__ == "__main__":
    main()
