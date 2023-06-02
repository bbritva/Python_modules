import numpy as np
import matplotlib.pyplot as plt


def  plot_with_loss(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    y: has to be an numpy.ndarray, a vector of dimension m * 1.
    theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
    Nothing.
    Raises:
    This function should not raise any Exception.
    """
    try:
        predicted = theta[0] + theta[1] * x
        loss = ((y - predicted) ** 2).sum() / (y.shape[0])
        plt.figure(figsize=(10,6))
        plt.title(f"Cost: {loss:6f}")
        plt.plot(x, predicted, c = "b")
        plt.scatter(x, y, marker='x', c='r')
        for i, ax in enumerate(x):
            plt.plot([ax, ax], [y[i], predicted[i]], "r--")
        plt.grid()
        plt.show()
    except:
        pass


x = np.arange(1,6)
y = np.array([11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568])
# Example 1:
theta1= np.array([18,-1])
plot_with_loss(x, y, theta1)
theta2 = np.array([14, 0])
plot_with_loss(x, y, theta2)
theta3 = np.array([12, 0.8])
plot_with_loss(x, y, theta3)