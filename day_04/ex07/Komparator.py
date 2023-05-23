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
        if isinstance(numerical_var, list):
            for num in numerical_var:
                self.compare_box_plots_inner(categorical_var, num)
        else:
            self.compare_box_plots_inner(categorical_var, numerical_var)

    @_guard_
    def compare_box_plots_inner(self, categorical_var, numerical_var):
        data = self.data[[categorical_var, numerical_var]].dropna()
        features = self.data[categorical_var].unique()

        fig, axs = plt.subplots(ncols=len(features), sharey=True)
        for i, feature in enumerate(features):
            axs[i].boxplot(data[data[categorical_var] == feature][numerical_var])
            axs[i].set_title(feature)
        fig.tight_layout()
        plt.show()

    @_guard_
    def density(self, categorical_var, numerical_var): 
        """Displays the density of the numerical variable. Each subpopulation
        should be represented by a separate curve on the graph."""
        if isinstance(numerical_var, list):
            for num in numerical_var:
                self.density_inner(categorical_var, num)
        else:
            self.density_inner(categorical_var, numerical_var)

    @_guard_
    def density_inner(self, categorical_var, numerical_var):
        data = self.data[[categorical_var, numerical_var]].dropna()
        features = self.data[categorical_var].unique()

        for feature in features:
            sb.kdeplot(data[data[categorical_var] == feature][numerical_var], label=feature)
        plt.show()


    @_guard_
    def compare_histograms(self, categorical_var, numerical_var): 
        """Plots the numerical variable in a separate histogram for each category.
        As an extra, you can use overlapping histograms with a color code."""
        if isinstance(numerical_var, list):
            for num in numerical_var:
                self.compare_histograms_inner(categorical_var, num)
        else:
            self.compare_histograms_inner(categorical_var, numerical_var)

    @_guard_
    def compare_histograms_inner(self, categorical_var, numerical_var):
        data = self.data[[categorical_var, numerical_var]].dropna()
        features = self.data[categorical_var].unique()

        fig, axs = plt.subplots(ncols=len(features), sharey=True)
        for i, feature in enumerate(features):
            axs[i].hist(data[data[categorical_var] == feature][numerical_var])
            axs[i].set_title(feature)
            axs[i].grid()
        fig.tight_layout()
        plt.show()


if __name__ == "__main__":
    try:
        raw_data = pd.read_csv('../data/athlete_events.csv')
        print("Loading dataset of dimensions", raw_data.shape[0], "x", raw_data.shape[1])
        print(raw_data[raw_data["Weight"] > 170][["Name", "Sport", "Weight"]])
        kmp = Komparator(raw_data)
        kmp.compare_box_plots("Sex", "Height")
        kmp.density("Sex", "Height")
        kmp.compare_histograms("Sex", "Height")
        kmp.compare_box_plots("Sex", ["Height", "Weight"])
        kmp.density("Sex", ["Height", "Weight"])
        kmp.compare_histograms("Sex", ["Height", "Weight"])
    except Exception as exc:
        print("Error: ", exc, file=sys.stderr)
