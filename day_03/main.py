import numpy as np

if __name__ == "__main__":
    # np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)

    c = []
    for i in range(5):
        c.append(i)
    a = np.array(c)
    b = np.array(c)
    print(b * a)

    ndarr = np.array([[1., 0., 0.], [0., 1.]])

    print(ndarr)
    print(ndarr.ndim, ndarr.shape, ndarr.size, ndarr.dtype, ndarr.itemsize)
    