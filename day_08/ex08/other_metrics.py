import numpy as np
import time
import math


from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


def calc_params(y, y_hat):
    tp = len(y[(y == 1) & (y_hat == 1)])
    fp = len(y[(y == 0) & (y_hat == 1)])
    tn = len(y[(y == 0) & (y_hat == 0)])
    fn = len(y[(y == 1) & (y_hat == 0)])
    return tp, fp, tn, fn


@_guard_
def accuracy_score_(y, y_hat):
    """
    Compute the accuracy score.
    Args:
    y:a numpy.ndarray for the correct labels
    y_hat:a numpy.ndarray for the predicted labels
    Returns:
    The accuracy score as a float.
    None on any error.
    Raises:
    This function should not raise any Exception.
    """
    # tp is the number of true positives,
    # fp is the number of false positives,
    # tn is the number of true negatives,
    # fn is the number of false negatives.
    tp, fp, tn, fn = calc_params(y, y_hat)
    return (tp + tn) / (tp + fp + tn + fn)


def precision_score_(y, y_hat, pos_label=1):
    """
    Compute the precision score.
    Args:
    y:a numpy.ndarray for the correct labels
    y_hat:a numpy.ndarray for the predicted labels
    pos_label: str or int, the class on which to report the precision_score (default=1)
    Return:
    The precision score as a float.
    None on any error.
    Raises:
    This function should not raise any Exception.
    """
    tp, fp, tn, fn = calc_params(y, y_hat)
    return tp / (tp + fp)


def recall_score_(y, y_hat, pos_label=1):
    """
    Compute the recall score.
    Args:
    y:a numpy.ndarray for the correct labels
    y_hat:a numpy.ndarray for the predicted labels
    pos_label: str or int, the class on which to report the precision_score (default=1)
    Return:
    The recall score as a float.
    None on any error.
    Raises:
    This function should not raise any Exception.
    """
    tp, fp, tn, fn = calc_params(y, y_hat)
    return tp / (tp + fn)


def f1_score_(y, y_hat, pos_label=1):
    """
    Compute the f1 score.
    Args:
    y:a numpy.ndarray for the correct labels
    y_hat:a numpy.ndarray for the predicted labels
    pos_label: str or int, the class on which to report the precision_score (default=1)
    Returns:
    The f1 score as a float.
    None on any error.
    Raises:
    This function should not raise any Exception.
    """
    precision = precision_score_(y, y_hat)
    recall = recall_score_(y, y_hat)
    return (2 * precision * recall) / (precision + recall)


if __name__ == "__main__":
    # Example 1:
    y_hat = np.array([1, 1, 0, 1, 0, 0, 1, 1]).reshape((-1, 1))
    y = np.array([1, 0, 0, 1, 0, 1, 0, 0]).reshape((-1, 1))
    # Accuracy
    # your implementation
    print("my accurancy =", accuracy_score_(y, y_hat))
    print("sclearn accurancy =", accuracy_score(y, y_hat))
    # Output:
    # 0.5

    # Precision
    # your implementation
    print("my Precision =", precision_score_(y, y_hat))
    print("sclearn Precision =", precision_score(y, y_hat))
    # Output:
    # 0.4

    # Recall
    # your implementation
    print("my Recall =", recall_score_(y, y_hat))
    print("sclearn Recall =", recall_score(y, y_hat))
    # Output:
    # 0.6666666666666666

    # F1-score
    # your implementation
    f1_score_(y, y_hat)
    print("my F1-score =", f1_score_(y, y_hat))
    print("sclearn F1-score =", f1_score(y, y_hat))
    # Output:
    # 0.5
