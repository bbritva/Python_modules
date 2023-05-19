import numpy as np

class ColorFilter:
    def _guard_(func):
        def wrapper(*args, **kwargs):
            if not isinstance(args[1], np.ndarray):
                return None
            try:
                return(func(*args, **kwargs))
            except:
                return None
        return wrapper

    @_guard_
    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        new_arr = 1 - array
        new_arr[:,:,3:] = array[:,:,3:]
        return new_arr 

    @_guard_
    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        new_arr = np.zeros(array.shape, dtype=np.float32)
        new_arr[:,:,2:4] = array[:,:,2:4]
        return new_arr

    @_guard_
    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        new_arr = array.copy()
        new_arr[:,:,0] *= 0
        new_arr[:,:,2] *= 0
        return new_arr

    @_guard_
    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        new_arr = array.copy()
        new_arr[:,:,0:3] -= self.to_blue(array)[:,:,0:3] + self.to_green(array)[:,:,0:3]
        return new_arr


    @_guard_
    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        new_arr = array.copy()
        color_arr = new_arr[:,:,0:3]
        slice_array = array[:,:,0:3]
        limits = np.linspace(5 / 6, 1 / 6, num=3, endpoint=True, dtype=np.float32)
        values = np.linspace(1, 0, num=4, endpoint=True, dtype=np.float32)
        color_arr[slice_array >= limits[0]] = values[0]
        mask = (slice_array < limits[0]) & (slice_array >= limits[1])
        color_arr[mask] = values[1]
        mask = (slice_array < limits[1]) & (slice_array >= limits[2])
        color_arr[mask] = values[2]
        color_arr[slice_array < limits[2]] = values[3]
        return new_arr

    @_guard_
    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = 'mean'/'m': performs the mean of RBG channels.
        For filter = 'weight'/'w': performs a weighted mean of RBG channels.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in ['m','mean','w','weight']
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        values = None
        if filter in ['m', 'mean']:
            values = np.sum(array[:,:, 0:3], axis=-1, keepdims=True, dtype=np.float32) / 3
        elif filter in ['w', 'weight'] \
            and isinstance(kwargs['weights'], list)\
                and len(kwargs['weights']) == 3\
                    and np.sum(kwargs['weights']) == 1:
            values = np.sum(array[:,:, 0:3] * kwargs['weights'], axis=-1, keepdims=True)
        return np.dstack((np.tile(values, 3), array[:,:, 3:4]))

