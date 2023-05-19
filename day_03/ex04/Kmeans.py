import sys
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def _guard_(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[1], np.ndarray):
            print("Not a numpy array", file=sys.stderr)
            return None
        try:
            return(func(*args, **kwargs))
        except Exception as e:
            print(e) 
            return None
    return wrapper

class KmeansClustering:
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
        print(repr(self.model.cluster_centers_))
        return self.model.labels_
    
    @_guard_
    def show(self, X):
        ax = plt.axes(projection='3d')
        centers = self.model.cluster_centers_
        ax.set_xlabel("height")
        ax.set_ylabel("weight")
        ax.set_zlabel("bone_density")
        ax.scatter(centers[:,0], centers[:,1], centers[:,2], c=np.arange(self.ncentroid), marker='+', s=150)
        ax.scatter3D(X[:,0], X[:,1], X[:,2], c=self.model.labels_)
        plt.show()


def get_param(name, argv):
    for arg in argv:
        if arg.startswith(name + '='):
            return arg[len(name) + 1 : ]
    raise ValueError


def parse_params(argv):
    try:
        if len(argv) is not 3:
            raise ValueError
        params = []
        params.append(get_param('filepath', argv))
        params.append(int(get_param('ncentroid', argv)))
        params.append(int(get_param('max_iter', argv)))
    except:
        print("wrong parameters\nUsage example: python Kmeans.py filepath='../resources/solar_system_census.csv' ncentroid=4 max_iter=30")
        return None
    print(params)
    return params


if __name__ == "__main__":
    params = parse_params(sys.argv[1:])
    if params:
        raw_data = np.genfromtxt(params[0], delimiter=',')[1:, 1:]
        model = KmeansClustering(max_iter=params[2], ncentroid=params[1])
        model.fit(raw_data)
        model.show(raw_data)
