import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def _guard_(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], pd.DataFrame) or not isinstance(args[1], list):
            print("Wrong parameters", type(args[0]), type(args[1]), file=sys.stderr)
            return None
        try:
            return(func(*args, **kwargs))
        except Exception as e:
            print(e) 
            return None
    return wrapper

class MyPlotLib:
    @staticmethod
    @_guard_
    def histogram(data, features):
        fig, axs = plt.subplots(ncols=len(features), nrows=1, figsize=(5.5, 3.5))
        for i, feature in enumerate(features):
            axs[i].hist(data[feature].dropna())
        plt.show()
    
    @_guard_
    @staticmethod
    def density(data, features):
        pass    
    
    @_guard_
    @staticmethod
    def pair_plot(data, features):
        pass    
    
    @_guard_
    @staticmethod
    def box_plot(data, features):
        pass


if __name__ == "__main__":
    raw_data = pd.read_csv('../data/athlete_events.csv')
    print("Loading dataset of dimensions", raw_data.shape[0], "x", raw_data.shape[1])
    MyPlotLib.histogram(raw_data, ["Height", "Weight"])