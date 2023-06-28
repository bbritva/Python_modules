import numpy as np


def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except:
            return None
    return wrapper


@_guard_
def add_polynomial_features(x, power):
    """Add polynomial features to vector x
    by raising its values up to the power given in argument."""
    res = x.copy()
    for i in range(1, power):
        res = np.c_[res, x ** (i + 1)]
    return res
