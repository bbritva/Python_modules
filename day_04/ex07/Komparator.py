import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return(func(*args, **kwargs))
        except Exception as e:
            print("exception", e) 
            return None
    return wrapper

class Komparator:
    @_guard_
    def __init__(self, data):
        if not isinstance(data, pd.DataFrame):
            raise ValueError("argument is not a pandas.DataFrame")
        self.data = data


    @_guard_
    def compare_box_plots(self, categorical_var, numerical_var): 
        """displays a series of box plots to compare how the distribution of the numerical variable changes
        if we only consider the subpopulation which belongs to each category. There should
        be as many box plots as categories. For example, with Sex and Height, we would
        compare the height distributions of men vs. women with two box plots"""
        data = self.data[[categorical_var, numerical_var]].dropna()
        features = self.data[categorical_var].unique()
        print(features)

        fig, axs = plt.subplots(ncols=len(features), sharey=True)

        for i, feature in enumerate(features):
            axs[i].boxplot(data[data[categorical_var] == feature][numerical_var])
            axs[i].set_title(feature)
            axs[i].set
        fig.tight_layout()
        plt.show()

    @_guard_
    def density(self, categorical_var, numerical_var): 
        """displays the density of the
        numerical variable. Each subpopulation should be represented by a separate curve
        on the graph."""
        pass

    @_guard_
    def compare_histograms(self, categorical_var, numerical_var): 
        """plots the numerical variable in a separate histogram for each category. As an extra, you can
        use overlapping histograms with a color code."""
        pass


if __name__ == "__main__":
    try:
        raw_data = pd.read_csv('../data/athlete_events.csv')
        print("Loading dataset of dimensions", raw_data.shape[0], "x", raw_data.shape[1])
        kmp = Komparator(raw_data)
        kmp.compare_box_plots("Sex", "Height")
    except:
        print("Error: File corrupt")
