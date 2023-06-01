import numpy as np
import matplotlib.pyplot as plt


def plot(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.array.
    Args:
    x: has to be an numpy.array, a vector of dimension m * 1.
    y: has to be an numpy.array, a vector of dimension m * 1.
    theta: has to be an numpy.array, a vector of dimension 2 * 1.
    Returns:
    Nothing.
    Raises:
    This function should not raise any Exceptions.
    """
    try:
        predicted = theta[0] + theta[1] * x
        plt.figure(figsize=(10,6))
        plt.plot(x, predicted, c = "b")
        plt.scatter(x, y, marker='x', c='r') 
        plt.grid()
        plt.show()
    except:
        pass


x = np.arange(1,6)
y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])
# Example 1:
theta1 = np.array([[4.5],[-0.2]])
plot(x, y, theta1)
theta2 = np.array([[-1.5],[2]])
plot(x, y, theta2)
theta3 = np.array([[3],[0.3]])
plot(x, y, theta3)