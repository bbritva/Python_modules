import numpy as np
import pandas as pd
import sys

from my_logistic_regression import MyLogisticRegression as MyLR

filename = "solar_system_census.csv"


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
        data = pd.read_csv("day_08/resources/" + filename)
    except FileNotFoundError:
        try:
            data = pd.read_csv("../resources/" + filename)
        except FileNotFoundError:
            exit()
