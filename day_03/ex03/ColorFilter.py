import numpy as np

class ColorFilter:
    basic_3_full_color = [255,255,255]
    basic_4_full_color = [255,255,255,0]


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
        new_arr = 255 - array
        new_arr[:,:,3:] = array[:,:,3:]
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
        new_arr = np.zeros(array.shape, dtype=np.int16)
        new_arr[:,:,2:4] = array[:,:,2:4]
        return new_arr

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
        limits = np.linspace(0, 250, num=3, endpoint=False)
        for limit in limits:
            color_arr[slice_array >= limit] = limit
        return new_arr

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
        new_arr = array.copy()
        color = new_arr[:,:,0:3]

        if filter == 'mean':
            return None

        return None
