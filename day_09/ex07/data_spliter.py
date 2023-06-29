import numpy as np

def data_spliter(x):
    """Shuffles and splits the dataset (given by x and y) into a training, cross-validation
    and a test set, while respecting the proportion 80-10-10.
    Args:
    x: has to be an numpy.array, a matrix of dimension m * n.
    Return:
    (train_set, cv_set, test_set) as a tuple of numpy.array
    Raises:
    This function should not raise any Exception.
    """
    try:
        print(type(x))
        np.random.shuffle(x)
        limit_train = int(0.8 * x.shape[0])
        limit_cv = x.shape[0] - int(0.1 * x.shape[0])
        return x[:limit_train,:], x[limit_train:limit_cv,:], x[limit_cv:,:]
    except Exception as e:
        print(e)
        return None

