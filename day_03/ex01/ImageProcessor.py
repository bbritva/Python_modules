import numpy as np
from PIL import Image


class ImageProcessor:
    def load(self, path):
        img = Image.open(path)
        print("Loading image of dimensions {} x {}".format(img.size[0], img.size[1]))
        return np.array(img)

    def display(self, array):
        img = Image.fromarray(array, 'RGB')
        img.show()

if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load("non_existing_file.png")
    print(repr(arr))
    # Output :
    # None
    arr = imp.load("empty_file.png")
    # Output :
    # Exception: OSError -- strerror: None
    print(repr(arr))
    # Output :
    # None
    arr = imp.load("../resources/42AI.png")
    # Output :
    # Loading image of dimensions 200 x 200
    print(repr(arr))