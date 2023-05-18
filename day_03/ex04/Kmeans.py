import sys
import numpy as np
import pandas as pd
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

def _guard_(func):
    def wrapper(*args, **kwargs):
        # if not isinstance(args[0], np.ndarray):
        #     print("Not a numpy array", file=sys.stderr)
        #     return None
        try:
            return(func(*args, **kwargs))
        except Exception as e:
            print(e) 
            return None
    return wrapper

class KmeansClustering:
    @_guard_
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids
        self.model = KMeans(n_clusters = self.ncentroid, max_iter = self.max_iter)


    @_guard_
    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        None.
        Raises:
        -------
        This function should not raise any Exception.
        """
        self.model.fit(X)

    @_guard_
    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
        This function should not raise any Exception.
        """
        self.fit(X)
        return self.model.labels_

if __name__ == "__main__":
    raw_data = pd.read_csv('./solar_system_census.csv', index_col = 0)

    model = KmeansClustering(max_iter=20, ncentroid=5)
    model.fit(raw_data)

    fig = plt.figure()
    ax = plt.axes(projection='3d')


    ax.scatter3D(raw_data['height'], raw_data['weight'], raw_data['bone_density'], c=model.predict(raw_data))
    plt.show()
