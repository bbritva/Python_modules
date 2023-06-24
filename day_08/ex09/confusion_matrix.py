import numpy as np
import time
import math


from sklearn.metrics import confusion_matrix

def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper

@_guard_
def confusion_matrix_(y_true, y_hat, labels=None, df_option=True):
    """
    Compute confusion matrix to evaluate the accuracy of a classification.
    Args:
    y:a numpy.array for the correct labels
    y_hat:a numpy.array for the predicted labels
    labels: optional, a list of labels to index the matrix.
    This may be used to reorder or select a subset of labels. (default=None)
    df_option: optional, if set to True the function will return a pandas DataFrame
    instead of a numpy array. (default=False)
    Return:
    The confusion matrix as a numpy array or a pandas DataFrame according to df_option value.
    None if any error.
    Raises:
    This function should not raise any Exception.
    """

    pos_labels = np.unique(np.c_[y_true, y_hat]) if labels is None else np.array(labels)
    res = np.zeros((pos_labels.shape[0], pos_labels.shape[0]), type(np.int32))
    for i in range(len(pos_labels)):
        for j in range(len(pos_labels)):
            res[i][j] = len(y_true[(y_true == pos_labels[i]) & (y_hat == pos_labels[j] )])
    return res


if __name__=="__main__":
    y_hat = np.array([['norminet'], ['dog'], ['norminet'], ['norminet'], ['dog'], ['bird']])
    y = np.array([['dog'], ['dog'], ['norminet'], ['norminet'], ['dog'], ['norminet']])
    # Example 1:
    ## your implementation
    print(confusion_matrix_(y, y_hat))
    ## Output:
    # array([[0 0 0]
    # [0 2 1]
    # [1 0 2]])
    ## sklearn implementation
    print(confusion_matrix(y, y_hat))
    ## Output:
    # array([[0 0 0]
    # [0 2 1]
    # [1 0 2]])
    # Example 2:
    ## your implementation
    print(confusion_matrix_(y, y_hat, labels=['dog', 'norminet']))
    ## Output:
    # array([[2 1]
    # [0 2]])
    ## sklearn implementation
    print(confusion_matrix(y, y_hat, labels=['dog', 'norminet']))
    ## Output:
    # array([[2 1]
    # [0 2]])
    
    
    #Example 3:
    print(confusion_matrix_(y, y_hat, df_option=True))
    #Output:
    # bird dog norminet
    # bird 0 0 0
    # dog 0 2 1
    # norminet 1 0 2
    #Example 2:
    print(confusion_matrix_(y, y_hat, labels=['bird', 'dog'], df_option=True))
    #Output:
    #      bird dog
    # bird    0   0
    # dog     0   2