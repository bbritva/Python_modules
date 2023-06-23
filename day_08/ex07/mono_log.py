import numpy as np
import pandas as pd
import sys

from my_logistic_regression import MyLogisticRegression as MyLR
from data_spliter import data_spliter


features = "solar_system_census.csv"
targets = "solar_system_census_planets.csv"


if __name__ == "__main__":
    """Check the arguments"""
    try:
        if len(sys.argv) > 1 and sys.argv[1].startswith("-zipcode=") and int(sys.argv[1][9:]) in range(4):
            zipcode = int(sys.argv[1][9:])
        else:
            raise ValueError
    except ValueError:
        print("Start progamm with zipcode argument: python mono_log.py -zipcode=x, with x being 0, 1, 2 or 3.")
        exit(0)
    print(zipcode)

    """ Read data """
    try:
        data_features = pd.read_csv("day_08/resources/" + features)
        data_targets = pd.read_csv("day_08/resources/" + targets)
    except FileNotFoundError:
        try:
            data_features = pd.read_csv("../resources/" + features)
            data_targets = pd.read_csv("../resources/" + targets)
        except FileNotFoundError:
            exit()

    planets = np.array(data_targets["Origin"]).reshape((-1, 1))
    Y = np.zeros(planets.shape, dtype='int8')
    Y[np.where(planets == zipcode)] = 1
    X = np.array(data_features[["weight", "height", "bone_density"]])
    x_train, x_test, y_train, y_test = data_spliter(X, Y, 0.8)
