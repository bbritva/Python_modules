import numpy as np

class ColorFilter:
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
        if array.shape[2] == 4:
            new_arr = np.full((array.shape[0], array.shape[1], 4), [255,255,255,0])
            transp_arr = new_arr[:,:,3:4]
            transp_arr += array[:,:,3:4]
        else:
            new_arr = np.full((array.shape[0], array.shape[1], 3), [255,255,255])
        color_arr = new_arr[:,:,0:3]
        color_arr -= array[:,:,0:3]
        return new_arr

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
        if array.shape[2] == 4:
            new_arr = np.full((array.shape[0], array.shape[1], 4), [0,0,255,255])
        else:
            new_arr = np.full((array.shape[0], array.shape[1], 3), [0,0,255])
        return np.bitwise_and(new_arr, array)

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
        if array.shape[2] == 4:
            new_arr = np.full((array.shape[0], array.shape[1], 4), [0,255,0,255])
        else:
            new_arr = np.full((array.shape[0], array.shape[1], 3), [0,255,0])
        return np.bitwise_and(new_arr, array)

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
        if array.shape[2] == 4:
            new_arr = np.full((array.shape[0], array.shape[1], 4), [255,0,0,255])
        else:
            new_arr = np.full((array.shape[0], array.shape[1], 3), [255,0,0])
        return np.bitwise_and(new_arr, array)

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
        pass

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
        pass