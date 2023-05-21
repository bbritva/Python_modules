import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


def _guard_(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], pd.DataFrame) or not isinstance(args[1], list):
            print("Wrong parameters", type(args[0]), type(args[1]), file=sys.stderr)
            return None
        try:
            return(func(*args, **kwargs))
        except Exception as e:
            print("exception", e) 
            return None
    return wrapper

class MyPlotLib:
    @staticmethod
    @_guard_
    def histogram(data, features):
        fig, axs = plt.subplots(ncols=len(features), nrows=1, layout="constrained")
        for i, feature in enumerate(features):
            axs[i].hist(data[feature].dropna())
            axs[i].set_title(feature)
            axs[i].grid()
        plt.show()
    
    @staticmethod
    @_guard_
    def density(data, features):
        sb.kdeplot(data[features].dropna())
        plt.show()    
    
    @staticmethod
    @_guard_
    def pair_plot(data, features):
        pd.plotting.scatter_matrix(data[features].dropna())
        plt.show()
    
    @staticmethod
    @_guard_
    def box_plot(data, features):
        fig, axs = plt.subplots()
        axs.boxplot(data[features].dropna(), labels=features)
        plt.show()


if __name__ == "__main__":
    raw_data = pd.read_csv('../data/athlete_events.csv')
    print("Loading dataset of dimensions", raw_data.shape[0], "x", raw_data.shape[1])
    MyPlotLib.histogram(raw_data, ["Height", "Weight"])
    MyPlotLib.density(raw_data, ["Height", "Weight"])
    MyPlotLib.pair_plot(raw_data, ["Height", "Weight"])
    MyPlotLib.box_plot(raw_data, ["Height", "Weight"])