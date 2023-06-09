import numpy as np
import math


def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


@_guard_
def sigmoid_(x):
    """
    Compute the sigmoid of a vector.
    Args:
    x: has to be a numpy.ndarray of shape (m, 1).
    Returns:
    The sigmoid value as a numpy.ndarray of shape (m, 1).
    None if x is an empty numpy.ndarray.
    Raises:
    This function should not raise any Exception.
    """
    if len(x.shape) == 2 and x.shape[1] == 1:
        return 1 / (1 + math.e ** -x)


if __name__=="__main__":
    # Example 1:
    x = np.array([[-4]])
    print(sigmoid_(x))
    # Output:
    # array([[0.01798620996209156]])
    # Example 2:
    x = np.array([[2]])
    print(sigmoid_(x))
    # Output:
    # array([[0.8807970779778823]])
    # Example 3:
    x = np.array([[-4], [2], [0]])
    print(sigmoid_(x))
    # Output:
    # array([[0.01798620996209156], [0.8807970779778823], [0.5]])
    # Example 4:
    x = np.array([])
    print(sigmoid_(x))
    # Output:
    # None
