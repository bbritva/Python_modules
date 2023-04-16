import numpy as np


class ScrapBooker:
    def crop(self, array, dim, position=(0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Return:
        -------
        new_arr: the cropped numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        try:
            return array[position[0]:position[0] + dim[0], position[1]:position[1] + dim[1]]
        except:
            return None


    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
        Args:
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Return:
        -------
        new_arr: thined numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        try:
            axis = 1 if axis == 0 else 0 
            return np.delete(array, np.arange(n - 1, array.shape[axis], n), axis)
                
        except:
            return None


    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Return:
        -------
        new_arr: juxtaposed numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        pass


    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Return:
        -------
        new_arr: mosaic numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        pass


if __name__ == "__main__":
    spb = ScrapBooker()
    arr1 = np.arange(0,25).reshape(5,5)
    print(repr(arr1))
    print(repr(spb.crop(arr1, (3,1), (1,0))))
    #Output :
        # array([[ 5],
                # [10],
                # [15]])
    arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
    print(repr(arr2))
    print(repr(spb.thin(arr2,3,0)))
    #Output :
        # array([['A', 'B', 'D', 'E', 'G', 'H'],
            # ['A', 'B', 'D', 'E', 'G', 'H'],
            # ['A', 'B', 'D', 'E', 'G', 'H'],
            # ['A', 'B', 'D', 'E', 'G', 'H'],
            # ['A', 'B', 'D', 'E', 'G', 'H'],
            # ['A', 'B', 'D', 'E', 'G', 'H']], dtype='<U1')
    arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
    print(repr(spb.juxtapose(arr3, 3, 1)))
    #Output :
        # array([[1, 2, 3, 1, 2, 3, 1, 2, 3],
                # [1, 2, 3, 1, 2, 3, 1, 2, 3],
                # [1, 2, 3, 1, 2, 3, 1, 2, 3]])